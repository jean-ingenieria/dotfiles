#!/usr/bin/env bash 

picom &
/usr/bin/emacs --daemon &
volumeicon &
nm-applet &
feh --bg-fill ~/wallpapers/01.png &
