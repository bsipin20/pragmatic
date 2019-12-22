import yaml
import os

# Set the directory you want to start from
rootDir = 'yaml_files'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        file_ = rootDir + "/" + fname
        with open(file_,"r") as fh:
            data = yaml.load(fh, Loader=yaml.FullLoader)
            print(data)

