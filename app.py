from flask import Flask, request, redirect, jsonify, render_template
import json
import os
import pytest
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

# 	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % (physio, longs, lat)

app = Flask(__name__, static_folder = "assets")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/physio')
def physio():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=AvZXOOO79Ko1HoL-HN1VuNQU0qtL842kjYVWuh3dL1uBLawZzHb9yydtD8rqhduA' % ('physiotherapy', '47.602038','-122.333964')
	#print(url)
	re = request.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal'] '47.602038','-122.333964'
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates'] #

		print(Result_name)
		Dict[i] = [Result_name,Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile

	r = request.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)
	return returnFile

@app.route('/dentist')
def dentist():
	url2 = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=' % ('dentist', '47.602038','-122.333964')
	#print(url)
	re2 = request.get(url2)
	returning2 = json.loads(re2.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning[f 'resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict2 = {}
	for i in range(len(returning2['resourceSets'][0]['resources'])-1):
		Result_name2 = returning2['resourceSets'][0]['resources'][i]['name']
		Result_coordinates2=returning2['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name2)
		Dict2[str(i)] = [Result_name2,Result_coordinates2]#47.602038,-122.333964
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = request.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict2)
@app.route('/psychologist')
def psychologist():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=' % ('psychologist', '47.602038','-122.333964')
	#print(url)
	re = request.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name)
		Dict[str(i)] = [Result_name,Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = request.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict)

@app.route('/clinic')
def clinic():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=' % ('psychologist', '47.602038','-122.333964')
	#print(url)
	re = request.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name)
		Dict[str(i)] = [Result_name,Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = request.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict)

@app.route('/doctor')
def doctor():
	url = 'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=%s&userLocation=%s,%s&key=' % ('psychologist', '47.602038','-122.333964')
	#print(url)
	re = request.get(url)
	returning = json.loads(re.text)
	#return returning['resourceSets']['0']['estimatedTotal']
	#print(type(returning['resourceSets'][0]['resources']))
	#print(returning['resourceSets'][0]['resources'][0]['point']['coordinates'])
	Dict = {}
	for i in range(len(returning['resourceSets'][0]['resources'])-1):
		Result_name = returning['resourceSets'][0]['resources'][i]['name']
		Result_coordinates=returning['resourceSets'][0]['resources'][i]['point']['coordinates']

		print(Result_name)
		Dict[Result_name] = [Result_coordinates]
	returnFile = json.dumps(Dict)
	payload = returnFile
	r = request.post('https://www.jsonstore.io/71fc6d609168087b1bd76dea68e7694b4f451bfa7bf7ab5ebb4717dd15bb65d8', json = payload)

	return json.dumps(Dict)

@app.route('/cisco')
def cisco():
	headers = {
    'X-Cisco-Meraki-API-Key': '',
	}
	re = request.get('https://api.meraki.com/api/v0/devices/Q2GV-XLK8-MDBK/camera/analytics/recent', headers=headers)
	returning = json.loads(re.text)

	print(round(returning[0]['averageCount'] * 200, 2))
	payload = str(round(returning[0]['averageCount'] * 200, 2))
	yeet = request.post('https://www.jsonstore.io/039e0e4f386c305904fa8f4ff8b2f4953466ffb2537854a943978dba2fa3336e', json = payload)

	account_sid = 'ACdbe67a5dd0793ed622caea1b81519704'
	auth_token = 'fe1e53e4b7259b5c60b2ec7780b9d4b4'
	client = Client(account_sid, auth_token)
	timeMinutes = payload
	doctorNumber = '+16475265284'
	call = client.calls.create(url='http://twimlets.com/echo?Twiml=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3CResponse%3E%0A%20%20%20%20%3CSay%20voice%20%3D%20%22alice%22%3EHello%20I%20represent%20a%20Destination%20Doc%20patient.%20I%20am%20on%20my%20way%20to%20your%20location%2C%20please%20book%20an%20appointment%20for%20earliest%20' + timeMinutes + '%20minutes.%20Thank%20you.%3C%2FSay%3E%0A%3C%2FResponse%3E&',
	                        to= doctorNumber,
	                        from_='+14388004097'
	                    )

	print(call.sid)
	return str(returning[0]['averageCount'] * 20)

@app.route('/json-example')
def jsonexample():
	return 'Todo...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9000)