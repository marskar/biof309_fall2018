" vim-bootstrap 55985df

"*****************************************************************************
"" Vim-PLug core
"*****************************************************************************
if has('vim_starting')
  set nocompatible               " Be iMproved
endif

let g:loaded_python_provider = 1 "disable python2 support
let g:jedi#force_py_version=3
let g:UltisnipsUsePythonVersion=3
" call jedi#force_py_version(3)
let g:python_host_prog = '/Users/marskar/miniconda3/bin/python3' "Use python3 instead of python2
let g:python3_host_prog = '/Users/marskar/miniconda3/bin/python3'
let vimplug_exists=expand('~/.config/nvim/autoload/plug.vim')

let g:vim_bootstrap_langs = "python"
let g:vim_bootstrap_editor = "nvim"				" nvim or vim

if !filereadable(vimplug_exists)
  if !executable("curl")
    echoerr "You have to install curl or first install vim-plug yourself!"
    execute "q!"
  endif
  echo "Installing Vim-Plug..."
  echo ""
  silent !\curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  let g:not_finish_vimplug = "yes"

  autocmd VimEnter * PlugInstall
endif

" Required:
call plug#begin(expand('~/.config/nvim/plugged'))

"*****************************************************************************
"" Plug install packages
"*****************************************************************************
" my plugins
" the main R plugin providing RStudio-esque features
Plug 'jalvesaq/Nvim-R'
" Allows sending Haskell, JavaScript, Julia, Lisp, Matlab, Prolog, Python, Ruby, and sh to interpreter
Plug 'jalvesaq/vimcmdline'
" autocompletion manager (NCM)
Plug 'roxma/nvim-completion-manager'
" autocompletion for R, works with NCM
Plug 'gaalcaras/ncm-R'
" R setup: https://kadekillary.work/post/nvim-r/
" R setup: https://github.com/beigebrucewayne/vim-ide-4-all/blob/master/R-neovim.md
" Optional: better Rnoweb support (LaTeX completion)
Plug 'lervag/vimtex'
" get definitions using <leader>d
" Plug 'rizzatti/dash.vim' " Use \rh instead

" For Rmarkdown syntax
Plug 'vim-pandoc/vim-pandoc'
Plug 'vim-pandoc/vim-pandoc-syntax'
" Plug 'vim-pandoc/vim-rmarkdown' " This plugin interferes with ncm-R
" Plug 'plasticboy/vim-markdown'
" Plug 'gabrielelana/vim-markdown'

Plug 'ervandew/supertab'
" Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }

" From Vimcast 73: http://vimcasts.org/episodes/neovim-eyecandy/
Plug 'machakann/vim-highlightedyank'

"Plug 'vyzyv/vimpyter' "jupyter notebook editing

" fuzzy find with fzf ( If installed using Homebrew )
" https://github.com/junegunn/fzf#installation
" PlugInstall and PlugUpdate will clone fzf in ~/.fzf and run install script
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

" Plug 'tommcdo/vim-exchange'
" Plug 'kien/ctrlp.vim'
" Plug 'godlygeek/tabular'
Plug 'terryma/vim-multiple-cursors'
" discussed here: https://www.oliversherouse.com/2017/08/21/vim_zero.html
" Plug 'lifepillar/vim-mucomplete'
" Plug 'chiel92/vim-autoformat'
" Plug 'flazz/vim-colorschemes'
" Plug 'jiangmiao/auto-pairs'

" Replacing gundo because mundo works with neovim
" gundo vimcast: http://vimcasts.org/episodes/undo-branching-and-gundo-vim/
Plug 'simnalamburt/vim-mundo'

" http://www.rushiagr.com/blog/2016/06/17/you-dont-need-vim-swap-files-and-how-to-get-rid-of-them/
Plug '907th/vim-auto-save'

" vim-bootstrap plugins
" Plug 'scrooloose/nerdtree'
" Plug 'jistr/vim-nerdtree-tabs'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-repeat'
Plug 'tpope/vim-abolish'
Plug 'tpope/vim-sensible'
Plug 'tpope/vim-rhubarb'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-obsession'
Plug 'tpope/vim-unimpaired'

