import requests
import unittest
urlSum = 'https://sum-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
urlMul = 'https://mul-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
urlSub = 'https://sub-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
urlDiv = 'https://div-service-dot-calculator-insa-rossard.ew.r.appspot.com/'
class ServiceTestCase(unittest.TestCase):
	def test_requestSum(self):
		""" Test Sum-Service """
		def sum(x,y):
			try:
				x = requests.post(urlSum, data = str(x)+" " +str(y))
			except Exception as err:
				print('Error connexion to Sum-Service' +err)
			return str(x.text)
		f = {'+': lambda x, y: sum(x,y),
		}

		resFinal = "8\r\n"
		self.assertEqual(resFinal, f['+'](3,5))

	
	def test_requestMul(self):
		""" Test Mul-Service """
		def mul(x,y):
			try:
				res = requests.post(urlMul, data = str(x)+" " +str(y))
			except Exception as err:
				print('Error connexion to Mul-Service' +err)
			return str(res.text)
		f = {'*': lambda x, y: mul(x,y),
		}

		resFinal = "8\r\n"
		self.assertEqual(resFinal, f['*'](2,4))
		
	def test_requestDiv(self):
		""" Test Div-Service """
		def div(x,y):
			try:
				res = requests.post(urlDiv, data = str(x)+" " +str(y))
			except Exception as err:
				print('Error connexion to Div-Service' +err)
			return str(res.text)
		f = {'/': lambda x, y: div(x,y),
		}

		resFinal = "8\r\n"
		self.assertEqual(resFinal, f['/'](16,2))
	
	def test_requestSub(self):
		""" Test Sub-Service """
		def sub(x,y):
			try:
				res = requests.post(urlSub, data = str(x)+" " +str(y))
			except Exception as err:
				print('Error connexion to Sub-Service' +err)
			return str(res.text)
		f = {'-': lambda x, y: sub(x,y),
		}

		resFinal = "8\r\n"
		self.assertEqual(resFinal, f['-'](16,8))

# [START main]
if __name__ == '__main__':
    unittest.main()
# [END main]
