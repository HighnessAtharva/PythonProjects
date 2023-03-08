class OddContainer:
    def __contains__(self, x):
        return bool(isinstance(x, int) and x % 2)
