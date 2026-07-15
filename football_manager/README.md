# Football Manager

A small custom Odoo 19.0 module for managing football teams and players — built to practice Many2one/One2many relationships and country-filtered dropdowns.

## Features

- Team form shows its players inline via a One2many field (`player_ids`) — add/edit players directly from the team without leaving the form
- Picking a Team's Country narrows the State dropdown to that country's states/provinces (`res.country.state`, domain on `country_id`)

## Model: `football.team`

| Field          | Type      | Notes                                              |
|----------------|-----------|-------------------------------------------------------|
| `name`         | Char      | Required                                            |
| `country_id`   | Many2one  | `res.country`                                       |
| `state_id`     | Many2one  | `res.country.state`, domain-filtered by `country_id`|
| `founded_year` | Integer   |                                                      |
| `player_ids`   | One2many  | Inverse of `football.player.team_id`                |

## Model: `football.player`

| Field           | Type      | Notes                                  |
|-----------------|-----------|-------------------------------------------|
| `name`          | Char      | Required                                 |
| `team_id`       | Many2one  | `football.team`                          |
| `position`      | Selection | Goalkeeper / Defender / Midfielder / Forward |
| `jersey_number` | Integer   |                                           |
| `age`           | Integer   |                                           |
| `market_value`  | Float     |                                           |
| `photo`         | Binary    | Image widget                             |

## How `team_id` / `player_ids` stay in sync

`team_id` on `football.player` is the only place the relationship is stored — a real foreign key column. `player_ids` on `football.team` is not a database column at all; it's a live query for "all players whose `team_id` equals this team." There's nothing to keep in sync because there's only one fact in the database.

## Requirements

- Odoo 19.0
- Depends only on core `base` (`res.country.state` ships with it — no extra dependency needed)
- Note: many countries have zero states in Odoo's data (e.g. Monaco, Singapore) — an empty State dropdown for those is expected, not a bug

## Installation

Clone the parent repo alongside your Odoo source and point `--addons-path` at it:

```bash
python odoo-bin \
  --addons-path=/path/to/odoo/addons,/path/to/odoo-custom-modules \
  -d your_database \
  -i football_manager
```

Or, once running, install it from **Apps** in the UI (remove the default filter, search "Football Manager").

## License

LGPL-3
