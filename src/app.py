"""
app.py - intended to be renamed later
"""
import sys
import logging
import configparser
from flask import Flask, request, jsonify

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
    return jsonify(command_to_execute)

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
        return jsonify(file_data)

@app.route('/quitter', methods=["POST"])
def quitter():
    """
    quitter - shutsdown the werkzeug server
    """
    LOGGER.debug("POST /quitter")
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return jsonify(system_status="quitting", game_status="")

@app.route('/logs', methods=['GET'])
def logs():
    """
    """
    LOGGER.debug("GET /logs")
    

def main():
    """
    stub for now - main function to be called and drive the whole shebang
    """
    LOGGER.info("Staring the application...")
    app.run(port=6666, debug=True)

    
if __name__ == "__main__":
    main()
