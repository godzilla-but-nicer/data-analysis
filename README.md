# Data Analysis Track

## Computing Set Up

Here are some things you will need to do all of the work in the data analysis
track.

### Access to a Unix-like terminal

If you are reading this from mac or some flavor of linux, congratulations!
You've done it! If you are on windows, you have a choice to make. One option is
to translate command line instructions into Windows PowerShell commands.
Another, better, option is to install linux using Windows Subsystem for
Linux (WSL). This is an official Microsoft tool for installing a linux
distribution inside of your Windows.

The official installation guide for installing linux using WSL can be found 
[at this link](https://learn.microsoft.com/en-us/windows/wsl/install) but it
boils down to this:

1. Open Windows Command Prompt as administrator
1. Type `wsl --install`
1. Wait a little bit, maybe type 'confirm' or whatever
1. Restart your computer

Following this reboot, if you run Command Prompt and enter `wsl` your terminal
will be transformed to a bona fide Ubuntu terminal.

### git

Your computer likely already has git. You can find out by typing `git --version`
into your terminal. If it says something other than "command not found" then
you have git. If your terminal really can't find the git command you can install
it with `sudo apt-get install git` for Debian/Ubuntu. If you're using fancy
linux you probably already know how to install packages.

On MacOS we have an extra step. First, install [homebrew](https://brew.sh/)
by running the following command to start the interactiove homebrew installer:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Now you can install git with `sudo brew install git`

### mamba

It's probably for the best that we're all using roughly the same version of
Python. We're also going to be using a lot of external libraries. The simplest
way to resolve these two issues is to use something like [Anaconda](https://www.anaconda.com/download)
we're going to use a faster, lighter version called
[miniforge](https://github.com/conda-forge/miniforge), this will give us a cool
called `mamba`First, we'll download the install script with:

```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

If that doesn't work, try:

```
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

Now we can run the script with `bash Miniforge3-$(uname)-$(uname -m).sh`. The
installer will ask if you want to "initialize" your terminal at the end. For now,
say yes. This just means that all terminal sessions will start inside a virtual
environment.

You may have to close and open back up your terminal but you should now see the
text `(base)` in front of your prompt. You will now have access to the `mamba`
command. This tool will keep track of different versions of python and
python packages for you and allow you to switch between them easily.

### vscode

You don't have to use [vscode](https://code.visualstudio.com) to edit code but
it is a very good editor. Ignore the marketing copy. You are welcome to use
any text editor you feel comfortable using. I use vscode so when I show my
screen it will usually be vscode. For linux and macOS you can just use the
website and install it like anything else.

If you're using WSL, its basically the same but you need to be a little careful.
You'll install vscode for windows but make sure you
read the options as you are installing it. At some point it will ask you
something about your `PATH`, make sure to say yes.

Regardless of your OS, after installation you can launch vscode from the
terminal with the command `code`. Its worth opening it and poking around a
bit. It will probably suggest you install some extensions for Python or
better WSL support and they are probably worth installing.

### A GitHub Account

Sorry for the back-to-back Microsoft recs. A decade or so ago they intentionally
bought up a bunch of stuff in the open-source world and now here we are. We will
use [GitHub](https://github.com/) to share code. After making your account, take
a look at [our class repo](https://github.com/godzilla-but-nicer/data-analysis)
(I may or may not have put code there by the time you do). Press the fork button
to get your own copy of the repo that tracks the changes I make to the original.
I'll let yall know when there is actually stuff there.
