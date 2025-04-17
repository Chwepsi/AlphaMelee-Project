from slippi import Game
from typing import Dict, Any, Optional

def load_slippi_game(file_path: str) -> Optional[Game]:
    """Charge un fichier Slippi et retourne l'objet Game"""
    try:
        return Game(file_path)
    except Exception as e:
        print(f"Erreur lors du chargement {file_path}: {e}")
        return None

def get_frame_data(game: Game, frame: int) -> Optional[Dict[str, Any]]:
    """Extrait les données d'une frame spécifique en évitant les cas critiques et les erreurs"""
    try:
        frame = game.frames[frame] # Essaye d'accéder à la frame
    except IndexError:
        return None #si la frame n'est pas trouvée, retourne None

    data = { 
        'frame': frame,
        'stage': game.start.stage.name,
        'players': {}
    } # Dictionnaire pour stocker les données des joueurs

    for port, port_data in enumerate(game.frames[frame].ports):  # Parcourt les ports et leurs informations
        if game.start.players[port] is None or port_data is None:
            continue  # Port non utilisé ou données manquantes

        player = port_data.leader

        # Calcul de la vélocité à partir de la différence de position entre deux frames (absence de fonction de vélocité dans le module)
        if frame > 0:  # Vérifie qu'il y a une frame précédente
            previous_frame = game.frames[frame - 1]
            previous_port_data = previous_frame.ports[port]
            if previous_port_data and previous_port_data.leader: # Vérifie que les données du port précédent existent
                # Calcul de la vélocité en utilisant la position actuelle et la position précédente
                previous_position = previous_port_data.leader.post.position
                current_position = player.post.position
                velocity_x = current_position.x - previous_position.x
                velocity_y = current_position.y - previous_position.y
            else:
                velocity_x, velocity_y = 0.0, 0.0  # Pas de données pour la frame précédente
        else:
            velocity_x, velocity_y = 0.0, 0.0  # Pas de frame précédente pour calculer la vélocité

        # Vérifie l'état d'invincibilité/intangibilité
        INVINCIBILITY_FLAGS = [
            0b10000000000000000000000000000100,
            0b10000000000000000000000000000000,
            0b0
        ]
        INTANGIBILITY_FLAGS = [
            0b100001000100,
            0b1000100,
            0b0,
            0b100000000000
        ]

        # Combine les deux états sous une seule qualité "invincible"
        is_invincible = any(player.post.flags & flag for flag in INVINCIBILITY_FLAGS + INTANGIBILITY_FLAGS)

        data['players'][port] = {
            'character': game.start.players[port].character.name,  # Nom du personnage
            'position': (player.post.position.x, player.post.position.y),  # Position (x, y)
            'percentage': player.post.damage,  # Pourcentage de dégâts
            'state': player.post.state.name,  # État actuel
            'shield': player.post.shield,  # Force du bouclier
            'velocity': (velocity_x, velocity_y),  # Vélocité calculée (x, y)
            'invincible': is_invincible  # Combine invincibilité et intangibilité
    } #informations cruciales à l'évaluation du jeu
    # Ajouter d'autres informations si nécessaire
    
    return data