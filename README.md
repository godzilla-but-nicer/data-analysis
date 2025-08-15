# Data Analysis

## Pre-class assignment

There is a lot of data out there, very little of it has been examined by folks
who genuinely want to make a better world and aren't pressured by the need to
publish academic articles or increase shareholder value or whatever. There is a
ton we can learn with just a little effort.

Throughout the week, we will develop the skills needed to ask and answer
questions from empirical data. Before we meet, I would like you to start
thinking about what kinds of questions you want answered. We might not be able
to answer them but we can certainly make progress. At the end of the week,
everyone will present a sort of final report. What goes in there is up to you.
My hope is that we can all work toward answering some of the questions we come
in with.

### Asking Questions

We all know that we don't know much. I'm sure that all of us have a ton of
questions about the world. Pick some.

Its okay to start really broad, something like "How does protest spread?" As we
get to work on what data seems useful and available, we will find new, more
immediately answerable questions. Something like "How much does number of
participants in a protest movement change the day after a NYT headline about
it?"

Its also ok to start dumb, I began working on course materials with the
question, "Can I find evidence of cocaine use in the Enron bankrupcy emails?"
I'd like to think I found some interesting things anyway. Maybe not quite so
dumb but certainly more obvious, we could ask "Do golf courses use a lot of
water?" We'll still be tripping over interesting findings.

Come up with some questions and write them down.

### Finding Data

Its pretty easy to find data if you know where to look. You might not find data
for your exact questions but you can probably start to answer the question
anyway. I probably can't find really good data on police encounters in
Bloomington, IN following the Palestinian solidarity emcampments but I probably
can for police encounters in New York.

The way I see it, we'll probably all want a sort of "core" dataset to work from.
Something really meaty we think we can get a lot out of. We want to learn about
protest so we go find a dataset about My advice is to start
in one of these places.

1. [Distributed Denial of Secrets](https://ddosecrets.org)
    - This is a sort of WikiLeaks 2. DDoSecrets is a repository for hacked and
      leaked datasets. Many of these are absolutely massive. For example, this
      dataset of hacked material from the [Israel Ministry ofJustice](https://ddosecrets.com/article/israel-ministry-of-justice) is
      245GB
1. [Data is Plural](https://www.data-is-plural.com/) Newsletter
    - Its a little silicon valley coded but this site has a ton of interesting
      stuff. I found the [Deportation Data Project](https://deportationdata.org/) through
      Data is Plural.

In addition, we might find ourselves wanting some additional data to help us
answer questions. Maybe we want to control for population size when we look
at water pollution around closed chemical factories. Population numbers are
probably not in our closed chemical factory dataset. We have to find that
elsewhere. Here are some good places to look for supplemental data like this.

1. Data is Plural again
    - Seriously there's so much weird stuff in there. Here's a dataset of
    [millions of newswire
    articles](https://huggingface.co/datasets/dell-research-harvard/newswire)
    written between 1878 and 1977 that I found on there. Is it useful? Probably
    no one (who isn't interested in training generative AI) knows.
1. The U.S. Government :salute-emoji:
    - most agencies publish data. A lot of it is really useful. We can get a ton
    of good economic and demographic data from big agencies like the census and
    the IRS. We can also get a lot of other stuff from FEMA, HHS, whoever.
1. [FiveThirtyEight's Old GitHub](https://github.com/fivethirtyeight/data)
    - They collected a ton of stuff and its just still there
1. Googling ["{thing-you-want-to-find} github data"](https://duckduckgo.com/?q=tweets+from+us+senators+github+data&t=newext&atb=v362-1&ia=web)
    - This works a surprising amount of the time

### Datasets I am bringing on a hard drive

I'm bringing some data on a hard drive. Here's what I've got at the time of
writing. If you want to use these, I'll have them.

1. Various kinds of census and other population data
    - State-level, City-level, something that appears to be individual level???
1. Various kinds of income and wealth data
    - state-level, city-level
1. The Enron Email Corpus
    - This is a [famous](https://en.wikipedia.org/wiki/Enron_Corpus) dataset of
    emails collected as evidence during Enron's bankrupcy trial. Its easy and
    fun to work with! (fuck me, in writing this I found a [more complete version](https://ddosecrets.com/article/enron-emails))
1. The Deportation Data Project (mentioned above) July 2025 release
    - Extremely cool dataset consisting of individual ICE encounters, arrests,
      detentions, and deportations.
1. [BlueLeaks](https://ddosecrets.com/article/blueleaks)
    - 300 GB of leaked internal police documents from around the world released
    in 2020.
1. [Heritage Foundation Emails](https://ddosecrets.com/article/heritage-foundation)
    - 1GB or so of leaked Heritage Foundation stuff. Mostly emails I think.
1. [American Golf](https://ddosecrets.com/article/american-golf)
    - Recently released hacked dataset of internal documents from a corporation
    that operates golf courses all over the country. ~100GB
1. [Israeli Defense Force](https://ddosecrets.com/article/israel-defense-forces-anonymous-for-justice)
    -Hacked materials from IDF, released in 2024, ~20GB
1. Handful of small datasets on protests
    - What I could find easily, idk.
1. [Billionares](https://www.piie.com/publications/working-papers/origins-superrich-billionaire-characteristics-database?ResearchID=2917)
    - A handful of characteristics from 2000 billionares

## Computing Set Up

Here are some things you will need to do all of the work in the course. I don't
nessecarily care that you use these specific tools, only that your computing
environment has the capabilities provided by these tools.

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
use [GitHub](https://github.com/) to share code. After making your account, DM
me on element and I'll add you to [our class
repo](https://github.com/godzilla-but-nicer/data-analysis) (I may or may not
have put code there by the time you do). I'll probably make it public later if
yall are cool with that but for now its invite only. Press the fork button if
you would like to get your own copy of the repo that tracks the changes I make
to the original. I'll let yall know when there is actually stuff there.
