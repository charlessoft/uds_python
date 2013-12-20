import utils
import json
from uds_documentMgr import *
def dotest():
    udsDocumentMgr = UDSMgr( "10.142.49.238", "/http/document!execute", 7002 )
    #udsDocumentMgr.UploadFile(
    #        "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"add\"}",
    #        "{\"object_type\":\"ecm_document\",\"file_type\":[\"txt\"],\"file_name\":[\"test\"]}",
    #        "{\"uploadFileDTO.fileList\":\"1.txt\"}")
    udsDocumentMgr.DownloadFile(
            "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"download\"}",
            "{\"documentid\":\"09027101801e01da\"}"
            )

dotest()
