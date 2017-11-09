import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from tqdm import tqdm

import pickle
from scipy.sparse import *

import get_raintg_X


def get_X():
    data_path = '../data/'
    train = pd.read_csv(data_path + 'train.csv')
    test = pd.read_csv(data_path + 'test.csv')
    
    X = train.drop(['source_system_tab', 'source_screen_name', 'source_type'],\
               axis=1)
    Y = train['target'].values
    X_test = test.drop(['id','source_system_tab',\
                        'source_screen_name', 'source_type'], axis=1)
    
    data = pd.concat([X, X_test], axis=0)
    data.msno = pd.Categorical(data.msno)
    data.msno = data.msno.cat.codes
    data.song_id = pd.Categorical(data.song_id)
    data.song_id = data.song_id.cat.codes
    
    num_songs = len(data.song_id.unique())
    num_users = len(data.msno.unique()) 
    
    pos_X = data[data.target == 1]
    
    
    
    row = pos_X.msno
    col = pos_X.song_id 
    content = np.ones(len(pos_X))
    return csc_matrix((content, (row, col)), \
                   shape=(num_users, num_songs)).toarray()
