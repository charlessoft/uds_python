import ConfigParser
class UDSConfigMgr:
    def __init__( self ):
        print
    def __init__( self, configPath ):
        self.LoadConfig( configPath )
    ## load config from config.ini
    def LoadConfig( self, configPath ):
        config = ConfigParser.ConfigParser()
        config.readfp( open( configPath, "rb" ) )
        self.m_Host = config.get( "UDS", "HOST" )
        self.m_Uri = config.get( "UDS", "URI" )
        self.m_Port = config.getint( "UDS", "PORT" )
        self.m_SysCheckCode = config.get( "SYS", "USERNAME" )
        self.m_SysCheckCode = config.get( "SYS", "SYSCHECKNO" )
        self.m_SysCheckCode = config.get( "SYS", "DOWNLOADFOLDER" )
        #print "HOST=", self.m_Host
        #print "URI=", self.m_Uri
        #print "PORT=", self.m_Port


