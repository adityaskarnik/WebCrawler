import urllib.request
import re
def get_images(url, depth):

    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()

    response = opener.open(url)

    links = re.findall('"((http)s?://.*?)"', str(response.read()))
    images = []
    for i in links:
        if not i[0].endswith('#') | i[0].endswith('"'):
            if i[0].endswith('.png') | i[0].endswith('.jpg') | ('img' in i[0]):
                images.append(i[0])
            else:
                try:
                    newLink = opener.open(i[0])
                    links = re.findall('"((http)s?://.*?)"', str(newLink.read()))
                    for l in links[:int(depth)-1]:
                        if not l[0].endswith('#') | l[0].endswith('"'):
                            if l[0].endswith('.png') | l[0].endswith('.jpg') | ('img' in i[0]):
                                images.append(l[0])
                except Exception as e:
                    print("Exception",e)

    return images