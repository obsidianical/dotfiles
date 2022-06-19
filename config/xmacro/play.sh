#!/usr/bin/bash
register=$(ls $HOME/xmacros | rofi -dmenu)

xmacroplay "$DISPLAY" < $HOME/xmacros/$register
