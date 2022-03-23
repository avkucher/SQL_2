from flask import Flask
import main
import json
app = Flask(__name__)


@app.route('/movie/<year1>/to/<year2>/')
def search_title_years(year1, year2):
    response = main.search_by_years(year1=year1, year2=year2)
    return app.response_class(response=json.dumps(response),
                              status=200,
                              mimetype='application/json')
#json.dumps(response)

if __name__ == "__main__":
    app.run()