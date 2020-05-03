# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, request
import requests

urlSum = 'https://sum-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
urlMul = 'https://mul-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
urlSub = 'https://sub-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
urlDiv = 'https://div-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
	def sum(x,y):
		try:
			x = requests.post(urlSum, data = x +" "+ y)
		except Exception as err:
			print('Error connexion to sumService' +err)
		return str(x.text)
	def mul(x,y):
		try:
			x = requests.post(urlMul, data = x +" "+ y)
		except Exception as err:
			print('Error connexion to sumService' +err)
		return str(x.text)

	def div(x,y):
		try:
			x = requests.post(urlDiv, data = x +" "+ y)
		except Exception as err:
			print('Error connexion to sumService' +err)
		return str(x.text)

	def sub(x,y):
		try:
			x = requests.post(urlSub, data = x +" "+ y)
		except Exception as err:
			print('Error connexion to sumService' +err)
		return str(x.text)

	if request.method == 'GET':
		x = request.args.get('x')
		y = request.args.get('y')
		# build a list of operations
		f = {'+': lambda x, y: sum(x,y),
			'-': lambda x, y: sub(x,y),
			'*': lambda x, y: mul(x,y),
			'/': lambda x, y: div(x,y),
             'C': lambda x, y: "",
            }
        # get page parameters
		operator = request.args.get('operator')
        # calculate 
		result = ""
		try:
			result = f[operator](x, y)
		except ValueError:
			result = "Error: Incorrect Number"
		except ZeroDivisionError:
			result = "Error: Division by zero"
		except KeyError:
			pass      
		return render_template('home.html',res=result)
	else:
		return render_template('home.html')


if __name__ == '__main__':
	# This is used when running locally only. When deploying to Google App
	# Engine, a webserver process such as Gunicorn will serve the app. This
	# can be configured by adding an `entrypoint` to app.yaml.
	app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]