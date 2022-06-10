#!/bin/sh

langs=$(tesseract --list-langs | tail +2)
menu="$langs exit"
selection=$(echo $menu | rofi -sep " " -dmenu)

tmp_img=`mktemp`
trap "rm $tmp_img*" EXIT

if $selection_menu1 == "exit" then; exit; fi 

tesseract_lang=$selection_menu1
flameshot gui -p $tmp_img.png -d 100
mogrify -modulate 100,0 -resize 400% $tmp_img.png

tesseract $tmp_img.png $tmp_img &> /dev/null
xclip -i $tmp_img.txt -selection clipboard
exit
