import requests
import xml.etree.ElementTree as ET

# tree = ET.parse('OAA.rss')
# root = tree.getroot()
# count = 1
# showname = "OAA"
# stuff = []
# for child in root.iter('enclosure'):
#     stuff.append(child)
# stuff = stuff[::-1][:4]
# for child in stuff:
#     epno = str(count)
#     item = (child.attrib)
#     r = requests.get(item['url'], stream=True)
#     epno = epno.zfill(3)
#     filename = f"{showname}-{epno}.mp3"
#     with open(filename, "wb") as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             # writing one chunk at a time to file
#             if chunk:
#                 f.write(chunk)
#     print(filename)
#     count += 1
# image episodes
# for child in root.iter('{http://www.itunes.com/dtds/podcast-1.0.dtd}image'):
#     stuff.append(child)
# stuff = stuff[::-1][:4]
# for child in stuff:
#     epno = str(count)
#     item = (child.attrib)
#     r = requests.get(item['href'], stream=True)
#     epno = epno.zfill(3)
#     filename = f"{showname}-{epno}.jpg"
#     with open(filename, "wb") as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             # writing one chunk at a time to file
#             if chunk:
#                 f.write(chunk)
#     print(filename)
#     print(item['href'])
#     count += 1

# image podcast
import json

# Reading json file

ref = ['0', '1', 'AAI', '3', 'FOA', 'FOW', '6', 'PAC',
       '8', 'XL', '10', 'XOA', '12', 'SOTF', '14', 'PDA', '16', '17', '18', '19', 'MM']


def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())


data = read_json('xero-on-air.json')
identifier = ref[data['showid']]
epno = "0"
epno = epno.zfill(3)
imagelink = data['podcastimg']
# image
# r = requests.get(
#     imagelink, stream=True)
# filename = f"{identifier}-{epno}.jpg"
# with open(filename, "wb") as f:
#     for chunk in r.iter_content(chunk_size=1024):
#         # writing one chunk at a time to file
#         if chunk:
#             f.write(chunk)


# print(data)
count = 0
for key, val in data.items():
    if type(val) == str or type(val) == int:
        continue
    epno = key.zfill(3)
    imagelink = val['heroimg']
    audiolink = val['finalaudio']
    # image
    # r = requests.get(
    #     imagelink, stream=True)
    # filename = f"{identifier}-{epno}.jpg"
    # with open(filename, "wb") as f:
    #     for chunk in r.iter_content(chunk_size=1024):
    #         # writing one chunk at a time to file
    #         if chunk:
    #             f.write(chunk)
    count += 1
    print('DONE', count)
    # audio
    r = requests.get(
        audiolink, stream=True)
    filename = f"{identifier}-{epno}.mp3"
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to file
            if chunk:
                f.write(chunk)

# r = requests.get(
#     "https://i1.sndcdn.com/avatars-000660812498-hq1zm1-original.jpg", stream=True)
# epno = "0"
# epno = epno.zfill(3)
# filename = f"{showname}-{epno}.jpg"
# with open(filename, "wb") as f:
#     for chunk in r.iter_content(chunk_size=1024):
#         # writing one chunk at a time to file
#         if chunk:
#             f.write(chunk)
