from requests import get
from json import loads
from random import randint
from os import getcwd, path
from ctypes import windll

headers = {"Authorization": "563492ad6f91700001000001e6da963077b249b7a8937d73c85ddf78"}
q = input("What type of background would you like?\n")
params = {"query": q, "per_page": 80, "orientation": "landscape", "page": 1}
imagePath = path.join(getcwd(), "wallpaper.png")

try:
    total = loads(get('https://api.pexels.com/v1/search', headers=headers, params=params).text)['total_results']
    params["page"] = randint(1, int(total / 80)) if total > 80 else 1
    image = loads(get('https://api.pexels.com/v1/search', headers=headers, params=params).text)['photos']
    image = get(image[randint(0, len(image) - 1)]['src']['large2x'], headers=headers).content
    with open("wallpaper.png", 'wb') as handler:
        handler.write(image)
    windll.user32.SystemParametersInfoW(20, 0, imagePath, 0)

except:
    print("Invalid search. Please try again with a valid query.")