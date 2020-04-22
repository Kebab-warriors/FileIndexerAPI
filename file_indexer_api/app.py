from flask import Flask
from flask_restful import Api
from controllers.indexer_controller import IndexerController
from controllers.search_controller import SearchController

app = Flask(__name__)
api = Api(app)

api.add_resource(IndexerController, '/index')
api.add_resource(SearchController, '/search')

