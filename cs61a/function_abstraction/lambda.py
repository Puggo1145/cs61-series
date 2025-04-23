a = 1
def f(g):
    a = 2
    return lambda y: a + g(y)

f(lambda y: a + y)(a)

# Global
    # a: 1
    # f: f(g)
# f1 <f>(g) [parent=Global]
    # g: <lambda1 y: a + y> [parent=Global]
    # local.a: 2
    # return value: <lambda2 y: 2 + g(y)> [parent=f1]
# f2 <lambda2>(y) [parent=f1]
    # y: 1
    # g(y): f3 <lambda1>(y) [parent=Global]
        # y: 1
        # Global.a = 1
        # return value: 2
    # return value: 4
