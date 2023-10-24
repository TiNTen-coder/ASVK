def travel(n):
    for i in range(n):
        yield "по кочкам"

    return "и в яму"

def travelwrap(n):
    s = yield from travel(n)
    yield s

print(list(travelwrap(10)))
