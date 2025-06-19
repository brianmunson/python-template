import json
from pathlib import Path

import pytest

def load_json(path):
    with Path(f"tests/fixtures/{path}").open("r") as f:
        data = f.read()
        return json.loads(data)
    
@pytest.fixture(scope="session")
def load_json_fixture():
    def fn(path):
        return load_json(path)
    
    return fn
