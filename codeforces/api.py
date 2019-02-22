"""Functions to call the codeforces api."""
import hashlib
import json
import os
import secrets
import time
import urllib.parse

import requests

from . import error

__all__ = ['call']


CODEFORCES_API_URL = "https://codeforces.com/api/"


def _generate_api_sig(method, args, secret):
    rand = "%06d" % secrets.randbelow(999999)
    url_args = urllib.parse.urlencode(sorted(args.items()))
    return rand + hashlib.sha512(
        ("%s/%s?%s#%s" % (rand, method, url_args, secret)).encode('utf-8')
    ).hexdigest()


def call(method, key=None, secret=None, **kwargs):
    """
    Call a Codeforces API method.

    Parameters
    ----------
    method: str
        Name of method to call, list of all methods can be found at
        https://codeforces.com/api/help.
    key: str, optional
        Your api key (needed for authorized calls)
    secret: str, optional
        Secret for your api key.
    **kwargs
        Arguments for the api call

    Returns
    -------
    any
        A python object containing the results of the api call.

    """
    params = kwargs.copy()

    if (key is not None) and (secret is not None):
        params['time'] = int(time.time())
        params['apiKey'] = key
        params['apiSig'] = _generate_api_sig(method, params, secret)

    url = os.path.join(CODEFORCES_API_URL, "%s" % method)

    with requests.get(url, params=params) as res:
        if res.status_code == 404:
            data = {
                'status': 'FAILED',
                'comment': "%s: No such method" % method
            }
        elif res.status_code in (429, 503):
            time.sleep(1)
            return call(method, key, secret, **kwargs)
        else:
            data = json.loads(res.text)

    if data['status'] == 'FAILED':
        raise error.CodeforcesAPIError(data['comment'], method, kwargs)

    return data['result']
