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

    """
    R3: The API consumer hits /users/register with a POST method With body
    Should check in database if the user exists, if so: Throws error that user exists
    If user not found, returns a 201 response with passed username.
    """
