#!/usr/bin/env python3

import pytest
import os
import json
import csv
from migrate_teams import save_results

def test_save_results_csv():
    results = [{"org": "new-enterprise", "team": "team_slug", "old_username": "old_user", "new_username": "new_user", "status": "added"}]
    file_path = "/tmp/results.csv"
    save_results(results, file_path, "csv")

    # Check if the file was created
    assert os.path.exists(file_path)

    # Read the CSV to verify contents
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["org"] == "new-enterprise"

    os.remove(file_path)

def test_save_results_json():
    results = [{"org": "new-enterprise", "team": "team_slug", "old_username": "old_user", "new_username": "new_user", "status": "added"}]
    file_path = "/tmp/results.json"
    save_results(results, file_path, "json")

    # Check if the file was created
    assert os.path.exists(file_path)

    # Read the JSON to verify contents
    with open(file_path, mode='r') as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]["org"] == "new-enterprise"

    os.remove(file_path)
