#!/bin/bash

tmp_directory="/tmp/trento_smart_move"
venv_directory="$tmp_directory/logs_venv"
script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$tmp_directory"

if [ -f "$venv_directory/activate" ]; then
    source "$venv_directory/bin/activate"
else
    python -m venv "$venv_directory"
    source "$venv_directory/bin/activate"
    pip install -r "$script_directory/requirements.txt"
fi

python "$script_directory/working_log.py" "$@"

deactivate
