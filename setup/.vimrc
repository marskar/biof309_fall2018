if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.vim/bundle')
Plug 'junegunn/vim-plug'

" Required
Plug 'Shougo/unite.vim'

" Visuals
Plug 'dracula/vim'
Plug 'Yggdroot/indentLine'

Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-repeat'
Plug 'tpope/vim-abolish'
Plug 'tpope/vim-commentary'
Plug 'tommcdo/vim-exchange'
Plug 'kien/ctrlp.vim'
Plug 'godlygeek/tabular'
Plug 'sjl/gundo.vim'
Plug 'terryma/vim-multiple-cursors'
Plug 'raimondi/delimitmate'
call plug#end()

set fileencodings+=utf-8
set encoding=utf-8

syntax enable
" let g:solarized_termcolors=256
set background=dark

" Configuration

" Theme: Dracula
color dracula

" vim-airline
let g:airline#extensions#tabline#enabled=1
let g:airline_powerline_fonts=1
set laststatus=2

" indentLine
let g:indentLine_enabled = 1
let g:indentLine_char = "⟩"

" Share system clipboard ("+) and unnamed ("") registers
" http://vimcasts.org/episodes/accessing-the-system-clipboard-from-vim/
" http://vimcasts.org/blog/2013/11/getting-vim-with-clipboard-support/
set clipboard=unnamed
if has('unnamedplus')
  set clipboard=unnamed,unnamedplus
endif
set go+=a
"Include some of the neovim defaults, others below
set autoindent
set autoread
set backspace=indent,eol,start
set belloff=all
set complete=.,w,b,u,t,i
set display+=lastline
set formatoptions=tcqj
set history=10000
set laststatus=2
set tabpagemax=50

" taken from https://www.johnhawthorn.com/2012/09/vi-escape-delays/
set timeoutlen=1000 ttimeoutlen=10

" Change the shape of the cursor in different modes, as per: http://vim.wikia.com/wiki/Change_cursor_shape_in_different_modes
let &t_SI = "\<Esc>]50;CursorShape=1\x7"
let &t_SR = "\<Esc>]50;CursorShape=2\x7"
let &t_EI = "\<Esc>]50;CursorShape=0\x7"

if exists('$TMUX')
  let &t_SI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=1\x7\<Esc>\\"
  let &t_SR = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=2\x7\<Esc>\\"
  let &t_EI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=0\x7\<Esc>\\"
else
  let &t_SI = "\<Esc>]50;CursorShape=1\x7"
  let &t_SR = "\<Esc>]50;CursorShape=2\x7"
  let &t_EI = "\<Esc>]50;CursorShape=0\x7"
endif

" Don't try to be backwards compatible with vi
set nocompatible

" Underline the line the cursor is on
set cursorline

" (In times of great desperation) allow use of the mouse
set mouse=a

" Show partially typed commands in the statusline
set showcmd

" use hybrid (absolute and relative) numbers
set number relativenumber

filetype plugin on

" enable builtin matchit package
packadd! matchit

" Copied from https://github.com/mcantor/no_plugins

" FINDING FILES:

" Search down into subfolders
" Provides tab-completion for all file-related tasks
set path+=**

" Display all matching files when we tab complete
set wildmenu

" NOW WE CAN:
" - Hit tab to :find by partial match
" - Use * to make it fuzzy

" THINGS TO CONSIDER:
" - :b lets you autocomplete any open buffer
" AUTOCOMPLETE:

" The good stuff is documented in |ins-completion|

" HIGHLIGHTS:
" - ^x^n for JUST this file
" - ^x^f for filenames (works with our path trick!)
" - ^x^] for tags only
" - ^n for anything specified by the 'complete' option

" NOW WE CAN:
" - Use ^n and ^p to go back and forth in the suggestion list

" FILE BROWSING:

" Tweaks for browsing
let g:netrw_banner=0        " disable annoying banner
let g:netrw_browse_split=4  " open in prior window
let g:netrw_altv=1          " open splits to the right
let g:netrw_liststyle=3     " tree view
let g:netrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide.=',\(^\|\s\s\)\zs\.\S\+'

" NOW WE CAN:
" - :edit a folder to open a file browser
" - <CR>/v/t to open in an h-split/v-split/tab
" - check |netrw-browse-maps| for more mappings

" Copied from https://github.com/amix/vimrc/blob/master/vimrcs/basic.vim
" Really great explanation of many things below: https://dougblack.io/words/a-good-vimrc.html

"Always show current position
set ruler

" Ignore case when searching
set ignorecase

" When searching try to be smart about cases 
set smartcase

" Highlight search results
set hlsearch

" Makes search act like search in modern browsers
set incsearch 

" Don't redraw while executing macros (good performance config)
set lazyredraw 

" For regular expressions turn magic on
set magic

" Show matching brackets when text indicator is over them
set showmatch 

" No annoying sound on errors http://vim.wikia.com/wiki/Disable_beeping
set noerrorbells
set novisualbell
set t_vb=
set tm=500

" Properly disable sound on errors on MacVim
if has("gui_macvim")
    autocmd GUIEnter * set vb t_vb=
endif

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Use spaces instead of tabs
set expandtab

" Be smart when using tabs ;)
set smarttab

" 1 tab == 4 spaces
set shiftwidth=4
set tabstop=4

" Linebreak on 500 characters
set lbr
set tw=500

set ai "Auto indent
set si "Smart indent
set wrap "Wrap lines

" taken from https://gist.github.com/millermedeiros/1262085
" --- performance / buffer ---
set hidden                  " can put buffer to the background without writing to disk, will remember history/marks.
set ttyfast                 " Send more characters at a given time.
