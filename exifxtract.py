from PIL import Image
from PIL.ExifTags import TAGS
import urllib.request
import random

def banner():
  print("""\033[0;31m
█▀▀ ▀▄▀ █ █▀▀ ▀▄▀ ▀█▀ █▀█ ▄▀█ █▀▀ ▀█▀
██▄ █░█ █ █▀░ █░█ ░█░ █▀▄ █▀█ █▄▄ ░█░\n""")

banner()

path_type = input("Image URL(Enter 1) or Image Path(Enter 2)\n>")

if path_type == "1":
  url = input("Enter Image URL\n>")
  print("\n")
  try:
    name = random.randint(0,100)
    urllib.request.urlretrieve(url, str(name)+".jpg")
    image_path = str(name)+".jpg"
    image = Image.open(image_path)

  # extracting the exif metadata
    exifdata = image.getexif()
    if image._getexif() == None:
      print("Image has no Exif Data")

    else:# looping through all the tags present in exifdata
      for tagid in exifdata:
      
      # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        # passing the tagid to get its respective value
        value = exifdata.get(tagid)
        
        # printing the final result
        print(f"\033[0;31m{tagname:25}: {value}")
  except:
    print("Enter Valid Url")

elif path_type == "2":
  image_path = input("Enter Image Name\n>")
  print("\n")
  try:
    image = Image.open(image_path)

  # extracting the exif metadata
    exifdata = image.getexif()
    if image._getexif() == None:
      print("Image has no Exif Data")

  # looping through all the tags present in exifdata
    else:

      for tagid in exifdata:
      
      # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        # passing the tagid to get its respective value
        value = exifdata.get(tagid)
        
        # printing the final result
        print(f"\033[0;31m{tagname:25}: {value}")
  except:
    print("Enter Valid Path")

else:
  print("Enter Valid Input")
