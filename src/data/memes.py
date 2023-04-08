import os
import random

FILE_DIR = "src/data/img/"

def get_random_file():
    files = [f for f in os.listdir(FILE_DIR) if os.path.isfile(os.path.join(FILE_DIR, f))]
    return FILE_DIR + random.choice(files)
