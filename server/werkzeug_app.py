#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response # type: ignore
@Request.application# this is a decorator that tells the werkzeug library that this function is a WSGI application 
def application(request):#application that handles all  the request that the server receives 
    print(f"This web server is running at  {request.remote_addr}")#print the IP address of the client that made the request
    return Response (" A WSGI generated this response!") #sends a message back to the client that made the request .
if __name__ == '__main__':#the entry point to the server application
    from werkzeug.serving import run_simple # type: ignore
    run_simple( 
    hostname='localhost',  # the hostname of the server on the local machine 
    port=5555,# the port number on which the server will listen for requests
    application = application)# the application that will handle the requests
    # run_simple('

