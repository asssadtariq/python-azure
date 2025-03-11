import azure.functions as func
import datetime
import json
import logging
from app.app import execute_logic

app = func.FunctionApp()


@app.route(route="TestFunction", auth_level=func.AuthLevel.ANONYMOUS)
def TestFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    params = req.params

    if params['mode'] == str(1):
        return func.HttpResponse(
            "pass",
            status_code=200,
        )

    return func.HttpResponse(
        "fail",
        status_code=200,
    )


@app.route(route="BlobFunction", auth_level=func.AuthLevel.ANONYMOUS)
def BlobFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    execute_logic()

    return func.HttpResponse(
        "pass",
        status_code=200,
    )
