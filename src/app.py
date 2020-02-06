"""
app.py - intended to be renamed later
"""
import sys
import logging
import configparser
from flask import Flask

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
FH = logging.FileHandler('conversion.log')
FORMATTER = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
FH.setFormatter(FORMATTER)
FH.setLevel(logging.DEBUG)
LOGGER.addHandler(FH)

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    LOGGER.info("status request coming in...")
    response = app.response_class(status=200)
    return response

@app.route('/command/<command>', methods=['POST'])
def command():
    LOGGER.info("command request coming in...")
    command_to_execute = request.form.get('command')
    # do cool stuff here

@app.route('/file', methods=['POST'])
def file():
    LOGGER.info("file request coming in...")
    if 'file' not in request.files:
        LOGGER.error(f"{file} not in request.files...")
        # something something dangerzone
        pass
    else:
        file_data = request.files['file']
        # secure save

def main():
    """
    stub for now - main function to be called and drive the whole shebang
    """
    LOGGER.info("Staring the application...")
    app.run(port=6666, debug=True)

if __name__ == "__main__":
    main()
