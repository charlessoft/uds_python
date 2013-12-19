import httplib
import json
import utils
class UDSMgr:
    m_ip = ''
    m_content = ''
    m_port = 80
    def __init__( self, ip, content, port ):
        self.m_ip = ip
        self.m_content = content
        self.m_port = port
    #def __init__( self, ip, port ):
    #    m_ip = ip
    #    m_port = port
    def do_Post( self, body, headers ):
        httpClient = None
        try:
            httpClient = httplib.HTTPConnection( self.m_ip, self.m_port )
            httpClient.request( "POST", self.m_content, body, headers)
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

    def UploadFile( self, strFormInfo, strFileProperty, strUploadFile ):
        dicfrmInfo = json.loads( strFormInfo )
        #dicfilePropty = json.loads( strFileProperty )
        dicfilePropty = {"property":strFileProperty}
        dicfileds = dicfrmInfo.copy()
        dicfileds.update( dicfilePropty )
        dicUploadFile = json.loads( strUploadFile )
        #for key in dicUploadFile:
        #    print 'key=%s value=%s' %(key, dicUploadFile[key])
        body_contype = utils.encode_multipart_formdata_key( dicfileds, dicUploadFile )
        #header = body_contype[0]
        headers = {"Content-type": body_contype[0]}
        body = body_contype[1]
        #print(body)
        self.do_Post( body, headers )

