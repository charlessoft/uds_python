#---php demo
#echo 'hello world python'


#coding = utf8
#---python code
import httplib
httpClient = None
try:
    httpClient = httplib.HTTPConnection( '192.168.1.100', 8081, timeout = 30 )
    httpClient.request( 'GET', '/index.php' )
#response is HTTPResponse
    response = httpClient.getresponse()
    print( response.status )
    print( response.reason )
    print( response.read() )
except Exception as e:
    print e
finally:
    if httpClient:
        httpClient.close()
