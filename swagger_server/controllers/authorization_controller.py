import os

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

TOKEN_DB = {
    os.getenv('SECRET'): {
        'uid': '100'
    }
}

def check_api_key_auth(api_key, required_scopes):
    info = TOKEN_DB.get(api_key)
    if not info:
        return None
    else:
        return info
