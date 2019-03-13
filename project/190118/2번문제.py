


import requests, json, os
from pprint import pprint

my_key = os.getenv("MOVIE_TOKEN")
movieCodesRaw = []
with open('boxoffice.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        movieCodesRaw.append((line.strip().split(','))[0])

movieCodes = movieCodesRaw[1:]
movie_infodata = {}

for movieCd in movieCodes:
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={my_key}&movieCd={movieCd}"
    req = requests.get(url)
    movie_info = req.json()['movieInfoResult']['movieInfo']
    if movieCd not in movie_infodata.keys():
        movie_infodata[movieCd]=[]
    movie_infodata[movieCd] += movie_info['movieCd'], movie_info['movieNm'].replace(",","."), movie_info['movieNmEn'].replace(",","."), movie_info['movieNmOg'], movie_info['openDt'], movie_info['showTm'], '/'.join([movie_info['genres'][i]['genreNm'] for i in range(len(movie_info['genres']))]), movie_info['directors'][0]['peopleNm'], movie_info['audits'][0]['watchGradeNm']
    if len(movie_info['actors'])>3:
        for j in range(3):
            movie_infodata[movieCd].append(movie_info['actors'][j]['peopleNm'])
    else:
        for j in range(len(movie_info['actors'])):
            movie_infodata[movieCd].append(movie_info['actors'][j]['peopleNm'])

results = []
for mcode, infos in movie_infodata.items():
    results.append(','.join(infos))

with open('movie.csv','w', encoding='utf-8') as f:
    f.write('movie_code,movie_name_ko,movie_name_en,movie_name_og,prdt_year,showtime,genres,directors,watch_grade_nm,actor1,actor2,actor3\n')
    for result in results:
        f.write(f'{result}\r')