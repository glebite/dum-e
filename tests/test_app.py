"""
test_app.py

All tests will be in @pytest markup format.

test_status
...
test_last
"""
import pytest
import requests
import subprocess
import time 

@pytest.mark.test_id(0)
def test_start_server():
    subprocess.Popen(['./launch_server.sh'], shell=True)
    time.sleep(10)
    assert True

@pytest.mark.test_id(2)
def test_status():
    """ test_status
    Confirms that the running server will return a 200 status_code
    when a get is performed on it.
    """
    response = requests.get('http://127.0.0.1:6666/status')
    assert response.status_code == 200
    
@pytest.mark.test_id(9999)
def test_quitter():
    """
    """
    response = requests.post('http://127.0.0.1:6666/quitter')
    assert response.status_code == 200
