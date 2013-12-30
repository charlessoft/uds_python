import os
import httplib, urllib
import mimetypes
import mimetools


def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0]

def encode_multipart_formdata_list(fields,files=[]):
    BOUNDARY = "---------------------------7dc2512d8124c"#mimetools.choose_boundary()
    CRLF = '\r\n'
    L = []
    for( key, value) in fields:
        L.append( '--' + BOUNDARY )
        L.append( 'Content-Disposition: form-data; name="%s"' % key )
        L.append( '' )
        L.append( value )
    for( key, filepath) in files:
        L.append( '--' + BOUNDARY )
        L.append( 'Content-Disposition: form-data; name="%s"; filename="%s"' %(key,os.path.basename(filepath)))
        L.append( 'Content-Type:%s' % get_content_type(filepath) )
        L.append( '' )
        L.append( open(filepath, 'rb').read() )
    L.append( '--' + BOUNDARY + '--' )
    L.append( '' )
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def encode_multipart_formdata_key(fields,files=[]):
    BOUNDARY = "---------------------------7dc2512d8124c"#mimetools.choose_boundary()
    CRLF = '\r\n'
    L = []
    for key in fields:
        L.append( '--' + BOUNDARY )
        L.append( 'Content-Disposition: form-data; name="%s"' % key )
        L.append( '' )
        L.append( '%s' %(fields[key]) )
    for key in files:
        L.append( '--' + BOUNDARY )
        L.append( 'Content-Disposition: form-data; name="%s"; filename="%s"' %(key,os.path.basename(files[key])))
        L.append( 'Content-Type:%s' % get_content_type(files[key]) )
        L.append( '' )
        L.append( open(files[key], 'rb').read() )
    L.append( '--' + BOUNDARY + '--' )
    L.append( '' )
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def post_multipart(host, uri, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTPConnection(host,7002)
    headers = {
        'User-Agent': 'INSERT USERAGENTNAME',
        'Content-Type': content_type
        }
    h.request('POST', uri, body, headers)
    res = h.getresponse()
    return res.status, res.reason.decode('utf-8'), res.read().decode('utf-8')

def encode_multipart_formdata(fields, files=[]):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------bound@ry_$'
    CRLF = '\r\n'
    L = []
    fields1 = dict([(str(k), str(v)) for k, v in fields.items()])
    for key in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key.encode("utf-8"))
        L.append('')
        L.append( '%s' %(fields1[key]))
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key.encode("utf-8"), filename.encode("utf-8")))
        L.append('Content-Type: %s' %( get_content_type(filename).encode("utf-8")))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


if __name__ == '__main__':
    myfields_ok = [
            ("method","add"),
            ("property","{'object_type':'ecm_document','file_type':['docx'],'file_name':['word docs']}"),
            ("sysCheckNo","74D631A4DF157D87B5B123369ADE61B9"),
            ("userName","admin")
            ]
    myfiles_ok = [
            ("uploadFileDTO.fileList","1.docx")
            ]

    myfields = {
            "method":"add",
            "property":"{'object_type':'ecm_document','file_type':['docx'],'file_name':['word docs']}",
            "sysCheckNo":"74D631A4DF157D87B5B123369ADE61B9",
            "userName":"admin"
            }
    myfiles = {
            "uploadFileDTO.fileList":"1.docx"
            }
    myfiles_ok_ext = [
            ("uploadFileDTO.fileList", "1.docx", open("1.docx", 'rb').read() )
            ]
    print post_multipart("10.142.49.238", "/http/document!execute", myfields,myfiles_ok_ext)
    #mydata = encode_multipart_formdata_ok(myfields_ok, myfiles_ok )
    #mydata = encode_multipart_formdata_key(myfields, myfiles )
    ##print mydata[0]
    ##print mydata[1]
    #httpClient = None
    #try:
    #    params = mydata[1]
    #    headers = {"Content-type": mydata[0]}
    #    httpClient = httplib.HTTPConnection( "10.142.49.238", 7002 )
    #    httpClient.request( "POST", "/http/document!execute", params, headers )
    #    response = httpClient.getresponse()
    #    print response.status
    #    print response.reason
    #    print response.read()
    #    print response.getheaders()

    #except Exception as e:
    #    print e
    #finally:
    #    if httpClient:
    #        httpClient.close()


