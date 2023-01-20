--###############################################
--################# KEYMAPS #####################
--###############################################

-- Alias
local map = vim.api.nvim_set_keymap
local opts = {noremap = true, silent = true}
local opt = {noremap = true}

vim.g.mapleader = " "

-- System
map("n","<C-s>",":w<CR>",opts)
map("i","<C-s>","<C-c>:w<CR>",opts)
map("n","<C-r>",":source %<CR>",opts)
map("n","<C-q>",":quitall<CR>",opts)

-- Telescope
map("n","<leader>fr",":Telescope oldfiles<CR>",opt)
map("n","<leader>ff",":Telescope find_files<CR>",opt)
map("n","<leader>fb",":Telescope file_browser<CR>",opt)
map("n","<leader>fw",":Telescope live_grep<CR>",opt)
map("n","<leader>ht",":Telescope colorscheme<CR>",opt)

-- Fzp lua
map("n","<C-f>",":Fzflua files<CR>",opts)

-- Neotree
map("n","<C-n>",":Neotree focus toggle<CR>",opts)
map("i","<C-n>","<C-c>:Neotree focus toggle<CR>",opts)
map("n","<C-e>",":Neotree focus<CR>",opts)
map("i","<C-e>","<C-c>:Neotree focus<CR>",opts)

-- BarBar
-- Previo next
map('n', '<A-,>', '<Cmd>BufferPrevious<CR>', opts)
map('n', '<A-.>', '<Cmd>BufferNext<CR>', opts)

-- Move
map('n', '<A-<>', '<Cmd>BufferMovePrevious<CR>', opts)
map('n', '<A->>', '<Cmd>BufferMoveNext<CR>', opts)

-- Goto 1 ... 9 
for i=1, 9 do
i=tostring(i)
    map('n', '<A-'..i..'>', '<Cmd>BufferGoto '..i..'<CR>', opts)
end

-- Goto Last +9
map('n', '<A-0>', '<Cmd>BufferLast<CR>', opts)

-- Pin
map('n', '<A-p>', '<Cmd>BufferPin<CR>', opts)

-- Close
map('n', '<A-c>', '<Cmd>BufferClose<CR>', opts)

-- Pick
map('n', '<C-p>', '<Cmd>BufferPick<CR>', opts)

-- Order
map('n', '<leader>bb', '<Cmd>BufferOrderByBufferNumber<CR>', opts)
map('n', '<leader>bd', '<Cmd>BufferOrderByDirectory<CR>', opts)
map('n', '<leader>bl', '<Cmd>BufferOrderByLanguage<CR>', opts)
map('n', '<leader>bw', '<Cmd>BufferOrderByWindowNumber<CR>', opts)
