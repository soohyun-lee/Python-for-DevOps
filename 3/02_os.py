import os

os.getcwd()
os.chdir('/tmp')
os.environ.get('LOGLEVEL')
os.environ['LOGLEVEL'] = 'DEBUG'
os.environ.get('LOGLEVEL')
os.getlogin()