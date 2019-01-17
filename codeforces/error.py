"""All exceptions used in codeforces."""

__all__ = ['CodeforcesAPIError']


class CodeforcesAPIError(Exception):
    """Raised by api.call if method returns a error or is not found."""

    def __init__(self, comment, method, args):
        self.comment = comment
        self.method = method
        self.method_args = args

        super(CodeforcesAPIError, self).__init__(comment)
