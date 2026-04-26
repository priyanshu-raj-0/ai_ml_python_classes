"""
use this command to download the uv in pc 
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"

open folder where you want to creater project folder ctrl + shift + right click > open in terminal and follow these commands
# Create new project
uv init <project-name>

# Add packages
uv add requests pandas

# remove project
uv remove pandas

# Install from existing project
uv sync

# Add development dependencies
uv add --dev pytest black

# Run Python
uv run python script.py

# Update packages
uv add --upgrade package-name

# Show installed packages
uv pip list

# Run Python scripts
uv run python script.py

# Convert requirements.txt to pyproject.toml
uv add -r requirements.txt

# Or just install from requirements.txt
uv pip install -r requirements.txt

"""

# https://python.datalumina.com/tools/dependencies/virtual-env visit this url