'''
Obtain some data from some API. 
Put the data into a dataframe.
Then, filter out unwanted data.
Finally, create a chart with the data.

Problem with the API example: there could be a limit on requests
'''

import requests 
import matplotlib.pyplot as plt


API_KEY = 'FCR4SVK07P3TOC7D'
DEMO_API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

def fetch_data(url):
    # replace the string 'demo' in url with API_KEY
    url = url.replace('demo', API_KEY)
    # send a request to the url 
    '''
    this prompt failed because none of the snippets worked, so I had to look online how to send a request to the target url
    Oh! The issue was a missing `requests` module import
    '''

    # fetch the data from the API
    response = requests.get(url)
    # convert the response to json
    # data = response.json()['Time Series (5min)']
    # a = response.json()
    data = list(response.json()['Time Series (5min)'].items())[:10]
    ''' 
    modified the line above 
    '''
    # the 'high' values of the data points
    highs = [float(point[1]['2. high']) for point in data] 
    # get the time portion of the timestamps from data
    times = [point[0].split(' ')[1] for point in data]

    return times, highs


def plot(ts, highs):
    # plot ts (x) and highs (y)
    plt.plot(ts, highs)
    # plt.show()


def main():
    ts, highs = fetch_data(DEMO_API_URL)
    plot(ts, highs)
    pass

main() 