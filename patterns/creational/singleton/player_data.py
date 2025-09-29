import threading

class PlayerDataManager:
    """Double-checked locking singleton pattern"""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        # First check (without locking)
        if cls._instance is None:
            with cls._lock:
                # Second check (with locking)
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._load_data()
                    print("DoubleCheckedSingleton instance created")
        return cls._instance
    
    def _load_data(self):
        # In a real app this might load from a DB or JSON file
        self.player_data = {
            "Mike Trout": {"home_runs": 35, "batting_average": 0.312, "RBIs": 88, "stolen_bases": 15},
            "Shohei Ohtani": {"home_runs": 44, "batting_average": 0.285, "RBIs": 95, "stolen_bases": 12},
            "Aaron Judge": {"home_runs": 62, "batting_average": 0.311, "RBIs": 131, "stolen_bases": 10},
            "Mookie Betts": {"home_runs": 29, "batting_average": 0.297, "RBIs": 87, "stolen_bases": 18},
            "Fernando Tatis Jr.": {"home_runs": 42, "batting_average": 0.282, "RBIs": 95, "stolen_bases": 25},
            "Juan Soto": {"home_runs": 31, "batting_average": 0.295, "RBIs": 90, "stolen_bases": 5},
            "Cody Bellinger": {"home_runs": 25, "batting_average": 0.278, "RBIs": 75, "stolen_bases": 7},
            "Freddie Freeman": {"home_runs": 28, "batting_average": 0.301, "RBIs": 92, "stolen_bases": 3},
            "Vladimir Guerrero Jr.": {"home_runs": 40, "batting_average": 0.309, "RBIs": 110, "stolen_bases": 2},
            "Trea Turner": {"home_runs": 21, "batting_average": 0.287, "RBIs": 68, "stolen_bases": 32},
        }
        print("Player data loaded")

    def get_player_stat(self, player_name, stat):
        return self.player_data.get(player_name, {}).get(stat, "Stat not found")