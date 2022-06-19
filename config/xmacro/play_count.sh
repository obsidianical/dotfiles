#!/usr/bin/bash

register=$(ls $HOME/xmacros | rofi -dmenu)
count=$(echo "2;5;10;20;50;100" | rofi -dmenu -sep ";" -l 5)

for i in $(seq $count); do 
	echo $i
	xmacroplay "$DISPLAY" < $HOME/xmacros/$register
done
