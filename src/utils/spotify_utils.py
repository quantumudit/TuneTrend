"""summary"""

import base64
import json
from datetime import datetime, timedelta

import httpx


def get_spotify_token(client_id: str, client_secret: str) -> str:
    """_summary_

    Args:
        client_id (str): _description_
        client_secret (str): _description_

    Returns:
        str: _description_
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    response = httpx.post(url, headers=headers, data=data)
    json_results = json.loads(response.content)
    access_token = json_results["access_token"]
    return access_token


def get_spotify_auth_headers(access_token: str) -> dict:
    """_summary_

    Args:
        token (str): _description_

    Returns:
        dict: _description_
    """
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }


def yesterday_spotify_timestamp() -> int:
    """_summary_

    Returns:
        int: _description_
    """
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterday_ts = yesterday.timestamp()
    yesterday_spotify_ts = int(yesterday_ts) * 1000
    return yesterday_spotify_ts
