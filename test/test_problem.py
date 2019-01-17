import codeforces
import pytest


class TestGetInfo(object):
    def test_normal_problem(self):
        contest_id = 1
        index = 'A'

        title, time_limit, memory_limit, sample_tests = codeforces.problem.get_info(contest_id, index)

        assert(title == 'A. Theatre Square')
        assert(time_limit == '1 second')
        assert(memory_limit == '256 megabytes')
        assert(list(sample_tests) == [('6 6 4', '4')])
