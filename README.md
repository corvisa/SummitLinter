SummitLinter
================================

This linter plugin for [SublimeLinter][docs] provides an interface to [Corvisa Cloud, LLC's SummitEditor](https://github.com/corvisacloud/SummitEditor) through `luacheck`. It will be used with files that have the “__Lua (Summit)__” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation]. SummitEditor must also be installed. If it is not installed, follow the [instructions](https://github.com/corvisacloud/SummitEditor/blob/master/README.md).

### Linter installation
Before using this plugin, you must ensure that `luacheck` is installed on your system. To install `luacheck`, follow the [instructions](https://github.com/mpeterv/luacheck/blob/master/README.md).

**Note:** `luacheck` requires `lua` to be installed.

### Linter configuration
In order for `luacheck` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `luacheck`, you can proceed to install the SummitLinter plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `SummitLinter`. Among the entries you should see `SummitLinter`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SummitLinter provides its own settings adapted from the [`luacheck` settings](https://github.com/mpeterv/luacheck#command-line-interface). Those marked as “Default Setting" have their own setting in SublimeLinter's user settings for `summitlinter`. Those not marked as "Default Setting" go in the `args` list in SublimeLinter's user settings for `summitlinter`.

|Setting|Description|Default Setting|
|:------|:----------|:-------------:|
|`-g, --no-global`|Do not check for accessing global variables.| |
|`-r, --no-redefined`|Do not check for redefined variables.| |
|`-u, --no-unused`|Do not check for unused variables.| |
|`-a, --no-unused-args`|Do not check for unused arguments and loop variables. ||
|`-v, --no-unused-values`|Do not check for unused values.||
|`globals [<global>]`|Defined globals.|&#10003;|
|`-c, --compat`|Adjust globals for Lua 5.1/5.2 compatibility.||
|`-e, --ignore-env`|Do not be _ENV-aware.||
|`ignore [<var>]`|Do not report warnings related to these variables|&#10003;|
|`only [<var>]`|Only report warnings related to these variables|&#10003;|
|`limit <limit>`|Exit with 0 if there are \<limit\> or less warnings.|&#10003;|
|`-q, --quiet`|Suppress output for files without warnings. `-qq`: Only print total number of warnings and errors. `-qqq`: Suppress output completely. ||

Settings marked as "Default Setting" may also be used inline as per [SublimeLinter's documentation][inline-settings]. Since, by default, `channel` and `require` are pre-defined as `globals`, using the `globals`setting inline requires you to include `channel` and `require` again in addition to any other settings. For example: `-- [SublimeLinter summitlinter-globals:channel,require,foo]` will maintain default behavior while adding `foo` as a global. This follows for any default settings saved in SublimeLinter's user settings as well. For example, if `"ignore": "foo"` is in your user settings, using `ignore` to ignore `bar` inline (while continuing to ignore `foo`) would require the following: `-- [SublimeLinter summitlinter-ignore:foo,bar]`.

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
