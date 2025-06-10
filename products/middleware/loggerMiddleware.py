class LoggerMiddleware:
    def __init__(self,get_response):  #get_response is a next pointer in linked list
        self.get_response = get_response

    def __call__(self, request):   #call method will be executed every time for http call
        print(f"[MiddleWare] {request.path} - {request.method}")
        response = self.get_response(request)

        print(f"[MiddleWare] statuscode {response.status_code}")
        return response

