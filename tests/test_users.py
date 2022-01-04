from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def mock_response(endpoint, json):
    received_fields = json.keys()
    completed_fields = ["username", "password", "fullname"]
    is_valid_body = all(complete_field in received_fields for complete_field in completed_fields)

    if endpoint == "/user/register":
        if not is_valid_body:
            return {"status_code": 422}
        return {"status_code": 201}


class TestUserRegistration:
    """Tests for /user/register"""

    """
    R1: The consumer hits /user/register with GET method should get Method Not Allowed.
    """
    def test_get_request_returns_405(self):
        response = client.get("/user/register")
        assert response.status_code == 405

    """
    R2: The API consumer hits /users/register with a POST method without body
    Should get error about required body parameters.
    """
    def test_post_request_without_body_returns_422(self):
        response = client.post("/user/register")
        assert response.status_code == 422

    """
    R3: The API consumer hits /users/register with a POST method With body
    Should check in database if the user exists, if so: Throws error that user exists
    If user not found, returns a 201 response with passed username.
    """
    @patch("fastapi.testclient.TestClient.post", side_effect=mock_response)
    def test_post_request_with_proper_body_returns_201(self, post):
        response = post(
            "/user/register",
            json={"username": "whatever", "password": "abc_123", "fullname": "JC somebody"}
        )
        assert response["status_code"] == 201

    """
    R4: The API consumer hits /users/register with a POST method With malformed body
.
    """
    @patch("fastapi.testclient.TestClient.post", side_effect=mock_response)
    def test_post_request_with_improper_body_returns_422(self, post):
        """all of username, password and fullname is required"""
        response = post(
            "/user/register",
            json={"username": "rojoyin"}
        )
        assert response["status_code"] == 422
