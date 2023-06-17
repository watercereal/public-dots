    
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from faker import Faker
fake = Faker()



from libqtile.config import Screen
from libqtile.bar import Gap, Bar, STRETCH
from libqtile.widget import GroupBox, Clock, Spacer

bg1 = fake.color() #replaces light grey
bg2 = fake.color() #replaces dark grey 


mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd("Search"), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),

    #sound thing:
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
## Custom Keybinds
    Key([mod], "b", lazy.spawn("qutebrowser"), desc="web"),
    Key([mod], "d", lazy.spawn("vscodium"), desc="vs code (ium)"),
    Key([mod], "v", lazy.spawn([terminal, "-e", "ranger"]), desc="ranger file manager"),
    Key([mod, "control"], "v", lazy.spawn("thunar"), desc="pcmanfm"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="screenshot"),
    Key([mod], "c", lazy.spawn("vscodium /home/water/.config/qtile/config.py"))    
    
]

groups = [Group(i) for i in "12345678p"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus="F7EBF5",border_normal="352032",border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4,margin=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


###MOUSE CALLBACKS###
"""
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras import widget

right_arrrow = { 
    "decorations": [
        PowerLineDecoration(
            path='arrow_right',
        ),
    ]
}

left_arrow = { 
    "decorations": [
        PowerLineDecoration(
            path='arrow_left',
        ),
    ]
}

back_slash = {
    "decorations": [
        PowerLineDecoration(
            path='back_slash',
        ),
    ]
}

fordward_slash = {
    "decorations": [
        PowerLineDecoration(
            path='fordward_slash'
        ),
    ]
}

zig_zag = {
    "decorations": [
        PowerLineDecoration(
            path="zig_zag"
        )
    ]
}

round_left = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_left"
        )
    ]
}

round_right = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right"
        )
    ]
}
"""
#uni ⎰ ⎱ 

colors = [
    ["#00000000","#000000","#000000"], #0
    ["#313244","#313244","#313244","#313244"], #1 background 1 
    ["1e2030","1e2030","1e2030","1e2030"], #2 background 2
    ["eba0ac","eba0ac","eba0ac","eba0ac"], #3 pink
    ["f38ba8","f38ba8","f38ba8","f38ba8"], #4 pink2
    ["c6a0f6","c6a0f6","c6a0f6","c6a0f6"], #5 purple 1
    ["8839ef","8839ef","8839ef","8839ef"], #6 purple 2
    ["f4dbd6","f4dbd6","f4dbd6","f4dbd6"], #7 pinkish white
    ["f5c2e7","f5c2e7","f5c2e7","f5c2e7"], #8 purple 3
    ["B085E7","B085E7","B085E7","B085E7"],#9 6 but darker 
    ["986ECD","986ECD","986ECD","986ECD"], #10 even darker
    ["250921","250921","250921","250921"], #11 black 
    ["F7EBF5","#F7EBF5","#F7EBF5","#F7EBF5"], #12 real white
    ["#352032","#352032","#352032","#352032"], #13 pink black 




]
widget_defaults = dict(
    font="Liberation Mono", #D050000L
    fontsize=22,
    padding=0,
    background=colors[13],
    foreground=colors[12],
    )
extension_defaults = widget_defaults.copy()

# ⟢	⟣


screens = [
    Screen(
        top=Bar(
            [
                widget.OpenWeather(location='Harrowsmith, CA',format='{main_feels_like}°{units_temperature} {weather}'),
                Spacer(12),
                widget.WindowTabs(fontsize=12),
                widget.AGroupBox(border=colors[13]),
                Spacer(STRETCH),  
                widget.Volume(),
                Spacer(12),
                Clock(
                    format="%a %d %b  %I:%M %p",
                ),
                widget.TextBox("|",foreground=colors[7],padding=3),
                widget.Systray(),
                widget.TextBox("|",foreground=colors[7],padding=3),

                Spacer(24),
            ],
            38,
            border_width=1,
            border_color=colors[12],
            margin=[10, 10, 10, 10],
            background=colors[13],
        ),
        bottom=Gap(12),
        left=Gap(12),
        right=Gap(12),
    ),
    ## FIRST SCREEN^
    ##
    ##
    ##
    ##
    ## SECOND SCREEN
    Screen(
    top=Bar(
        [
            Spacer(12),
            widget.WindowTabs(fontsize=12),
            widget.AGroupBox(border=colors[13]),
            Spacer(STRETCH),  
            widget.TextBox("󰧑",fontsize=30), #brain
            widget.Memory(measure_mem='G',),
            widget.TextBox("||",foreground=colors[7],padding=3),
            widget.TextBox("󰃬",fontsize=30), #calculator
            widget.CPU(padding=3,format='CPU {load_percent}%'),
            widget.TextBox("",fontsize=22,padding=3), #calculator                    
            widget.ThermalZone(padding=3),
            widget.TextBox("||",foreground=colors[7],padding=3),
            widget.Net(format=' {down}'),
            widget.TextBox("||",foreground=colors[7],padding=3),

            Spacer(24),
        ],
        38,
        border_width=1,
        border_color=colors[12],
        margin=[10, 10, 10, 10],
        background=colors[13],
    ),
    bottom=Gap(12),
    left=Gap(12),
    right=Gap(12),
)
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
