import time,sys
for x in range(1,101):
    print( "%s/r" %("|"*(x/2)+ " " +str(x) + "%")),
    time.sleep(0.1)
