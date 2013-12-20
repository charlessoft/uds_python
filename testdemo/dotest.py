import utils
import json
from uds_documentMgr import *
import ConfigParser
import cmd
import sys
import os
from thread_queue import *
import uuid
import string
import random




class BuildData(Producer):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name = t_name )
        self.data = queue
    def run(self):
        strfilepath = './temp/' + str(uuid.uuid1()) + '.txt'
        self.buildData( strfilepath, random.randint(1,10) )

    def _GenreateData( self, length ):
        chars = string.ascii_letters + string.digits;
        return ''.join([random.choice(chars) for i in range(length)])

    def buildData( self, path, size ):
        file = open( path, "wb" )
        #file.seek( 1024*1024*size )
        file.write( self._GenreateData(size*1024*1024) )
        file.close()

class udsTest( cmd.Cmd ):
    m_Host = ""
    m_Uri = ""
    m_Port = ""
    def __init__( self ):
        cmd.Cmd.__init__( self )
        self.prompt = "UDS >"
        self.loadConfig()
        self.do_hello( "" )

    def do_hello( self, arg ):
        print "********************************************"
        print "Create by charlesoft"
        print "cmd \"upload\" for upload"
        print "cmd \"download\" for download"
        print "cmd \"muldownload\" for multithreaded"
        print "********************************************"

    def do_help( self, arg ):
        self.do_help( "" )

    def do_quit( self, arg ):
        print "thanks!"
        sys.exit(1)

    def default( self, line ):
        print 'input =', line
        self.do_hello( "" )

    def do_muldownload():
        print("s")

    def do_test():
        udsDocumentMgr = UDSMgr( "10.142.49.238", "/http/document!execute", 7002 )
        udsDocumentMgr.UploadFile(
                "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"add\"}",
                "{\"object_type\":\"ecm_document\",\"file_type\":[\"txt\"],\"file_name\":[\"test\"]}",
                "{\"uploadFileDTO.fileList\":\"1.txt\"}")
        #udsDocumentMgr.DownloadFile(
        #        "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"download\",\"encryptData\":\"\"}",
        #        "{\'documentid\':\'09027101801e01da\'}"
        #        )

    ## load config from config.ini
    #  @param self The object pointer
    def loadConfig( self ):
        config = ConfigParser.ConfigParser()
        config.readfp( open("./config.ini", "rb" ))
        print "loadConfig"
        self.m_Host = config.get( "UDS", "HOST" )
        self.m_Uri = config.get( "UDS", "URI" )
        self.m_Port = config.get( "UDS", "PORT" )
        print "HOST=", self.m_Host
        print "URI=", self.m_Uri
        print "PORT=", self.m_Port

    ## download cmd
    # @param self The object pointer
    def do_download( self, arg ):
        strFormInfo ="{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"download\",\"encryptData\":\"\"}"
        strProperty = "{\'documentid\':\'09027101801e01da\'}"
        udsdocMgr = UDSMgr( self.m_Host, self.m_Uri, self.m_Port )
        udsdocMgr.DownloadFile( strFormInfo, strProperty )

    def do_upload( self, arg ):
        filename = "1.txt"
        strFormInfo = "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"add\"}"
        strProperty = "{\"object_type\":\"ecm_document\",\"file_type\":[\"%s\"],\"file_name\":[\"%s\"]}" %(os.path.splitext(filename)[1][1:], os.path.splitext(filename)[0])
        strfiles = "{\"uploadFileDTO.fileList\":\"%s\"}" %(filename)
        print strFormInfo
        print strProperty
        print strfiles
        udsdocMgr = UDSMgr( self.m_Host, self.m_Uri, self.m_Port )
        udsdocMgr.UploadFile( strFormInfo, strProperty, strfiles )
        #udsdocMgr.UploadFile(
        #        "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"add\"}",
        #        "{\"object_type\":\"ecm_document\",\"file_type\":[\"txt\"],\"file_name\":[\"test\"]}",
        #        "{\"uploadFileDTO.fileList\":\"1.txt\"}")
def main():
    queue = Queue()
    test1 = BuildData("prox",queue)
    test1.start()
    test1.join()
    #term = udsTest()
    #term.cmdloop()
if __name__ == '__main__':
    main()
