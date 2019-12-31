class Err(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise(Err(3*2))
except Err as e:
    print(e.value)
