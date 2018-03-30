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

Confluence:

Locally installed version: 6.7.2
Latest available version: 6.8.0
Release notes: http://confluence.atlassian.com/display/DOC/Confluence+6.8+Release+Notes


Bamboo:

Locally installed version: 6.4.0
Latest available version: 6.4.1
Release notes: https://confluence.atlassian.com/display/BAMBOO/Bamboo+6.4+Release+Notes


Bitbucket:

Locally installed version: 5.8.1
Latest available version: 5.9.0
Release notes: http://confluence.atlassian.com/display/BitbucketServer/Bitbucket+Server+5.9+release+notes
```
