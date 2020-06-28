# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:59:22 2020

@author: subham
"""
try:
    from flask_incoming_request import app
    import unittest
    
except Exception:
    print("Some modules are missing")

class FlaskTestCase(unittest.TestCase):
    
    #to check if response is 200
    def test_index(self):
        tester= app.test_client(self)
        response=tester.get("/form")
        statuscode=response.status_code
        self.assertEqual(statuscode, 200)
        
    def test_index_content(self):
        tester= app.test_client(self)
        response=tester.get("/form")
        self.assertEqual(response.content_type,"text/html")
    
    def test_index_data(self):
       tester= app.test_client(self)
       response=tester.get("/form")
       self.assertEqual(b'name' in response.data)
   
if __name__ == "__main__":
    unittest.main()