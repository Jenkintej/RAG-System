import os
from pathlib import Path
import logging
logging.basicConfig(Level=logging.INFO,format='[%(asctime)s]:%message)s:')

list_of_files=[
    f"src/_init_.py",
    f"src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]
