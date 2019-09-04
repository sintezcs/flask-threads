from unittest.mock import Mock

import pytest

from flask import g
from flask import jsonify
from flaskthreads import AppContextThread
from flaskthreads import ThreadPoolWithAppContextExecutor

TEST_URL = '/test'
TEST_G = 'TEST'
TEST_RESULT = {'ok': True}


def test_app_context_thread(flask_app):
    """Test accessing flask.g from another thread."""
    mock_action = Mock()

    @flask_app.route(TEST_URL)
    def test_handler():
        g.test = TEST_G
        thread = AppContextThread(target=lambda: mock_action.action(g.test))
        thread.start()
        thread.join()
        return jsonify(TEST_RESULT)

    with flask_app.test_client() as client:
        result = client.get(TEST_URL)

    assert result.get_json() == TEST_RESULT
    mock_action.action.assert_called_with(TEST_G)


def test_running_without_flask_context():
    """Test running AppContextThread outside of flask app raises an error."""
    mock_action = Mock()
    with pytest.raises(RuntimeError):
        thread = AppContextThread(target=lambda: mock_action.action())
        thread.start()
        thread.join()
        mock_action.action.assert_not_called()


def test_app_context_executor(flask_app):
    """Test accessing flask.g from another thread with futures."""
    mock_action = Mock()

    @flask_app.route(TEST_URL)
    def test_handler():
        g.test = TEST_G
        with ThreadPoolWithAppContextExecutor(max_workers=2) as pool:
            future = pool.submit(lambda: mock_action.action(g.test))
            future.result()
        return jsonify(TEST_RESULT)

    with flask_app.test_client() as client:
        result = client.get(TEST_URL)

    assert result.get_json() == TEST_RESULT
    mock_action.action.assert_called_with(TEST_G)


def test_executor_running_without_flask_context():
    """Test running ThreadPoolWithAppContextExecutor without flask."""
    mock_action = Mock()
    with pytest.raises(RuntimeError):
        with ThreadPoolWithAppContextExecutor(max_workers=2) as pool:
            future = pool.submit(lambda: mock_action.action())
            future.result()
        mock_action.action.assert_not_called()
