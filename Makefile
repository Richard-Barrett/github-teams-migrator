
.PHONY: install clean docker

install:
    pip install .

clean:
    rm -rf build dist migrate_teams.egg-info

docker:
    docker build -t migrate-teams .
