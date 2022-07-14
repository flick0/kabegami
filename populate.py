import os

image_folders = ["art", "abstract", "irl", "minimal", "tiles"]


with open("./readme.md", "a") as readme:
    for folder in image_folders:
        readme.write("\n\n## " + folder + "\n")
        for file in os.listdir(folder):
            if file.endswith(".jpg") or file.endswith(".png"):
                readme.write(
                    "![{}](./{}/{})<br>\n".format(file[:-4], folder, file)
                )
