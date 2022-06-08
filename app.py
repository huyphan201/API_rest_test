from flask import Flask, jsonify
import utils

app = Flask(__name__)

# API 1: Get news
@app.route('/urlnews', methods=['GET'])         # @ : Được sử dụng để xác định tuyến API
def get_urlnews():
    rows = utils.get_all("SELECT * FROM urlnews")
    data = []
    for r in rows:
        #get all table news
        data.append({
            "id": r[0],
            "name": r[1],
            "urlsnews": r[2]
        })

    return jsonify({"categories": data})


@app.route('/news', methods=['GET'])         # @ : Được sử dụng để xác định tuyến API
def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        #get all table news
        data.append({
            "title": r[0],
            "time": r[1],
            "description": r[2],
            "image": r[3],
            "content": r[4],
            "author": r[5],
            "tags": r[6],
            "dom": r[7],
            "domn_names": r[8],
            "domn_url": r[9]
        })

    return jsonify({"news": data})

# API 2: Get news id
@app.route('/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    pass

# API 3: ADD news, khi them or edit, thuong dung POST 
@app.route("/news/add", methods=['POST'])
def insert_news():
    pass


if __name__=="__main__":
    app.run()


