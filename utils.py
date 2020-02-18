import numpy as np
import pandas as pd
from joblib import load

keys = ["country","region","visitortype","referrer"]


def json_to_pd(data: list):

    """
    Takes a list of features for the model and creates a pandas Series that fits the model
    :param data: list of features extracted with extract_json()
    :return: Pandas Series
    """

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

    """
    Checks whether the keys in the dictionary from the json POST request are correct
    :param received: dictionary from the json POST request
    :return: boolean
    """

    for key in received.keys():
        if key not in keys:
            return False
        
    return True


def extract_json(request):
    """
    Takes the dictionary from a json POST request and returns a list of the features needed by the model
    :param request: dictionary from json POST request
    :return: list of features
    """
    try:
        country = request['country']
        region = request['region']
        visitor_type = request['visitortype']
        referrer = int(request["referrer"])
        referrer = True if referrer else False

        data = [country, region, visitor_type, referrer]

        return data

    except:
        return False

