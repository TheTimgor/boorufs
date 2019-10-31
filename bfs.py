from fs.base import FS
from fs.errors import ResourceReadOnly, ResourceNotFound
from io import StringIO


class BFS(FS):
    def __init__(self):
        self.files = {
            'hello': 'hello world!',
            'hewwo': 'hewwo wowd!'
        }
        super(BFS, self).__init__()

    def getinfo(self, path, namespaces=None):
        if path == '/':
            return {
                'basic': {
                    'name': '/',
                    'is_dir': True
                }
            }
        else:
            return {
                'basic':{
                    'name': path.split('/')[-1],
                    'is_dir': False
                }
            }

    def listdir(self, path):
        if path == '/':
            return self.files.keys()
        else:
            raise ResourceNotFound('Resource does not exist')

    def makedir(self, path, permissions=None, recreate=False):
        raise ResourceReadOnly

    def openbin(self, path, mode="r", buffering=-1, **options):
        return StringIO(self.files['path'])

    def remove(self, path):
        raise ResourceReadOnly

    def removedir(self, path):
        raise ResourceReadOnly

    def setinfo(self, path, info):
        raise ResourceReadOnly
