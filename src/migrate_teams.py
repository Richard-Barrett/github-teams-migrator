
import requests
import logging
import argparse
import csv
import json

# Define helper functions for API interactions
def does_user_exist(username, token):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def is_user_in_team(org, team_slug, username, token):
    url = f"https://api.github.com/orgs/{org}/teams/{team_slug}/memberships/{username}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def add_user_to_team(org, team_slug, username, token, dry_run=False):
    if dry_run:
        logging.info(f"Dry run: would add {username} to {org}/{team_slug}")
    else:
        url = f"https://api.github.com/orgs/{org}/teams/{team_slug}/memberships/{username}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json"
        }
        response = requests.put(url, headers=headers)
        if response.status_code == 200:
            logging.info(f"Added {username} to {org}/{team_slug}")
        else:
            logging.error(f"Failed to add {username} to {org}/{team_slug}, status code: {response.status_code}")

def migrate_teams(old_enterprise, new_enterprise, old_token, new_token, dry_run=False, log_file='migration.log', results_file=None, output_format="json"):
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    results = []
    orgs = get_orgs(new_enterprise, new_token)  # You need to define this function

    for org in orgs:
        teams = get_teams(new_enterprise, org, new_token)  # You need to define this function
        for team in teams:
            team_slug = team['slug']
            old_members = get_old_members(old_enterprise, team_slug, old_token)  # You need to define this function
            for old_username in old_members:
                new_username = convert_username(old_username)  # You need to define this function

                if not does_user_exist(new_username, new_token):
                    logging.warning(f"⚠️ User {new_username} does not exist in GitHub — skipping")
                    results.append({
                        "org": org,
                        "team": team_slug,
                        "old_username": old_username,
                        "new_username": new_username,
                        "status": "user-not-found"
                    })
                    continue

                if is_user_in_team(org, team_slug, new_username, new_token):
                    logging.info(f"🔁 {new_username} is already in {org}/{team_slug} — skipping")
                    results.append({
                        "org": org,
                        "team": team_slug,
                        "old_username": old_username,
                        "new_username": new_username,
                        "status": "already-member"
                    })
                    continue

                add_user_to_team(org, team_slug, new_username, new_token, dry_run=dry_run)

                results.append({
                    "org": org,
                    "team": team_slug,
                    "old_username": old_username,
                    "new_username": new_username,
                    "status": "dry-run" if dry_run else "added"
                })

    if results_file:
        save_results(results, results_file, output_format)  # You need to define this function

def main():
    parser = argparse.ArgumentParser(description="Migrate users to new GitHub enterprise teams")
    parser.add_argument("--old-enterprise", required=True, help="Name of the old GitHub enterprise")
    parser.add_argument("--new-enterprise", required=True, help="Name of the new GitHub enterprise")
    parser.add_argument("--old-token", required=True, help="GitHub token for the old enterprise")
    parser.add_argument("--new-token", required=True, help="GitHub token for the new enterprise")
    parser.add_argument("--log-file", default="migration.log", help="File to write logs to (default: migration.log)")
    parser.add_argument("--results-file", help="File to store results in CSV or JSON format")
    parser.add_argument("--output", choices=["csv", "json"], default="json", help="Output format (default: json)")
    parser.add_argument("--dry-run", action="store_true", help="Only simulate the migration")

    args = parser.parse_args()
    migrate_teams(args.old_enterprise, args.new_enterprise, args.old_token, args.new_token, args.dry_run, args.log_file, args.results_file, args.output)
