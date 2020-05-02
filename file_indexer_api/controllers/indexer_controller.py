from flask_restful import Resource, reqparse
from rpyc import connect

parser = reqparse.RequestParser()
parser.add_argument('path')

class IndexerController(Resource):
  def post(self):
    args = parser.parse_args()
    connection = connect('localhost', 18861)
    result = connection.root.index(args['path'])

    if (result is True):
      return {'message': 'indexed path {}'.format(args['path'])}

    return {'message': 'could no index path {}'.format(args['path'])}
