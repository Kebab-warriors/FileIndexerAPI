from file_indexer_api.common.connection_handler import ConnectionHandler

class SearcherHandler(ConnectionHandler):
    root = ConnectionHandler.root.searcher()
