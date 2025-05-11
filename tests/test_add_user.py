#!/usr/bin/env python3

from unittest.mock import patch
import logging
from migrate_teams import add_user_to_team

@patch("migrate_teams.requests.put")
def test_add_user_to_team(mock_put):
    # Simulate a successful response
    mock_put.return_value.status_code = 200

    with patch("migrate_teams.logging.info") as mock_info:
        add_user_to_team("new-enterprise", "team_slug", "new_username", "new-token", dry_run=False)
        mock_info.assert_called_with("Added new_username to new-enterprise/team_slug")

    # Simulate a failure
    mock_put.return_value.status_code = 400
    with patch("migrate_teams.logging.error") as mock_error:
        add_user_to_team("new-enterprise", "team_slug", "new_username", "new-token", dry_run=False)
        mock_error.assert_called_with("Failed to add new_username to new-enterprise/team_slug, status code: 400")
