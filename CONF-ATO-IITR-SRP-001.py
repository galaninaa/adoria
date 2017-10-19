import json
import requests

url = 'http://sandbox-api.beth.dev.adoriasoft.org/sbrservice/iitr/prelodge'
payload = {
  "ABN": "78330347529",
  "TFN": "31781647",
  "TAN": "17801003",
  "StartDate": "2015-07-01",
  "EndDate": "2016-06-30",
  "Year": 2016,
  "Documents": [
    {
      "FormName": "BASE",
      "Version": 1,
      "DocumentName": "IITR",
      "DocumentType": 1,
      "Payload": [
                {

                  "Alias": "IITR10",
                  "Value": "2016",
                  "IsDecimals": False,
                  "Decimals": 0,
                  "UnitRef": 1
                },
                {
                  "Alias": "IITR19",
                  "Value": "true",
                  "IsDecimals": False,
                  "Decimals": 0,
                  "UnitRef": 1
                }
              ]
    }
  ]
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(payload), headers=headers)


print r.text