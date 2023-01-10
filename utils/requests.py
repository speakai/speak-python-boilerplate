import requests
import logging
logger = logging.getLogger('speakLogger')

def get_request(url):
    response = requests.get(url)
    return response

def post_request(url, result):
    response = requests.post(url, json = result)
    logger.info('Post request sent successfully.',  extra = { 'response' : response })    
