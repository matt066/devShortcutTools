from fastapi import FastAPI
import base64_tool
import json_tool
import jwt_tool
import uuid_tool

app = FastAPI()


@app.get("/v1/")
def home():
    return 'API Tools está no ar'


@app.get("/v1/uuid")
def return_uuid():
    return uuid_tool.get_uuid()


@app.get("/v1/json/{unformatted_json}")
def return_formatted_json(unformatted_json: str):
    return json_tool.adjust_json(unformatted_json)


@app.get("/v1/base64/encode/{content_to_encode}")
def return_encode_b64(content_to_encode: str):
    return base64_tool.encode_base64(content_to_encode)


@app.get("/v1/base64/decode/{content_to_decode}")
def return_encode_b64(content_to_decode: str):
    return base64_tool.decode_base64(content_to_decode)
