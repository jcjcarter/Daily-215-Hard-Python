fmt = "{0!r:>{width}} {1}".format

m = 0

vs = [None]

for n, k in sorted(vars(__build_class__).items()):
    if not isinstance(k,type):
        # not interested
        continue

    try:
        b = k()
    except (TypeError, RuntimeError):
        continue

    if b:
        continue

    vs.append(b)

    for a in [("123",), (b"1",), (("ab",),)]:
        try:
            v = k(*a)
        except (TypeError, ValueError):
            continue
        vs.append(v)
        m = max(m,len(repre(v)))
        break

for v in vs:
    print(fmt(v, not not v, width = m))