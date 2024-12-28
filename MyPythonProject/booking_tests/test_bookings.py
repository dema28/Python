from api_requests.get_requests import get_all_bookings
from api_requests.post_requests import create_booking
from api_requests.patch_requests import update_booking
from api_requests.delete_requests import delete_booking
from assertions import Assertions


def test_get_all_bookings():
    response = get_all_bookings()
    Assertions.assert_status_code(response, 200)
    print("Test 1 passed: GET all bookings")


def test_create_and_verify_booking():
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-12-01", "checkout": "2024-12-10"},
        "additionalneeds": "Breakfast"
    }
    response = create_booking(booking_data)
    Assertions.assert_status_code(response, 200)
    booking_id = response.json().get("bookingid")

    response = get_all_bookings(booking_id)
    Assertions.assert_status_code(response, 200)
    booking_details = response.json()

    Assertions.assert_booking_data(booking_data, booking_details)
    print("Test 2 passed: Create and verify booking")


def test_update_booking():
    booking_data = {
        "firstname": "Alice",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {"checkin": "2024-12-05", "checkout": "2024-12-15"},
        "additionalneeds": "Dinner"
    }
    response = create_booking(booking_data)
    Assertions.assert_status_code(response, 200)
    booking_id = response.json().get("bookingid")

    update_data = {"firstname": "Bob", "lastname": "Brown"}
    response = update_booking(booking_id, update_data)
    Assertions.assert_status_code(response, 200)

    updated_details = response.json()
    Assertions.assert_booking_data(update_data, updated_details)
    print("Test 3 passed: Update booking")


def test_delete_booking():
    booking_data = {
        "firstname": "Jane",
        "lastname": "Doe",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-12-20", "checkout": "2024-12-25"},
        "additionalneeds": "Lunch"
    }
    response = create_booking(booking_data)
    Assertions.assert_status_code(response, 200)
    booking_id = response.json().get("bookingid")

    response = delete_booking(booking_id)
    Assertions.assert_status_code(response, 201)

    response = get_all_bookings(booking_id)
    Assertions.assert_status_code(response, 404)
    print("Test 4 passed: Delete booking")


# Запуск тестов
test_get_all_bookings()
test_create_and_verify_booking()
test_update_booking()
test_delete_booking()
