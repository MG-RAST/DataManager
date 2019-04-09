from unittest.mock import patch, ANY, Mock

from .shock import send, get_filehandle, ShockClient

shock_url = 'fake_shock_url'
test_dict = {'foo': 'bar', 'baz': 'bot'}
auth_token = 'OAuth 9dd8fc232028397e965cf4e1b52c0c0d'
shockobj = ShockClient(shock_url, token='9dd8fc232028397e965cf4e1b52c0c0d')
node_id = 'some-node-id'
acl = ':some-acl'
user = 'some-user'
query = 'foo=bar&baz=bot'

@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_shock_basic_case(r, encoder):
    send('GET', shock_url)
    r.assert_called_with('GET', shock_url, headers={})
    encoder.assert_not_called()

@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_send_args(r, encoder):
    kwargs = {'headers': test_dict, 'decode': False, 'auth': auth_token, 'addional_kwarg': True}
    send('GET', shock_url, **kwargs)

    kwargs['headers']['Authorization'] = auth_token
    kwargs.pop('auth')
    kwargs.pop('decode')

    r.assert_called_with('GET', shock_url, **kwargs)
    encoder.assert_not_called()

@patch('seqcenter.shock.logger')
@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_send_connection_exception_logging(r, encoder, logger):
    r.side_effect = ConnectionError()
    send('GET', shock_url)
    assert r.called
    assert logger.exception.called
    assert not encoder.called

@patch('seqcenter.shock.logger')
@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_send_value_exception_logging(r, encoder, logger):
    r.side_effect = ValueError()
    send('GET', shock_url)
    assert r.called
    assert logger.exception.called
    assert not encoder.called

@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_send_multipart_get(r, encoder):
    raised_exception = False
    try:
        send('GET', shock_url, fields=test_dict)
    except ValueError as e:
        assert e.args[0] == 'Invalid http method used with multipart form.'
        raised_exception = True
    assert not r.called
    assert raised_exception

@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_send_multipart(r, encoder):
    send('POST', shock_url, fields=test_dict)
    assert encoder.called
    r.assert_called_with(
        'POST', shock_url, headers={'Content-Type': ANY},
        data=ANY,allow_redirects=True
    )

@patch('seqcenter.shock.MultipartEncoder')
@patch('seqcenter.shock.request')
def test_send_multipart_auth(r, encoder):
    send('POST', shock_url, fields=test_dict, auth=auth_token)
    assert encoder.called
    r.assert_called_with(
        'POST', shock_url, headers={'Content-Type': ANY, 'Authorization': auth_token},
        data=ANY, allow_redirects=True
    )

@patch('seqcenter.shock.StringIO')
@patch('seqcenter.shock.open')
@patch('seqcenter.shock.path')
def test_get_filehandle_path(path, open_patch, stringio):
    d = '/some/path'
    path.exists.return_value = True
    path.basename.return_value = 'filename'

    get_filehandle(d)
    path.exists.assert_called_with(d)
    path.basename.assert_called_with(d)
    open_patch.assert_called_with(d)
    assert not stringio.called

@patch('seqcenter.shock.StringIO')
@patch('seqcenter.shock.open')
@patch('seqcenter.shock.path')
def test_get_filehandle_stringio(path, open_patch, stringio):
    d = 'some-string-data'
    stringio.return_value = 'stringio'
    path.exists.return_value = False

    results = get_filehandle(d)
    path.exists.assert_called_with(d)
    assert not path.basename.called
    assert not open_patch.called
    stringio.assert_called_with(d)
    assert results == ('unknown', 'stringio')

@patch('seqcenter.shock.StringIO')
@patch('seqcenter.shock.open')
@patch('seqcenter.shock.path')
def test_get_filehandle_handle(path, open_patch, stringio):
    d = object()

    results = get_filehandle(d, name='some-name')
    assert not path.exists.called
    assert not path.basename.called
    assert not open_patch.called
    assert not stringio.called
    assert results == ('some-name', d)

