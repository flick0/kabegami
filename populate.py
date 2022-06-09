import os

image_folders = ["abstract","anime_ish","irl","minimal","painted","tiles"]


with open("./readme.md", "a") as readme:
    for folder in image_folders:
        for file in os.listdir(folder): 
            if file.endswith(".jpg") or file.endswith(".png"):
                readme.write("![{}](./{}/{})<br>\n".format(file[:-4],folder,file))
        