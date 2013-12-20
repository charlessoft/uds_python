import random
import string
def GenPassword(length):
    chars=string.ascii_letters+string.digits
    return ''.join([random.choice(chars) for i in range(length)])
if __name__=="__main__":
    for i in range(10):
        print GenPassword(200)
