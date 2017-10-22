import json
import requests
import ReuestParsing

abn = '78330347529'
tfn = '43138890'
tan = '17801003'
paths = ['C:\\PyCharmProj\\adoria\\Payload\\17\\CONF-ATO-IITR-SRP-017_Prelodge_Request_01.xml',
          ]
for path in paths:
    payload_json_1 = []
    payload_json_2 = []
    payload_json_3 = []
    res = []
    alias = []
    version = []

    res = ReuestParsing.xml_request_parsing(path, abn)
    #print res
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
    for elements in res:
        alias, version  = ReuestParsing.get_alias_(elements[1],elements[-1])
        #print alias,
        elements[0] = alias[0]
        elements[-3] = version

    #print res

    doc_name = None
    docs = []

    for elements in res:
        alias_ = elements[0]
        #print alias_,
        version = elements[-3]
        #print version,
        if version == 1:
            if elements[3]==None:
                demical = False
            else:
                demical = True
            payload_ = {
          "Alias": str(alias_),
          "Value": str(elements[-2]),
          "IsDecimals": demical,
          "Decimals": 0,
          "UnitRef": 1
        }
            #print payload_
            payload_json_1.append(payload_)
        if version == 2:
            if elements[3] == None:
                demical = False
            else:
                demical = True
            payload_ = {
                "Alias": str(alias_),
                "Value": str(elements[-2]),
                "IsDecimals": demical,
                "Decimals": 0,
                "UnitRef": 1
            }
           # print payload_
            payload_json_2.append(payload_)
        if version == 3:
            if elements[3] == None:
                demical = False
            else:
                demical = True
            payload_ = {
                "Alias": str(alias_),
                "Value": str(elements[-2]),
                "IsDecimals": demical,
                "Decimals": 0,
                "UnitRef": 1
            }
            #print payload_
            payload_json_3.append(payload_)

    if len(payload_json_1)!=0:
      doc_1 =  {
              "FormName": "BASE",
              "Version": 1,
              "DocumentName": "IITR",
              "DocumentType": 1,
              "Payload": payload_json_1
            }
      docs.append(doc_1)
    if len(payload_json_2)!=0:
      doc_2 = {
              "FormName": "SCHEDULE",
              "Version": 2,
              "DocumentName": "PIITR",
              "DocumentType": 1,
              "Payload": payload_json_2
            }
      docs.append(doc_2)
    if len(payload_json_3)!=0:
      doc_3 = {
              "FormName": "SCHEDULE",
              "Version": 3,
              "DocumentName": "RS",
              "DocumentType": 2,
              "Payload": payload_json_3
            }
      docs.append(doc_3)

    #print docs

    url = 'http://sandbox-api.beth.dev.adoriasoft.org/sbrservice/iitr/prelodge'
    payload = {
      "ABN": abn,
      "TFN": tfn,
      "TAN": tan,
      "StartDate": "2015-07-01",
      "EndDate": "2016-06-30",
      "Year": 2016,
      "Documents": docs
    }
    print payload
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #r = requests.post(url, data=json.dumps(payload), headers=headers)

    #print r.text