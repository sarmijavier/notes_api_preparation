#!/bin/sh -e

if [ $# -eq 0 ]; then
  ve_dir=venv
else
  ve_dir="$1"
fi

if [ ! -d "$ve_dir" ]; then
  python3.10 -m venv "$ve_dir"
fi

"$ve_dir"/bin/pip install -r requirements.txt

ve/bin/python mysite/manage.py migrate
yes | ve/bin/python mysite/manage.py flush