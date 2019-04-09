import logging
from functools import partialmethod
from io import StringIO
from os import path

from requests.api import request
from requests.exceptions import HTTPError
from requests.utils import requote_uri

from requests_toolbelt import MultipartEncoder

logger = logging.getLogger(__name__)

def send(method, url, headers={}, decode=True, auth=None, fields={}, **kwargs):
    '''
        Convienence function for making Shock requests.
        
        Required:
            method      HTTP method string. See requests library for 
                        details. Common values 'GET' 'PUT' 'POST' 
                        'DELETE' 'OPTIONS'.
            url         Full url to Shock server.

        Optional:
            headers     Key value diction of HTTP headers.
            decode      Set to false to get response object 
                        rather than decode json.
            auth        Value of HTTP 'Authorization' header.
            fields      Dictionary containing fields to be multipart
                        form encoded. 
            **kwargs    Addition options that will be passed through
                        to request library requests.api.request. 
    '''
    # set headers and initialize kwargs
    if not kwargs:
        kwargs = {'headers': headers}
    elif not kwargs.get('headers'):
        kwargs['headers'] = headers

    # encode data and set content-type
    if fields:
        if method not in ['POST', 'PUT']:
            raise ValueError('Invalid http method used with multipart form.')
        d = MultipartEncoder(fields=fields)
        kwargs.update({'data': d, 'allow_redirects': True})
        kwargs['headers']['Content-Type'] = d.content_type
        print(d)

    # set auth header
    if auth:
        kwargs['headers']['Authorization'] = auth

    # send it
    try:
        r = request(method, url, **kwargs)
        if not (r.ok and r.text):
            r.raise_for_status()
        if not decode:
            return r
        body = r.json()
    except ConnectionError:
        logger.exception('Unable to connect to Shock server.')
    except (HTTPError, ValueError):
        logger.exception('Invalid response from Shock server.')
    else:
        return body['data']

def get_filehandle(d, name='unknown'):
    if type(d) is type(''):
        if path.exists(d):
            if name is 'unknown':
                name = path.basename(d)
            # file path
            return (name, open(d))
        else:
            # file content
            return (name, StringIO(d))
    # file handle
    return (name, d)


class ShockClient(object):
    def __init__(self, url='http://shock.mg-rast.org', bearer='OAuth', token=None):
        self.base_url = url
        self.auth = None
        if token:
            self.auth = '{} {}'.format(bearer, token)

    def get_acl(self, node, acl=None, user=None, public=False):
        return self.manage_acl('GET', node, acl, user, public)

    def add_acl(self, node, acl=None, user=None, public=False):
        return self.manage_acl('PUT', node, acl, user, public)

    def delete_acl(self, node, acl=None, user=None, public=False):
        return self.manage_acl('DELETE', node, acl, user, public)

    def manage_acl(self, method, node, acl, user, public):
        url = f'{self.base_url}/node/{node}/acl'
        if acl and user:
            url = f'{url}{acl}?users={requote_uri(user)}'
        elif acl and public:
            url = f'{url}/public_{acl}'
        return send(method, url, auth=self.auth)

    def get_node(self, node):
        return send('GET', f'{self.base_url}/node/{node}', auth=self.auth)

    def query_node(self, query):
        return send('GET', f'{self.base_url}/node/?query&{requote_uri(query)}', auth=self.auth)

    def delete_node(self, node):
        return send('DELETE', f'{self.base_url}/node/{node}', auth=self.auth)

    def copy_node(self, node, attributes_file=None, copy_index=True):
        fields = {'copy_data': node}
        if attributes_file:
            fields['attributes'] = get_filehandle(attributes_file)
        if copy_index:
            fields['copy_indexes'] = 'true'
        return send('POST', f'{self.base_url}/node/{node}', fields=fields, auth=self.auth)

    def create_node(self, upload_file=None, attributes=None):
        fields = {}
        if upload_file:
            fields['upload'] = get_filehandle(upload_file)
        if attributes:
            fields['attributes'] = ('attributes.json', StringIO(attributes))
        return send('POST', f'{self.base_url}/node', fields=fields, auth=self.auth)
    
    def update_node(self, node, upload_file=None, attributes_file=None, expiration=None, remove_expiration=False):
        fields = {}
        if upload_file:
            fields['upload'] = get_filehandle(upload_file)
        if attributes_file:
            fields['attributes'] = get_filehandle(attributes_file)
        if not expiration and remove_expiration:
            fields['remove_expiration'] = 'true'
        if expiration and not remove_expiration:
            fields['expiration'] = expiration
        return send('PUT', f'{self.base_url}/node/{node}', fields=fields, auth=self.auth)

    def download_node(self, node, path=None, index=None, part=None, chunk=None, binary=False):
        options = ''
        if index and part:
            options = f'&index={requote_uri(index)}&part={part}'
        elif index and part and chunk:
            options = f'&index={requote_uri(index)}&part={part}&chunk_size={chunk}'
        url = f'{self.base_url}/node/{node}?download{options}'
        if not path:
            response = send('GET', url, decode=False, auth=self.auth)
            if binary:
                return response.content
            else:
                return response.text
        else:
            response = send('GET', url, decode=False, auth=self.auth, stream=True)
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192): 
                    if chunk:
                        f.write(chunk)
                        f.flush()
        return path
