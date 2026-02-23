# Sandlertools

> A metapackage of computational tools based on Sandler's *Chemical, Biochemical, and Engineering Thermodynamics* (5th ed.)

Sandlertools bundles six companion packages into a single installation and
wires their command-line interfaces into one unified `sandlertools` command.
It should be used for educational purposes only.

## Installation

```sh
pip install sandlertools
```

## Included packages

| Package | Description | Links |
|---------|-------------|-------|
| `sandlerprops` | Pure-component properties database | [GitHub](https://github.com/cameronabrams/sandlerprops) · [PyPI](https://pypi.org/project/sandlerprops/) · [Docs](https://sandlerprops.readthedocs.io/) |
| `sandlersteam` | Steam tables | [GitHub](https://github.com/cameronabrams/sandlersteam) · [PyPI](https://pypi.org/project/sandlersteam/) · [Docs](https://sandlersteam.readthedocs.io/) |
| `sandlercubics` | Cubic equations of state | [GitHub](https://github.com/cameronabrams/sandlercubics) · [PyPI](https://pypi.org/project/sandlercubics/) · [Docs](https://sandlercubics.readthedocs.io/) |
| `sandlercorrespondingstates` | Corresponding-states chart reads | [GitHub](https://github.com/cameronabrams/sandlercorrespondingstates) · [PyPI](https://pypi.org/project/sandlercorrespondingstates/) · [Docs](https://sandlercorrespondingstates.readthedocs.io/) |
| `sandlerchemeq` | Chemical equilibrium calculations | [GitHub](https://github.com/cameronabrams/sandlerchemeq) · [PyPI](https://pypi.org/project/sandlerchemeq/) · [Docs](https://sandlerchemeq.readthedocs.io/) |
| `sandlermisc` | Miscellaneous utilities (gas constant, ideal-gas functions, unit registry) | [GitHub](https://github.com/cameronabrams/sandlermisc) · [PyPI](https://pypi.org/project/sandlermisc/) · [Docs](https://sandlermisc.readthedocs.io/) |

## Command-line usage

```sh
sandlertools [<global-options>] <command> [<command-options>]
```

```
$ sandlertools --help
```

Global options (`--banner`/`--no-banner`, `--logging-level`, `--log`) apply to
all subcommands.  Each subcommand's own options and examples are described in
the corresponding package's documentation.

| Subcommand | Delegates to |
|------------|--------------|
| `props`    | `sandlerprops` |
| `cubic`    | `sandlercubics` |
| `steam`    | `sandlersteam` |
| `cs`       | `sandlercorrespondingstates` |
| `chemeq`   | `sandlerchemeq` |

## Python API

`sandlertools` re-exports the public API of each sub-package so that a single
import is sufficient for most use cases:

```python
from sandlertools import (
    # sandlerprops
    Compound, PropertiesDatabase, get_database, Properties,
    # sandlersteam
    SandlerSteamState, SteamTables, get_tables,
    # sandlercubics
    IdealGasEOS, VanDerWaalsEOS, SoaveRedlichKwongEOS, PengRobinsonEOS,
    # sandlercorrespondingstates
    CSState,
    # sandlerchemeq
    Component, Reaction, ChemEqSystem,
    # sandlermisc
    R, ureg, DeltaH_IG, DeltaS_IG,
)
```

`Properties` and `SteamTables` are lazy singletons — the underlying data files
are parsed only on first access.  See each sub-package's documentation for
class signatures and usage examples.

## Release history

* **0.5.1** — changed default banner behaviour
* **0.5.0** — reports versions of all tools in banner message
* **0.4.0** — `sandlerchemeq` integration
* **0.3.0** — `SteamRequest` implemented
* **0.2.0** — updated readme
* **0.1.0** — initial release

## Meta

Cameron F. Abrams — cfa22@drexel.edu
Distributed under the MIT license. See `LICENSE` for more information.
<https://github.com/cameronabrams>

## Contributing

1. Fork it (<https://github.com/cameronabrams/sandlertools/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
