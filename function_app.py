import azure.functions as func
import datetime
import json
import logging
from app.app import execute_logic

app = func.FunctionApp()


@app.route(route="BlobFunction", auth_level=func.AuthLevel.ANONYMOUS)
def BlobFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    execute_logic()

    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200,
    )
