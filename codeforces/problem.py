"""Functions to info about a problem."""
import urllib.parse

import requests
from bs4 import BeautifulSoup

__all__ = ['get_info']

CODEFORCES_URL = "https://codeforces.com"


def get_info(contest_id, index, gym=False, lang='en'):
    """
    Get info for a contest problem.

    Parameters
    ----------
    contest_id: int
        Id of the contest. It is not the round number. It can be seen in
        contest URL. For example: /contest/**566**/status
    index: str
        Usually a letter of a letter, followed by a digit, that
        represent a problem index in a contest. It can be seen in
        problem URL. For example: /contest/566/**A**
    gym: bool
        If true gym problem is returned otherwise regular problem is
        returned.

    Returns
    -------
    title: str
        Title of the problem.
    time_limit: str
        Time limit specification for the problem.
    memory_limit: str
        Memory limit specification for the problem.
    sample_tests: zip
        Sample tests given for the problem.

    """
    if gym:
        problem_url = urllib.parse.urljoin(CODEFORCES_URL, "gym/%d/problem/%s" % (contest_id, index))
    else:
        problem_url = urllib.parse.urljoin(CODEFORCES_URL, "contest/%d/problem/%s" % (contest_id, index))

    with requests.get(problem_url, params={'lang': lang}) as res:
        soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.find_all("div", class_="title")[0].text

    time_limit = soup.find_all("div", class_="time-limit")[0].text[19:]
    memory_limit = soup.find_all("div", class_="memory-limit")[0].text[21:]

    inputs = [i.pre.get_text('\n').lstrip('\n') for i in soup.find_all("div", class_="input")]

    outputs = [i.pre.get_text('\n').lstrip('\n') for i in soup.find_all("div", class_="output")]

    sample_tests = zip(inputs, outputs)

    return (title, time_limit, memory_limit, sample_tests)
