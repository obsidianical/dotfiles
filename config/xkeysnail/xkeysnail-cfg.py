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

define_keymap(re.compile("Firefox|Google-chrome|LibreWolf|Chromium"), {
    K("C-M-k"): K("C-TAB"),
    K("C-M-j"): K("C-Shift-TAB"),
}, "Firefox and Chrome")

#basic emacs
define_keymap(lambda wm_class: wm_class not in ("Emacs", "konsole", "cool-retro-term", "kitty", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea", "Gimp-2.10", "obsidian", "gw2-64.exe"), {
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
}, "Basic emacs keys etc")


define_keymap(lambda wm_class: wm_class not in ("discord", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea", "nheko", "Signal", "gw2-64.exe"), {
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
})

# other emacs like
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt", "konsole", "cool-retro-term", "discord", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea", "Gimp-2.10", "obsidian", "nheko", "Signal"), {
    # Beginning/End of file
    K("M-Shift-comma"): with_mark(K("C-home")),
    K("M-Shift-dot"): with_mark(K("C-end")),
}, "Emacs-like keys")

define_keymap(lambda wm_class: wm_class not in ("Emacs", "konsole", "cool-retro-term", "jetbrains-webstorm", "jetbrains-clion", "jetbrains-pycharm", "jetbrains-dataspell", "jetbrains-idea", "gw2-64.exe"),  {
    K("C-j"): K("F6")
})

define_keymap(re.compile("nheko"), {
    K("M-j"): K("C-down"),
    K("M-k"): K("C-up"),
})

define_keymap(re.compile("Signal"), {
    K("C-k"): K("C-t"),
    K("M-k"): K("M-up"),
    K("M-j"): K("M-down"),
})

# discord mappings
define_keymap(re.compile("discord"), {# {{{
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
})# }}}
