#! /bin/bash

echo "Running server..."
python bottle.py --bind=0.0.0.0:80 server
echo "Done."


