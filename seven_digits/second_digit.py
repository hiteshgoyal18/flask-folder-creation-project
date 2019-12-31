class Eiffel:

    def roi(self):
        return 10


class Tower(Eiffel):

    def roi(self):
        return super().roi()
        # return 11


et = Tower()
print(et.roi())
