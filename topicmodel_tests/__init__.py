import unittest
def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('topicmodel_tests', pattern='test*.py')
    return test_suite
