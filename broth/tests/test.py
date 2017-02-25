#-*- coding: utf-8 -*-
import signal, unittest
from datetime import datetime
from date_extractor import *
from inspect import getargspec
from broth import Broth
from requests import get

class Test(unittest.TestCase):

    def testBroth(self):
        broth = Broth(get("http://danieljdufour.com/").text)
        self.assertTrue(broth != None)

    def testTables(self):
        broth = Broth(get("http://www.nuforc.org/webreports/ndxlAK.html").text)
        tables = broth.tables
        self.assertEqual(len(broth.tables), 1)
        

if __name__ == '__main__':
    unittest.main()
