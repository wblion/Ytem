import sys
sys.path.append(r"D:\work\YQ\lib")
import time
from lxml import etree

lastmod_txt = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
root = etree.Element("cache_info")
root.append(etree.Element("instance",name="boy",namespace="boy1",creat_time=lastmod_txt))
root.append(etree.Element("instance",name="boy",namespace="boy2",creat_time=lastmod_txt))
root.append(etree.Element("instance",name="boy",namespace="boy3",creat_time=lastmod_txt))

tree = etree.ElementTree(root)
tree.write(r'D:\work\YQ\tem\cache_info.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')