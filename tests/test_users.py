import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


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
    def test_post_request_with_proper_body_returns_201(self):
        response = client.post(
            "/user/register",
            json={"username": "santosh", "password": "sntsh", "fullname": "Santosh Kumar"}
        )
        assert response.status_code == 201

    """
    R4: The API consumer hits /users/register with a POST method With malformed body
.
    """
    def test_post_request_with_improper_body_returns_422(self):
        """all of username, password and fullname is required"""
        response = client.post(
            "/user/register",
            json={"username": "santosh"}
        )
        assert response.status_code == 422
