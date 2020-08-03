import requests
import re

SUPERSTAR_ELEMENT = '<div class="subtitle klavikav grey1" >superstar</div>'

for i in range(0, 100):
    r = requests.get("https://incidecoder.com/ingredients/all?offset={}".format(i))
    ingrs = re.findall('/ingredients/[^"]*', r.text)

    print("Page", i)

    if len(ingrs) == 0:
        break

    for ingr in ingrs:
        url = "https://incidecoder.com{}".format(ingr)

        r2 = requests.get(url)
        if SUPERSTAR_ELEMENT in r2.text:
            print(url)
