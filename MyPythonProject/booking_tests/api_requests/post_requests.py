import requests

BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}

def create_booking(booking_data):
    return requests.post(f"{BASE_URL}/booking", json=booking_data, headers=HEADERS)
