from file_indexer_api.common.connection_handler_factory import ConnectionHandlerFactory

class Searcher():
    def __init__(self):
        self.searcher = ConnectionHandlerFactory.create_connection_handler('indexer')

    def search(self, query): 
        self.searcher.get_handler(query)
