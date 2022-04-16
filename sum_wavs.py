import os
from pydub import AudioSegment

print(">>> SCRIPT STARTED")

os.chdir("Name of working directory")
directoryToScan = os.getcwd()

#get the list of all files and files that ends with -R1.wav
fileListR1 = [] #filenames with R1 in the end but this ending will be removed
fileListAll = [] #all filenames
for root, dirs, files in os.walk(directoryToScan):
    for fileName in files:
        fileListAll.append(fileName)
        if fileName.endswith("-R1.wav"):
            index = fileName.find('1.wav')
            fileName = fileName[:index]
            fileListR1.append(fileName)

silence = AudioSegment.silent(duration = 100)

for fileNameR1 in fileListR1:
    combined = AudioSegment.silent(duration=0)
    print ("fileNameR1 = " + fileNameR1)
    for fileNameAll in fileListAll:
        if (fileNameAll.find(fileNameR1) == 0):
            print ("fileNameAll = " + fileNameAll)
            combined = combined + AudioSegment.from_file(fileNameAll, format="wav") + silence
    combined.export(fileNameR1 + "_combined.wav")
    print (fileNameR1 + " exported")

print(">>> SCRIPT DONE!")
