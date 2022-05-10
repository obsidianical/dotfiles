#!/bin/bash

tesseract_lang=$(echo "eng,deu,spa" | rofi -sep "," -dmenu)

tmp_img=`mktemp`
trap "rm $tmp_img*" EXIT

flameshot gui -p $tmp_img.png

mogrify -modulate 100,0 -resize 400% $tmp_img.png

tesseract $tmp_img.png $tmp_img &> /dev/null
xclip -i $tmp_img.txt -selection clipboard
exit
