from difflib import Differ
import sys
name = sys.argv[1]
fv = sys.argv[2]
mode = "line"
try:
    if sys.argv[4] == "c":
        mode = "char"
except:
    pass
if mode == "line":
    with open("versions/{}/{}".format(fv,name)) as f:
        v1 = f.readlines()
    with open("../{}".format(name)) as f:
        v2 = f.readlines()
else:
    with open("versions/{}/{}".format(fv,name)) as f:
        v1 = f.read()
    with open("../{}".format(name)) as f:
        v2 = f.read()
d = Differ()
difference = list(d.compare(v1, v2))
difference = '\n'.join(difference)
print(difference)