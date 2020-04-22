from flask import Flask
from flask_restful import Api
from file_indexer_api.controllers.indexer_controller import IndexerController
from file_indexer_api.controllers.search_controller import SearchController

app = Flask(__name__)
api = Api(app)

api.add_resource(IndexerController, '/index')
api.add_resource(SearchController, '/search')

