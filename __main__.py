"""
Usage: python main folder file

python main.py gui hello-world
"""

from pathlib import Path
import sys
import os

try:
    foldername = sys.argv[1]
    filename = sys.argv[2]

    filename = filename.rstrip('.py') + '.py'
except KeyError:
    print('Usage: gui python_script_name')


cmdline = f"python {foldername}/{filename}"
os.system(cmdline)
