from email.mime import image
import os

image_folders = ["art", "abstract", "irl", "minimal", "tiles","animated"]
image_folders.sort()
print(image_folders)

pre = """
# welcome to my personal wallpaper dump

## previews
<hr>
"""

post = """
"""
with open("./readme.md", "w") as f:
    f.write("")

with open("./readme.md", "a") as readme:
    readme.write(pre)
    for folder in image_folders:
        readme.write("\n\n## " + folder + "\n")
        readme.write("<details><summary></summary>\n")
        for file in os.listdir(folder):
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".webp") or file.endswith(".webm"):
                readme.write(
                    "![{}](./{}/{})<br>\n".format(file[:-4], folder, file)
                )
        readme.write("</details>\n")
    readme.write(post)
