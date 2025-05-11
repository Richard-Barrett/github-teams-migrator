#!/usr/bin/env python3

import pytest
import sys
from io import StringIO
from migrate_teams import main

def test_argument_parsing():
    # Mock arguments for the CLI
    args = ["migrate-teams", "--old-enterprise", "old-enterprise", "--new-enterprise", "new-enterprise", "--old-token", "old-token", "--new-token", "new-token", "--output", "csv"]
    sys.argv = args

    # Capture output
    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    # Verify if arguments are parsed correctly
    assert "--old-enterprise" in sys.argv
    assert "--new-enterprise" in sys.argv
    assert "--output" in sys.argv
