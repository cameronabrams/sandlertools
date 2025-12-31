# Sandlertools

> A metapackage of utilities from Sandler's 5th ed.

Sandlertools combines several packages that implement computational tools based on _Chemical, Biochemical, and Engineering Thermodynamics_ (5th edition) by Stan Sandler (Wiley, USA). It should be used for educational purposes only.


## Installation 

Sandlertools is available via `pip`:

```sh
pip install sandlertools
```

This will install 
* `sandlerprops` -- pure component properties database
* `sandlersteam` -- steam tables
* `sandlercubics` -- real-gas cubic equations of state
* `sandlercorrespondingstates` -- corresponding-states chart reads
* `sandlermisc` -- miscellaneous utilities

## Usage

### Command-line

The general structure of a `sandlertools` command is

```sh
$ sandlertools [<global-options>] <tool> [<tool-options>]
```

```sh
$ sandlertools --help
usage: sandlertools [-h] [-b | --banner | --no-banner] [--logging-level {None,info,debug,warning}] [-l LOG] <command> ...

Sandler Tools: A collection of computational tools based on Chemical, Biochemical, and Engineering Thermodynamics (5th edition) by Stan Sandler

options:
  -h, --help            show this help message and exit
  -b, --banner, --no-banner
                        toggle banner message
  --logging-level {None,info,debug,warning}
                        Logging level for messages written to diagnostic log
  -l LOG, --log LOG     File to which diagnostic log messages are written

subcommands:
  <command>
    props               query and manipulate thermophysical property data
    cubic               query and manipulate cubic equation of state calculations
    steam               work with steam tables and properties of water/steam
    cs                  work with corresponding states calculations
```

### API

`sandlertools` exposes several classes, objects, and functions from its component packages:

* `PropertiesDatabase` -- the pure-component properties database class from the `sandlerprops.properties` module
* `SandlerSteamState`  -- the `State` class from the `sandlersteam.state` module
* `SteamTables` -- the `SteamTables` object from the `sandlersteam.state` module
* `IdealGasEOS`, `GeneralizedVDWEOS`, and `PengRobinsonEOS` classes from the `sandlercubics.eos` module
* `CorrespondingStatesChartReader` class from the `sandlercorrespondingstates.charts` module
* `GasConstant` class from the `sandlermisc.gas_constant` module
* `DeltaH_IG` and `DeltaS_IG` functions from `sandlermisc.thermals`

## Release History

* 0.1.0
    * Initial release

## Meta

Cameron F. Abrams – cfa22@drexel.edu

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/cameronabrams](https://github.com/cameronabrams/)

## Contributing

1. Fork it (<https://github.com/cameronabrams/sandlertools/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
