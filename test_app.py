import subprocess

def test_app():
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    assert "Hello CI/CD World!" in result.stdout