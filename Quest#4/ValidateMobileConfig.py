from lxml import etree


xmlschema_doc = etree.parse('BryMobileConfig.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

xml_doc = etree.parse('MobileConfig.xml')
result = xmlschema.validate(xml_doc)

if result == True:
    print("Valid XML!")
else:
    print('Invalid XML!')
