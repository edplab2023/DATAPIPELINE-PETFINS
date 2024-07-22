# This Python wrapper facilitates the use of webhooks by encapsulating the REST API calls.
 
import mlflow
import urllib
import json
 
class HttpClient:
  def __init__(self, base_url, token):
    self.base_url = base_url
    self.token = token
  
  def createWebhook(self, request):
    return self._post('api/2.0/mlflow/registry-webhooks/create', request)
 
  def updateWebhook(self, request):
    return self._patch('api/2.0/mlflow/registry-webhooks/update', request)
 
  def listWebhooks(self, request):
    return self._get('api/2.0/mlflow/registry-webhooks/list', request)
 
  def deleteWebhook(self, request):
    return self._delete('api/2.0/mlflow/registry-webhooks/delete', request)
  
  def testWebhook(self, request):
    return self._post('api/2.0/mlflow/registry-webhooks/test', request)
    
  def _get(self, uri, params):
    data = urllib.parse.urlencode(params)
    url = f'{self.base_url}/{uri}/?{data}'
    headers = { 'Authorization': f'Bearer {self.token}'}
 
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return json.load(response)
 
  def _post(self, uri, body):
    json_body = json.dumps(body)
    json_bytes = json_body.encode('utf-8')
    headers = { 'Authorization': f'Bearer {self.token}'}
 
    url = f'{self.base_url}/{uri}'
    req = urllib.request.Request(url, data=json_bytes, headers=headers)
    response = urllib.request.urlopen(req)
    return json.load(response)
 
  def _patch(self, uri, body):
    json_body = json.dumps(body)
    json_bytes = json_body.encode('utf-8')
    headers = { 'Authorization': f'Bearer {self.token}'}
 
    url = f'{self.base_url}/{uri}'
    req = urllib.request.Request(url, data=json_bytes, headers=headers, method='PATCH')
    response = urllib.request.urlopen(req)
    return json.load(response)
 
  def _delete(self, uri, body):
    json_body = json.dumps(body)
    json_bytes = json_body.encode('utf-8')
    headers = { 'Authorization': f'Bearer {self.token}'}
 
    url = f'{self.base_url}/{uri}'
    req = urllib.request.Request(url, data=json_bytes, headers=headers, method='DELETE')
    response = urllib.request.urlopen(req)
    return json.load(response)