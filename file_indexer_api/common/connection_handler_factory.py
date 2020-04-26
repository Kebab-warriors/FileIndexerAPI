from file_indexer_api.common.connection_handler import ConnectionHandler
from file_indexer_api.common.indexer_handler import IndexerHandler
from file_indexer_api.common.searcher_handler import SearcherHandler

class ConnectionHandlerFactory():
  @staticmethod
  def create_connection_handler(type):
    if type == 'indexer':
      return IndexerHandler

    if type == 'searcher':
      return SearcherHandler
