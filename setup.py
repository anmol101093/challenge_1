from pathlib import Path
from setuptools import setup, find_packages
 
# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]
 
setup(
    name="challenge1_app",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[required_packages],
)