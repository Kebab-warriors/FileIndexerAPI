from file_indexer_api.common.connection_handler import ConnectionHandler

class IndexerHandler(ConnectionHandler):
    root = ConnectionHandler.root.index()
