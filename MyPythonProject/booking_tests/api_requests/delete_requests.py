import requests

BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}


def delete_booking(booking_id):
    auth_data = {"username": "admin", "password": "password123"}
    auth_response = requests.post(f"{BASE_URL}/auth", json=auth_data, headers=HEADERS)
    token = auth_response.json().get("token")
    auth_headers = {**HEADERS, "Cookie": f"token={token}"}

    return requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=auth_headers)
