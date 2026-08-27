# Setup Git

=== "Mac"

    It is highly recommended to install and use the package manager **Homebrew** for many programs, including git. If you do not have Homebrew installed follow the instructions on [Homebrew](https://brew.sh).

    Once Homebrew is installed, install Git using command:

    ```sh
    brew install git
    ```

    Git might already be installed on your system bundled with **Xcode Command Line Tools** If not you can install **Xcode Command Line Tools** with `xcode-select --install`

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
