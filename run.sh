#!/bin/bash
echo "Starting Auto Mouse Mover..."
echo "Press Ctrl+C to stop."

# Check if python3 exists
if command -v python3 &> /dev/null; then
    python3 auto_mouse_mover.py
else
    echo "Python3 could not be found. Please install it."
    exit 1
fi
