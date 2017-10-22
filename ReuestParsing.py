from lxml import etree
from StringIO import StringIO
import pyodbc

path = 'C:\\PyCharmProj\\adoria\\Payload\\1\\CONF-ATO-IITR-SRP-001_Prelodge_Request_01.xml'
abn = '78330347529'

def xml_request_parsing(path, abn):
    abn = str(abn)
    parser = etree.XMLParser()
    tree =etree.parse(path,parser)
    result = []
    demicals = []

    nodes = tree.xpath('//*[@contextRef]')
    for node in nodes:
        res = node.tag
        list = res.split('}')

        contextRef =  node.get('contextRef')
        if  contextRef=='Context_Duration_POS_ReportingParty':
            context = 'RP.POS'
        elif contextRef=='Context_Duration_BUS_ReportingParty':
            context = 'RP.BUS'
        elif contextRef=='Context_Duration_ReportingParty':
            context = 'RP'
        elif contextRef=='Context_Duration_RES_ReportingParty':
            context = 'RP.RES'
        elif contextRef=='Context_Duration_ReportingParty_Spouse':
            context = 'RP.SPOUSE'
        elif contextRef=='Context_Duration_ReportingParty_LOSSSqNum_1':
            context = 'RP.{LOSSSeqNum}'
        elif contextRef=='Context_Duration_ReportingParty_LOSSSqNum_2':
            context = 'RP.{LOSSSeqNum}'
        elif contextRef=='RP.Partnership':
            context = 'RP.Partnership'
        elif contextRef=='RP.Trust':
            context = 'RP.Trust'
        elif contextRef=='RP.PrimaryProduction':
            context = 'RP.Prim'
        elif contextRef=='Context_Duration_ReportingParty_SWSqNumDim_1':
            context = 'RP.{SaWSeqNum}'
        else:
            context = None
        SBRVersionId = None
        payload_line = [None, list[1], node.get('contextRef'), node.get('decimals'), node.get('unitRef'), SBRVersionId, node.text, context]

        result.append(payload_line)

    return result

#this is old method
def get_alias(tag):
    result = []
    #connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server}; Server=192.168.82.78,32779; uid=SA; pwd=93799922Ag#$')
    connection = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server}; Server=localhost,1433; uid=SA; pwd=9379992Ag#$')
    cursor = connection.cursor()
    cursor.execute('use qa_test')
    SQLCommand = ("SELECT alias from [MessageStructurePayload] where element_name= '" + tag + "'")
    cursor.execute(SQLCommand)
    row = cursor.fetchone()
    while row:
        result.append(row[0])
        row = cursor.fetchone()
    return result

#this is new
def get_alias_(tag, context):
    result = []
    connection = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server}; Server=localhost,1433; uid=SA; pwd=9379992Ag#$')
    cursor = connection.cursor()
    cursor.execute('use qa_test')
    if context!=None:
        SQLCommand = ("SELECT alias, SBRVErsionid from [MessageStructurePayload] where element_name= '" + tag + "' and context = '" + context + "'")
    else:
        SQLCommand = (
        "SELECT alias, SBRVErsionid from [MessageStructurePayload] where element_name= '" + tag + "'")
    cursor.execute(SQLCommand)
    row = cursor.fetchone()
    version = 0
    while row:
        result.append(row[0])
        version= row[1]
        row = cursor.fetchone()
    return result,version


def get_version(alias):
    alias = ''.join([i for i in alias if not i.isdigit()])
    #print alias
    lenght = len(alias)
    #print lenght
    if lenght == 2:
        result, doc_name  = '3', 'RS'
    if lenght == 5:
        result, doc_name  = '2', 'PIITR'
    if lenght == 4:
        result, doc_name = '1', 'IITR'
    return result, doc_name

def tmp(path):
    import xml.etree.ElementTree as ET
    tree = ET.parse(path)
    root = tree.getroot()
    #root = ET.fromstring(country_data_as_string)
    print root
'''
res = xml_request_parsing(path, abn)
print res
'''
'''

for elements in res:
    alias = get_alias(elements[1])

    if len(alias)>1:

        for el in alias:

            connection = pyodbc.connect(
                'Driver={ODBC Driver 13 for SQL Server}; Server=localhost,1433; uid=SA; pwd=9379992Ag#$')
            cursor = connection.cursor()
            cursor.execute('use qa_test')
            SQLCommand = ("SELECT context from [MessageStructurePayload] where element_name= '" + elements[1] + "' and alias='"+el+"'")
            cursor.execute(SQLCommand)
            row = cursor.fetchone()
            #print row
            while row:
                print el, elements[1],elements[2],'; ',row[0]
                row = cursor.fetchone()
        #return result
'''

'''
for elements in res:
    alias,version = get_alias_(elements[1],elements[-1])
    elements[0] = alias[0]
    elements.append(version)
print res
'''
