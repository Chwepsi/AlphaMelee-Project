import pytest
from src.data_processing import load_slippi_game, get_frame_data

def test_load_valid_file():
    game = load_slippi_game("data/replays/Game_20220928T194206.slp")
    assert game is not None, "Le chargement du fichier a échoué"

def test_frame_extraction():
    game = load_slippi_game("data/replays/Game_20220928T194206.slp")
    frame_data = get_frame_data(game, 0)
    
    assert frame_data is not None
    assert 'players' in frame_data
    assert len(frame_data['players']) >= 2