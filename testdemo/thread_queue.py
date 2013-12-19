from Queue import Queue
import random
import threading
import time

#producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self,name=t_name)
        self.data = queue
    def run(self):
        for i in range(500):
            print( "%s:%s is producing %d to the queue!\n" %(time.ctime(), self.getName(),i) )
            self.data.put(i)
            time.sleep(random.randrange(10)/5)
            #print ("%s:%s finished!" %(time.ctime(), self.getName()))


#Consumer thread

class Consumer(threading.Thread):
    def __init__(self, t_name, queue ):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        #for i in range(5):
        while(True):
        #for i in range(3):
        #     time.sleep(1)
        #     msg = "I'm "+self.name+' @ '+str(i)
        #     print msg

            val = self.data.get()
            print("        %s:%s is consumin. %d in the quque is consumed!\n" %(time.ctime(), self.getName(), val ))
            time.sleep(random.randrange(2))
            print("%s:%s finished!" %(time.ctime(), self.getName()) )

#Main thread
def main():
    queue = Queue()
    producer = Producer("Pro",queue)
    producer.start()
    for i in range(5):
        strconsumer = "Con.%d" %(i)
        consumer = Consumer(strconsumer,queue)
        consumer.start()
        #consumer.join()
    #producer.join()
    queue.join()
    print("All thread terminate!")

if __name__ == "__main__":
    main()

