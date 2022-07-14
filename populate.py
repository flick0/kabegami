import os

image_folders = ["art", "abstract", "irl", "minimal", "tiles"]

pre = """
# welcome to my personal wallpaper dump

## previews

<details>
<summary></summary>
"""

post = """
</details>
"""
with open("./readme.md", "w") as f:
    f.write("")

with open("./readme.md", "a") as readme:
    readme.write(pre)
    for folder in image_folders:
        readme.write("\n\n## " + folder + "\n")
        for file in os.listdir(folder):
            if file.endswith(".jpg") or file.endswith(".png"):
                readme.write(
                    "![{}](./{}/{})<br>\n".format(file[:-4], folder, file)
                )
    readme.write(post)
