from fs.opener import Opener
from fs.opener.errors import OpenerError
from bfs import BFS


class BFSOpener(Opener):
    protocols = ['booru']

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        if writeable:
            raise OpenerError('BFS must be readonly!')
        return BFS()
