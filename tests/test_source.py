# import unittest
# from app.models import source

# class SourceTest(unittest.TestCase):
#     '''
#     Test Class to tests if the methods/functions used return  the expected result
#     '''

#     def setUp(self):
#         '''
#         Set up method that will run before every Test method
#         '''
#         self.new_source = source("BBC News","Theranos founder hit with criminal charges","Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.", "http://www.bbc.co.uk/news/business-44501631","https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg","2018-06-15T22:25:40Z")

#     def test_instance(self):
#         '''
#         test case function that checks if the object (new_source)
#         is an instance or subclass of classinfo class (source).
#         '''
#         self.assertTrue(isinstance(self.new_source,source))

#     def test_init(self):
#         '''
#         init test
#         '''
#         self.assertEqual(self.new_source.author,"BBC News")
#         self.assertEqual(self.new_source.title,"Theranos founder hit with criminal charges")
#         self.assertEqual(self.new_source.description,"Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.")
#         self.assertEqual(self.new_source.url,"http://www.bbc.co.uk/news/business-44501631")
#         self.assertEqual(self.new_source.urlToImage,"https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg")
#         self.assertEqual(self.new_source.publishedAt,"2018-06-15T22:25:40Z")