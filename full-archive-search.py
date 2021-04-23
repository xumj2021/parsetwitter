import requests
import os
import json
import csv
import time

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = "xxx"

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
def setpara(firm,start_time,end_time):
    query_params = {'start_time': "%s"%start_time, 'end_time':"%s"%end_time,
    'query': "%s"%firm, 'tweet.fields': "created_at,public_metrics",'max_results': 10}
    return(query_params)

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers,params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def updatepara(oldpara, next_token):
    newpara = {**oldpara,**{'next_token':next_token}}
    return(newpara)

def csvjson(firm, start_time, end_time, json_response):
    with open("/Users/mengjiexu/Documents/TwitterParsing/%s_%s_%s.csv"%(firm, start_time,end_time),'a') as f:
        w = csv.writer(f)
        tweets = json_response['data']
        for tw in tweets:
            created_at = tw['created_at']
            list = [tw['created_at'], tw['id'],tw['text'],tw['public_metrics']['retweet_count'],tw['public_metrics']['reply_count'], tw['public_metrics']['like_count']]
            w.writerow(list)

    meta = json_response['meta']
    try:
        next_token = meta['next_token']
    except:
        next_token = False
    return(next_token)

def dealjson(firm, start_time, end_time, json_response):
    headers = create_headers(bearer_token)
    next_token = csvjson(firm, start_time, end_time, json_response)
    
    while next_token:
        newpara = updatepara(setpara(firm,start_time,end_time), next_token)
        time.sleep(2)
        json_response = connect_to_endpoint(search_url, headers, newpara)
        next_token = csvjson(firm, start_time, end_time, json_response)
        print(next_token)

def mainparse(firm,start_time,end_time):
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, setpara(firm,start_time,end_time))
    dealjson(firm, start_time, end_time, json_response)

    #print(json.dumps(json_response, indent=4, sort_keys=True))
mainparse('$AAPL','2013-01-01T15:00:00Z','2013-01-01T16:00:00Z')

