#!/usr/bin/env python

import attrdict
import traceback
import json

j = json.loads('{"a": 1, "b": "blat", "c": {"d": "e"}}')
ad = attrdict.AttrDict(j)

print(ad.c.d)
print(repr(ad.foo.bar))
ad.foo.bar = "hello"
ad.foo.bar += ", world"
ad.foo.baz = "yaarrrr"
print(+ad.foo)
print(+ad)
try:
    print(+ad.c.x.y.z)
except KeyError as e:
    traceback.print_exc()
ad.c.x.y.z = 3
del ad.foo.bar
print(+ad)
del ad.foo
print(+ad)
print("****")
try:
    del ad.bar.baz
except KeyError as e:
    traceback.print_exc()
print(+ad is j)
print(sorted(ad.c.x))
for a in ad.c.x:
    q = ad.c.x[a]
    print("  ad.c.x.%s == (%s) %s" % (a, type(q), str(q)))

print("%s, %s" % (type(ad), type(ad).__name__))

print("SUCCESS")
