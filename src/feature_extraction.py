## Dans ce fichier, nous allons raffiner les informations brutes  extraites du replay file
## afin de les rendre plus exploitables pour l'entraînement de notre modèle. (feature engineering, ou ingénérie des caractéristiques)

from slippi import Game
from typing import Dict, List, Callable
from src.data_processing import get_frame_data
#features à implémenter : 
# frames_before_actionable, off_stage, stage_control, percentage, position, velocity, state, distance_between_players, shield, stock, damage

class FeatureExtractor:
    def __init__(self):
        self.feature_registry = { # Création du registre de features, qui sépare les features de base et celles raffinées
            'basic': [
                self._position_features,
                self._damage_features,
                self._state_features,
                self._shield_features,
                self._velocity_features
            ],
            'calculated': [
                self._distance_between_players,
                #self._stage_control_score
            ]
        }

    def extract_game_features(self, game: Game, frame : int, feature_groups: List[str] = ['basic']) -> Dict[str, float]: 
        """Extraction des features pour une frame donnée d'une game Slippi pour un groupe de features spécifique"""
        frame_data = get_frame_data(game, frame)
        if not frame_data:
            return {}

        features = {}
        
        # Activation des groupes de fonctionnalités demandés
        for group in feature_groups:
            if group in self.feature_registry:
                for feature_func in self.feature_registry[group]:
                    try:
                        features.update(feature_func(frame_data))
                    except Exception as e:
                        print(f"Error in {feature_func.__name__}: {e}")

        return features

    # Basic Features ######################################################
    def _position_features(self, frame_data: dict) -> Dict[str, float]:
        """
        Extrait les positions des joueurs à partir des données de la frame.
        """
        if not frame_data:
            return {}

        positions = {}
        for port, player_data in frame_data['players'].items():
            positions[f"p{port}_position_x"] = player_data['position'][0]
            positions[f"p{port}_position_y"] = player_data['position'][1]
        return positions

    def _damage_features(self, frame_data: dict) -> Dict[str, float]:
        """
        Extrait les pourcentages de dégâts actuels des joueurs.
        """
        if not frame_data:
            return {}

        return {f"p{port}_damage": player['percentage'] 
                for port, player in frame_data['players'].items()}

    def _shield_features(self, frame_data: dict) -> Dict[str, float]:
        """
        Extrait la force du bouclier pour chaque joueur.
        """
        if not frame_data:
            return {}

        return {f"p{port}_shield": player['shield'] 
                for port, player in frame_data['players'].items() if 'shield' in player}

    def _velocity_features(self, frame_data: dict) -> Dict[str, float]:
        """
        Extrait les vélocités des joueurs à partir des données de la frame.
        """
        if not frame_data:
            return {}

        velocities = {}
        for port, player_data in frame_data['players'].items():
            velocities[f"p{port}_velocity_x"] = player_data['velocity'][0]
            velocities[f"p{port}_velocity_y"] = player_data['velocity'][1]
        return velocities

    def _state_features(self, frame_data: dict) -> Dict[str, float]:
        """
        Extrait l'état (state) actuel de chaque joueur à partir des données de la frame.
        """
        if not frame_data:
            return {}

        state_features = {}
        for port, player_data in frame_data['players'].items():
            if 'state' in player_data:
                state = player_data['state']
                # Encode chaque état comme une clé binaire
                state_features[f"p{port}_state_{state}"] = 1.0
        return state_features

    # Calculated Features ##################################################
    def _distance_between_players(self, frame_data: dict) -> Dict[str, float]: #en plus de la distance euclidienne entre les deux joueurs, on va aussi extraire la distance sur les axes x et y
        from math import sqrt

        if not frame_data or len(frame_data['players']) < 2:
            return {}

        # Récupérer les positions des deux joueurs
        players = list(frame_data['players'].values())
        p1_pos = players[0]['position']
        p2_pos = players[1]['position']

        # Calcul des distances
        dx = p1_pos[0] - p2_pos[0]
        dy = p1_pos[1] - p2_pos[1]

        return {
            'distance': sqrt(dx**2 + dy**2),
            'distance_x': dx,
            'distance_y': dy
        }
    


def extract_game_features(game: Game, frame: int, **kwargs) -> Dict[str, float]: #Fonction de simplification  d'acces à  l'extracteur de features
    """Fonction d'extraction de features pour une frame donnée d'une game Slippi"""
    return FeatureExtractor().extract_game_features(game, frame, **kwargs)