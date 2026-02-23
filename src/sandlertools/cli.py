"""
Command-line interface for sandlertools.

Provides a unified ``sandlertools`` command whose subcommands delegate directly
to the CLI entry points of each dependency package::

    sandlertools props   → sandlerprops.cli.cli()
    sandlertools cubic   → sandlercubics.cli.cli()
    sandlertools steam   → sandlersteam.cli.cli()
    sandlertools cs      → sandlercorrespondingstates.cli.cli()
    sandlertools chemeq  → sandlerchemeq.cli.cli()

Delegation is done by rewriting ``sys.argv`` before calling the sub-package
CLI function (see ``cli()`` for details).
"""
import argparse as ap
import shutil
import logging
import os
import sys

from sandlerprops.cli import cli as props_cli
from sandlersteam.cli import cli as steam_cli
from sandlercubics.cli import cli as cubics_cli
from sandlercorrespondingstates.cli import cli as cs_cli
from sandlerchemeq.cli import cli as chemeq_cli

from . import versions

banner = """ 
╔════════════════════════════════════════════════════════════╗
   __             __        ___  __  ___  __   __        __  
  /__`  /\  |\ | |  \ |    |__  |__)  |  /  \ /  \ |    /__` 
  .__/ /~~\ | \| |__/ |___ |___ |  \  |  \__/ \__/ |___ .__/ 
              (c) 2025, Cameron F. Abrams <cfa22@drexel.edu>
╚════════════════════════════════════════════════════════════╝
"""
for tool in ['sandlerprops', 'sandlersteam', 'sandlercubics', 'sandlercorrespondingstates', 'sandlermisc', 'sandlerchemeq']:
    banner += f'\n  {tool:>26s} {versions[tool]}'

class ConditionalBannerFormatter(ap.RawDescriptionHelpFormatter):
    """argparse help formatter that prepends the ASCII art version banner.

    By default ``argparse`` prints help as::

        usage: sandlertools ...

        <description>
        <options>

    This formatter reorders the output to::

        <banner>

        <description>
        usage: sandlertools ...
        <options>

    so the banner and description appear prominently before the usage line.
    The banner is suppressed when ``--no-banner`` is present in ``sys.argv``
    (checked directly because argparse has not yet parsed the flag when
    ``format_help`` is called).
    """

    def format_help(self):
        help_text = super().format_help()

        # argparse separates the usage line, description, and options sections
        # with double newlines.  Split on the first two to extract each piece.
        parts = help_text.split('\n\n', 2)

        if len(parts) >= 2:
            usage = parts[0]        # "usage: sandlertools ..."
            description = parts[1]  # the description= string
            rest = parts[2] if len(parts) > 2 else ''  # options / subcommands

            # Reassemble: banner first, then description, then usage+options.
            result = []
            if '--no-banner' not in sys.argv:
                result.append(banner)
            result.extend([description, usage, rest])
            return '\n\n'.join(result)

        # Fallback: couldn't split into expected sections; prepend banner as-is.
        if '--no-banner' not in sys.argv:
            return banner + '\n' + help_text
        return help_text

logger = logging.getLogger(__name__)


