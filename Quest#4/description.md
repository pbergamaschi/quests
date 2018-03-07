# quest#4
Your target for this mission is to write a python program that checks the integrity and the validity of an XML file. 
The file you need to validate is 'MobileConfig.xml', you have to assure that the value of each field follows a predetermined list of rules:


    <cfg-root></cfg-root>

The tag <cfg-root> appears exacly once in the document

    <path>
        <xsl-templates>.\XslTemplates</xsl-templates>
        <log>.\Log</log>
        <temp>.\Temp</temp>
    </path>

The tag <path> appears exaclty once in the document and contains three subtags: <xsl-templates>, <log> and <temp>, each one must contain a valid path ( either an absolute one like "c:\arteco\log" or a relative one like "..\log")


    <network>
        <connection tcpPort="7002" timeout="60000" auth-method="DIGEST"/>
        <!--> "DIGEST" (default) || "NONE"<-->
        <transmission timeout="60000"/>
        <rtsp port="554" max_transcoding_output_fps="8" http_tunneling_port="0"/>
    </network>

The Tag <network> appears exaclty once and cointains three subtags: 

- <connection> 
    must accept the following attributes
    - tcpPort that should cointain a numeric value from 0 to 65535
    - timeout that should cointain a numeric value from 0 to 60000
    and can accept the following attribute (optional):
    - auth-method if the attribute is present, his value MUST be either "DIGEST" or "NONEx"

- <transmission> 
    must accept the following attribute
    - timeout that should cointain a numeric value from 0 to 60000

- <rtsp> 
    must accept the following attributes:
    - port that should cointain a numeric value from 0 to 65535
    - max_transcoding_output_fps contains a numeric value from 1 to 60 
    - http_tunneling_port should cointain a numeric value from 0 to 65535


    <servers>
        <server url="localhost" port="7000" codename="" descr=""/>
    </servers>

The Tag <servers> appears exaclty once and cointains at least 1 <server> tag (but possibly more)
- <server>
    must accept the following attributes:
    - url can either contain a string like "localhost" or an IP address like "192.168.10.16"
    - port that should cointain a numeric value from 0 to 65535
    - codename is a string that cannot contain the " " (space) charachter
    - descr is a free string


    <image width="120" height="80" quality="7" fps="2"/>

The Tag <image> appears exaclty once 
    must accept the following attributes:
    - width is a numeric field, the values can be from 80 to 80000
    - height is a numeric field, the values can be from 60 to 60000
    - quality is a numeric field, the values can be from 1 to 100


    <firebase-server-key value="AAAAg4psWoM:APA91bG0DNMaEpdWYfEBB25l8HEmaqicaIkGwjugeZACM4pdu3sSxPqAOyECxnOOV1_0CdlooG1AwZPZ5rWjHmmXTiYAi1J8D3eTz7-QSyVe9z-ouVZBxTtU_sf0GjOoZ1qM20QKLetl"/>
    <firebase-notification-play-sound value="1"/>


The Tag <firebase-server-key> can appears once, IF it's present , another tag called <firebase-notification-play-sound> must follow it 
    The Tag <firebase-server-key> must accept the following attribute:
    - value is a 152 characters (exaclty) long string, that mustn't contain spaces. 
    The tag <firebase-notification-play-sound> must accept the following attribute:
    - value is either "1" or "0"


In order to validate the file you can use Python, but your program must call an external xsd file that will contains the collections of rules the xml has to follow in order to be declares "valid", you'll find an extensive guide about xsd format [here](https://www.w3schools.com/xml/schema_intro.asp)

