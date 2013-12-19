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
    #mydata = encode_multipart_formdata_ok(myfields_ok, myfiles_ok )
    mydata = encode_multipart_formdata_key(myfields, myfiles )
    #print mydata[0]
    #print mydata[1]
    httpClient = None
    try:
        params = mydata[1]
        headers = {"Content-type": mydata[0]}
        httpClient = httplib.HTTPConnection( "10.142.49.238", 7002 )
        httpClient.request( "POST", "/http/document!execute", params, headers )
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()

    except Exception as e:
        print e
    finally:
        if httpClient:
            httpClient.close()


