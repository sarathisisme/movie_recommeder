# import std libraries
from IPython.display import HTML
import json
import streamlit as st
from recommenders import *

TITLES = ["-"] + list(MOVIES['title'].sort_values()) 


# sidebar
with st.sidebar:
    # title
    st.title("It's movie time!")
    # image
    st.image('images/movie_time.jpg')
    # blank space
    st.write("")
    # selectbox
    page = st.selectbox(
        "what would you like?",
        [
            "welcome page",
            "popular movies",
            "rate some movies",
            "recommended movies"
            ]
        ) 

##########################################################
# Welcome Page
##########################################################

if page == "welcome page":
    # slogan
    st.write("""
    *Movies are like magic tricks (Jeff Bridges)*
    """)
    # blank space
    st.write("")
    # image
    st.image('images/movie_pics.png')

##########################################################
# Popular Movies
##########################################################

elif page == "popular movies":
    # title
    st.title("Popular Movies")
    st.markdown("")
    col1,col2,col3,col4 = st.columns([10,1,5,5])
    with col1:
        n = st.slider(
        label="how many movies?",
        min_value=1,
        max_value=10,
        value=5
        ) 
    with col3:
        st.markdown("")
        st.markdown("")
        genre = st.checkbox("include genres")
    with col4:
        st.markdown("")
        show_button = st.button(label="show movies") 
    
    movies = MOVIES.rename(index=lambda x: x+1)
    if genre:
        popular_movies = movies[['movie','genres']]
    else:
        popular_movies = movies[['movie']]

    st.markdown("###")
    if show_button:
        st.write(
            HTML(popular_movies.head(n).to_html(escape=False)),
            unsafe_allow_html = True
            )

##########################################################
# Rate Movies
##########################################################

elif page == "rate some movies":
    # title
    st.title("Rate Movies")
    #
    col1,col2,col3 = st.columns([10,1,5])
    with col1:
        m1 = st.selectbox("movie 1", TITLES)
        st.write("")
        m2 = st.selectbox("movie 2", TITLES)
        st.write("")
        m3 = st.selectbox("movie 3", TITLES)
        st.write("")
        m4 = st.selectbox("movie 4", TITLES)
        st.write("")
        m5 = st.selectbox("movie 5", TITLES) 
    
    with col3:
        r1 = st.slider(
            label="rating 1",
            min_value=1,
            max_value=5,
            value=3
            ) 
        st.write("")
        r2 = st.slider(
            label="rating 2",
            min_value=1,
            max_value=5,
            value=3
            ) 
        st.write("")
        r3 = st.slider(
            label="rating 3",
            min_value=1,
            max_value=5,
            value=3
            ) 
        st.write("")
        r4 = st.slider(
            label="rating 4",
            min_value=1,
            max_value=5,
            value=3
            ) 
        st.write("")
        r5 = st.slider(
            label="rating 5",
            min_value=1,
            max_value=5,
            value=3
            ) 

    query_movies = [m1,m2,m3,m4,m5]
    query_ratings = [r1,r2,r3,r4,r5]
    
    user_query = dict(zip(query_movies,query_ratings))

    # get user query
    st.markdown("")
    user_query_button = st.button(label="save user query") 
    if user_query_button:
        json.dump(
            user_query,
            open("user_query.json",'w')
            )
        st.write("")
        st.write("user query saved successfully")

##########################################################
# Movie Recommendations
##########################################################
else:
    # title
    st.title("Movie Recommendations")
    col1,col2,col3,col4,col5 = st.columns([1,5,1,5,1])
    with col2:
        recommender = st.radio(
            "recommender type",
            ["NMF Recommender","Distance Recommender"]
            )
    with col4:
        st.write("")
        st.write("")
        recommend_button = st.button(label="recommend movies")

    #load user input
    user_input = json.load(open("user_query.json"))
    
    user_input, user_vec = vectorize_user_input(user_input)
    neighbor_ids = get_neighbors(user_vec)
    df_rec = cf_recommendations(neighbor_ids, user_input)

    st.markdown('###')
    if recommend_button:
        st.write(
            HTML(df_rec[['movie','genres']].head().to_html(escape=False)),
            unsafe_allow_html = True
            )
    
    