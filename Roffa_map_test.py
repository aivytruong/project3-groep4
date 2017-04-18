
#pip install geoplotlib
import geoplotlib
from geoplotlib.utils import BoundingBox
from geoplotlib.colors import ColorMap
from geoplotlib.utils import json
import json
import requests



# verandert de kleur van bepaalde stukken op de map idk zoiets
def get_color(properties):
    key = str(int(properties['jaar'])) + properties['acode']
    if key in Roffa:
        return cmap.to_color(Roffa.get(key), .15, 'lin')
    else:
        return [0, 0, 0, 0]


with open('Rotterdam_map.json','r') as fin:
    Roffa = json.load(fin)
    print (Roffa)

cmap = ColorMap('Reds', alpha=255, levels=10)
geoplotlib.geojson('Rotterdam_map.json', fill=True, color=[255, 255, 255, 64], f_tooltip=lambda properties: properties['jaar'])
geoplotlib.geojson('Rotterdam_map.json', fill=False, color=[255, 255, 255, 64])
# geoplotlib.set_bbox(BoundingBox.east)
geoplotlib.show()
