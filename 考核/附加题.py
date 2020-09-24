import requests
from lxml import etree
import datetime
import time

def main():
  url = "https://cn.bing.com/"
  rs = requests.get(url=url)
  html = etree.HTML(rs.content)
  imgUrl ="https://cn.bing.com/" + html.xpath('//*[@id="bgLink"]/@href')[0]
  imgRs = requests.get(url=imgUrl)

  tupian = datetime.datetime.now()
  str_time = datetime.datetime.strftime(tupian,"%Y-%m-%d")
  print(tupian)
  path = "./picture/{}.jpg".format(str_time)
  with open(path,"wb")as f:
    f.write(imgRs.content)
if __name__ == '__main__':
    while True:
        main()
        time.sleep(24 * 60 * 60)