import os
import httplib, urllib
import mimetypes
import mimetools
def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0]
def encod_multipart_formdata(fields,files=[]):
    BOUNDARY = mimetools.choose_boundary()
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
        #print(open(filepath,'rb').read())
        #print(open(filepath, 'rb').read())
        L.append( open(filepath, 'rb').read() )
    L.append( '--' + BOUNDARY + '--' )
    L.append( '' )
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body
if __name__ == '__main__':
    myfields = [("method","add"),("property","{'object_type':'ecm_document','file_type':['txt'],'file_name':['test']}"),("sysCheckNo","74D631A4DF157D87B5B123369ADE61B9"), ("userName","admin")]
    myfiles = [("name","1.txt")]
    mydata = encod_multipart_formdata(myfields, myfiles )
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


