#!/usr/bin/env python3

import pytest
from unittest.mock import patch
from migrate_teams import does_user_exist

@patch("migrate_teams.requests.get")
def test_does_user_exist(mock_get):
    # Simulate a successful response where the user exists
    mock_get.return_value.status_code = 200
    assert does_user_exist("username", "new-token") == True

    # Simulate a failed response where the user doesn't exist
    mock_get.return_value.status_code = 404
    assert does_user_exist("nonexistent_user", "new-token") == False
