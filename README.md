
# Task Management System
This project helps with managing tasks assigned to each member of the company.

## How does it work ?
The program works with two text files, user.txt and tasks.txt.

 * The tasks.txt stores a list of all the tasks that the team is working on.
 * The data for each task is stored on a separate line in the text file. Each line includes the following data about a task in this order:
    * The username of the person to whom the task is assigned.
    * The title of the task.
    * A description of the task.
    * The date that the task was assigned to the user.
    * The due date for the task.
    * Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.
 
 * The user.txt stores the username and password for each user that has permission to use the program
 * The username and password for each user must be written to this file in the following format:
    * First, the username followed by a comma, a space and then the password.
    * One username and corresponding password per line.

When the program is executed it prompts the user to enter the username and password, if the user is not registered they are denied access.
* When the user has been successfully granted access, the menu is printed.
* From the menu the user can choose to register the user, add task, view all the task, view assigned tassks or exit the program.
* If the user chooses to register the user, the program prompts him to enter the new username and password and store the information on user.txt
* If the the user chooses add task the user will be prompted to enter name of the person the task will assgined to,  the title of
  the task, a description of the task and the due date of the task. The data about the new task will be stored in tasks.txt file.
* If the user chooses to view all the tasks, the tasks will printed in a user-friendly manner.
* If the user chooses to view his tasks, all the tasks assigned to him will be printed in user-friendly manner.
## Installation

### Installing Git on windows
Check if Git is already installed on windows
    git  --version
If the version is not shown and command not printed rather, the Git is not installed

#### To install Git on windows follow the following steps:
    1. If Git is not installed navigate to the Git website’s download page(https://git-scm.com/download/win) on windows
    2. Double click on recent version og Git to download Git for windows
    3. When you seen an install prompt, click yes
    4. Agree to the GNU license terms:
    5. Select the directory you want Git to be installed in or use default location.
    6. Select the components that you want to install. If you are unsure, go ahead with the default selection.
    7. Choose the default editor for Git
    8. Select how you want to use Git from the command line from the options that are presented
    9. Select the SSL/TLS library that you want Git to use for HTTPs connections.
    10. Select how Git should treat the line endings in text files
    11. Select your terminal emulator, default behavior of git pull, and some extra configuring options.
    12. For the simplest installation, keep MinTTY for the terminal emulator, use the default behavior (fast-forward or merge), and enable file system caching in configuring extra options. When you are done selecting your configuration options, click Install at the end
    13. Click on Finish. You should have a working Git installation on your Windows machine.

### Installing Git on Mac
Check if Git is already installed on Mac
    git  --version
If the version is not shown and command not printed rather, the Git is not installed

#### To install Git on Mac follow the following steps:
    1. Execute the following command /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" on Mac terminal
    2. Press return once you are prompted. You should see an installation success message once the installation is complete.
    3. The Homebrew version you just installed may not be the most recent stable build. Therefore, it’s a good practice to update it. To update Homebrew, enter the following command in your terminal.
    4. Finally, to install Git run.

### Installing Git on Linux
Check if Git is already installed on Linux
    git  --version

If you need to install Git, your terminal shows the following error (-bash: git: command not found)
If your terminal confirms that there’s no pre-installed version of Git, move on to the next section that is appropriate for your Linux system’s distribution.

#### To install on Git on Ubuntu or Debian follow the following steps:
    1. To install Git run the following command (sudo apt install git)
    2. If you see an error, consider running the following command before you install Git for Ubuntu(sudo apt update)

##### Installing Git on CentOS
    1. Option 1: Installing Git on CentOS using Yum
        To install Git on CentOS using Yum, run the following command:
            sudo yum install git
    2. In order to install Git from source install its dependencies first using the following commands:
            sudo yum group install “Development tools”
            sudo yum install gettext-devel openssl-devel perl-CPAN perl-devel zlib-devel
    3. Now, go to Git’s release (https://github.com/git/git/releases) page and select the version that you prefer to install. Find a stable Git version (select the one without an -rc suffix):
    4. After finding the right Git version, click on it. You should see two files included in the release version you selected (with .zip and tar.gz extensions).
    5. Right click and copy the link for the file with the tar.gz extension. For example, if you selected the version v2.29.1, your download link is (https://github.com/git/git/archive/v2.29.1.tar.gz).
    6. Use wget to download your selected Git version on CentOS. Replace the example URL with the one you copied in the previous step.
            wget https://github.com/git/git/archive/v2.29.1.tar.gz -O gitdownloadversion.tar.gz
            This command downloads v2.29.1.tar.gz as gitdownloadversion.tar.gz.
    7. Unpack the file using tar. Decompress it and the extract files using the -zxf option. Use the following command to do it:
            ar -zxf gitdownloadversion.tar.gz
    8. Change your directory to the unpacked folder:
            cd gitdownloadversion-*
    9. Create a Makefile in this directory to help compile the downloaded Git files:
            make configure
            ./configure --prefix=/usr/local
    10. Once your Makefile is in place, compile your Git files using:
            sudo make install
    11. When completed, check the Git version to ensure the installation was successful.
            git --version

### Installing Git on Fedora
    Similar to CentOS, installing Git on Fedora can be done using two options:
        Install Git using Yum
        Install Git from source

    The process to install Git from source is similar to the CentOS installation above. To install Git using Yum on Fedora, enter the following command:
        sudo yum install git-core

    Once successful, view the Git version that is running to confirm the installation:
        git --version

### Installing Git on Arch Linux
    To install Git on Arch Linux using pacman, run the following command:
        sudo pacman -Sy git

### Installing Git on Gentoo
    You can install Git on Gentoo using emerge:
        sudo emerge --ask --verbose dev-vcs/git

## Contributing
Contributions are always welcome!

1. Fork (copy) the repository ()
2. Clone the fork of your repository
3. Make edits to your local cloned repository on your computer by the following steps:
4. Create your feature branch: (`git checkout -b my-new-feature`)
5. Commit your changes: `(git commit -am 'Add some feature'`)
6. Push edits back to your on GitHub repository copy : (`git push origin my-new-feature`)
7. Submit a pull request  for your edits to be added to the original repository


## Authors
- [@aneletyesi](https://www.github.com/shakes1520)


## Acknowledgements
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [linode guides and turorial](https://www.linode.com/docs/guides/)
 - [open-source-guide](https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md)
## Used By

This project is used by the following :
- Registered users of the company

## License

[Python License v-3.10.4](https://docs.python.org/3/license.html#psf-license-agreement-for-python-release)