Plug 'qpkorr/vim-bufkill'
Plug 'sheerun/vim-polyglot'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'airblade/vim-gitgutter'
" Plug 'vim-scripts/grep.vim'
" Plug 'vim-scripts/CSApprox'
Plug 'bronson/vim-trailing-whitespace'
" Plug 'majutsushi/tagbar'

"" Snippets
Plug 'sirver/ultisnips'

Plug 'honza/vim-snippets'

"" Color
Plug 'dracula/vim'

Plug 'davidhalter/jedi-vim'

call plug#end()

" Required:
filetype plugin indent on

" add this too I guess
filetype plugin on

" Colors
" set termguicolors
syntax on
color dracula

"*****************************************************************************
"" Basic Setup
"*****************************************************************************"
" deoplete tab completion
" https://github.com/Shougo/deoplete.nvim/issues/542
" set completeopt+=noinsert

" NCM tab completion
" https://github.com/roxma/nvim-completion-manager/blob/master/doc/nvim-completion-manager.txt
" inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
" inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

" set foldmethod=manual
" set nofoldenable "I do not like automatic folding

let g:pandoc_bibfiles = ['~/gdrive/nhanes/bib/nhanes.bib']

" From https://github.com/simnalamburt/vim-mundo/blob/master/doc/mundo.txt
nnoremap <F5> :MundoToggle<CR>
let g:mundo_verbose_graph=0

" Autosave setting 
" http://www.rushiagr.com/blog/2016/06/17/you-dont-need-vim-swap-files-and-how-to-get-rid-of-them/
" Enable autosave plugin
let g:auto_save = 1  " enable AutoSave on Vim startup
" Only save in Normal mode periodically. If the value is changed to '1',
" then changes are saved when you are in Insert mode too, as you type, but
" I would say prefer not save in Insert mode
let g:auto_save_in_insert_mode = 0
" Silently autosave. If you disable this option by changing value to '0',
" then in the vim status, it will display "(AutoSaved at <current time>)" all
" the time, which might get annoying
let g:auto_save_silent = 0
" And now turn Vim swapfile off
set noswapfile
set nobackup

" let g:auto_save_write_all_buffers = 1  " write all open buffers as if you would use :wa

