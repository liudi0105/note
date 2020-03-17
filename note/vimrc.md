# 我的 vim 配置

```bash
set number  # 显示第行号
set tabstop=4  # 制表符为四格
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab
set nocursorline  # 当前行不进行高亮
set nobackup  # 不生成备份文件
set noerrorbells  # 禁止警告声
set showmatch
set mouse=a  # 可以鼠标操作
set enc=utf-8  # 默认文件编码
set hlsearch  # 高亮显示搜索结果
"set scrolloff=5
"set clipboard=unnamed
set nocompatible
set autoindent
set backspace=indent,eol,start
set smartindent
set cindent
set laststatus=2
set listchars=tab:>-,trail:●,extends:>,precedes:<
set rtp+=~/.vim/bundle/Vundle.vim

filetype plugin indent on
filetype on
syntax on  # 语法高亮

call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'https://github.com/scrooloose/nerdtree.git'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'https://github.com/godlygeek/tabular.git'
Plugin 'w0rp/ale'
call vundle#end()

nnoremap <F3> :NERDTreeToggle<CR>
nnoremap <F2> :NERDTreeFocus<CR>
inoremap { {}<ESC>i
inoremap {} {}
inoremap {<CR> {}<ESC>i<CR><ESC>O

let g:airline_powerline_fonts = 1
let g:airline_theme='dark'
let g:ale_sign_column_always = 2
let g:ale_sign_error = '>>'
let g:ale_sign_warning = '>>'
let g:ale_lint_on_enter = 1
let g:ale_linters_explicit = 1
let g:ale_linters = {'javascript': ['eslint']}
let g:ale_set_highlights = 0
let g:airline#extensions#ale#enabled = 1
nmap <silent> <C-k> <Plug>(ale_previous_wrap)
nmap <silent> <C-j> <Plug>(ale_next_wrap)
```
