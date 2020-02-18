import pandas as pd
import numpy as np
from flask import Flask, request, render_template, send_from_directory, after_this_request
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from joblib import load

keys = ["country","region","visitortype","referrer"]

def json_to_pd(data: list):

    try:
        columns = ['country_from_ip', 'region_from_ip',
               'visitor_rec_type', "referrer_no_parameters"]
    
        ser = pd.DataFrame(np.array([data]), columns=columns)

        return ser
    except:
        return False


def load_model(file_path: str):
    
    model = load(file_path)
    
    return model

def check_keys(received):
    
    for key in received.keys():
        if key not in keys:
            return False
        
    return True

def extract_json(request):

    country = request['country']
    region = request['region']
    visitor_type = request['visitortype']
    referrer = int(request["referrer"])
    referrer = True if referrer else False

    data = [country, region, visitor_type, referrer]

    return data

