from flask import Flask
import main
import json
app = Flask(__name__)


@app.route('/genre/<listed_in>')
def search_by_10_genre(listed_in):
    response = main.search_by_genre(listed_in=listed_in)
    return app.response_class(response=json.dumps(response),
                              status=200,
                              mimetype='application/json')

        #json.dumps(response)




if __name__ == "__main__":
    app.run()