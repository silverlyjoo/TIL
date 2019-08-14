from django.shortcuts import render
from datetime import datetime, timedelta
import requests, os



def index(request):
    return render(request, 'utilities/index.html')

def bye(request):
    byeday = (datetime(2019,2,28) - datetime.now())//timedelta(days=1)
    # printday = byeday.strftime("d%")
    return render(request, 'utilities/bye.html', {'byeday': byeday})
    
def graduation(request):
    graday = (datetime(2019,5,28) - datetime.now())//timedelta(days=1)
    return render(request, 'utilities/graduation.html', {'graday': graday})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    today = datetime.now()
    KEY = os.getenv('WEATHERKEY')
    print(KEY)
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID={KEY}'
    req = requests.get(url).json()
    weather = req['weather'][0]['description']
    max_temp1 = req['main']['temp_max']-273.15
    min_temp1 = req['main']['temp_min']-273.15
    temp1 = req['main']['temp']-273.15
    max_temp = f'{max_temp1:.1f}'
    min_temp = f'{min_temp1:.1f}'
    temp = f'{temp1:.1f}'
    return render(request, 'utilities/today.html', {'weather': weather, 'max_temp':max_temp, 'min_temp':min_temp, 'temp':temp, 'today':today})
    
    
def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts':fonts})
    
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    print(font, text)
    req = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}').text
    return render(request, 'utilities/ascii_make.html', {'req':req})
    
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    originaltext = request.POST.get('originaltext')
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
    "source": "ko",
    "target": "en",
    "text": originaltext
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'reply_text':reply_text})
    
