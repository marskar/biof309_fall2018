# Mac System Preferences
## In System Preferences > Keyboard > Keyboard:
### Key Repeat: Fast
### Delay Until Repeat: Short
### Caps Lock Key: Escape
## Remove most icons from Dock
## Drag and Drop Documents from Finder to the Dock in between Applications and Download
## 2-finger click on Dock and Turn Dock Hiding On
## Add Home to to Finder sidebar
## Under General > Appearance select 'Use Dark menu bar and Dock' and 'Automatically hide and show the menu bar'

# Install Karabiner-Elements from homepage dmg
https://pqrs.org/osx/karabiner/
### Could also try `brew cask install karabiner-elements`
### Under Complex modifications > Rules > Add Rule (Modifier Keys > Change caps_lock key (rev 2) > Change caps_lock to control if pressed with other keys, to escape if pressed alone.)

# Mac Terminal 
## Install homebrew (this also installs xcode tools needed for git)
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

## Install neovim
brew install neovim

## Install zsh
brew install zsh


## Install Fira Code Nerdfont
brew tap caskroom/fonts

brew cask install font-firacode-nerd-font

## In terminal, set Default background to black, text to white, and select Fura Code Nerdfont size 18

## Install iterm2
brew cask install iterm2

## In iterm2, select Fura Code Nerdfont size 18 in Profiles > Text > Change Font and check Use Ligatures

## Install chrome
brew cask install google-chrome

## Install keycastr
brew cask install keycastr

## Install shiftit
brew cask install shiftit

## Install flycut
brew cask install flycut

## Move [.gitconfig](https://raw.githubusercontent.com/marskar/biof309_fall2018/master/setup/.gitconfig), [.ideavimrc](https://raw.githubusercontent.com/marskar/biof309_fall2018/master/setup/.ideavimrc), [.pypirc](https://raw.githubusercontent.com/marskar/biof309_fall2018/master/setup/.pypirc), and [.vimrc](https://raw.githubusercontent.com/marskar/biof309_fall2018/master/setup/.vimrc) to ~ and change password in `.pypirc`

## Move [init.vim](https://raw.githubusercontent.com/marskar/biof309_fall2018/master/setup/init.vim) to ~/.config/nvim/
mkdir .config/

mkdir .config/nvim

## Install oh-my-zsh et al.

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

## Move [.zshrc](https://raw.githubusercontent.com/marskar/biof309_fall2018/master/setup/.zshrc) to ~ and restart terminal

# Python and R

## Install Anaconda: this includes vs code text editor
bash Downloads/Anaconda3-5.2.0-MacOSX-x86_64.sh

# Install PyCharm: no command line installer (only on Ubuntu using snap)
## Select MacOS X 10.5+ Keymap and add Hide All Tool Windows shortcut: Cmd+0 and Save As...: Cmd+Shift+S
## In Appearance & Behavior > Appearance, Use Dark Window headers and select Fura Code Nerd Font size 18
## In Editor > Font, select Fura Code Nerd Font size 18 and Enable font ligatures
## Check Change font size (Zoom) with Command+Mouse Wheel in Editor > General
## Check Show Whitespace in Editor > General > Appearance
## If you use the Deep Ocean Editor theme from the [Material UI](https://www.material-theme.com/) plugin, change docstring color to [`30B000`](https://www.beautycolorcode.com/30b000)
## Install [IdeaVim](https://github.com/JetBrains/ideavim) plugin
## Install [BashSupport](https://plugins.jetbrains.com/plugin/4230-bashsupport) plugin
## Install [R Language Support](http://holgerbrandl.github.io/r4intellij/) plugin

## Install RStudio and `r-essentials` (RStudio is not working for me right now)
conda install -y rstudio
