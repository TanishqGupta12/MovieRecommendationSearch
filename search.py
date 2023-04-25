import requests
# import streamlit as st
# from streamlit_player import st_player

# https://api.themoviedb.org/3/discover/movie?api_key=88cdc0cdb44a687b97e2d0bb57e5328f&with_genres=27


def fetch_poster(search):
    return "https://image.tmdb.org/t/p/w500/" + search


def fetch_video(search):
    response=requests.get('https://api.themoviedb.org/3/search/movie?api_key=88cdc0cdb44a687b97e2d0bb57e5328f&query={}&page=1&include_adult=false'.format(search))
    vote_data=response.json()
    response=requests.get('https://api.themoviedb.org/3/movie/{}/videos?api_key=88cdc0cdb44a687b97e2d0bb57e5328f&language=en-US'.format(vote_data['results'][0]['id']))
    video_data=response.json()
    return 'https://www.youtube.com/watch?v=' +video_data['results'][0]['key']

def searching (movie_search):
    obj= requests.get('https://api.themoviedb.org/3/discover/movie?api_key=88cdc0cdb44a687b97e2d0bb57e5328f&with_genres={}'.format(movie_search))
    title_list = []
    poster_list = []
    overview_list = []
    release_date_list = []
    popularity_list = []
    vote_average_list = []
    # video_list =[]

    movie_list_id = []

    lists = obj.json()
    for i in range(0,5):
        title_list.append(lists['results'][i]['title'])
        poster_list.append(fetch_poster(lists['results'][i]['poster_path']))
        # original_language_list.append(lists['results'][i]['original_language'])
        overview_list.append(lists['results'][i]['overview'])
        release_date_list.append(lists['results'][i]['release_date'])
        popularity_list.append(lists['results'][i]['popularity'])
        vote_average_list.append(lists['results'][i]['vote_average'])
        # elemet = fetch_video(lists['results'][i]['id'])
        # video_list.append(elemet)
    

    return  title_list,poster_list,overview_list, release_date_list, popularity_list, vote_average_list

