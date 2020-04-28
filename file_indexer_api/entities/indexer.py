from file_indexer_api.common.connection_handler_factory import ConnectionHandlerFactory

class Indexer:
  def __init__(self):
    self.indexer = ConnectionHandlerFactory.create_connection_handler('indexer')

  def index(self, path):
    index_status = self.indexer.get_handler(path)

    if index_status is True:
      return True

    return False
