#!/bin/sh

langs=$(tesseract --list-langs | tail +2)
first_menu="$langs exit"
selection_menu1=$(echo $first_menu | rofi -sep " " -dmenu)

tmp_img=`mktemp`
trap "rm $tmp_img*" EXIT


echo $selection_menu1

case $selection_menu1 in
	"eng"|"deu"|"spa"|"osd"|"fra")
		tesseract_lang=$selection_menu1
		flameshot gui -p $tmp_img.png -d 100
		mogrify -modulate 100,0 -resize 400% $tmp_img.png
		;;
	"exit")
		exit
		;;
esac

tesseract $tmp_img.png $tmp_img &> /dev/null
xclip -i $tmp_img.txt -selection clipboard
exit
