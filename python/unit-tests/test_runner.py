import unittest

def run_tests():
    test_loader = unittest.TestLoader()

    test_suite = test_loader.discover(start_dir='', pattern='*_tests.py')
    
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == '__main__':
    run_tests()
