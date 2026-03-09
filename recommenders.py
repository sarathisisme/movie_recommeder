# import std libraries
import numpy as np
import pandas as pd
import pickle


MOVIES = pd.read_csv("data/movies.csv")
RATINGS = pd.read_csv("data/user_ratings.csv")

with open('distance_recommender.pkl', 'rb') as file:
    DISTANCE_MODEL = pickle.load(file)

def get_movie_id(movie_name):
    """"""
    movie_id = MOVIES[MOVIES.title==movie_name]['movie_id'].values[0]
    return movie_id

def vectorize_user_input(user_input):
    """"""
    user_vec = np.repeat(0, MOVIES.shape[0])
    user_input = {get_movie_id(k):v for k,v in user_input.items()} 
    for k,v in user_input.items():
        user_vec[k] = v
    return user_input, user_vec

def get_neighbors(user_vec):
    """"""
    neighbor_ids = DISTANCE_MODEL.kneighbors(
        [user_vec],
        n_neighbors=10,
        return_distance=True
            )[1][0]
    return neighbor_ids

def cf_recommendations(neighbor_ids, user_input):
    """"""
    neighborhood = RATINGS[RATINGS.user_id.isin(neighbor_ids)]
    df_score = neighborhood.groupby('movie_id')[['rating']].sum()
    df_score.rename(columns={'rating': 'score'}, inplace=True)
    df_score.reset_index(inplace=True)
    df_score['score'] = df_score.apply(
        lambda x: 0 if x.movie_id in user_input else x.score,
        axis=1
        )
    df_score.sort_values(
        by='score',
        ascending=False,
        inplace=True,
        ignore_index=True
        )
    df_score = df_score.head()
    df_rec = MOVIES[MOVIES.movie_id.isin(df_score.movie_id)]
    df_rec.reset_index(drop=True, inplace=True)
    df_rec.rename(index=lambda x: x+1, inplace=True)
    return df_rec