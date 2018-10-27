__all__ = ['CodeforcesAPIError']

class CodeforcesAPIError(Exception):
    def __init__(self, comment, method, args):
        self.comment = comment
        self.method = method
        self.method_args = args

        super(CodeforcesAPIError, self).__init__(comment)
