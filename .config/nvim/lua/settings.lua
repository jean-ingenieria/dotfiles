--############################################################
--####################### SETTINGS ###########################
--############################################################

-- Alias
local o = vim.o

-- Colors
o.termguicolors = true

-- Update time
o.timeoutlen = 500
o.updatetime = 200

-- Scroll
o.scrolloff = 8

-- UI editor
o.number = true
o.numberwidth = 4
o.relativenumber = true
o.signcolumn = "yes"
o.cursorline = true

-- Experience editing
o.expandtab = true
o.smarttab = true
o.cindent = true
o.autoindent = true
o.wrap = true
o.textwidth = 300
o.tabstop = 4
o.shiftwidth = 4
o.softtabstop = -1
o.list = true
o.listchars = "trail:·,nbsp:◇,tab:→ ,extends:▸,precedes:◂"

-- Makes neovim clipboard OS
o.clipboard = "unnamedplus"

-- Case insensitive searching
o.ignorecase = true
o.smartcase = true

-- Undo and backup options
o.backup = false
o.writebackup = false
o.undofile = true
o.swapfile = false

-- Remenber items
o.history = 100

-- Better buffer splitting
o.splitright = true
o.splitbelow = true
