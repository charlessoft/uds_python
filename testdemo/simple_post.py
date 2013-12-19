#---php demo
#var_dump($POST)

#---python code
import httplib,urllib
httpClient = None
try:
    params = urllib.urlencode( {'name':'tom','age':22} )
    headers = { "Content-type":"application/x-www-form-urlencoded", "Accept:":"text/plain" }
    httpClient = httplib.HTTPConnection( "192.168.1.100", 8081, timeout = 30 )
    httpClient.request( "POST", "/index.php", params, headers )

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #get headers
except Exception as e:
    print e
finally:
    if httpClient:
        httpClient.close()
