/*
 * slide-gallery.js
 * ----------------
 * Turns a `<div class="slide-gallery" markdown="1">` block containing plain
 * markdown images (one per slide) into an interactive viewer with:
 *   - single-slide view with prev/next controls (and left/right arrow keys)
 *   - a full screen toggle (native Fullscreen API)
 *   - a "slide sorter" grid toggle to view/jump between all slides at once
 *
 * Usage in a page (requires the `md_in_html` markdown extension, already
 * enabled in mkdocs.yml):
 *
 *   <div class="slide-gallery" markdown="1">
 *
 *   ![Slide 1](../slides/<name>/slide_001.png)
 *   ![Slide 2](../slides/<name>/slide_002.png)
 *
 *   </div>
 *
 * Image paths are written as normal markdown so MkDocs rewrites them
 * correctly for the built site; this script only reads the already-resolved
 * `src` from the rendered <img> elements, so it never needs to compute a
 * relative path itself.
 */
(function () {
  "use strict";

  function pad(n) {
    return String(n).padStart(3, "0");
  }

  function buildToolbar() {
    var toolbar = document.createElement("div");
    toolbar.className = "slide-gallery__toolbar";
    toolbar.innerHTML =
      '<button type="button" class="slide-gallery__btn" data-action="prev" title="Previous slide" aria-label="Previous slide">&#8592;</button>' +
      '<span class="slide-gallery__counter">1 / 1</span>' +
      '<button type="button" class="slide-gallery__btn" data-action="next" title="Next slide" aria-label="Next slide">&#8594;</button>' +
      '<span class="slide-gallery__spacer"></span>' +
      '<button type="button" class="slide-gallery__btn" data-action="grid" title="Toggle slide sorter view" aria-label="Toggle slide sorter view">&#9638;&#xFE0E; Slide sorter</button>' +
      '<button type="button" class="slide-gallery__btn" data-action="fullscreen" title="Toggle full screen" aria-label="Toggle full screen">&#10021;&#xFE0E; Full screen</button>';
    return toolbar;
  }

  function requestFullscreen(el) {
    var fn =
      el.requestFullscreen ||
      el.webkitRequestFullscreen ||
      el.msRequestFullscreen;
    if (fn) fn.call(el);
  }

  function exitFullscreen() {
    var fn =
      document.exitFullscreen ||
      document.webkitExitFullscreen ||
      document.msExitFullscreen;
    if (fn) fn.call(document);
  }

  function isFullscreen() {
    return !!(
      document.fullscreenElement ||
      document.webkitFullscreenElement ||
      document.msFullscreenElement
    );
  }

  function initGallery(gallery) {
    if (gallery.dataset.slideGalleryInit === "true") return;
    gallery.dataset.slideGalleryInit = "true";

    var images = Array.prototype.slice.call(gallery.querySelectorAll("img"));
    if (!images.length) return;

    var stage = document.createElement("div");
    stage.className = "slide-gallery__stage";

    var grid = document.createElement("div");
    grid.className = "slide-gallery__grid";

    images.forEach(function (img, i) {
      img.classList.add("slide-gallery__slide");
      img.loading = "lazy";
      stage.appendChild(img);

      var thumbBtn = document.createElement("button");
      thumbBtn.type = "button";
      thumbBtn.className = "slide-gallery__thumb";
      thumbBtn.dataset.index = String(i);
      thumbBtn.setAttribute("aria-label", "Go to slide " + (i + 1));

      var thumbImg = document.createElement("img");
      thumbImg.src = img.src;
      thumbImg.alt = img.alt || "Slide " + (i + 1);
      thumbImg.loading = "lazy";
      thumbBtn.appendChild(thumbImg);

      var label = document.createElement("span");
      label.className = "slide-gallery__thumb-label";
      label.textContent = i + 1;
      thumbBtn.appendChild(label);

      grid.appendChild(thumbBtn);
    });

    var toolbar = buildToolbar();
    gallery.textContent = "";
    gallery.appendChild(toolbar);
    gallery.appendChild(stage);
    gallery.appendChild(grid);
    gallery.tabIndex = 0;

    var counter = toolbar.querySelector(".slide-gallery__counter");
    var current = 0;

    function show(index) {
      current = Math.max(0, Math.min(images.length - 1, index));
      images.forEach(function (img, i) {
        img.hidden = i !== current;
      });
      counter.textContent = current + 1 + " / " + images.length;
      gallery.classList.remove("is-grid");
    }

    toolbar.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-action]");
      if (!btn) return;
      switch (btn.dataset.action) {
        case "prev":
          show(current - 1);
          break;
        case "next":
          show(current + 1);
          break;
        case "grid":
          gallery.classList.toggle("is-grid");
          break;
        case "fullscreen":
          if (isFullscreen()) {
            exitFullscreen();
          } else {
            requestFullscreen(gallery);
          }
          break;
      }
    });

    grid.addEventListener("click", function (e) {
      var btn = e.target.closest("button.slide-gallery__thumb");
      if (!btn) return;
      show(parseInt(btn.dataset.index, 10));
    });

    gallery.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight" || e.key === "ArrowDown") show(current + 1);
      if (e.key === "ArrowLeft" || e.key === "ArrowUp") show(current - 1);
      if (e.key === "Escape") gallery.classList.remove("is-grid");
    });

    show(0);
  }

  function init() {
    document.querySelectorAll(".slide-gallery").forEach(initGallery);
  }

  // mkdocs-material's instant navigation (navigation.instant) swaps page
  // content via XHR without a full reload, so DOMContentLoaded alone would
  // miss subsequent page views. `document$` fires on every content change,
  // including the very first one.
  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
