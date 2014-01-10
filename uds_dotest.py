import sys,os
import argparse
from uds_documentMgr import UDSMgr
from uds_config import *
parser = argparse.ArgumentParser()
parser.add_argument( "-c" "--config", help = "the full path of config file" )
parser.add_argument( "-t" "--thread", help = "the use thread nums", type = int )
parser.add_argument( "-a" "--add", help = "add document" )
parser.add_argument( "-as" "--adds", help = "adds document" )

if __name__ == "__main__":
    udsConfigMgr = UDSConfigMgr("./config.ini")
    print udsConfigMgr.m_Host
    print udsConfigMgr.m_SysCheckCode
    udsDocumentMgr = UDSMgr( udsConfigMgr.m_Host, udsConfigMgr.m_Uri, udsConfigMgr.m_Port )
    udsDocumentMgr.Add(
                "{\"userName\":\"admin\",\"sysCheckNo\":\"74D631A4DF157D87B5B123369ADE61B9\",\"method\":\"add\"}",
                "{\"object_type\":\"ecm_document\",\"file_type\":[\"docx\"],\"file_name\":[\"worddd\"]}",
                "{\"uploadFileDTO.fileList\":\"1.docx\"}")
    #print 'http_code http_size conn_time pre_tran start_tran total_time'
    #print "%d %d %f %f %f %f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
