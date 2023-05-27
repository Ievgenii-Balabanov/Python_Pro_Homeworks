from django.test import TestCase
import pytest


@pytest.mark.urls()
def test_index_redirects_to_football_player(client):
    response = client.get('/')
    assert response.status_code == 302

