import os

def test_app_file_exists():
    assert os.path.exists("app111.py"), "Файл app.py не найден!"