#!/usr/bin/bash
register=$(ls $HOME/xmacros | rofi -dmenu)

xmacrorec2 > $HOME/xmacros/$register
