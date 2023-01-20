# -*- coding: utf-8 -*-
from libqtile.dgroups import simple_key_binder
import os
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List 

# -- VARIABLES -- #
mod = "mod4"
myTerminal = "alacritty"  #OK
xterminal = "xterm" #OK
kterminal = "kitty" #OK
myBrowser = "qutebrowser" #OK 
browser = "brave" #OK
screenshot = "flameshot gui" #OK
menuLauncher = "dmenu_run -c -l 15 -g 10" #OK
menuApps = "rofi -show drun" #OK
menuWindows = "rofi -show" #OK
vimEditor = "alacritty -e nvim" #OK
emEditor = "emacsclient -c -a 'emacs'"
fileManager = "alacritty -e /home/je4n/.config/vifm/scripts/vifmrun" #OK
fileExplorer = "pcmanfm" #OK

# -- KEYBINDINGS -- #
keys = [
    # The essentials
    # -- Terminal alacritty
    Key([mod], "Return",
        lazy.spawn(myTerminal),
        ),
    # -- Terminal xterm
    Key([mod,"mod1"], "Return",
        lazy.spawn(xterminal),
        ),
    Key([mod,"shift"], "Return",
        lazy.spawn(kterminal),
        ),
    # -- Launcher
    Key([mod], "d",
        lazy.spawn(menuLauncher),
        ),
    Key([mod],"m",
        lazy.spawn(menuApps),
        ),
    Key([mod], "w",
        lazy.spawn(menuWindows),
        ),
    # -- Web browser
    Key([mod], "b",
        lazy.spawn(myBrowser),
        ),
    Key([mod, "shift"],"b",
        lazy.spawn(browser),
        ),
    # -- Screenshot
    Key([mod, "shift"], "s",
        lazy.spawn(screenshot),
        ),
    # -- File manager explorer
    Key([mod], "e",
        lazy.spawn(fileManager),
        ),
    Key([mod,"shift"],"e",
        lazy.spawn(fileExplorer),
        ),
    # -- Vim Editor
    Key([mod], "c",
        lazy.spawn(vimEditor),
        ),
    # -- EM Editor
    Key([mod,"mod1"], "e",
        lazy.spawn(emEditor),
        ),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # -- Windows
    Key([mod], "Tab",
        lazy.next_layout(),
        ),
    Key([mod, "shift"], "c",
        lazy.window.kill(),
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        ),

    # Treetab controls
    Key([mod, "shift"], "h",
        lazy.layout.move_left(),
        ),
    Key([mod, "shift"], "l",
        lazy.layout.move_right(),
        ),

    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        ),
    Key([mod], "k",
        lazy.layout.up(),
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "shift"], "n",
        lazy.layout.normalize(),
        ),
    Key([mod, "shift"], "m",
        lazy.layout.maximize(),
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        ),

    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        ),
    Key([mod], "space",
        lazy.layout.next(),
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        ),
]

# --- Groups --- #
groups = [Group("DEV", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("DOC", layout='monadtall'),
          Group("VBOX", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MUS", layout='monadtall'),
          Group("VID", layout='monadtall'),
          Group("GFX", layout='floating')]

# --- Layouts --- #
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    layout.Floating(**layout_theme)
]

# --- Colors --- #
colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# --- Widgets --- #
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=10,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[0],
            foreground=colors[3],
            padding=0,
            fontsize=37
        ),
        widget.Net(
            interface="enp2s0f2",
            format='Net: {down} ↓↑ {up}',
            foreground=colors[1],
            background=colors[3],
            padding=5
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[3],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.ThermalSensor(
            foreground=colors[1],
            background=colors[4],
            threshold=90,
            fmt='Temp: {}',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[4],
            foreground=colors[5],
            padding=0,
            fontsize=37
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="Updates: {updates} ",
            foreground=colors[1],
            colour_have_updates=colors[1],
            colour_no_updates=colors[1],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                myTerm + ' -e sudo pacman -Syu')},
            padding=5,
            background=colors[5]
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[5],
            foreground=colors[6],
            padding=0,
            fontsize=37
        ),
        widget.Memory(
            foreground=colors[1],
            background=colors[6],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fmt='Mem: {}',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[6],
            foreground=colors[7],
            padding=0,
            fontsize=37
        ),
        widget.Volume(
            foreground=colors[1],
            background=colors[7],
            fmt='Vol: {}',
            padding=5,
            chanel='Master'
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[7],
            foreground=colors[8],
            padding=0,
            fontsize=37
        ),
        widget.KeyboardLayout(
            foreground=colors[1],
            background=colors[8],
            fmt='Keyboard: {}',
            padding=5,
            configured_keyboards=['es'],
            update_interval=1
        ),
        widget.TextBox(
            text='',
            font="Ubuntu Mono",
            background=colors[8],
            foreground=colors[9],
            padding=0,
            fontsize=37
        ),
        widget.Clock(
            foreground=colors[1],
            background=colors[9],
            format="%A, %B %d - %H:%M "
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # Slicing removes unwanted widgets (systray) on Monitors 1,3
    del widgets_screen1[9:10]
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
