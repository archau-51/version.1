import glob as g
import shutil
import os
import json
import itertools


def increment_version(current_version: str) -> str:
    spl = int("".join(current_version.split(".")))
    spl += 1
    spl = [*str(spl)]
    if len(spl) == 1:
        spl.append([0, 0])
        spl = list(itertools.chain(*spl))
        spl = spl[::-1]
        return (str(spl))
    elif len(spl) == 2:
        spl = [[0, spl]]
        spl = list(itertools.chain(*spl))
        return (str(spl))
    else:
        return (str(spl))


def verinc(current_version) -> str:
    ver = increment_version(current_version)
    ver = str(ver.replace("[", ""))
    ver = str(ver.replace("]", ""))
    ver = str(ver.replace("'", ""))
    ver = str(ver.replace(" ", ""))
    ver = str(ver.replace(",", "."))
    return ver


files = g.glob('../*.*')
for file in files:
    sfiles = g.glob('versions/*/*.*')
    lfiles = []
    for file2 in sfiles:
        lfiles.append(file2.split("/")[-1])
    if file[3:] not in lfiles:
        print("Adding {} to versioning".format(file))
        if not os.path.exists("./versions/0.0.1/"):
            os.mkdir('./versions/0.0.1')
        shutil.copyfile(file, "./versions/0.0.1/{}".format(file[3:]))
        with open('./versions/versions.json') as f:
            lmao = f.read()
        ver = json.loads(lmao)
        with open(file) as f:
            try:
                ver["0.0.1"] = ver["0.0.1"]
            except:
                ver["0.0.1"] = dict({})
            finally:
                ver["0.0.1"][file[3:]] = f.readlines()
                os.remove("./versions/versions.json")
                json_object = json.dumps(ver, indent=4)
                with open("./versions/versions.json", "w") as outfile:
                    outfile.write(json_object)
    else:
        foldernum = 0
        foldercopy = foldernum
        for folder in g.glob("./versions/*"):
            for item in g.glob("{}/*.*".format(folder)):
                if file[3:] == item.split("/")[-1]:
                    foldernum += 1
        with open(file) as f:
            comp1 = f.read()
        flist = g.glob("./versions/*")
        flist.remove("./versions/versions.json")
        flist_names = []
        for fld in flist:
            flist_names.append(fld[11:])
        print(flist_names[foldernum-1])
        flist = sorted(flist)
        flist_names = sorted(flist_names)
        with open("{}/{}".format(flist[foldernum-1], file[3:])) as f:
            comp2 = f.read()
        if comp1 != comp2:
            print("{} is different".format(file[3:]))
            print(sorted(flist))
            if not os.path.exists("./versions/{}/".format(verinc(flist_names[foldernum-1]))):
                os.mkdir(
                    './versions/{}'.format(verinc(flist_names[foldernum-1])))
            shutil.copyfile(
                file, "./versions/{}/{}".format(verinc(flist_names[foldernum-1]), file[3:]))
            with open('./versions/versions.json') as f:
                lmao = f.read()
            ver = json.loads(lmao)
            with open(file) as f:
                try:
                    ver[verinc(flist_names[foldernum-1])
                        ] = ver[verinc(flist_names[foldernum-1])]
                except:
                    ver[verinc(flist_names[foldernum-1])] = dict({})
                finally:
                    ver[verinc(flist_names[foldernum-1])
                        ][file[3:]] = f.readlines()
                    os.remove("./versions/versions.json")
                    json_object = json.dumps(ver, indent=4)
                    with open("./versions/versions.json", "w") as outfile:
                        outfile.write(json_object)
