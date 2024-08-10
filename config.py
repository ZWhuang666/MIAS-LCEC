import site
import sys
import os
import json


conda_sitepackages_path = site.getsitepackages()
if conda_sitepackages_path != []:

    print("path of present site package of this conda envirtonment is ",site.getsitepackages())

    fileDirPath = os.path.abspath(os.path.dirname(__file__))

    confileJsonPath = fileDirPath + "/bin/python/config.json"
    if os.path.exists(confileJsonPath):
        print(confileJsonPath)
        with open(confileJsonPath, 'r') as file:
            fileConfig = json.load(file)
            fileConfig["path"]["ros"] = "/bin/python"
            fileConfig["path"]["conda"] = conda_sitepackages_path[0]
            fileConfig["path"]["sam"] = fileDirPath + "/bin/MobileSAM"
            print("Config file is",fileConfig)
            file.close()
            with open(confileJsonPath, 'w') as file:
                json.dump(fileConfig, file, ensure_ascii=False, indent=4)
                print("config python conda path done",fileConfig)
                file.close()
    else:
        print("config.json not found !")
else:
    print("site packages not found !")