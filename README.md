
# Migrate Teams CLI Tool

This CLI tool is used to migrate users and teams from one GitHub enterprise account to another, ensuring that users are bucketed correctly under their new usernames. It handles edge cases such as missing users, existing memberships, and allows for dry-runs.

## Installation

```bash
pip install migrate-teams
```

## Usage

```bash
migrate-teams --old-enterprise old-enterprise-name --new-enterprise new-enterprise-name --old-token old-token --new-token new-token
```

## Options

- `--old-enterprise`: Name of the old GitHub enterprise
- `--new-enterprise`: Name of the new GitHub enterprise
- `--old-token`: Token for the old GitHub enterprise
- `--new-token`: Token for the new GitHub enterprise
- `--log-file`: File to write logs to (default: `migration.log`)
- `--results-file`: File to store the results in either CSV or JSON format
- `--output`: The output format for the results (`csv` or `json`)
- `--dry-run`: If set, the tool will only simulate the migration and not actually add users to teams
