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

## Connect Git to GitHub

You can set up an SSH key pair on your computer and connect it to your github account. That way Github automatically knows your computer is you and allows you to push and pull from your repositories, without having to enter your password every time you connect. 

To do this, you need to generate an SSH key pair (one private and one public key) on your local machine. These are created as two separate files. You then add the public key to your GitHub account. The private key should stay on your computer, be kept secret and never shared with anyone.

It's called a key-pair, but really you can think of it as a lock (public key) and a key (private key). You generate a key pair, put the lock (public key) on the service you want to access and keep the key (private key) on your local machine. When you connect, the service checks if you have the right key to unlock the lock.

GitHub supports two main ways to authenticate:

#### 1. Generate an SSH key

=== "Mac"

    Open Terminal and run:

    ```sh
    ssh-keygen -t ed25519 -C "you@example.org"
    ```

    Press **Enter** to accept the default file location (`~/.ssh/id_ed25519`).
    Optionally set a passphrase for extra security, but this kind of defeates the purpose of using SSH keys as you will have to type it in every time you use the key.

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

Your computer runs an "SSH agent" that manages your keys in the background. You need to add your private key to the agent so it can be used for authentication.

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

Copy your public key to your clipboard so you can add (paste) it to GitHub.

It will look something like: <br>
`ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK0wmN/Cr3JXqmLW7u+g9pTh+wyqDHpSQEIQczXkVx9q email.address@internet.com`

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

    In Git Bash, print your public in the terminal:

    ```sh
    cat ~/.ssh/id_ed25519.pub
    ```

    Select the output and copy it. 
    
    Alternatively, you can open the public key file (`~/.ssh/id_ed25519.pub`) in a text editor and copy it from there. Where your home directory is located is sometimes a mystery on windows, but it is usually in `C:\Users\<YourName>\.ssh\`.

#### 4. Add the key to GitHub

1. In GitHub, click your avatar/portrait in the top right corner → **Settings**.
2. In the left sidebar, click **SSH and GPG keys**.
3. Click **New SSH key**.
4. Paste your key into the **Key** field.
5. Give it a title like `Work laptop`.
6. Click **Add SSH key**.
7. You will have to authenticate with your GitHub password to confirm.

## Verify the connection

```sh
ssh -T git@github.com
```

You should see a message like:

```text
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see a warning about the host fingerprint, that is expected on first use. Type `yes` to continue.

## Checklist

- [x] You have a GitHub account with a verified email.
- [x] You have an ssh key-pair generated and with the public key added to your GitHub account.
- [x] You can run `ssh -T git@github.com` successfully.

.. now make sure you have [R installed](./install-r.md), go [setup Positron](./positron-setup.md) and you'll be ready to start the course!

## Bonus: Clone a public repository
You can try to clone a public repository from GitHub to your local machine to make sure everything is working. For example, running this command in your terminal:

```sh
git clone git@github.com:NiklasEdvall/an-approved-repo.git
```

.. will clone [this example repository](https://github.com/NiklasEdvall/an-approved-repo) to your local machine. You can then navigate into the directory and check the files.
