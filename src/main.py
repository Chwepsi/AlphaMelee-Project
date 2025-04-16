from src.data_processing import load_slippi_game, get_frame_data

def main():
    game = load_slippi_game("data/replays/Game_20220928T194206.slp")
    if game is None:
        return

    # Analyser la frame 1234
    frame_data = get_frame_data(game, 1234)
    if frame_data:
        print(f"Stage: {frame_data['stage']}")
        for port, player in frame_data['players'].items():
            print(f"Joueur {port}: {player['character']} - {player['position']}")

if __name__ == "__main__":
    main()