import os

def test_app_file_exists():
    assert os.path.exists("app.py"), "Файл app.py не найден!"