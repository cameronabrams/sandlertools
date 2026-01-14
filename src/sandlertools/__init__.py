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
from sandlercorrespondingstates import CorrespondingStatesChartReader
from sandlermisc import GasConstant, DeltaH_IG, DeltaS_IG
from sandlerchemeq import Component, Reaction, ChemEqSystem

from importlib.metadata import version

SteamTables = get_tables()
Properties = get_database()

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
            'CorrespondingStatesChartReader', 
            'GasConstant', 
            'DeltaH_IG', 
            'DeltaS_IG',
            'Component',
            'Reaction',
            'ChemEqSystem' ]