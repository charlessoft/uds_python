import pycurl
import StringIO
class uds_httpData:
    def __init__( self ):
        self.data = None
        self.datalen = datalen
        self.postion = 0
        self.totalen = 0
class uds_curl:
    #def HttpRequest( self,  http_method, url ):
    def __init__( self ):
        self.m_headers = []
    def HttpRequest( self,  http_method, url, httpData=None, custom_headers=[] ):
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
            c.setopt( pycurl.HTTPPOST, 1 )
            c.setopt( pycurl.POSTFIELDS, httpData.data )
            c.setopt( pycurl.POSTFIELDSIZE, httpData.datalen )
        elif http_method == "PUT":
            print "PUTxxxx"
        print self.m_headers
        c.setopt( pycurl.HTTPHEADER, self.m_headers )
        c.perform()
        print c.fp.getvalue()
if __name__ == "__main__":
    curl = uds_curl()
    curl.HttpRequest( "GET", "http://10.142.49.127:8081/index.html" )


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
