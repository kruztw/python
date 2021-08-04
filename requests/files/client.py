import unittest
import requests

with open("test.jpg", "rb") as f:
   res = requests.post(
           url="http://localhost:5000/view",
           files={
               "image[]": (
                   "test.jpg",
                   f.read(),
                   "image/jpeg"
               ),
           },
           data={
               "token": "4e4bad2093c856bfdabaf852d77c64bd06ec17a3"
           }
       )
