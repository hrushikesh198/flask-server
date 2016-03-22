from collections import OrderedDict
import logging
from os.path import abspath, dirname
import sys
from urllib import urlencode
from urlparse import urlparse

from flask import Flask, request, abort, json
from flask_request_id import RequestID
import requests
from lxml import etree

app = Flask(__name__)
app.debug = False
fl_req_id = RequestID(app)

@app.route("/")
def hello():
    return """
    Solve some captchas <br>
    <ol>
        <li><a href ='/amz_get_cap' >amazon</a></li>
    </ol>
    """
    
if __name__ == "__main__":
    app.run()
