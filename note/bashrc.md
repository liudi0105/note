# Windows Terminal Profile

```bash
// To view the default settings, hold "alt" while clicking on the "Settings" button.
// For documentation on these settings, see: https://aka.ms/terminal-documentation
{
    "$schema": "https://aka.ms/terminal-profiles-schema",
    "defaultProfile": "{1caa0dad-35be-5f56-a8ff-afceeeaa6101}",
    "initialCols": 100,
    "initialRows": 24,
    "profiles": [
        {
            // Make changes here to the cmd.exe profile
            "guid": "{1caa0dad-35be-5f56-a8ff-afceeeaa6101}",
            "name": "cygwin",
            "fontFace": "Cascadia Code PL",
            "fontSize": 10,
            "commandline": "D:\\Developer\\cygwin64\\bin\\bash.exe --login -i",
            "cursorShape": "filledBox",
            "padding": "2",
            "hidden": false
        },
        {
            // Make changes here to the powershell.exe profile
            "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
            "name": "Windows PowerShell",
            "commandline": "powershell.exe",
            "cursorShape": "filledBox",
            "hidden": false,
            "fontFace": "Cascadia Code PL",
            "fontSize": 10
        },
        {
            // Make changes here to the cmd.exe profile
            "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
            "name": "cmd",
            "commandline": "cmd.exe",
            "hidden": false,
            "fontFace": "Cascadia Code PL",
            "fontSize": 10,
            "cursorShape": "filledBox"
        },
        {
            "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
            "hidden": true,
            "name": "Azure Cloud Shell",
            "cursorShape": "filledBox",
            "fontFace": "Cascadia Code",
            "fontSize": 10,
            "source": "Windows.Terminal.Azure"
        },
        {
            "guid": "{2c4de342-38b7-51cf-b940-2309a097f518}",
            "hidden": false,
            "name": "Ubuntu",
            "source": "Windows.Terminal.Wsl",
            "cursorShape": "filledBox",
            "fontFace": "Cascadia Code PL",
            "padding": 2,
            "fontSize": 10
        }
    ],
    // Add custom color schemes to this array
    "schemes": [],
    // Add any keybinding overrides to this array.
    // To unbind a default keybinding, set the command to "unbound"
    "keybindings": [
        {
            "command": "switchToTab0",
            "keys": [
                "alt+1"
            ]
        },
        {
            "command": "switchToTab1",
            "keys": [
                "alt+2"
            ]
        },
        {
            "command": "switchToTab2",
            "keys": [
                "alt+3"
            ]
        },
        {
            "command": "switchToTab3",
            "keys": [
                "alt+4"
            ]
        },
        {
            "command": "switchToTab4",
            "keys": [
                "alt+5"
            ]
        },
        {
            "command": "switchToTab4",
            "keys": [
                "alt+5"
            ]
        },
        {
            "command": "switchToTab5",
            "keys": [
                "alt+6"
            ]
        },
        {
            "command": "switchToTab6",
            "keys": [
                "alt+7"
            ]
        },
        {
            "command": "switchToTab7",
            "keys": [
                "alt+8"
            ]
        },
        {
            "command": "switchToTab8",
            "keys": [
                "alt+9"
            ]
        }
    ]
}
```
