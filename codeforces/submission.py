import json

import requests
from bs4 import BeautifulSoup


def get_submission(submission_id):
    """Get source code associated with a submission_id

    Parameters
    ----------
    submission_id: int
        Id of the submission.
        For example: /contest/1113/submission/**50046519**

    Returns
    -------
    source code of the submission
    """
    with requests.Session() as sess:
        sess.headers.update({'User-Agent': 'python-codeforces/0.1.0'})

        res = sess.get('https://codeforces.com')
        soup = BeautifulSoup(res.text, 'html.parser')

        csrf_token = soup.find('meta', attrs={'name': 'X-Csrf-Token'})['content']

        res = sess.post(
            'https://codeforces.com/data/submitSource',
            {'submissionId': submission_id, 'csrf_token': csrf_token},
            headers={'X-Csrf-Token': csrf_token}
        )

    return json.loads(res.text)['source']
