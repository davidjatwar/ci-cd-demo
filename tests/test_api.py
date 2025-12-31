"""API tests using requests library"""
import requests
import pytest

class TestJSONPlaceholderAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def test_get_posts(self):
        """Test getting all posts"""
        response = requests.get(f"{self.BASE_URL}/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert isinstance(response.json(), list)
    
    def test_get_single_post(self):
        """Test getting a single post"""
        response = requests.get(f"{self.BASE_URL}/posts/1")
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == 1
        assert 'title' in data
        assert 'body' in data
    
    def test_create_post(self):
        """Test creating a new post"""
        payload = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == payload['title']
        assert data['body'] == payload['body']
    
    def test_invalid_endpoint(self):
        """Test handling of invalid endpoint"""
        response = requests.get(f"{self.BASE_URL}/invalid")
        assert response.status_code == 404