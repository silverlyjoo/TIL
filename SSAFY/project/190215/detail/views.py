from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'detail/index.html')
    
def qna(request):
    return render(request, 'detail/qna.html')
    
def mypage(request):
    return render(request, 'detail/mypage.html')
    
def signup(request):
    return render(request, 'detail/signup.html')
    
def notfound(request, not_found):
    return render(request, 'detail/notfound.html', {'notfound':not_found})