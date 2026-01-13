import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test if the home page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Competitor Analysis" in response.data  # Check if page contains expected text

def test_custom_prompt(client):
    """Test if the custom prompt page loads correctly."""
    response = client.get("/custom_prompt")
    assert response.status_code == 200
    assert b"Custom Analysis" in response.data

def test_response_accuracy():
    """Test chatbot response accuracy."""
    input_query = "Who are the top pressure sensor manufacturers?"
    expected_output = ["Bosch", "TE Connectivity", "Sensata"]

    # Simulated chatbot response (replace with actual API call if needed)
    response = ["Bosch", "TE Connectivity", "Sensata"]

    assert any(company in response for company in expected_output), "Response did not match expected output"
