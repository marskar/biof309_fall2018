
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
# TERM=xterm-256color
ZSH_THEME="powerlevel9k/powerlevel9k"
POWERLEVEL9K_MODE='nerdfont-complete'
# SABLE_AUTO_TITLE="true"

POWERLEVEL9K_BATTERY_CHARGING='yellow'
POWERLEVEL9K_BATTERY_CHARGED='green'
POWERLEVEL9K_BATTERY_DISCONNECTED='$DEFAULT_COLOR'
POWERLEVEL9K_BATTERY_LOW_THRESHOLD='10'
POWERLEVEL9K_BATTERY_LOW_COLOR='red'
POWERLEVEL9K_BATTERY_ICON='\uf1e6 '
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=''
# POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX='\uf0da'
POWERLEVEL9K_VCS_GIT_ICON='\ue60a'
POWERLEVEL9K_VCS_CLEAN_FOREGROUND='black'
POWERLEVEL9K_VCS_CLEAN_BACKGROUND='green'
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='11'
POWERLEVEL9K_VCS_UNTRACKED_FOREGROUND='black'
POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='09'
#POWERLEVEL9K_VCS_UNTRACKED_ICON='?'


POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(vi_mode)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status vcs dir time background_jobs ram virtualenv anaconda battery)

POWERLEVEL9K_SHORTEN_STRATEGY="truncate_from_right"
POWERLEVEL9K_SHORTEN_DIR_LENGTH=3

#POWERLEVEL9K_CUSTOM_TIME_FORMAT="%D{\uf017 %H:%M:%S}"
POWERLEVEL9K_TIME_FORMAT="%D{\uf017 %H:%M \uf073 %d.%m.%y}"

POWERLEVEL9K_STATUS_VERBOSE=false
#https://github.com/bhilburn/powerlevel9k
#POWERLEVEL9K_PROMPT_ON_NEWLINE=true
#POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX="↱"
#POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX="↳ "

POWERLEVEL9K_DIR_HOME_BACKGROUND="blue"
POWERLEVEL9K_DIR_HOME_FOREGROUND="black"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND="cyan"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="black"
POWERLEVEL9K_DIR_DEFAULT_BACKGROUND="magenta"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="black"

# Vi-Mode
POWERLEVEL9K_VI_MODE_INSERT_FOREGROUND='white'
POWERLEVEL9K_VI_MODE_INSERT_BACKGROUND='black'

POWERLEVEL9K_VI_MODE_NORMAL_FOREGROUND='red'
POWERLEVEL9K_VI_MODE_NORMAL_BACKGROUND='black'
# Set list of themes to load
# Setting this variable when ZSH_THEME=random
# cause zsh load theme from this variable instead of
# looking in ~/.oh-my-zsh/themes/
# An empty array have no effect
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.

# https://github.com/zsh-users/zsh-autosuggestions
# https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md
# https://github.com/zsh-users/zsh-syntax-highlighting
# https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md
plugins=(git zsh-autosuggestions brew zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
export EDITOR='nvim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

alias v="nvim"
alias c="calcurse"
alias r="ranger"
# alias python=python3
# export PATH=/usr/local/bin/python3:$PATH
export PATH=/Users/skarzynskimw/anaconda3/bin:$PATH
#export PATH=/Users/skarzynskimw/anaconda3/lib:$PATH
# export PATH="/usr/local/opt/python/libexec/bin:$PATH"
# taken from https://dougblack.io/words/zsh-vi-mode.html
bindkey -v

bindkey '^P' up-history
bindkey '^N' down-history
bindkey '^?' backward-delete-char
bindkey '^h' backward-delete-char
bindkey '^w' backward-kill-word
# bindkey '^r' history-incremental-search-backward

# taken from https://emily.st/2013/05/03/zsh-vi-cursor/
function zle-keymap-select zle-line-init
{
    # change cursor shape in iTerm2
    case $KEYMAP in
        vicmd)      print -n -- "\E]50;CursorShape=0\C-G";;  # block cursor
        viins|main) print -n -- "\E]50;CursorShape=1\C-G";;  # line cursor
    esac

    zle reset-prompt
    zle -R
}

function zle-line-finish
{
    print -n -- "\E]50;CursorShape=0\C-G"  # block cursor
}

zle -N zle-line-init
zle -N zle-line-finish
zle -N zle-keymap-select

export KEYTIMEOUT=1

prompt_context() {}

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

