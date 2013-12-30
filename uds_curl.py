import pycurl
import mimetypes
import StringIO
class uds_httpData:
    def __init__( self ):
        self.data = None
        self.datalen = 0
        self.postion = 0
        self.totalen = 0
class uds_curl:
    #def HttpRequest( self,  http_method, url ):
    def __init__( self ):
        self.m_headers = []
    def HttpRequest( self,  http_method, url, httpData, datalen, custom_headers=[] ):
        c = pycurl.Curl()
        c.setopt( pycurl.URL, url )
        #b = StringIO.StringIO()
        c.fp = StringIO.StringIO()
        c.setopt( pycurl.FOLLOWLOCATION, 1)
        c.setopt( pycurl.HEADER, False )
        c.setopt( pycurl.WRITEFUNCTION, c.fp.write )
        c.setopt( pycurl.SSL_VERIFYPEER, False )
        c.setopt( pycurl.SSL_VERIFYHOST, False )
        c.setopt( pycurl.VERBOSE, True )
        c.setopt( pycurl.NOPROGRESS, False )
        print http_method
        print cmp(http_method, "GET")
        if http_method == "GET":
            print "GETxx"
            c.setopt( pycurl.HTTPGET, 1 )
            self.m_headers.append( "Content-Type: application/atom+xml" )
        elif http_method == "POST":
            print "POSTXX"
            #c.setopt( pycurl.HTTPPOST, )
            c.setopt( pycurl.POSTFIELDS, httpData)
            c.setopt( pycurl.POSTFIELDSIZE, datalen )
        elif http_method == "PUT":
            print "PUTxxxx"
        print self.m_headers
        c.setopt( pycurl.HTTPHEADER, self.m_headers )
        c.perform()
        print c.fp.getvalue()

def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0]

def encode_multipart_formdata(fields, files):
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
if __name__ == "__main__":

    myfields = {
            "method":"add",
            "property":"{'object_type':'ecm_document','file_type':['docx'],'file_name':['word docs']}",
            "sysCheckNo":"74D631A4DF157D87B5B123369ADE61B9",
            "userName":"admin"
            }
    myfiles_ok_ext = [
            ("uploadFileDTO.fileList", "1.docx", open("1.docx", 'rb').read() )
            ]
    curl = uds_curl()
    #print post_multipart("10.142.49.238", "/http/document!execute", myfields,myfiles_ok_ext)
    content_type,body = encode_multipart_formdata( myfields, myfiles_ok_ext )
    #print content_type
    print body

    httpData = uds_httpData()
    httpData.data = body
    httpData.data = len(body)
    httpData.totalen = len(body)
    curl.HttpRequest("POST","http://10.142.49.238:7002/http/document!execute", body, len(body), content_type)
    #curl.HttpRequest( "GET", "http://10.142.49.127:8081/index.html" )


#curl_easy_setopt(curl, CURLOPT_ERRORBUFFER, errorBuffer);
#-okcurl_easy_setopt(curl, CURLOPT_URL, url.c_str());
#-ok#curl_easy_setopt(curl, CURLOPT_HEADER, 0);
#-okcurl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1);
#curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
#curl_easy_setopt(curl, CURLOPT_WRITEDATA, lpService);
#curl_easy_setopt(curl, CURLOPT_HEADERFUNCTION,WriteHeaderCallback); // our static function
#curl_easy_setopt(curl, CURLOPT_WRITEHEADER, lpService); //"headers" is a member variable referencing HttpHeaders
#curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
#curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
#curl_easy_setopt(curl, CURLOPT_VERBOSE , 1);
#
#curl_easy_setopt(curl, CURLOPT_NOPROGRESS, FALSE);
#curl_easy_setopt(curl, CURLOPT_PROGRESSFUNCTION, ProgressCallback);
#curl_easy_setopt(curl, CURLOPT_PROGRESSDATA, lpService);
#