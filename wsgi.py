from Typing_Tester.views import start_test, notfound, end_test

def typing_tester(environ, start_response):

    path = environ['PATH_INFO']
    request_body = environ['wsgi.input'].read().decode('utf-8')
    request_method = environ['REQUEST_METHOD']

    if path == '/start' and request_method == 'GET':

        return start_test(start_response, request_body)

    elif path == '/end' and request_method == 'POST':

        return end_test(start_response, request_body)
    else:

        return notfound(start_response)










