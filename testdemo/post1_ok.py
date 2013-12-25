import os
import mimetypes
import mimetools
def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0]
def encod_multipart_formdata(fields,files=[]):
    BOUNDARY = mimetools.choose_boundary()
    #print(" BOUNDARY = %s"%(BOUNDARY))
    CRLF = '\r\n'
    L = []
    for key in fields:
        #print "key=%s, value=%s" % (key, fields[key])
        L.append( '--' + BOUNDARY )
        L.append( 'Content-Disposition: form-data; name="%s"' % key )
        L.append( ' ' )
        L.append( '"%s"' %(fields[key]) )
    for( key, filepath) in files:
        L.append( '--' + BOUNDARY )
        L.append( 'Content-Disposition: form-data; name="%s"; filename="%s"' %(key,os.path.basename(filepath)))
        L.append( 'Content-Type:%s' % get_content_type(filepath) )
        L.append( '' )
        #L.append( openfile(filepath, 'rb').read() )
    L.append( '--' + BOUNDARY + '--' )
    L.append( '' )
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body
if __name__ == '__main__':
    #myfile = {'name':'1','age':'20'}
    #myfile = ['a','b','c','ad']
    #myfile = ["I","you","he","she"]
    myfields = {"name":"1","age":"20"}
    #myfiles = {"file1":"1.txt","file2":"2.txt"}
    #myfiles = [("key":"txt1")]
    myfiles = [("key","1.txt"),("key2","1.txt")]
    mydata = encod_multipart_formdata(myfields, myfiles)
    print 'mydata[0] =' ,mydata[0]
    print 'mydata[1] = ' ,mydata[1]


