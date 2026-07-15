# Odoo Custom Modules

A collection of small custom Odoo 19.0 modules, built as learning exercises to practice module structure, views, and field relationships.

## Modules

- [`fault_log/`](fault_log/README.md) — log and track equipment/machine faults
- [`football_manager/`](football_manager/README.md) — teams and players, with Many2one/One2many and country→state relational fields

See each module's own README for its fields, dependencies, and install/upgrade command.

## Installation

Clone this repo alongside your Odoo source and point `--addons-path` at it:

```bash
python odoo-bin \
  --addons-path=/path/to/odoo/addons,/path/to/this/repo \
  -d your_database \
  -i fault_log,football_manager
```

Or, once running, install each from **Apps** in the UI (remove the default filter, search by module name).

## License

LGPL-3
