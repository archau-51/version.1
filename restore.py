import sys
import os
import shutil
import glob
import json
name = sys.argv[1]
ver = sys.argv[2]
try:
    os.remove("../{}".format(name))
except:
    pass
shutil.copyfile("./versions/{}/{}".format(ver,name), "../{}".format(name))
folders = glob.glob("versions/*")
folders.remove("versions/versions.json")
folders = sorted(folders)
idx = folders.index("versions/{}".format(ver))
folders = folders[idx+1:]
print(folders)
for folder in folders:
    try:
        os.remove("{}/{}".format(folder,name))
        with open("./versions/versions.json") as f:
            jsoon = f.read()
        json_obj = json.loads(jsoon)
        del json_obj[folder[9:]][name]
        if json_obj[folder[9:]] == {}:
            del json_obj[folder[9:]]
            os.rmdir("versions/{}".format(folder[9:]))
        os.remove("./versions/versions.json")
        json_object = json.dumps(json_obj, indent=4)
        with open("./versions/versions.json", "w") as outfile:
             outfile.write(json_object)
    except:
        pass