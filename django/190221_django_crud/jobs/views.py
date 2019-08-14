import os
from django.shortcuts import render
from .models import Job
from faker import Faker
import requests

#giphy

# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')
    
def pastlife(request):
    name = request.GET.get('name')
    person = Job.objects.filter(name=name).first()
    if person:
        pastjob = person.pastjob
    else:
        faker = Faker('ko_kr')
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)
        person.save()
    
    GIPHY_API2 = os.getenv('GIPHY_API')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API2}&q={pastjob}&limit=1&lang=ko'
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')
    return render(request, 'jobs/pastlife.html', {'person':person, 'image':image})