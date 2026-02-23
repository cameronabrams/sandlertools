"""
Sandler Tools

A metapackage combining several computational tools based on
Chemical, Biochemical, and Engineering Thermodynamics (5th edition)
by Stan Sandler
https://www.pearson.com/us/higher-education/program/Sandler-Chemical-Biochemical-and-Engineering-Thermodynamics-5th-Edition/PGM332005.html

Copyright (c) 2025 Cameron F Abrams
"""

from sandlerprops import Compound, PropertiesDatabase, get_database
from sandlersteam import State as SandlerSteamState
from sandlersteam import get_tables
from sandlercubics import IdealGasEOS, VanDerWaalsEOS, SoaveRedlichKwongEOS, PengRobinsonEOS
from sandlercorrespondingstates import CSState
from sandlermisc import R, DeltaH_IG, DeltaS_IG, ureg
from sandlerchemeq import Component, Reaction, ChemEqSystem
from importlib.metadata import version

def __getattr__(name):
    """Lazy-load expensive singleton objects on first access.

    ``SteamTables`` and ``Properties`` each require significant time and memory
    to initialise (parsing large data files), so they are not created at import
    time.  Instead, Python's module-level ``__getattr__`` hook defers
    construction until the first attribute access.  The object is then stored as
    a module-level global so that subsequent accesses return the cached instance
    without re-parsing.

    Parameters
    ----------
    name : str
        Attribute name being looked up on the module.

    Returns
    -------
    object
        The requested singleton object.

    Raises
    ------
    AttributeError
        If *name* is not a recognised lazy attribute.
    """
    global SteamTables, Properties
    if name == 'SteamTables':
        SteamTables = get_tables()
        return SteamTables
    if name == 'Properties':
        Properties = get_database()
        return Properties
    raise AttributeError(f"module 'sandlertools' has no attribute {name!r}")

# Installed versions of each dependency, queried at import time.
# Consumed by cli.py to display the version banner.
versions = {
    'sandlerprops': version('sandlerprops'),
    'sandlersteam': version('sandlersteam'),
    'sandlercubics': version('sandlercubics'),
    'sandlercorrespondingstates': version('sandlercorrespondingstates'),
    'sandlermisc': version('sandlermisc'),
    'sandlerchemeq': version('sandlerchemeq'),
}

__all__ = [ 'Compound',
            'PropertiesDatabase',
            'get_database',
            'Properties',
            'SandlerSteamState', 
            'SteamTables', 
            'get_tables',
            'IdealGasEOS', 
            'VanDerWaalsEOS', 
            'SoaveRedlichKwongEOS', 
            'PengRobinsonEOS', 
            'CSState',
            'R',
            'ureg', 
            'DeltaH_IG', 
            'DeltaS_IG',
            'Component',
            'Reaction',
            'ChemEqSystem' ]