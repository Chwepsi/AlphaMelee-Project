## Dans ce fichier, nous allons rafiner les informations brutes  extraites du replay file, 
# afin de les rendre plus exploitables pour l'entraînement de notre modèle.
#
from slippi import Game

def extract_game_features(game, max_frames=1000):
    """Extrait les features temporelles pour l'entraînement"""
    features = []
    
    for frame_num in range(min(len(game.frames), max_frames)):
        frame_data = get_frame_data(game, frame_num)
        if not frame_data:
            continue
            
        # Exemple de features complexes
        player_features = {
            'distance_entre_joueurs': calculate_distance(frame_data),
            'delta_damage': calculate_damage_diff(frame_data),
            'stage_control': calculate_stage_control(frame_data)
        }
        features.append(player_features)
    
    return features