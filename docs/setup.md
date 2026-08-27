# Before The Course

This page collects the practical setup tasks from Day 0 into one place so participants can prepare their workstation before the course starts.

## Prerequisites Checklist

- [ ] You have a laptop with permission to install software.
- [ ] You can connect to the internet and sign in to GitHub.
- [ ] You know which email address to use for your Git commits.
- [ ] You have access to an R installation if you plan to follow the R-based examples.

## Install Git

=== "Mac"

    It is highly recommended to install and use the package manager **Homebrew** for many programs, including git. If you do not have Homebrew installed follow the instructions on [Homebrew](https://brew.sh).

    Once Homebrew is installed, install Git using command:

    ```sh
    brew install git
    ```

    Git might already be installed on your system bundled with **Xcode Command Line Tools** If not you can install **Xcode Command Line Tools**. 

    ```sh
    xcode-select --install
    ```
    A dialog will appear; click **Install** and wait for it to finish. 

    Confirm the installation:

    ```sh
    git --version
    ```

=== "Linux"

    Use your distribution's package manager:

    ```sh
    # Debian / Ubuntu
    sudo apt update && sudo apt install git

    # Fedora
    sudo dnf install git

    # Arch
    sudo pacman -S git
    ```

    Confirm the installation:

    ```sh
    git --version
    ```

=== "Windows"

    Download and run the installer from [git-scm.com/downloads](https://git-scm.com/downloads/win).

    During setup:

    - Leave the default editor as-is (or choose one you know).
    - On the **"Adjusting your PATH environment"** screen, keep the recommended option
      **"Git from the command line and also from 3rd-party software"**.
    - Accept all other defaults unless your local IT policy requires something else.

    After installation, open **Git Bash** (installed alongside Git) or **PowerShell** and confirm:

    ```powershell
    git --version
    ```

After installing, check your configurations
```sh
git config --list --show-origin
```

Set your identity so commits are attributed correctly:

```sh
git config --global user.name "Your Name"
git config --global user.email "you@example.org"
```

## Install Positron

=== "Mac"

    Again you can use Homebrew to install positron

    ```sh
    brew install positron
    ```
    Or, do it manually:

    1. Go to [positron.posit.co](https://positron.posit.co/) and click **Download**.
    2. Open the downloaded `.dmg` file, drag **Positron** into your **Applications** folder.
   
    Launch Positron from Applications. If macOS shows a security dialog the first time,
        open **System Settings → Privacy & Security** and click **Open Anyway**.

=== "Linux"

    1. Go to [positron.posit.co](https://positron.posit.co/) and download the `.deb` or `.rpm`
       package that matches your distribution.
    2. Install it:

        ```sh
        # Debian / Ubuntu (.deb)
        sudo dpkg -i positron-*.deb
        sudo apt-get install -f   # fix any missing dependencies

        # Fedora / RHEL (.rpm)
        sudo rpm -i positron-*.rpm
        ```

    3. Launch Positron from your application menu or by running `positron` in a terminal.

=== "Windows"

    1. Go to [positron.posit.co](https://positron.posit.co/) and click **Download**.
    2. Run the downloaded `.exe` installer and follow the prompts, accepting the defaults.
    3. Launch **Positron** from the Start menu.

After launching, open a local folder so you are ready to work with course materials on Day 0 and Day 2.

## Refresh The Basics

Use the precourse material to make sure these basics are familiar before live sessions begin:

- opening a project folder in an editor
- creating and saving plain text files
- understanding folders, file paths, and working directories
- running basic R code if you will follow the R examples

## Verify Your Setup

Run through this final check before the course starts:

- [ ] `git --version` works in a terminal.
- [ ] Your global Git `user.name` and `user.email` are configured.
- [ ] Positron starts successfully.
- [ ] You can open a local folder in Positron.
- [ ] You have reviewed the [Setup instructions](setup.md).
