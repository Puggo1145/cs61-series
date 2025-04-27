# yield from delegate part of a generator's operation to another generator
# it automatically yields elements in a iterator/generator

def countdown(count: int):
    if count > 0:
        yield count
        yield from countdown(count - 1)
    else:
        yield "Balst"


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


def substring(s):
    if s:
        yield from prefixes(s)
        yield from substring(s[1:])

# substring("top")
# s: top
# prefixes: [t, to, top]
#   s: op
#   prefixes: [o, op]
#       s: p
#       prefixes: p
# combined: [t, to, top, o, op, p]


def subfixes(s):
    if s:
        yield from subfixes(s[1:])
        yield s

