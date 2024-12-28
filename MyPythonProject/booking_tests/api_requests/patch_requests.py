import requests

BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}


def update_booking(booking_id, update_data):
    auth_data = {"username": "admin", "password": "password123"}
    auth_response = requests.post(f"{BASE_URL}/auth", json=auth_data, headers=HEADERS)
    token = auth_response.json().get("token")
    auth_headers = {**HEADERS, "Cookie": f"token={token}"}

    return requests.patch(f"{BASE_URL}/booking/{booking_id}", json=update_data, headers=auth_headers)
