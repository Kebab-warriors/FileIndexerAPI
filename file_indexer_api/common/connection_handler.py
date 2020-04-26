from rpyc import connect

class ConnectionHandler(object):
  connection = connect('localhost', 18861)
  root = None

  def get_handler(self):
    return self.root
