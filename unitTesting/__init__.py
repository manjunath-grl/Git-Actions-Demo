# from pathlib import Path
# from unittest import TestSuite

# def load_tests(loader, tests, pattern):
#     suite = TestSuite()
#     loader.testMethodPrefix = 'demo_'
#     tests = loader.discover(
#         Path(__file__).parent.as_posix(),
#         pattern='demo_*.py',
#     )
#     suite.addTests(tests)
#     return suite
import os
import sys

cwd = os.getcwd()
sys.path.insert(0, cwd)
