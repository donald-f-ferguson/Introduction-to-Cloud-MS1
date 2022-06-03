import json

# DFF TODO -- Use logging framework and patterns

from datetime import datetime

# DFF TODO -- Explain CORS in a later lecture.
# from flask_cors import CORS

#
# These packages provide functions for deliverying a web application using Flask.
# Students can look online for education resources.
#
from flask import Flask, Response, request
from flask_cors import CORS

# DFF TODO At some point, explain the service factory pattern
from src.service_factory import ServiceFactory

# Create the Flask application object.
app = Flask(__name__)
CORS(app)

service_factory = ServiceFactory()


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "Introduction-to-Cloud-MS1",
        "health": "Good",
        "when": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/api/students/<id>", methods=["GET"])
def get_student_by_id(id):

    svc = service_factory.get_service("students")

    result = svc.get_by_id(id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


