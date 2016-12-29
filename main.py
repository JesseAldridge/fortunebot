import subprocess, urllib, time

import requests

import secrets

while True:
    channel = '#testing'
    proc = subprocess.Popen('fortune', stdout=subprocess.PIPE)
    slack_str = proc.communicate()[0]

    print 'slack_str:', slack_str

    url = (
        'https://slack.com/api/chat.postMessage?token={}'
        '&channel={}&text={}&pretty=1').format(
        secrets.slack_api_key, urllib.quote(channel), urllib.quote(slack_str))
    print 'url:', url
    requests.post(url)
    time.sleep(60 * 60 * 24)
