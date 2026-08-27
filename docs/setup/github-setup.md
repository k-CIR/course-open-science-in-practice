# Setup GitHub

This guide covers creating a GitHub account and connecting your local Git installation to GitHub via SSH or HTTPS.

## Create a GitHub account

1. Go to [github.com/signup](https://github.com/signup).
2. Enter your **email address**, create a **password**, and choose a **username**.
3. Complete the verification steps GitHub shows.
4. On the **"Choose your plan"** page, select the **Free** plan unless your organization requires otherwise.
5. Check your email for a verification link and confirm your address.

## Use a university email or GitHub Student Developer Pack

If you are a student or academic staff, you can use your university email address when creating your account and claim the **GitHub Student Developer Pack**.

### Register with your university email

1. On the GitHub signup page, enter your **university email address** instead of a personal one.
2. Complete the rest of the account setup as usual.
3. Verify the address using the confirmation email sent to your university inbox.

### Claim the Student Developer Pack

The pack gives free access to tools, cloud credits, and learning resources while you study.

1. Go to [education.github.com/pack](https://education.github.com/pack).
2. Click **Get student benefits** and sign in with your GitHub account.
3. Follow the instructions to verify your student status.
4. GitHub usually accepts:
      - A university email address
      - A student ID
      - Proof of enrollment from your school

If GitHub asks for additional proof, upload a photo or scan of your student ID or an enrollment certificate.

### Benefits you may get

- Free private repositories with unlimited collaborators
- Free domain names
- Cloud credits from major providers
- Developer tools and learning platforms

## Configure your Git identity

Make sure Git knows your name and email. Use the same email you used for GitHub so commits are linked to your account.

```sh
git config --global user.name "Your Name"
git config --global user.email "you@example.org"
```

You can verify the settings with:

```sh
git config --list --show-origin
```

## Connect Git to GitHub

GitHub supports two main ways to authenticate:

- **SSH** — recommended for daily use. No password prompts after setup.
- **HTTPS** — simpler for beginners, but you will authenticate on every push unless you use a credential helper.

### Option A — SSH (recommended)

SSH lets Git talk to GitHub without typing your password every time. It uses a key pair stored on your machine.

#### 1. Generate an SSH key

=== "Mac"

    Open Terminal and run:

    ```sh
    ssh-keygen -t ed25519 -C "you@example.org"
    ```

    Press **Enter** to accept the default file location (`~/.ssh/id_ed25519`).
    Optionally set a passphrase for extra security.

    If your system does not support `ed25519`, use:

    ```sh
    ssh-keygen -t rsa -b 4096 -C "you@example.org"
    ```

=== "Linux"

    Open a terminal and run:

    ```sh
    ssh-keygen -t ed25519 -C "you@example.org"
    ```

    Press **Enter** to accept the default file location (`~/.ssh/id_ed25519`).
    Optionally set a passphrase for extra security.

    If your system does not support `ed25519`, use:

    ```sh
    ssh-keygen -t rsa -b 4096 -C "you@example.org"
    ```

=== "Windows"

    Open **Git Bash** and run:

    ```sh
    ssh-keygen -t ed25519 -C "you@example.org"
    ```

    Press **Enter** to accept the default file location (`/c/Users/YourName/.ssh/id_ed25519`).
    Optionally set a passphrase for extra security.

    If you see an error about `ed25519`, use:

    ```sh
    ssh-keygen -t rsa -b 4096 -C "you@example.org"
    ```

#### 2. Add the SSH key to the ssh-agent

=== "Mac"

    ```sh
    eval "$(ssh-agent -s)"
    ssh-add --apple-use-keychain ~/.ssh/id_ed25519
    ```

=== "Linux"

    ```sh
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

=== "Windows"

    In Git Bash:

    ```sh
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

#### 3. Copy the public key to your clipboard

=== "Mac"

    ```sh
    pbcopy < ~/.ssh/id_ed25519.pub
    ```

=== "Linux"

    ```sh
    cat ~/.ssh/id_ed25519.pub
    ```

    Select and copy the output, or use:

    ```sh
    xclip -sel clip < ~/.ssh/id_ed25519.pub
    ```

    If `xclip` is not installed:

    ```sh
    sudo apt install xclip
    ```

=== "Windows"

    In Git Bash:

    ```sh
    cat ~/.ssh/id_ed25519.pub
    ```

    Select the output and copy it with **Ctrl+Shift+C**, or open the file in Notepad:

    ```sh
    notepad ~/.ssh/id_ed25519.pub
    ```

#### 4. Add the key to GitHub

1. In GitHub, click your avatar → **Settings**.
2. In the left sidebar, click **SSH and GPG keys**.
3. Click **New SSH key**.
4. Paste your key into the **Key** field.
5. Give it a title like `Work laptop`.
6. Click **Add SSH key**.

### Option B — HTTPS

If you prefer HTTPS, use the repository URL that starts with `https://github.com/...`.

#### Use a credential helper

So you do not have to type your username and password on every push.

=== "Mac"

    ```sh
    git config --global credential.helper osxkeychain
    ```

=== "Linux"

    ```sh
    git config --global credential.helper cache
    ```

    Or for longer caching:

    ```sh
    git config --global credential.helper 'cache --timeout=3600'
    ```

=== "Windows"

    ```sh
    git config --global credential.helper manager-core
    ```

Git Credential Manager will prompt for credentials once and store them securely.

## Verify the connection

```sh
ssh -T git@github.com
```

You should see a message like:

```text
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see a warning about the host fingerprint, that is expected on first use. Type `yes` to continue.

## Test with a real repository

### Clone an existing repository

```sh
git clone git@github.com:<owner>/<repo>.git
```

Replace `<owner>` and `<repo>` with a real GitHub repository path. If you do not have one yet, create a new empty repository on GitHub and clone it.

## Troubleshooting

- **Permission denied (publickey)**  
  Make sure you added the correct public key to GitHub and that the ssh-agent is running with the private key loaded.

- **Host key verification failed**  
  Remove stale GitHub entries from `~/.ssh/known_hosts` and try the `ssh -T` test again.

- **HTTPS keeps asking for a password**  
  Enable the credential helper for your OS above, or switch to SSH.

- **Commits show the wrong author on GitHub**  
  Double-check that `git config user.email` matches the email on your GitHub account.

## Checklist

- [ ] You have a GitHub account with a verified email.
- [ ] Your global Git `user.name` and `user.email` are configured.
- [ ] You can run `ssh -T git@github.com` successfully.
- [ ] You can clone or push to a GitHub repository.
