from pathlib import Path

class Paths:
    """ data class to initialize path variables"""
    root: Path= Path(__file__).parent
    image: Path=root /"data"/"mapping"/"images.csv"
    annotations: Path=root /"data"/"mapping"/"annotations.csv"