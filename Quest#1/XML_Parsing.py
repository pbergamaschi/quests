from xml.etree.ElementTree import parse, tostring
doc = parse('MobileConfig.xml')
elem = doc.findall('max_transcoding_output_fps')[0]
elem.text = input('Enter a new value: ')
print tostring(doc.getroot())
