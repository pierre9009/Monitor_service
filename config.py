#config.py
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='/app/.env')

SLAVES = [
    os.getenv('WORKER1'),
    os.getenv('WORKER2'),
    os.getenv('WORKER3')
]