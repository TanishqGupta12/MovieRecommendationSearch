import streamlit as st
import pandas as pd
from streamlit_player import st_player
from api import   movie_list
from search import searching

st.markdown("""
                    <style>
                    .id {
                        font-size:20px; 
                        }  
                    </style>
            """, unsafe_allow_html=True)

genre_list = pd.read_csv('data\list.csv')
datas = pd.read_csv('data\datafiles.csv' , encoding = "ISO-8859-1")
option=['Introduction' , 'Excution'] 
def Introduction() :
    st.title('INTRODUCTION PROJECT ')
    st.subheader('MOVIE RECOMMENDER SYSTEM')

    st.markdown('<p class="id">A movie recommendation system, or a movie recommender system, is an ML-based approach to filtering or predicting the users film preferences based on their past choices and behavior.</p>' , unsafe_allow_html=True)

    st.subheader('MOVIE SEARCH ENGINE')
    
    obj= st.markdown('<p class="id">MovieSearch is a content speciﬁc search engine with the aim to retrieve movie information given the contents of a users query.</p>' , unsafe_allow_html=True)

    option = st.selectbox(
     obj,
    ('Email', 'Home phone', 'Mobile phone'))

    if(option == "Email"):
        st.write('You selected:', option)

    
sidebar = st.sidebar
sidebar.title('User Options')
seloption = sidebar.selectbox( 'Select an Option', option)
 
def Excution():

    options=['MOVIE RECOMMENDER SYSTEM' , 'MOVIE SEARCH ENGINE']  
    def recommended():
        st.title('MOVIE RECOMMENDER SYSTEM')
        selected_movie_name = st.selectbox('how wolud you like to be contacted?' ,(datas['title'].values))

        if st.button('RECOMMAND'):
            data ,poster , genress , original_language ,overview  , release_date , status , vote_average , Video  = movie_list(selected_movie_name)
            tab1, tab2 = st.tabs(["RECOMMENDBER", "ABOUT"])
            st.markdown("""
                    <style>
                    .big {
                        font-size:30px; 
                        }  
                    </style>
            """, unsafe_allow_html=True)

            with tab1 :
                    for n in range(0,10):

                        st.header(data[n])
                        st.image(poster[n] , width=250)
                        st.write('--------------------------------------------------------')       
  
            with tab2:
     
                    st.header(data[0])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write( genress [0])
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[0])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[0] )
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[0] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[0] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[0] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[0])

                    st.write('------------------------------------------------------------------------------------')

                    st.header(data[1])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write(genress[1] )
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[1])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[1] )
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[1] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[1] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[1] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[1])
                    
                    st.write('------------------------------------------------------------------------------------')
                    
                    st.header(data[2])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)    
                    st.write( genress[2] )
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[2])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[2] )
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[2] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[2] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[2] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[2])

                    st.write('------------------------------------------------------------------------------------')
                    
                    st.header(data[3])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)    
                    st.write(genress[3] )
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[3])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[3])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[3] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[3] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[3] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[3])

                    st.write('------------------------------------------------------------------------------------')

                    st.header(data[4])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)   
                    st.write( genress[4] )
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[4])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[4])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[4] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[4] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[4] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[4])

                    st.write('------------------------------------------------------------------------------------')

                    st.header(data[5])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write(genress[5])
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[5])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[5])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[5] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[5] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[5] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[5])
                   
                    st.write('------------------------------------------------------------------------------------')

                    st.header(data[6])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write(genress[6])
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[6])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[6])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[6] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[6] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[6] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[6])

                    st.write('------------------------------------------------------------------------------------')

                    st.header(data[7])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write('genress -' ,genress[7])
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[7])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write( overview[7])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[7] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[7] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[7] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[7])

                    st.write('------------------------------------------------------------------------------------')

                    st.header(data[8])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write(genress[8])
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[8])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.write(overview[8])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[8] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[8])
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[8] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[8])
                   
                    st.write('------------------------------------------------------------------------------------')
                    
                    st.header(data[9])
                    st.markdown('<p class="big">Genres</p>', unsafe_allow_html=True)
                    st.write(genress[9])
                    st.markdown('<p class="big">Original Language</p>', unsafe_allow_html=True)
                    st.write(original_language[9])
                    st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
                    st.markdown(overview[9])
                    st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
                    st.write(release_date[9] )
                    st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
                    st.write(status[9] )
                    st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
                    st.write(vote_average[9] )
                    st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
                    st_player(Video[9])

                    st.write('------------------------------------------------------------------------------------')

    seloptions = sidebar.selectbox( 'Select an Option', options)
    def search():
        st.title('MOVIE SEARCH ENGINE')

        st.markdown("""
                    <style>
                    .big {
                        font-size:30px; 
                        }  
                    </style>
            """, unsafe_allow_html=True)

        gener_id = st.selectbox('how wolud you like to be contacted?' ,(genre_list['genre_name'].values))
        for index ,items in genre_list.iterrows():
            if items['genre_name'] == gener_id:
                    title ,poster ,overview  , release_date , status , vote_average  = searching(items['genre_id'])

        for i in range(0,5):
            st.header(title[i])
            st.image(poster[i] , width=250)
            st.markdown('<p class="big">Overview</p>', unsafe_allow_html=True)
            st.write(overview[i])
            st.markdown('<p class="big">Release Date</p>', unsafe_allow_html=True)
            st.write(release_date[i])
            st.markdown('<p class="big">Status</p>', unsafe_allow_html=True)
            st.write(status[i])
            st.markdown('<p class="big">Vote Average</p>', unsafe_allow_html=True)
            st.write(vote_average[i])
            # st.markdown('<p class="big">Video</p>', unsafe_allow_html=True)
            # st_player(video[i])

    if seloptions == options[0] :
        recommended()
    elif seloptions == options[1]:
        search()

                    
if seloption == option[0] :
    Introduction()
elif seloption == option[1]:
    Excution()