def setup_logging(args):
    """Configure the root logger for a sandlertools session.

    Two handlers are set up:

    * **File handler** (optional) — writes timestamped records at the level
      specified by ``--logging-level`` (default ``debug``).  If the log file
      already exists it is copied to ``<file>.bak`` before being overwritten.
    * **Console handler** — always present; writes ``INFO``-and-above messages
      to stderr in a compact ``LEVEL> message`` format.  Verbose debug output
      is intentionally excluded from the console so as not to overwhelm users.

    Parameters
    ----------
    args : argparse.Namespace
        Parsed command-line arguments.  Expected attributes:

        ``logging_level`` : str
            One of ``'debug'``, ``'info'``, or ``'warning'``.
        ``log`` : str
            Path to the diagnostic log file, or an empty string to skip
            file logging.
    """
    loglevel_numeric = getattr(logging, args.logging_level.upper())
    if args.log:
        if os.path.exists(args.log):
            # Preserve the previous log so a failed run can be diagnosed.
            shutil.copyfile(args.log, args.log + '.bak')
        logging.basicConfig(
            filename=args.log,
            filemode='w',
            format='%(asctime)s %(name)s %(message)s',
            level=loglevel_numeric,
        )
    # Console output is always limited to INFO so debug noise stays in the file.
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s> %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def cli():
    """Entry point for the ``sandlertools`` command.

    Parses the top-level arguments (``--logging-level``, ``--log``,
    ``--banner``/``--no-banner``) and a required subcommand name, then
    delegates to the corresponding sub-package CLI function.

    Delegation strategy
    -------------------
    Each sub-package CLI (e.g. ``sandlerprops``) is a self-contained function
    that reads its own arguments from ``sys.argv``.  To reuse those functions
    without modification, sandlertools:

    1. Strips its own arguments from ``sys.argv`` via ``parse_known_args``,
       leaving only the subcommand-specific arguments in ``remaining``.
    2. Replaces ``sys.argv`` with ``['sandlertools-<command>'] + remaining``
       so the sub-package parser sees a sensible program name and its own flags.
    3. Calls the sub-package ``cli()`` function, which then parses ``sys.argv``
       as if it had been invoked directly.
    """
    subcommands = {
        'props': dict(
            func = props_cli,
            help = 'query and manipulate thermophysical property data'
        ),
        'cubic': dict(
            func = cubics_cli,
            help = 'query and manipulate cubic equation of state calculations'
        ),
        'steam': dict(
            func = steam_cli,
            help = 'work with steam tables and properties of water/steam'
        ),
        'cs': dict(
            func = cs_cli,
            help = 'work with corresponding states calculations'
        ),
        'chemeq': dict(
            func = chemeq_cli,
            help = 'work with chemical equilibrium calculations'
        ),
    }
    parser = ap.ArgumentParser(
        description="Sandlertools: A collection of computational tools based on Chemical, Biochemical, and Engineering Thermodynamics (5th edition) by Stan Sandler",
        formatter_class = ConditionalBannerFormatter,
        epilog="(c) 2025, Cameron F. Abrams <cfa22@drexel.edu>")
        
    parser.add_argument(
        '-b',
        '--banner',
        default=True,
        action=ap.BooleanOptionalAction,
        help='toggle banner message'
    )
    parser.add_argument(
        '--logging-level',
        type=str,
        default='debug',
        choices=[None, 'info', 'debug', 'warning'],
        help='Logging level for messages written to diagnostic log'
    )
    parser.add_argument(
        '-l',
        '--log',
        type=str,
        default='', # no log file by default
        help='File to which diagnostic log messages are written'
    )
    subparsers = parser.add_subparsers(
        title="subcommands",
        dest="command",
        metavar="<command>",
        required=True,
    )
    command_parsers={}
    for k, specs in subcommands.items():
        command_parsers[k] = subparsers.add_parser(
            k,
            help=specs['help'],
            formatter_class=ap.RawDescriptionHelpFormatter,
            add_help=False
        )
        command_parsers[k].set_defaults(func=specs['func'])

    # parse_known_args consumes sandlertools' own flags and returns any
    # unrecognised tokens in `remaining` (the subcommand's arguments).
    args, remaining = parser.parse_known_args()

    # Rewrite sys.argv so the sub-package CLI sees a clean argument list:
    #   argv[0]  → 'sandlertools-<command>'  (used as the program name in help)
    #   argv[1:] → the subcommand-specific flags passed by the user
    sys.argv = [f'sandlertools-{args.command}'] + remaining

    if hasattr(args, 'func'):
        setup_logging(args)
        args.func()   # calls the sub-package CLI, which re-parses sys.argv
        print('Thanks for using sandlertools!')
    else:
        # Reached only if subparsers required=True is somehow bypassed.
        my_list = ', '.join(list(subcommands.keys()))
        print(f'No subcommand found. Expected one of {my_list}')