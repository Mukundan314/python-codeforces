"""Functions to call the codeforces api."""
import hashlib
import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request

from . import error

__all__ = ['call']


CODEFORCES_API_URL = "https://codeforces.com/api/"


def _generate_api_sig(method, args, secret):
    rand = "%06d" % random.randint(0, 999999)
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
    args = kwargs.copy()

    if (key is not None) and (secret is not None):
        args['time'] = int(time.time())
        args['apiKey'] = key
        args['apiSig'] = _generate_api_sig(method, args, secret)

    url_args = urllib.parse.urlencode(args)
    url = os.path.join(CODEFORCES_API_URL, "%s?%s" % (method, url_args))

    try:
        with urllib.request.urlopen(url) as res:
            data = json.loads(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        if err.code == 400:
            data = json.loads(err.read())
        elif err.code == 404:
            data = {
                'status': 'FAILED',
                'comment': "%s: No such method" % method
            }
        elif err.code in (429, 503):
            time.sleep(1)
            return call(method, key, secret, **kwargs)
        else:
            raise

    if data['status'] == 'FAILED':
        raise error.CodeforcesAPIError(data['comment'], method, kwargs)

    return data['result']
