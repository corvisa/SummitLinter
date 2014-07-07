#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
#
# Copyright (c) 2014 CorvisaCloud, LLC
#
# License: MIT
#

"""This module exports the LuaSummit plugin class."""

from SublimeLinter.lint import Linter, util


class SummitLinter(Linter):
    """Provides an interface to luacheck for the SummitEditor syntax."""
    syntax = 'summit'
    tempfile_suffix = 'lua'
    defaults = {
        '--ignore:,': 'channel',
        '--only:,': '',
        '--limit=': None,
        '--globals: ': '',
    }
    comment_re = r'\s*-[-*]'
    inline_settings = ('ignore', 'limit', 'only', 'globals')
    cmd = 'luacheck @ *'
    regex = r'^(?P<filename>[^:]+):(?P<line>\d+):(?P<col>\d+): (?P<message>.*)$'
    def build_args(self, settings):
        """Return args, transforming --ignore, --only, and --globals args into a format luacheck understands."""
        args = super().build_args(settings)
        try:
            index = args.index('--ignore')
            # Split the comma-separated arg after --ignore into separate elements
            vars = args[index + 1].split(',')
            args[index + 1:index + 2] = vars
        except ValueError:
            pass
        
        try:
            index = args.index('--only')
            vars = args[index + 1].split(',')
            args[index + 1:index + 2] = vars
        except ValueError:
            pass

        try:
            index = args.index('--globals')
            vars = args[index + 1].split(',')
            args[index + 1:index + 2] = vars
        except ValueError:
            pass
            
        return args
