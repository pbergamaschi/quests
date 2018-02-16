#script to parse an xml file and change input of a 'element' within

import xml.etree.ElementTree as ET

#My program

#read the data from the file, get the root
tree = ET.parse('MobileConfig.xml')
root = tree.getroot()

#ask user for input for new fps value
new = input('Choose a new value for max transcoding output fps: ')

#iterate to the proper node, then .set the new value
for rtsp in root.iter('rtsp'):
    rtsp.set('max_transcoding_output_fps', new)
    
tree.write('MobileConfigTest.xml',encoding="UTF-8",xml_declaration=True,method="xml")

# YAY! I did it, but unfortunately I can't get the comments to write in the
# new file, nor have the elements stay in order...


