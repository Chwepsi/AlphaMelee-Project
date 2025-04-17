from enum import Enum
from typing import Dict, Tuple, List

class Stage(Enum):
    """Représentation normalisée des stages avec données géométriques"""
    YOSHIS_STORY = "Yoshi's Story"
    FINAL_DESTINATION = "Final Destination"
    FOUNTAIN_OF_DREAMS = "Fountain of Dreams"
    DREAM_LAND = "Dream Land 64"
    BATTLEFIELD = "Battlefield"
    POKEMON_STADIUM = "Pokemon Stadium"

    #on encapsule les données pour simplifier l'accès
    @property 
    def blast_zones(self) -> Tuple[float, float, float, float]:
        return _STAGE_DATA[self.value]["blast_zones"] # (left, right, top, bottom)
    
    @property
    def platforms(self) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        return _STAGE_DATA[self.value]["platforms"]

# Données techniques séparées
_STAGE_DATA = {
    "Yoshi's Story": {
        "blast_zones": (-175.70, 173.60, 168.00, -91.00),  # Dead0N et Dead1N
        "stage_floor": [
            (-54.6000, -47.2450), (-52.6750, -45.3200), (-52.6750, -30.8000),
            (-53.7250, -29.7500), (-53.7250, -28.0000), (-52.6750, -26.9500),
            (-52.6750, -12.2500), (-56.0000, -6.6500), (-56.0000, -3.5000),
            (-39.2000, 0.0000), (39.2000, 0.0000), (56.0000, -3.5000),
            (56.0000, -6.6500), (52.6750, -12.2500), (52.6750, -26.9500),
            (53.7250, -28.0000), (53.7250, -29.7500), (52.6750, -30.8000),
            (52.6750, -45.3200), (54.6000, -47.2450)
        ],
        "platforms": [
            ((-15.75, 42.00), (15.75, 42.00)),  # Top platform
            ((-59.50, 23.45), (-28.00, 23.45)),  # Left platform
            ((28.00, 23.45), (59.50, 23.45))  # Right platform
        ]
    },
    "Final Destination": {
        "blast_zones": (-246.00, 246.00, 188.00, -140.00),  # Dead0N et Dead1N
        "stage_floor": [
            (-47.4702, -55.3870), (-53.7742, -54.2572), (-61.4170, -47.3683),
            (-65.8426, -31.3573), (-65.7957, -20.4538), (-85.5606, -10.5094),
            (-85.5606, 0.0000), (85.5606, 0.0000), (85.5606, -10.5094),
            (65.7957, -20.4538), (65.8426, -31.3573), (61.4170, -47.3683),
            (53.7742, -54.2572), (47.4702, -55.3870)
        ],
        "platforms": []  # Pas de plateformes
    },
    "Fountain of Dreams": {
        "blast_zones": (-198.75, 198.75, 202.50, -146.25),  # Dead0N et Dead1N
        "stage_floor": [
            (-8.6809, -71.8312), (-18.9105, -48.6670), (-41.1778, -41.9127),
            (-56.8736, -19.5537), (-63.2570, -4.3985), (-63.3500, 0.6214),
            (-53.5835, 0.6214), (-51.2608, 0.0000), (51.2608, 0.0000),
            (53.5835, 0.6214), (63.3500, 0.6214), (63.2570, -4.3985),
            (56.8736, -19.5537), (41.1778, -41.9127), (18.9105, -48.6670),
            (8.6809, -71.8312)
        ],
        "platforms": [
            ((-14.25, 42.75), (14.25, 42.75)),  # Top platform
            ((-49.50, 27.375), (-21.00, 27.375)),  # Left highest
            ((-49.50, 16.125), (-21.00, 16.125)),  # Left start
            ((-49.50, 12.375), (-21.00, 12.375)),  # Left lowest
            ((21.00, 27.375), (49.50, 27.375)),  # Right highest
            ((21.00, 22.125), (49.50, 22.125)),  # Right start
            ((21.00, 12.375), (49.50, 12.375))  # Right lowest
        ]
    },
    "Dream Land 64": {
        "blast_zones": (-255.00, 255.00, 250.00, -123.00),  # Dead0N et Dead1N
        "stage_floor": [
            (-65.7610, -35.7543), (-76.3364, -11.0418), (-77.2700, 0.0100),
            (77.2700, 0.0100), (76.3364, -11.0418), (65.7610, -35.7543)
        ],
        "platforms": [
            ((-19.0188, 51.4264), (19.0188, 51.4264)),  # Top platform
            ((-61.3896, 30.1422), (-31.7215, 30.1422)),  # Left platform
            ((31.7051, 30.2425), (63.0764, 30.2425))  # Right platform
        ]
    },
    "Battlefield": {
        "blast_zones": (-224.00, 224.00, 200.00, -108.80),  # Dead0N et Dead1N
        "stage_floor": [
            (-68.4000, 0.0000), (68.4000, 0.0000)
        ],
        "platforms": [
            ((-18.80, 54.40), (18.80, 54.40)),  # Top platform
            ((-57.60, 27.20), (-20.00, 27.20)),  # Left platform
            ((20.00, 27.20), (57.60, 27.20))  # Right platform
        ]
    },
    "Pokemon Stadium": {
        "blast_zones": (-240.00, 240.00, 180.00, -111.00),  # Dead0N et Dead1N
        "stage_floor": [
            (-105.00, 00.00), (-90.00, 00.00), (-75.00, 00.00), (-60.00, 00.00),
            (-45.00, 00.00), (-30.00, 00.00), (-15.00, 00.00), (0.00, 00.00),
            (15.00, 00.00), (30.00, 00.00), (45.00, 00.00), (60.00, 00.00),
            (75.00, 00.00), (90.00, 00.00), (105.00, 00.00)
        ],
        "platforms": [
            ((-67, 35), (-29.00, 35)),  # Left platform
            ((29.00, 35), (67, 35))  # Right platform
        ]
    }
}

# Accès pratique
def get_stage_dimensions(stage_name: str) -> Dict:
    """Helper pour compatibilité ascendante"""
    try:
        stage = Stage(stage_name)
        return {
            'blast_zones': stage.blast_zones,
            'platforms': stage.platforms
        }
    except ValueError:
        return {}

