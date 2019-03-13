

import requests, json, os
from datetime import datetime, timedelta
from pprint import pprint


my_key = os.getenv("MOVIE_TOKEN")

def weeklyboxoffice(year, month, day):
    targetDts = []
    defaultday = datetime(year, month, day)
    for tenweeks in range(10):
        targetDts.append((defaultday-timedelta(weeks=tenweeks)).strftime('%Y%m%d'))
    movie_Cds = []
    movie_Nms = []
    movie_Accs = []
    movie_yearWeekTime = []

    for Dt in targetDts:
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={my_key}&targetDt={Dt}&weekGb=0"
        req = requests.get(url)
        movie_result = req.json()['boxOfficeResult']
        movie_list = movie_result['weeklyBoxOfficeList']

        for movies in movie_list:
            if movies['movieCd'] not in movie_Cds:
                movie_Cds.append(movies['movieCd'])
                movie_Nms.append(movies['movieNm'])
                movie_Accs.append(movies['audiAcc'])
                movie_yearWeekTime.append(movie_result['yearWeekTime'])
            elif movie_Nms[movie_Cds.index(movies['movieCd'])] < movies['movieNm']:
                movie_Nms[movie_Cds.index(movies['movieCd'])] = movies['movieNm']
                movie_yearWeekTime[movie_Cds.index(movies['movieCd'])] = movie_result['yearWeekTime']

    with open('boxoffice.csv','w') as f:
        f.write('movie_code,title,audience,recorded_at\n')
        for i in range(len(movie_Cds)):
            f.write(f'{movie_Cds[i]},{movie_Nms[i]},{movie_Accs[i]},{movie_yearWeekTime[i]}\r')

