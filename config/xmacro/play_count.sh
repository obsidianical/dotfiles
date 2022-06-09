#!/usr/bin/bash

register=$(ls $HOME/xmacros | rofi -dmenu)
count=$(echo "2\n5\n10\n20\n50\n100" | rofi -dmenu -l 5)

for i in {1..$count}; do 
	xmacroplay "$DISPLAY" < $HOME/xmacros/$register
done
