from flask_restful import Resource, reqparse
from rpyc import connect

parser = reqparse.RequestParser()
parser.add_argument('query')

class SearchController(Resource):
  def post(self):
    args = parser.parse_args()
    connection = connect('localhost', 18861, config={"allow_all_attrs": True})
    result = connection.root.search(args['query'])

    return {'data': result}
