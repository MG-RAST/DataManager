import logging
import json
from pathlib import PurePath
from functools import lru_cache

from datetime import datetime
from django.core.files.storage import Storage
from filebrowser.storage import StorageMixin
from filebrowser.settings import DIRECTORY
from .shock import ShockClient

logger = logging.getLogger(__name__)

time_fmt = '%Y-%m-%dT%H:%M:%S.%fZ'

class ShockStorage(StorageMixin, ShockClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.isdir(DIRECTORY):
            self.makedirs(DIRECTORY)

    def get_named(self, name):
        r = self.query_node(f'name={name}')
        if not r:
            return None
        return r[0]

    def path(self, name):
        return name

    # public api 
    def save(self, name, content):
        self.add_to_dir(name)
        self.create_node(upload_file=content, attributes=json.dumps({'name': name}))

    def delete(self, name):
        node = self.get_named(name)
        self.delete_node(node['id'])

    def exists(self, name):
        if self.get_named(name):
            return True
        return False

    def listdir(self, path):
        r = self.query_node(f'name={path}&directory')
        if r[0]:
            contents = r[0]['attributes']['contents']
            if contents:
                return (contents['directories'], contents['files'])
        return ([], [])

    def size(self, name):
        node = self.get_named(name)
        return node['file']['size']

    def url(self, name):
        node = self.get_named(name)
        if not node:
            return ''
        node_id = node['id']
        return f'http://{self.base_url}/node/{node_id}'

    def get_accessed_time(self, name):
        raise NotImplementedError()

    def get_created_time(self, name):
        node = self.get_named(name)
        return datetime.strptime(r['created_on'], time_fmt)

    def get_modified_time(self, name):
        node = self.get_named(name)
        return datetime.strptime(r['last_modified'], time_fmt)

    def isfile(self, name):
        node = self.get_named(name)
        if not node or node['attributes'].get('directory'):
            return False
        return True

    def isdir(self, name):
        node = self.get_named(name)
        if node and node['attributes'].get('directory'):
            return True
        return False

    def move(self, old_file_name, new_file_name, allow_overwrite=False):
        if self.exists(new_file_name):
            if allow_overwrite:
                self.delete(new_file_name)
            else:
                raise "Can't do that."

        if self.exists(old_file_name):
            node = self.get_node(old_file_name)
            self.copy_node(node['id'], attributes_file=json.dumps({'name': new_file_name}))
        else:
            self.create_node(upload_file=old_file_name, attributes=json.dumps({'name': new_file_name}))

    def add_to_dir(self, path):
        directory = self.get_named(PurePath(path).parent)
        if directory:
            directory['attributes']['files'].append(PurePath(path).name)
            self.update_node(directory['id'], attributes_file=json.dumps({directory['attributes']}))

    def makedirs(self, name):
        self.add_to_dir(name)
        if not self.exists(name):
            self.create_node(attributes=json.dumps({
                'name': name,
                'directory': True,
                'contents': {
                    'directories': [],
                    'files': [],
                }
            }))

    def rmtree(self, name):
        raise NotImplementedError()

    def setpermission(self, name):
        raise NotImplementedError()
