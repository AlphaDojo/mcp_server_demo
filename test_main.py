from main import add, get_player_stat
import logging

# def test_add():
#     result = add(2, 2)
#     logging.warning(f"Result: {result}") 
#     assert result == 4


def test_get_player_stat_success():
    result = get_player_stat("Shohei Ohtani", "home_runs")
    logging.warning(f"Result: {result}") 
    assert result == '44'

def test_get_player_stat_player_not_found():
    result = get_player_stat("Pee Wee Reese", "home_runs")
    logging.warning(f"Result: {result}") 
    assert result == 'Player not found'

def test_get_player_stat_stat_not_found():
    result = get_player_stat("Shohei Ohtani", "ERA")
    logging.warning(f"Result: {result}") 
    assert result == 'Stat not found'