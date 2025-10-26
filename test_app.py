from app import app

def test_root():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200
    assert b"Halo dari Flask + Docker + Jenkins!" in r.data