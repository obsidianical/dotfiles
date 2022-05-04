import re
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] Change modifier keys as in xmodmap
# define_modmap({
    # Key.CAPSLOCK: Key.RIGHT_CTRL
# })

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(lambda wm_class, device_name: device_name.startswith("Apple"), {
    Key.Y: Key.Z,
    Key.Z: Key.Y,
    # Key.GRAVE: Key.BACKSLASH,
    # Key.BACKSLASH: Key.GRAVE
})

# [Multipurpose modmap] Give a key two meanings. A normal key when pressed and
# released, and a modifier key when held down with another key. See Xcape,
# Carabiner and caps2esc for ideas and concept.
    # To use this example, you can't remap capslock with define_modmap.

# [Conditional multipurpose modmap] Multipurpose modmap in certain conditions,
# such as for a particular device.
define_conditional_multipurpose_modmap(lambda wm_class, device_name: device_name.startswith("Apple"), {
    # Enter is enter when pressed and released. Control when held down.
    Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL],
    # Capslock is escape when pressed and released. Control when held down.
    Key.CAPSLOCK: [Key.ESC, Key.RIGHT_CTRL],
})

# define_keymap(lambda wm_class, device_name: device_name.startswith("Apple"), {
    # K("y"): K("z"),
    # K("z"): K("y"),
# }, "zy swap apl")


# Keybindings for Firefox/Chrome
define_keymap(re.compile("Firefox|Google-chrome|LibreWolf|Chromium"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("C-M-k"): K("C-TAB"),
    K("C-M-j"): K("C-Shift-TAB"),
}, "Firefox and Chrome")

#basic emacs
define_keymap(lambda wm_class: wm_class not in ("Emacs", "konsole", "cool-retro-term", "kitty", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea", "Gimp-2.10", "obsidian"), {
    # Cursor
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    K("C-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("C-left")),
    K("M-f"): with_mark(K("C-right")),
    # Beginning/End of line
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    # Escape
    K("C-q"): escape_next_key,
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    K("M-d"): [K("C-delete"), set_mark(False)],
        # Page up/down
    # K("M-v"): with_mark(K("page_up")),
    # K("C-v"): with_mark(K("page_down")),
    # Copy
    # K("C-w"): [K("C-x"), set_mark(False)],
    # K("M-w"): [K("C-c"), set_mark(False)],
    # K("C-z"): [K("C-v"), set_mark(False)],
    # Enter
    # K("C-m"): K("enter"),
    # Newline without going there
    # K("C-o"): [K("enter"), K("left")],
    # Mark
    # K("C-space"): set_mark(True),
    # K("C-M-space"): with_or_set_mark(K("C-right")),
    # Undo
    # K("C-slash"): [K("C-y"), set_mark(False)],
    # Cancel
    # K("C-g"): [K("esc"), set_mark(False)],
    # C-x YYY
    # K("C-x"): {
        # # C-x h (select all)
        # K("h"): [K("C-home"), K("C-a"), set_mark(True)],
        # # C-x C-f (open)
        # K("C-f"): K("C-o"),
        # # C-x C-s (save)
        # K("C-s"): K("C-s"),
        # # C-x k (kill tab)
        # K("k"): K("C-f4"),
        # # C-x C-c (exit)
        # K("C-c"): K("C-q"),
        # # cancel
        # K("C-g"): pass_through_key,
        # # C-x u (undo)
        # K("u"): [K("C-y"), set_mark(False)],
    # }
}, "Basic emacs keys etc")


define_keymap(lambda wm_class: wm_class not in ("discord", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea"), {
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
})
# other emacs like
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt", "konsole", "cool-retro-term", "discord", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea", "Gimp-2.10", "obsidian"), {
    # Beginning/End of file
    K("M-Shift-comma"): with_mark(K("C-home")),
    K("M-Shift-dot"): with_mark(K("C-end")),
    # Search
    # K("C-s"): K("F3"),
    # K("C-r"): K("Shift-F3"),
    K("M-Shift-key_5"): K("C-h"),
}, "Emacs-like keys")

define_keymap(lambda wm_class: wm_class not in ("Emacs", "konsole", "cool-retro-term", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea"),  {
    K("C-j"): K("F6")
})

# discord mappings
define_keymap(re.compile("discord"), {
    # Navigate servers
    K("M-Shift-j"): K("C-M-down"),
    K("M-Shift-k"): K("C-M-up"),
    # Navigate channels
    K("M-j"): K("M-down"),
    K("M-k"): K("M-up"),
    # Navigate history
    K("C-M-j"): K("M-left"),
    K("C-M-k"): K("M-right"),
    # Navigate unread channels
    K("C-M-p"): K("M-Shift-up"),
    K("C-M-n"): K("M-Shift-down"),
    # Search
    K("M-f"): K("C-f"),
    # toggle last server and dms
    K("M-t"): K("C-M-right"),
    # start drag and drop
    K("M-Shift-d"): K("C-d"),
    # Call controls
    K("M-c"): {
        # Mute
        K("m"): K("C-Shift-m"),
        # Deafen
        K("d"): K("C-Shift-d"),
        # accept call
        K("a"): K("C-enter"),
        # decline
        K("q"): K("esc"),
        # current call
        K("c"): K("C-M-Shift-V"),
        # cancel
        K("C-g"): pass_through_key,
    },
    # Chat controls
    K("M-l"): {
        # Open pins popup
        K("p"): K("C-p"),
        # emoji picker
        K("e"): K("C-e"),
        # gif picker
        K("g"): K("C-g"),
        # sticker picker
        K("s"): K("C-s"),
        # upload file
        K("u"): K("C-Shift-u"),
        # inbox
        K("i"): K("C-i"),
        # new group
        K("n"): K("C-Shift-t"),
        # Oldest unread/newest message
        K("C-p"): K("Shift-page_up"),
        K("C-n"): K("Shift-page_down"),
        # cancel
        K("C-g"): pass_through_key,
    }
})
