#Libraries
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
#Terminal Config
terminal = "kitty"
#Mod key
mod = "mod4"
#Keybindings
keys = [
    #Move focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(["mod1"], "Tab", lazy.layout.down(), desc="Move focus down"),
    Key(["mod1", "shift"], "Tab", lazy.layout.up(), desc="Move focus down"),
    #Move focused window
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    #Grow focused window
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Normalize
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    #Launch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #Toggle layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    #Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    #Maximize Minimize
    Key([mod, "shift"], "m", lazy.layout.maximize(), desc="Toggle Size"),
    #Close window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    #Launch rofi (drun)
    Key(["mod1"], "space", lazy.spawn("rofi -show drun"), desc="lauch rofi"),
    #Launch rofi (run)
    Key(["mod5"], "space", lazy.spawn("rofi -show run"), desc="lauch rofi run"),
    #Launch rofi (window)
    Key([mod, "shift"], "w", lazy.spawn("rofi -show window"), desc="lauch rofi window"),
    #Volume Up
    Key([],"XF86AudioRaiseVolume",
        lazy.spawn("volume /usr/share/icons/Papirus-Dark/symbolic/status/audio-volume-high-symbolic.svg"), desc="Volume up"),
    #Volume Down
    Key([],"XF86AudioLowerVolume",
        lazy.spawn("volume /usr/share/icons/Papirus-Dark/symbolic/status/audio-volume-medium-symbolic.svg"), desc="Volume down"),
    #Volume Mute
    Key([],"XF86AudioMute",
        lazy.spawn("volume /usr/share/icons/Papirus-Dark/symbolic/status/audio-volume-muted-symbolic.svg"), desc="Volume muted"),
    #Help
    Key(["mod5", "shift"], "h", lazy.spawn("qutebrowser :open https://wiki.archlinux.org"), desc="ArchWiki"),
    #Reload Qtile
    Key(["mod5", "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    #Quit Qtile
    Key(["mod5", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile")
]
#Workspaces
groups = [Group(i) for i in "1234567890"]
for i in groups:
    keys.extend(
        [
            Key(["mod5"], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
            Key(["mod5", "shift"], i.name, lazy.window.togroup(i.name), desc="Switch to group {}".format(i.name))
        ]
    )
#Panels
#Widgets config
widget_defaults = dict(
    font="Ubuntu Regular",
    fontsize=14,
)
extension_defaults = widget_defaults.copy()
#Top bar widgets
top_widgets = [
#    widget.CurrentLayout(),
    widget.Spacer(),
    widget.Clock(format="%A %d %B %Y %I:%M:%S %p", font="Ubuntu Bold"),
    widget.Spacer(),
    widget.Systray(icon_size=16, padding=5)
]
#Top bar
top=bar.Bar(
    #Widgets
    top_widgets,
    #Bar height
    18,
    background="#10100E",
    border_width=[0, 0, 2, 0],
    border_color="#FFFAFA",
)
screens = [Screen(top)]
#Layouts
focus="#f7d171"
normal="#c5c6d0"
width=1
columnas = layout.Columns(
    border_focus=focus,
    border_normal=normal,
    margin = 2,
    margin_on_single=2,
    border_width=width,
    border_on_single=True
)
maximizar = layout.Max(
    border_width=0
)
floating_layout = layout.Floating(
    border_focus=focus,
    border_normal=normal,
    border_width=width,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry")
    ]
)
layouts = [columnas, maximizar, floating_layout]
#Mouse
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
