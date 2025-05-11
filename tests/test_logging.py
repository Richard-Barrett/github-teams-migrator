#!/usr/bin/env python3

import logging
from unittest.mock import patch

@patch("migrate_teams.logging.warning")
@patch("migrate_teams.logging.info")
def test_logging(mock_info, mock_warning):
    # Simulate logging behavior for missing user
    with patch("migrate_teams.does_user_exist", return_value=False):
        # Check that the warning is logged when a user does not exist
        mock_warning.reset_mock()
        test_user = "missing_user"
        migrate_teams.add_user_to_team("new-enterprise", "team_slug", test_user, "new-token", dry_run=True)
        mock_warning.assert_called_with(f"⚠️ User {test_user} does not exist in GitHub — skipping")

    # Simulate logging behavior for a successful team addition
    mock_info.reset_mock()
    test_user = "new_username"
    migrate_teams.add_user_to_team("new-enterprise", "team_slug", test_user, "new-token", dry_run=False)
    mock_info.assert_called_with(f"Added {test_user} to new-enterprise/team_slug")