" vanilla vim autopairs replacement
" https://stackoverflow.com/questions/21316727/automatic-closing-brackets-for-vim
ino " ""<left>
ino ' ''<left>
ino ( ()<left>
ino [ []<left>
ino { {}<left>
ino {<CR> {<CR>}<ESC>O
ino {;<CR> {<CR>};<ESC>O
ino {,<CR> {<CR>},<ESC>O

" from https://github.com/LukeSmithxyz/voidrice/tree/6c6b33635a204a339868e00a18a63547954cbf3c
" watch https://www.youtube.com/watch?v=hvc-pHjbhdE&t=262s
autocmd BufRead,BufNewFile /tmp/calcurse*,~/.calcurse/notes/* set filetype=markdown

let g:pandoc#modules#disabled = ["folding"]
let g:pandoc#syntax#conceal#blacklist = ["codeblock_start", "codeblock_delim"]

"If you want to use vim-pandoc-syntax without vim-pandoc, you'll need to tell Vim to load it for certain files. Just add something like this to your vimrc:
" https://github.com/vim-pandoc/vim-pandoc-syntax
    " augroup pandoc_syntax
    "     au! BufNewFile,BufFilePre,BufRead *.md set filetype=markdown.pandoc
    " augroup END
" https://www.oliversherouse.com/2017/08/21/vim_zero.html
set nospell spelllang=en_us
set splitright
" nnoremap <leader><space> :nohls <enter>

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

" Underline the line/column the cursor is on
" set cursorline
" set cursorcolumn

" (In times of great desperation) allow use of the mouse
set mouse=a

" Show partially typed commands in the statusline
set showcmd

" use hybrid (absolute and relative) numbers
set number relativenumber

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

" From Vimcast 73: http://vimcasts.org/episodes/neovim-eyecandy/
set inccommand=nosplit

"" Encoding
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=utf-8
set bomb
set binary


"" Fix backspace indent
set backspace=indent,eol,start

"" Tabs. May be overridden by autocmd rules
set tabstop=4
set softtabstop=0
set shiftwidth=4
set expandtab
set autoindent

"" Map leader to <space>
let mapleader=' '

"" Enable hidden buffers
set hidden " Allow background buffers without saving

set fileformats=unix,dos,mac

if exists('$SHELL')
    set shell=$SHELL
else
    set shell=/bin/sh
endif

" session management
let g:session_directory = "~/.config/nvim/session"
let g:session_autoload = "no"
let g:session_autosave = "no"
let g:session_command_aliases = 1

"*****************************************************************************
"" Visual Settings
"*****************************************************************************

" settings :: Nvim-R plugin
" R output is highlighted with current colorscheme
let g:rout_follow_colorscheme = 1
" R commands in R output are highlighted
let g:Rout_more_colors = 1
" always equal vertical split
autocmd BufNew * wincmd =
let R_min_editor_width = 20
let cmdline_vsplit      = 1
" let R_rconsole_width = winwidth(0) / 2

syntax on
set ruler

"" Status bar
set laststatus=2

"" Use modeline overrides
set modeline
set modelines=10

set title
set titleold="Terminal"
set titlestring=%F

set statusline=%F%m%r%h%w%=(%{&ff}/%Y)\ (line\ %l\/%L,\ col\ %c)\

" Search mappings: These will make it so that going to the next one in a
" search will center on the line it's found in.
nnoremap n nzzzv
nnoremap N Nzzzv

if exists("*fugitive#statusline")
  set statusline+=%{fugitive#statusline()}
endif

" vim-airline
let g:airline_theme = 'powerlineish'
let g:airline#extensions#syntastic#enabled = 1
let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tagbar#enabled = 1
let g:airline_skip_empty_sections = 1

"*****************************************************************************
"" Abbreviations
"*****************************************************************************
"" no one is really happy until you have this shortcuts
cnoreabbrev W! w!
cnoreabbrev Q! q!
cnoreabbrev Qall! qall!
cnoreabbrev Wq wq
cnoreabbrev Wa wa
cnoreabbrev wQ wq
cnoreabbrev WQ wq
cnoreabbrev W w
cnoreabbrev Q q
cnoreabbrev Qall qall

"" The PC is fast enough, do syntax highlight syncing from start unless 200 lines
augroup vimrc-sync-fromstart
  autocmd!
  autocmd BufEnter * :syntax sync maxlines=200
augroup END

"" Remember cursor position
augroup vimrc-remember-cursor-position
  autocmd!
  autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g`\"" | endif
augroup END

"*****************************************************************************
"" Mappings
"*****************************************************************************
" Keyboard shortcuts for <- -> and other operators in R specific files
" https://github.com/jalvesaq/Nvim-R/issues/85
" The trailing spaces below are intentional!
autocmd FileType r inoremap <buffer> <A-n> <Esc>:normal! a %>%<CR>a<CR>
autocmd FileType rnoweb inoremap <buffer> <A-n> <Esc>:normal! a %>%<CR>a<CR>
autocmd FileType rmd inoremap <buffer> <A-n> <Esc>:normal! a %>%<CR>a<CR>
autocmd FileType r inoremap <buffer> <A-m> <Esc>:normal! a %>%<CR>a 
autocmd FileType rnoweb inoremap <buffer> <A-m> <Esc>:normal! a %>%<CR>a 
autocmd FileType rmd inoremap <buffer> <A-m> <Esc>:normal! a %>%<CR>a 
autocmd FileType r inoremap <buffer> <A-i> <Esc>:normal! a %in%<CR>a 
autocmd FileType rnoweb inoremap <buffer> <A-i> <Esc>:normal! a %in%<CR>a 
autocmd FileType rmd inoremap <buffer> <A-i> <Esc>:normal! a %in%<CR>a 
autocmd FileType r inoremap <buffer> <A-.> <Esc>:normal! a -><CR>a 
autocmd FileType rnoweb inoremap <buffer> <A-.> <Esc>:normal! a -><CR>a 
autocmd FileType rmd inoremap <buffer> <A-.> <Esc>:normal! a -><CR>a 
autocmd FileType r inoremap <buffer> <A-/> <Esc>:normal! a %/%<CR>a 
autocmd FileType rnoweb inoremap <buffer> <A-/> <Esc>:normal! a %/%<CR>a 
autocmd FileType rmd inoremap <buffer> <A-/> <Esc>:normal! a %/%<CR>a 
autocmd FileType r inoremap <buffer> <A-8> <Esc>:normal! a %*%<CR>a 
autocmd FileType rnoweb inoremap <buffer> <A-8> <Esc>:normal! a %*%<CR>a 
autocmd FileType rmd inoremap <buffer> <A-8> <Esc>:normal! a %*%<CR>a 
" http://sherifsoliman.com/2017/07/22/nvim-r/
" press alt+, to have Nvim-R insert the assignment operator: <-
let R_assign_map = "<A-,>"

" set a minimum source editor width
" let R_min_editor_width = 80

" make sure the console is at the bottom by making it really wide
" let R_rconsole_width = 1000

" show arguments for functions during omnicompletion
let R_show_args = 1

" Don't expand a dataframe to show columns by default
" let R_objbr_opendf = 0

" https://www.oliversherouse.com/2017/08/21/vim_zero.html
" there do not work with my Keyboard setup: https://github.com/jasonrudolph/keyboard
nnoremap <C-H> :bp <enter>
nnoremap <C-L> :bn <enter>
nnoremap <Leader>w :w <enter>
nnoremap <Leader>q :bd <enter>

" Nvim-R mappings
" remapping the basic :: send line
nmap <space> <Plug>RSendLine
" remapping selection :: send multiple lines
vmap <space> <Plug>RDSendSelection
" remapping selection :: send multiple lines + echo lines
vmap <space>e <Plug>RESendSelection
" from https://github.com/beigebrucewayne/vim-ide-4-all/blob/master/R-neovim.md
nmap <space>p <Plug>RPrintObj


"" Split
noremap <Leader>h :<C-u>split<CR>
noremap <Leader>v :<C-u>vsplit<CR>

"" Git
noremap <Leader>ga :Gwrite<CR>
noremap <Leader>gc :Gcommit<CR>
noremap <Leader>gps :Gpush<CR>
noremap <Leader>gpl :Gpull<CR>
noremap <Leader>gs :Gstatus<CR>
noremap <Leader>gb :Gblame<CR>
noremap <Leader>gd :Gvdiff<CR>
noremap <Leader>gr :Gremove<CR>

" session management
nnoremap <leader>so :OpenSession<Space>
nnoremap <leader>ss :SaveSession<Space>
nnoremap <leader>sd :DeleteSession<CR>
nnoremap <leader>sc :CloseSession<CR>

"" Tabs
nnoremap <S-Tab> gT
nnoremap <silent> <S-t> :tabnew<CR>

"" Set working directory
nnoremap <leader>. :lcd %:p:h<CR>

"" Opens an edit command with the path of the currently edited file filled in
noremap <Leader>e :e <C-R>=expand("%:p:h") . "/" <CR>

"" Opens a tab edit command with the path of the currently edited file filled
noremap <Leader>te :tabe <C-R>=expand("%:p:h") . "/" <CR>

" snippets
" see http://vimcasts.org/episodes/meet-ultisnips/
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"
let g:UltiSnipsEditSplit="vertical"

" Disable visualbell
set noerrorbells visualbell t_vb=
if has('autocmd')
  autocmd GUIEnter * set visualbell t_vb=
endif

"" Copy/Paste/Cut
" if has('unnamedplus')
"   set clipboard=unnamed,unnamedplus
" endif

noremap YY "+y<CR>
noremap <leader>p "+gP<CR>
noremap XX "+x<CR>

if has('macunix')
  " pbcopy for OSX copy/paste
  vmap <C-x> :!pbcopy<CR>
  vmap <C-c> :w !pbcopy<CR><CR>
endif

"" Buffer nav
noremap <leader>z :bp<CR>
noremap <leader>q :bp<CR>
noremap <leader>x :bn<CR>
noremap <leader>w :bn<CR>

"" Close buffer
noremap <leader>c :bd<CR>

"" Clear search (highlight)
nnoremap <silent> <leader><space> :noh<cr>

"" Switching windows
" noremap <C-j> <C-w>j
" noremap <C-k> <C-w>k
" noremap <C-l> <C-w>l
" noremap <C-h> <C-w>h

"" Vmap for maintain Visual Mode after shifting > and <
vmap < <gv
vmap > >gv

"" Move visual block
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

"" Open current line on GitHub
nnoremap <Leader>o :.Gbrowse<CR>

"*****************************************************************************
"" Custom configs
"*****************************************************************************
" Python Version
" https://www.oliversherouse.com/2017/08/21/vim_zero.html
augroup python3
    au! BufEnter *.py setlocal omnifunc=python3complete#Complete
augroup END

"" Autocompletion
" https://www.oliversherouse.com/2017/08/21/vim_zero.html
set completeopt=menuone,longest
set shortmess+=c " Turn off completion messages

" let g:mucomplete#enable_auto_at_startup = 1 
" call add(g:mucomplete#chains['default'], 'ulti')

" python
" vim-python
augroup vimrc-python
  autocmd!
  autocmd FileType python setlocal expandtab shiftwidth=4 tabstop=8 colorcolumn=79
      \ formatoptions+=croq softtabstop=4
      \ cinwords=if,elif,else,for,while,try,except,finally,def,class,with
augroup END

" jedi-vim
let g:jedi#popup_on_dot = 0
let g:jedi#goto_assignments_command = "<leader>g"
let g:jedi#goto_definitions_command = "<leader>d"
let g:jedi#documentation_command = "K"
let g:jedi#usages_command = "<leader>n"
let g:jedi#rename_command = "<leader>r"
let g:jedi#show_call_signatures = "0"
let g:jedi#completions_command = "<C-Space>"
let g:jedi#smart_auto_mappings = 0


" vim-airline
let g:airline#extensions#virtualenv#enabled = 1

" Syntax highlight
" Default highlight is better than polyglot
let g:polyglot_disabled = ['python']
let python_highlight_all = 1

" vim-airline
if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif

if !exists('g:airline_powerline_fonts')
  let g:airline#extensions#tabline#left_sep = ' '
  let g:airline#extensions#tabline#left_alt_sep = '|'
  let g:airline_left_sep          = '▶'
  let g:airline_left_alt_sep      = '»'
  let g:airline_right_sep         = '◀'
  let g:airline_right_alt_sep     = '«'
  let g:airline#extensions#branch#prefix     = '⤴' "➔, ➥, ⎇
  let g:airline#extensions#readonly#symbol   = '⊘'
  let g:airline#extensions#linecolumn#prefix = '¶'
  let g:airline#extensions#paste#symbol      = 'ρ'
  let g:airline_symbols.linenr    = '␊'
  let g:airline_symbols.branch    = '⎇'
  let g:airline_symbols.paste     = 'ρ'
  let g:airline_symbols.paste     = 'Þ'
  let g:airline_symbols.paste     = '∥'
  let g:airline_symbols.whitespace = 'Ξ'
else
  let g:airline#extensions#tabline#left_sep = ''
  let g:airline#extensions#tabline#left_alt_sep = ''

  " powerline symbols
  let g:airline_left_sep = ''
  let g:airline_left_alt_sep = ''
  let g:airline_right_sep = ''
  let g:airline_right_alt_sep = ''
  let g:airline_symbols.branch = ''
  let g:airline_symbols.readonly = ''
  let g:airline_symbols.linenr = ''
endif

highlight Normal ctermfg=white ctermbg=black
