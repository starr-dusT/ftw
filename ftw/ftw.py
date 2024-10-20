from ftw import starfield, blank 
import importlib.resources as impr
from wand.image import Image
from wand.color import Color
import sys
import subprocess

def create_wallpaper(ship_name, bg_color, res=(2560,1440)):
    bg = blank.create_blank(res, bg_color)
    stars = starfield.create_star_field(num_stars=300, cluster_ratio_range=(0.5, 0.7), num_clusters_range=(3, 8), cluster_size_range=(5, 10), cluster_elongation_range=(1, 4))
    resources = impr.files("ftw") / "res"
    ship = Image(filename=resources / "{}.png".format(ship_name))

    with Image(width=res[0], height=res[1], background=Color('transparent')) as canvas:
        canvas.composite(bg, left=(res[0] - bg.width) // 2, top=(res[1] - bg.height) // 2)
        canvas.composite(stars, left=(res[0] - stars.width) // 2, top=(res[1] - stars.height) // 2)
        canvas.composite(ship, left=(res[0] - ship.width) // 2, top=(res[1] - ship.height) // 2)
        canvas.save(filename='/tmp/ftw.png')

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    create_wallpaper(sys.argv[1], sys.argv[2])
    subprocess.run(["gsettings","set","org.gnome.desktop.background","picture-uri","file:///tmp/ftw.png"])
    subprocess.run(["gsettings","set","org.gnome.desktop.background","picture-uri-dark","file:///tmp/ftw.png"])