@patch('seqcenter.shock.send')
def test_ShockClient_get_acl(send_patch):
    shockobj.get_acl(node_id)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/{node_id}/acl', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_add_acl(send_patch):
    shockobj.add_acl(node_id)
    send_patch.assert_called_with(
        'PUT', f'{shock_url}/node/{node_id}/acl', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_add_acl_user(send_patch):
    shockobj.add_acl(node_id, acl=acl, user=user)
    send_patch.assert_called_with(
        'PUT', f'{shock_url}/node/{node_id}/acl{acl}?users={user}', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_add_acl_public(send_patch):
    shockobj.add_acl(node_id, acl=acl, public=True)
    send_patch.assert_called_with(
        'PUT', f'{shock_url}/node/{node_id}/acl/public_{acl}', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_delete_acl(send_patch):
    shockobj.delete_acl(node_id)
    send_patch.assert_called_with(
        'DELETE', f'{shock_url}/node/{node_id}/acl', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_delete_acl_public(send_patch):
    shockobj.delete_acl(node_id, acl, public=True)
    send_patch.assert_called_with(
        'DELETE', f'{shock_url}/node/{node_id}/acl/public_{acl}', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_get_node(send_patch):
    shockobj.get_node(node_id)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/{node_id}', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_query_node(send_patch):
    shockobj.query_node(query)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/?query&{query}', auth=auth_token
    )

@patch('seqcenter.shock.send')
def test_ShockClient_delete_node(send_patch):
    shockobj.delete_node(node_id)
    send_patch.assert_called_with(
        'DELETE', f'{shock_url}/node/{node_id}', auth=auth_token
    )

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_copy_node(send_patch, get_filehandle):
    shockobj.copy_node(node_id)
    send_patch.assert_called_with(
        'POST', f'{shock_url}/node/{node_id}', fields={'copy_data': node_id, 'copy_indexes': 'true'}, auth=auth_token
    )
    assert not get_filehandle.called

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_copy_node_attributes(send_patch, get_filehandle):
    fh = object()
    get_filehandle.return_value = fh
    shockobj.copy_node(node_id, attributes_file='path')
    send_patch.assert_called_with(
        'POST', f'{shock_url}/node/{node_id}', fields={'attributes': fh, 'copy_data': node_id, 'copy_indexes': 'true'},
        auth=auth_token
    )

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_create_node(send_patch, get_filehandle):
    fh = object()
    get_filehandle.return_value = fh
    shockobj.create_node(upload_file='path', attributes_file='path')
    send_patch.assert_called_with(
        'POST', f'{shock_url}/node', fields={'attributes': fh, 'upload': fh}, auth=auth_token
    )

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_update_node(send_patch, get_filehandle):
    fh = object()
    get_filehandle.return_value = fh
    shockobj.update_node(node_id, upload_file='path', attributes_file='path')
    send_patch.assert_called_with(
        'PUT', f'{shock_url}/node/{node_id}', fields={'attributes': fh, 'upload': fh}, auth=auth_token
    )

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_download_node(send_patch, get_filehandle):
    fh = object()
    send_patch.return_value = send_patch
    send_patch.content = 'some-content'
    send_patch.text = 'some-context'
    results = shockobj.download_node(node_id)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/{node_id}?download', decode=False, auth=auth_token
    )
    assert results == 'some-context'

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_download_node(send_patch, get_filehandle):
    fh = object()
    send_patch.return_value = send_patch
    send_patch.content = 'some-content'
    send_patch.text = 'some-context'
    results = shockobj.download_node(node_id, binary=True)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/{node_id}?download', decode=False, auth=auth_token
    )
    assert results == 'some-content'

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_download_node_idx(send_patch, get_filehandle):
    fh = object()
    get_filehandle.return_value = fh
    shockobj.download_node(node_id, index='some idx', part=42)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/{node_id}?download&index=some%20idx&part=42', decode=False, auth=auth_token
    )

@patch('seqcenter.shock.get_filehandle')
@patch('seqcenter.shock.send')
def test_ShockClient_download_node_chunk(send_patch, get_filehandle):
    fh = object()
    get_filehandle.return_value = fh
    shockobj.download_node(node_id, index='some idx', part=42, chunk=42)
    send_patch.assert_called_with(
        'GET', f'{shock_url}/node/{node_id}?download&index=some%20idx&part=42', decode=False, auth=auth_token
    )


