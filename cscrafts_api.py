from flask import Flask, request
import json_helpers

app = Flask(__name__)

stickersData = json_helpers.readJsonData("stickers_data.json")["data"]
weaponsData = json_helpers.readJsonData("weapons_data.json")["data"]

collection = "Paris 2023 Teams"


@app.route("/api/sticker-collections", methods=["GET"])
def get_sticker_collections():
    collections = {"data": list(stickersData.keys())}
    print(collections)
    return collections


@app.route("/api/stickers", methods=["GET"])
def get_stickers():
    collection = request.args.get("collection")
    response = {"data": stickersData[collection]}
    return response


if __name__ == "__main__":
    app.run()
