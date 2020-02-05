"""
app.py - intended to be renamed later
"""
import sys
import logging
import configparser
from flask import Flask

@app.route('/status', methods=['GET'])
def status():
    pass

@app.route('/command/<command>', methods=['POST'])
def command(command=None):
    pass

@app.route('/file', methods=['POST'])
def file():
    pass

def main():
    """
    stub for now - main function to be called and drive the whole shebang
    """

if __name__ == "__main__":
    main()
