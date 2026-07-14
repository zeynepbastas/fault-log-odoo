# Odoo Custom Modules

A collection of small custom Odoo 19.0 modules, built as learning exercises to practice module structure, views, and field relationships.

## Modules

- [`fault_log/`](fault_log) — log and track equipment/machine faults
- [`football_manager/`](football_manager) — teams and players, with Many2one/One2many and country→city relational fields

## Installation

Clone this repo alongside your Odoo source and point `--addons-path` at it:

```bash
python odoo-bin \
  --addons-path=/path/to/odoo/addons,/path/to/this/repo \
  -d your_database \
  -i fault_log,football_manager
```

Or, once running, install each from **Apps** in the UI (remove the default filter, search by module name).

---

## `fault_log`

Logs equipment/machine faults — inspired by a client's need to track recurring machine faults by product and severity.

**Features**
- Log faults with a title, related product/machine, severity, description, and report date
- Track each fault through a simple workflow: **New → Investigating → Resolved**

**Model: `fault.log`**

| Field           | Type       | Notes                                |
|-----------------|------------|----------------------------------------|
| `name`          | Char       | Required. Short fault title            |
| `product_id`    | Many2one   | `product.product` — machine/product    |
| `severity`      | Selection  | Low / Medium / High                    |
| `description`   | Text       |                                         |
| `date_reported` | Date       | Defaults to today                      |
| `state`         | Selection  | New / Investigating / Resolved         |

**Depends on:** core `product` module

---

## `football_manager`

Teams and players, built specifically to practice Many2one/One2many relationships and a country-filtered city dropdown.

**Features**
- Team form shows its players inline via a One2many field (`player_ids`) — add/edit players directly from the team without leaving the form
- Picking a Team's Country narrows the City dropdown to that country's cities (`res.city`, domain on `country_id`)

**Model: `football.team`**

| Field          | Type      | Notes                                          |
|----------------|-----------|--------------------------------------------------|
| `name`         | Char      | Required                                        |
| `country_id`   | Many2one  | `res.country`                                   |
| `city_id`      | Many2one  | `res.city`, domain-filtered by `country_id`     |
| `founded_year` | Integer   |                                                  |
| `player_ids`   | One2many  | Inverse of `football.player.team_id`            |

**Model: `football.player`**

| Field           | Type      | Notes                                  |
|-----------------|-----------|-------------------------------------------|
| `name`          | Char      | Required                                 |
| `team_id`       | Many2one  | `football.team`                          |
| `position`      | Selection | Goalkeeper / Defender / Midfielder / Forward |
| `jersey_number` | Integer   |                                           |
| `age`           | Integer   |                                           |
| `market_value`  | Float     |                                           |
| `photo`         | Binary    | Image widget                             |

**Depends on:** core `base_address_extended` module (provides `res.city`). Ships a small seed of sample cities for US/UK/Germany/Spain (`data/football_city_data.xml`), since `base_address_extended` provides the model but no data itself.

## License

LGPL-3
