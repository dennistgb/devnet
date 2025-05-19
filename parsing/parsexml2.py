import xml.etree.ElementTree as ET
import re #provides functions for regular expressions

xml = ET.parse("myfile.xml")
root = xml.getroot()
print(f"root is {root}")

ns = re.match('{.*}', root.tag).group(0)

namespace = root.find(f"{ns}xmlns")

editconf = root.find(f"{ns}edit-config")

defaultop = editconf.find(f"{ns}default-operation") 
testop = editconf.find(f"{ns}test-option")

print(defaultop.text)


