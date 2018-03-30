# Atlassian Version Checker

## Installation
1. Start by installing the Python dependencies:
```bash
pip install -r requirements.txt
```
2. Open `main.py` in a text editor (like vim or nano if on Linux) and edit the server URLs and Confluence credentials.

**Note:** The Confluence user must have sysadmin privileges. The URL containing the Confluence version info isn't available to non-sysadmin users.

## Usage
```bash
python main.py
```
