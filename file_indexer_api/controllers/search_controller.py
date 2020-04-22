from flask_restful import Resource, reqparse

class SearchController(Resource):
    def get(self):
        return {'message': 'SearchController'}
