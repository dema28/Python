import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def get_all_bookings(booking_id=None):
    url = f"{BASE_URL}/booking"
    if booking_id:
        url = f"{BASE_URL}/booking/{booking_id}"
    return requests.get(url)
