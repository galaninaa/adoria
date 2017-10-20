import json
import requests
import ReuestParsing

abn = '78330347529'
tfn = '31781647'
tan = '17801003'
path = '/Users/galaninaa/PycharmProjects/adoria/Payload/1/CONF-ATO-IITR-SRP-001_Prelodge_Request_01.xml'

tag,demicals = ReuestParsing.xml_request_parsing(path,abn)

print demicals

aliases = ReuestParsing.get_alias(tag)
payload_json_1 = []
payload_json_2 = []
payload_json_3 = []

version = 0
doc_name = None
docs = []

for alias in aliases:
  version, doc_name = ReuestParsing.get_version(alias)
  if version == '1' and doc_name == "IITR":
    payload_ = {
      "Alias": str(alias[1:]),
      "Value": "2016",
      "IsDecimals": False,
      "Decimals": 0,
      "UnitRef": 1
    }
    print payload_
    payload_json_1.append(payload_)
  if version == '2' and doc_name == "PIITR":
    payload_ = {
      "Alias": str(alias[1:]),
      "Value": "2016",
      "IsDecimals": False,
      "Decimals": 0,
      "UnitRef": 1
    }
    print payload_
    payload_json_2.append(payload_)
  if version == '3' and doc_name == "RS":
    payload_ = {
      "Alias": str(alias[1:]),
      "Value": "2016",
      "IsDecimals": False,
      "Decimals": 0,
      "UnitRef": 1
    }
    print payload_
    payload_json_2.append(payload_)
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
          "Payload": payload_json_1
        }
  docs.append(doc_2)
if len(payload_json_3)!=0:
  doc_3 = {
          "FormName": "SCHEDULE",
          "Version": 3,
          "DocumentName": "RS",
          "DocumentType": 2,
          "Payload": payload_json_1
        }
  docs.append(doc_3)

print docs

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
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

print r.text