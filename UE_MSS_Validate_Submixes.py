import unreal
import time

print ("Script started!")

pathWorkingDirectory = "C:/Users/user_name/Desktop/PythonResults/"
pathsAllRaw = unreal.EditorAssetLibrary.list_assets("/content_directory/sub_directory/Audio/")
pathsAll = []
pathsMSS = []
pathsMSSEmptySubmixes = []

# function to get object from its path
def ObjectFromPath(path):
    assetData = unreal.EditorAssetLibrary.find_asset_data(path)
    object = unreal.AssetData.get_asset(assetData)
    return object

# remove the not needed extension from the asset paths
for path in pathsAllRaw:
    indexFirst = path.find(".")
    pathsAll.append(path[0:indexFirst])

# find only MSS assets
for path in pathsAll:
    if type(ObjectFromPath(path)) == unreal.MetaSoundSource:
        pathsMSS.append(path)

# find only MSS without any submixes
for path in pathsMSS:
    if len(ObjectFromPath(path).sound_submix_sends) == 0:
        pathsMSSEmptySubmixes.append(path)

# save the list of assets into file
if len(pathsMSSEmptySubmixes) != 0 :
    fileResult = open(pathWorkingDirectory + 'MSSEmptySubmixes_' + time.strftime('%y%m%d') + '.csv', 'w')
    pathsMSSEmptySubmixes = sorted(list(set(pathsMSSEmptySubmixes)))
    for line in pathsMSSEmptySubmixes:
        fileResult.write(line+'\n')
    fileResult.close()
    print("There was ", len(pathsMSSEmptySubmixes), "MSS assets without any submixes connected to them")
    print("All of them was stored in a file on your desktop")
else :
    print("All MSS have some submixes assigned to them")

print ("Script finished!")
