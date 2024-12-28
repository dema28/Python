class Assertions:
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"

    @staticmethod
    def assert_booking_data(expected_data, actual_data):
        assert expected_data["firstname"] == actual_data["firstname"], "Firstname mismatch"
        assert expected_data["lastname"] == actual_data["lastname"], "Lastname mismatch"
        assert expected_data["totalprice"] == actual_data["totalprice"], "Total price mismatch"
        assert expected_data["depositpaid"] == actual_data["depositpaid"], "Deposit mismatch"
        assert expected_data["bookingdates"] == actual_data["bookingdates"], "Booking dates mismatch"
        assert expected_data["additionalneeds"] == actual_data["additionalneeds"], "Additional needs mismatch"
