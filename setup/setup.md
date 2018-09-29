# change keyboard settings 
## Key Repeat: Fast
## Delay Until Repeat: Short
## Caps Lock Key: Escape
# Remove most icons from Dock
# Add Documents in between Applications and Download in Dock
# Turn Dock Hiding on
# Under General > Appearance select Use Dark menu bar and Dock and Automatically hide and show the menu bar

# Install homebrew (this also installs xcode tools needed for git)
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# install chrome
brew cask install google-chrome

# install keycastr
brew cask install keycastr

# install shiftit
brew cask install shiftit

# install flycut
brew cask install flycut

# install Anaconda: this includes vs code text editor
bash Downloads/Anaconda3-5.2.0-MacOSX-x86_64.sh

# install PyCharm: no command line installer (only on Ubuntu using snap)
## Select MacOS X 10.5+ Keymap and add Hide All Tool Windows shortcut: Cmd+0
## In Appearance & Behavior > Appearance, Use Dark Window headers and select Fura Code Nerd Font size 18
## In Editor > Font, select Fura Code Nerd Font size 18 and Enable font ligatures

# move .gitconfig, .ideavimrc, and .vimrc to ~

# install Fira Code Nerdfont
brew tap caskroom/fonts

brew cask install font-firacode-nerd-font

# In terminal, set Default background to black, text to white, and select Fira Code size 18

# install iterm2
brew cask install iterm2

# In iterm2, select Fira Code size 18 in Profiles > Text > Change Font and check Use Ligatures

# install neovim
brew install neovim

# move init.vim to ~/.config/nvim/
mkdir .config/

mkdir .config/nvim


# zsh
