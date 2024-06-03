from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)

def test_whether_similarity_of_exact_same_strings_is_one():
    response = client.post("/findSimilarity",json={"sent1": "good","sent2": "good"})
    assert response.status_code == 200
    assert response.json()["similarity_score"] == 1.0

def test_whether_similarity_with_blank_is_zero():
    response = client.post("/findSimilarity",json={"sent1": "good","sent2": ""})
    assert response.status_code == 200
    assert response.json()["similarity_score"] < 0.01

def test_whether_similarity_with_special_character_is_zero():
    response = client.post("/findSimilarity",json={"sent1": "good","sent2": "#"})
    assert response.status_code == 200
    assert response.json()["similarity_score"] < 0.01

def test_whether_similarity_of_opposites_not_high():
    response = client.post("/findSimilarity",json={"sent1": "good","sent2": "bad"})
    assert response.status_code == 200
    assert response.json()["similarity_score"] <= 0.5

def test_whether_similarity_of_verbose_and_succint_sentences_is_high():
    response = client.post("/findSimilarity",json={"sent1": "That's an excellent way of putting it","sent2": "well said"})
    assert response.status_code == 200
    assert response.json()["similarity_score"] >= 0.5