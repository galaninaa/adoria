from lxml import etree
from StringIO import StringIO
import pyodbc

path = '/Users/galaninaa/PycharmProjects/adoria/Payload/1/CONF-ATO-IITR-SRP-001_Prelodge_Request_01.xml'
abn = '78330347529'

def xml_request_parsing(path, abn):
    abn = str(abn)
    parser = etree.XMLParser()
    tree =etree.parse(path,parser)
    result = []
    demicals = []

    nodes = tree.xpath('//*[text()="' + abn + '"]')
    for node in nodes:
        res = node.tag
        demical = node.get("decimals")
        print demical
        if demical== None:
            demicals_result = False
        else:
            demicals_result = True
        list = res.split('}')
        result.append(list[1])
        demicals.append(demicals_result)
    return result,demicals



def get_alias(tag):
    result = []
    connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server}; Server=192.168.82.78,32779; uid=SA; pwd=93799922Ag#$')
    cursor = connection.cursor()
    cursor.execute('use qa_test')
    for elements in tag:
        SQLCommand = ("SELECT alias from [MessageStructurePayload] where element_name= '" + elements + "'")
        cursor.execute(SQLCommand)
        row = cursor.fetchone()
        while row:
            result.append(row[0])
            row = cursor.fetchone()
    return result

def get_version(alias):
    alias = ''.join([i for i in alias if not i.isdigit()])
    lenght = len(alias)
    if lenght == 2:
        result, doc_name  = '3', 'RS'
    if lenght == 5:
        result, doc_name  = '2', 'PIITR'
    if lenght == 4:
        result, doc_name = '1', 'IITR'
    return result, doc_name


print xml_request_parsing(path, abn)
