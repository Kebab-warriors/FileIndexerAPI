from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('path')

class IndexerController(Resource):
  def post(self):
    args = parser.parse_args()

    return {'path': args['path']}
