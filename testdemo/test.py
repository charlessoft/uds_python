class mytest:
    def sayHello(self):
        print("hello")
    def testSay(self):
        self.sayHello()

if __name__ == '__main__':
    test = mytest()
    test.sayHello() #ok
    test.testSay()
