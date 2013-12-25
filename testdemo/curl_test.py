from uds_curl import *
if __name__ == "__main__":
    curl = uds_curl()
    curl.HttpRequest("GET","http://10.142.49.127:8081/index.html")
