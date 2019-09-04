import pytest
from flask import Flask


@pytest.fixture
def flask_app():
    app = Flask('test')
    return app
