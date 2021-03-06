items="lock screen;log out;toggle picom;shut down;reboot;update all"

selection=$(echo $items | rofi -sep ";" -dmenu)

case $selection in
	"lock screen")
		i3lock-fancy
		;;
	"log out")
		killall i3
		;;
	"toggle picom")
		killall picom || picom --experimental-backend -b
		;;
	"shut down")
		shutdown now
		;;
	"reboot")
		systemctl reboot
		;;
	"update all")
		kitty zsh -c "upg"
		;;
esac
