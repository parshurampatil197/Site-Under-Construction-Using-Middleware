from django.shortcuts import HttpResponse, render


class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print("call from Middleware Before view")
        # response = HttpResponse("This is Under Construction")
        response = render(request, 'mysite/siteuc.html')
        print("call from Middleware After view")
        return response
        