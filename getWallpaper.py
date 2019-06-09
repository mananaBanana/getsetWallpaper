from os import path
from os import system
import urllib
from bs4 import BeautifulSoup as BS

# NASA APOD Site
apod_url = "https://apod.nasa.gov/apod/astropix.html"

script_dir = path.dirname(__file__) # Directory of the script
print script_dir

try:
    sock = urllib.urlopen(apod_url)
    html_data = sock.read()
except Exception, sockerror:
    print "urllib request rejected."
    print sockerror

soup = BS(html_data, "lxml")

img_url = "https://apod.nasa.gov/apod/" + soup.img.parent['href']
print soup.img['src']
if script_dir:
    img_name = script_dir + path.sep + 'images/' + soup.img['src'].split('/')[-1]
else:
    img_name = 'images/' + soup.img['src'].split('/')[-1]


# Download image
try:
    print "Downloading... ", img_url
    urllib.urlretrieve(img_url, img_name)
except Exception, e:
    print "Can't download image. Try again some other day"
    print e
    
try:
    # Get absolute path of image
    img_path = path.abspath(img_name)
    # Prepend "file://" for gsettings
    img_path = "file://" + img_path

    # Command to set the wallpaper
    print "Setting wallpaper..."
    print img_path
    system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri " + img_path)
    # Set scale of wallpaper
    print "Wallpaper set"
except Exception, e:
    print e

    # Save description to file
with open("wallpaper.txt", "w") as desc:
    desc.write(soup.text.encode("UTF-8"))
