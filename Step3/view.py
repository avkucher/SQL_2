from flask import Flask
import main
import json
app = Flask(__name__)


@app.route('/rating/<rating>/')
def search_by_rating(rating):
    response = main.search_by_rating(rating=rating)
    return app.response_class(response=json.dumps(response),
                              status=200,
                              mimetype='application/json')
#json.dumps(response)

if __name__ == "__main__":
    app.run()