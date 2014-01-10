import pycurl
import mimetypes
import StringIO
import json
import utils
class uds_httpData:
    def __init__( self ):
        self.data = None
        self.datalen = 0
        self.postion = 0
        self.totalen = 0
class uds_curl:
    def __init__( self ):
        self.m_headers = []
    def WriteHeaderCallback( self, buf ):
        #print type(buf)
        print
        #self.m_respHeader += buf
    def HttpRequest( self,  http_method, url, httpData=[],  custom_headers=[] ):
        self.m_headers = custom_headers
        c = pycurl.Curl()
        c.setopt( pycurl.URL, url )
        c.fp = StringIO.StringIO()
        c.setopt( pycurl.FOLLOWLOCATION, 1)
        c.setopt( pycurl.HEADER, False )
        c.setopt( pycurl.WRITEFUNCTION, c.fp.write )
        c.setopt( pycurl.HEADERFUNCTION, self.WriteHeaderCallback )
        c.setopt( pycurl.SSL_VERIFYPEER, False )
        c.setopt( pycurl.SSL_VERIFYHOST, False )
        #c.setopt( pycurl.VERBOSE, True )
        #c.setopt( pycurl.NOPROGRESS, False )
        if http_method == "GET":
            print "GETxx"
            c.setopt( pycurl.HTTPGET, 1 )
        elif http_method == "POST":
            c.setopt( pycurl.POSTFIELDS, httpData.data )
            c.setopt( pycurl.POSTFIELDSIZE, httpData.datalen )
        elif http_method == "PUT":
            print "PUTxxxx"
        c.setopt( pycurl.HTTPHEADER, self.m_headers )
        c.perform()
        print c.fp.getvalue()

        http_code = c.getinfo(pycurl.HTTP_CODE)
        http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
        http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
        http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
        http_total_time = c.getinfo(pycurl.TOTAL_TIME)
        http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
        #print 'http_code http_size conn_time pre_tran start_tran total_time'
        #print "%d %d %f %f %f %f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
        #print self.m_respHeader
        return c.fp.getvalue(), http_code, http_conn_time, http_pre_tran, http_start_tran, http_total_time, http_size

if __name__ == "__main__":
#upload-----
    #myfields = {
    #        "method":"add",
    #        "property":"{'object_type':'ecm_document','file_type':['txt'],'file_name':['test']}",
    #        "sysCheckNo":"74D631A4DF157D87B5B123369ADE61B9",
    #        "userName":"admin"
    #        }
    #myfiles_ok_ext = [
    #        ("uploadFileDTO.fileList", "1.txt", open("1.txt", 'rb').read() )
    #        ]
    #curl = uds_curl()
    #content_type,body = utils.encode_multipart_formdata( myfields, myfiles_ok_ext )

    #httpData = uds_httpData()
    #httpData.data = body
    #httpData.datalen = len(body)
    #httpData.totalen = len(body)
    #strheaders = "Content-type:" + content_type
    #headers = list()
    #headers.append( strheaders )
    #curl.HttpRequest("POST","http://10.142.49.238:7002/http/document!execute", httpData, headers )

#download ----

    strFormInfo ="{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"download\",\"encryptData\":\"\"}"
    strProperty = "{\'documentid\':\'09027101801e01da\'}"
    httpData = uds_httpData()
    curl = uds_curl()

    dicfrmInfo = json.loads( strFormInfo )
    dicfilePropty = { "property" : strProperty }
    dicfields = dicfrmInfo.copy()
    dicfields.update( dicfilePropty )
    body_contype,body = utils.encode_multipart_formdata( dicfields )
    #headers = {"Content-type": body_contype[0]}
    curl.HttpRequest( "GET", "http://10.142.49.238:7002/http/document!execute" )
    #content_type,body = utils.encode_multipart_formdata( strFormInfo,


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
