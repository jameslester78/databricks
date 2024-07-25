import requests

token = dbutils.widgets.get('token')
apiCallType = dbutils.widgets.get('apiCallType')
scope = dbutils.widgets.get('scope')
secretKey = dbutils.widgets.get('secretKey')
secretValue = dbutils.widgets.get('secretValue')

print (apiCallType)

authValue = f'Bearer {token}'
scopeValue =scope

headers = {"Authorization": authValue}

if  token == '':
  dbutils.notebook.exit("no token provided")

if apiCallType == 'list scopes':
  response = requests.get('https://shellenergy-prod.cloud.databricks.com/api/2.0/secrets/scopes/list', headers = headers)
  print (response.text)

if apiCallType == 'list secrets':
  params = {'scope': scopeValue}
  response = requests.get('https://shellenergy-prod.cloud.databricks.com/api/2.0/secrets/list', headers = headers, params = params)
  print (response.text)

if apiCallType == 'delete scope':
  params = {'scope': scopeValue}
  response = requests.post('https://shellenergy-prod.cloud.databricks.com/api/2.0/secrets/scopes/delete', headers = headers, params = params)
  print (response.text)

if apiCallType == 'create scope':
  params = {'scope': scopeValue}
  response = requests.post('https://shellenergy-prod.cloud.databricks.com/api/2.0/secrets/scopes/create', headers = headers, params = params)
  print (response.text)  
  
if apiCallType == 'create secret':
  params = {'scope': scopeValue,'key':secretKey,'string_value':secretValue}
  response = requests.post('https://shellenergy-prod.cloud.databricks.com/api/2.0/secrets/put', headers = headers, params = params)
  print (response.text) 
