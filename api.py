import requests
import pandas as pd
import pickle
# https://api.themoviedb.org/3/search/movie?api_key=88cdc0cdb44a687b97e2d0bb57e5328&language=en-US&page=1&include_adult=false
# poster api
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=88cdc0cdb44a687b97e2d0bb57e5328f&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def video(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}/videos?api_key=88cdc0cdb44a687b97e2d0bb57e5328f&language=en-US'.format(movie_id))
    video_data=response.json()
    return 'https://www.youtube.com/watch?v=' + video_data['results'][0]['key']


datas = pd.read_csv('data\datafiles.csv' , encoding = "ISO-8859-1")

similarity = pickle.load(open('data\similarity.pkl','rb'))

'release_date','status','vote_average'
def movie_list( movie):
                
    movie = datas[datas['title'] == movie].index[0]
    distance = similarity[movie]
    movi_list = sorted(list(enumerate(distance)) ,reverse = True ,key=lambda x: x[1])[1:11] 

    data = []
    poster =[]
    genress = []
    original_language = []
    overview = []
    release_date =[]
    status = []
    vote_average=[]
    video_path=[]

    for i in movi_list:
        
        movis_id = datas.iloc[i[0]].id

        data.append(datas.iloc[i[0]].title)
        # with api
        poster.append(fetch_poster(movis_id))
        genress.append(datas.iloc[i[0]].genres)
        original_language.append(datas.iloc[i[0]].original_language)
        overview.append(datas.iloc[i[0]].overview)
        release_date.append(datas.iloc[i[0]].release_date)
        status.append(datas.iloc[i[0]].status)
        vote_average.append(datas.iloc[i[0]].vote_average)
        # with api
        video_path.append(video(movis_id))

    return data , poster , genress , original_language ,overview , release_date , status , vote_average , video_path 