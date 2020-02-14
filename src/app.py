"""
app.py - intended to be renamed later

A FLASK server that will run on a remote system such as a raspberry pi.
The intention is to provide files to it (transfer) and then be built and 
transferred to a connected Arduino-based board.

This arduino code will in my case be attached to a robot arm.
"""
import sys
import logging
import configparser
from flask import Flask, request, jsonify, make_response, flash, redirect, url_for
from werkzeug.utils import secure_filename

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
FH = logging.FileHandler('app.log')
FORMATTER = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
FH.setFormatter(FORMATTER)
FH.setLevel(logging.DEBUG)
LOGGER.addHandler(FH)

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    """
    status
    200 OK
    """
    LOGGER.info("status request coming in...")
    response = app.response_class(status=200)
    return response

@app.route('/command/<command_instruction>', methods=['POST'])
def command(command_instruction):
    """
    command
    status
    201 - command sent
    404 - command not found
    """
    LOGGER.info("command request coming in...")
    command_to_execute = request.json
    LOGGER.info(str(command_to_execute))
    # do cool stuff here
    return make_response(jsonify(command_to_execute), 200)

@app.route('/file', methods=['POST'])
def file():
    """
    file
    status
    201 - file processing
    404 -file not found
    """
    LOGGER.info("file request coming in...")
    if 'file' not in request.files:
        LOGGER.error("file not in request.files...")
        # something something dangerzone
        pass
    else:
        file_data = request.files['file']
        return make_response(jsonify(file_data), 200)

@app.route('/quitter', methods=["POST"])
def quitter():
    """
    quitter - shutsdown the werkzeug server
    """
    LOGGER.debug("POST /quitter")
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return make_response(jsonify(system_status="quitting", game_status=""), 200)

@app.route('/logs', methods=['GET'])
def logs():
    """
    """
    LOGGER.debug("GET /logs")
    return make_response(jsonify(something="something else"), 200)
    

def main():
    """
    stub for now - main function to be called and drive the whole shebang
    """
    LOGGER.info("Staring the application...")
    app.run(port=6666, debug=True)

    
if __name__ == "__main__":
    main()
