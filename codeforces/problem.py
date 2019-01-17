import os
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

__all__ = ['get_info']

CODEFORCES_URL = "https://codeforces.com"


def get_info(contest_id, index, lang='en'):
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

    problem_url = os.path.join(
        CODEFORCES_URL,
        "contest/%d/problem/%s?lang=%s" % (contest_id, index, lang)
    )

    with urllib.request.urlopen(problem_url) as res:
        soup = BeautifulSoup(res.read(), 'html.parser')

    title = soup.find_all("div", class_="title")[0].text

    time_limit = soup.find_all("div", class_="time-limit")[0].text[19:]
    memory_limit = soup.find_all("div", class_="memory-limit")[0].text[21:]

    i = [i.pre.text.lstrip('\n') for i in soup.find_all("div", class_="input")]
    o = [i.pre.text.lstrip('\n') for i in soup.find_all("div", class_="output")]

    sample_tests = zip(i, o)

    return (title, time_limit, memory_limit, sample_tests)
