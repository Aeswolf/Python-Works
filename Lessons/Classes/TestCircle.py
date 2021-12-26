import Circle


class TestCircle(Circle.Circle):
    pass


test = TestCircle(0, 3, 10)
test.__str__()
