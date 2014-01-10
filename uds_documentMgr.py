import httplib
import json
import utils
import sys
from uds_curl import *
reload(sys)
sys.setdefaultencoding("utf-8")
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
        self.m_urlpath = "http://%s:%d%s" %( host, port, uri )
        print self.m_urlpath
    def _download( self, data, headers ):
        strfilename = ''
        for key,filename in headers:
            if key == "filename":
                strfilename = './downloads/'+filename

                file_obj = open( strfilename, "wb" )
                try:
                    file_obj.write( data )
                    file_obj.close()
                    print strfilename, "---ok"
                except Exception as e:
                    print e
                finally:
                    file_obj.close()

    def do_Post_byCurl( self, body, headers = {} ):
        curl = uds_curl()
        httpData = uds_httpData()
        httpData.data = body
        httpData.datalen = len( body )
        httpData.totalen = len( body )
        curl.HttpRequest( "POST", self.m_urlpath, httpData, headers )

    def do_Post_byHttplib( self, flag, body, headers={} ):
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
        except Exception as e:
            print e
        finally:
            if httpClient:
                httpClient.close()

    def UploadFile( self, strFormInfo, strFileProperty, strUploadFile ):
        dicfrmInfo = json.loads( strFormInfo )
        dicfilePropty = {"property":strFileProperty}
        dicfields = dicfrmInfo.copy()
        dicfields.update( dicfilePropty )
        dicUploadFile = json.loads( strUploadFile )
        arrUploadFile = [("uploadFileDTO.fileList", dicUploadFile["uploadFileDTO.fileList"], open(dicUploadFile["uploadFileDTO.fileList"]).read() )]

        #print type(arrUploadFile)
        content_type, body = utils.encode_multipart_formdata( dicfields, arrUploadFile )
        headers = {"Content-type":content_type}
        self.do_Post( UPLOADFLAG, body, headers)

        #utils.encode_multipart_formdata( dicfields,
        #body_contype = utils.encode_multipart_formdata_key( dicfields, dicUploadFile )
        #headers = {"Content-type": body_contype[0]}
        #body = body_contype[1]
        #self.do_Post( UPLOADFLAG, body, headers )

    def DownloadFile( self, strFormInfo, strFileProperty ):
        dicfrmInfo = json.loads( strFormInfo )
        dicfilePropty = { "property" : strFileProperty }
        dicfields = dicfrmInfo.copy()
        dicfields.update( dicfilePropty )
        body_contype = utils.encode_multipart_formdata_key( dicfields )
        headers = {"Content-type": body_contype[0]}
        body = body_contype[1]
        #print headers
        #print body
        self.do_Post( DOWNLOADFLAG, body, headers )

    def Add( self, strFormInfo, strFileProperty, strUploadFile ):
        dicfrmInfo = json.loads( strFormInfo )
        dicfilePropty = { "property" : strFileProperty }
        dicfields = dicfrmInfo.copy()
        dicfields.update( dicfilePropty )
        dicUploadFile = json.loads( strUploadFile )
        arrUploadFile = [("uploadFileDTO.fileList", dicUploadFile["uploadFileDTO.fileList"],
                        open(dicUploadFile["uploadFileDTO.fileList"]).read() )]
        content, body = utils.encode_multipart_formdata( dicfields, arrUploadFile )
        headers = list()
        headers.append( "Content-type:" + content )
        self.do_Post_byCurl( body, headers )

    def Adds( self, strFormInfo, strFileProperty ):
        print "Adds"

    def AddAttachment( self, strFormInfo, strFileProperty ):
        print "AddAttachment"

    def Modify( self, strFormInfo, strFileProperty ):
        print "Modify"

    def Download( self, strFormInfo, strFileProperty ):
        print "Download"

    def DownloadAttachment( self, strFormInfo, strFileProperty ):
        print "downloadAttachment"

    def DelDocument( self, strFormInfo, strFileProperty ):
        print "DeleteDocument"

    def GetProperty( self, strFormInfo, strFileProperty ):
        print "GetProperty"

    def SimpleQuery( self, strFormInfo, strFileProperty ):
        print "SimpleQuery"



