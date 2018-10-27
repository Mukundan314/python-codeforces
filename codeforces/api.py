import time
import os
import json
import random
import hashlib
import urllib.request
import urllib.error
import urllib.parse
from . import error


__all__ = ['call']


CODEFORCES_API_URL = "https://codeforces.com/api/"


def __generate_api_sig(method, args, secret):
    rand = "%06d" % random.randint(0, 999999)
    url_args = urllib.parse.urlencode(sorted(args.items()))
    return rand + hashlib.sha512(
        ("%s/%s?%s#%s" % (rand, method, url_args, secret)).encode('utf-8')
    ).hexdigest()


def call(method, key=None, secret=None, **kargs):
    """call a Codeforces API method"""
    args = kargs.copy()

    if (key is not None) and (secret is not None):
        args['time'] = int(time.time())
        args['apiKey'] = key
        args['apiSig'] = __generate_api_sig(method, args, secret)

    url_args = urllib.parse.urlencode(args)
    url = os.path.join(CODEFORCES_API_URL, "%s?%s" % (method, url_args))

    try:
        with urllib.request.urlopen(url) as res:
            data = json.loads(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        if err.code == 400:
            data = json.loads(err.read())
        elif err.code == 404:
            data = {'status': 'FAILED', 'comment': "%s: No such method" % method}
        elif (err.code in (429, 503)):
            time.sleep(1)
            return call(method, key, secret, **kargs)
        else:
            raise

    if data['status'] == 'FAILED':
        raise error.CodeforcesAPIError(data['comment'], method, kargs)

    return data['result']
