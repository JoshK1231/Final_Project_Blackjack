import json
from datetime import datetime
from pathlib import Path
"""This is what I have so far. I did not like how I previously had this code set up. I am now figuring out how I want my data
 from the games to be stored. I want to use a user ID for games instead of entering a name because blackjack doesn't ask
  for player names. """
BASE_DIR = Path(__file__).resolve().parent

GAME_DATA = BASE_DIR / "blackjack_data.txt"
ERROR_LOG = BASE_DIR / "error.txt"
#TODO record and log errors info

def show_game_data():

def save_game_data():

def create_game_data(game_data):
    games = load_game_logs():
    game_logs = game_data_copy()
""""work in progress"""

def write_game_data(games):

def update_game

def log error:




