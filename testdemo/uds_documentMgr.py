import httplib
import json
import utils
DOWNLOADFLAG = 1
UPLOADFLAG = 2
class UDSMgr:
    m_host = ''
    m_uri= ''
    m_port = 80
    def __init__( self, host, uri, port ):
        self.m_host = host
        self.m_uri = uri
        self.m_port = port
    #def __init__( self, ip, port ):
    #    m_ip = ip
    #    m_port = port
    def _download( self, data, headers ):
        strfilename = ''
        for key,filename in headers:
            if key == "filename":
                print 'key=filename'
                strfilename = './downloads/'+filename
                #print type(filename)
                print strfilename

                file_obj = open( strfilename, "wb" )
                try:
                    file_obj.write( data )
                    file_obj.close()
                except Exception as e:
                    print e
                finally:
                    file_obj.close()

    def do_Post( self, flag, body, headers={} ):
        global DOWNLOADFLAG
        global UPLOADFLAG
        httpClient = None
        try:
            httpClient = httplib.HTTPConnection( self.m_host, self.m_port )
            httpClient.request( "POST", self.m_uri, body, headers )
            response = httpClient.getresponse()
            print response.status
            print response.reason
            data = response.read()
            respheader = response.getheaders()
            if flag == DOWNLOADFLAG:
                self._download( data, respheader )
            else:
                print data

#            print respheader["filename"]
        except Exception as e:
            print e
        finally:
            if httpClient:
                httpClient.close()

    def UploadFile( self, strFormInfo, strFileProperty, strUploadFile ):
        dicfrmInfo = json.loads( strFormInfo )
        #dicfilePropty = json.loads( strFileProperty )
        dicfilePropty = {"property":strFileProperty}
        dicfields = dicfrmInfo.copy()
        dicfields.update( dicfilePropty )
        dicUploadFile = json.loads( strUploadFile )
        body_contype = utils.encode_multipart_formdata_key( dicfields, dicUploadFile )
        headers = {"Content-type": body_contype[0]}
        body = body_contype[1]
        self.do_Post( UPLOADFLAG, body, headers )

    def DownloadFile( self, strFormInfo, strFileProperty ):
        dicfrmInfo = json.loads( strFormInfo )
        dicfilePropty = { "property" : strFileProperty }
        dicfields = dicfrmInfo.copy()
        dicfields.update( dicfilePropty )
        body_contype = utils.encode_multipart_formdata_key( dicfields )
        headers = {"Content-type": body_contype[0]}
        body = body_contype[1]
        print headers
        print body
        self.do_Post( DOWNLOADFLAG, body, headers )


