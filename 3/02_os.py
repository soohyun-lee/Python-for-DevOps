import os

# 현재 작업중인 디렉토리 구하기
os.getcwd()

# 디렉토리 이동하기
os.chdir('./tmp')

# os 모듈이 로드된 시점의 LOGLEVEL 호출
os.environ.get('LOGLEVEL')

# LOGLEVEL이라는 환경변수 설정
os.environ['LOGLEVEL'] = 'DEBUG'

# LOGLEVEL 호출
os.environ.get('LOGLEVEL')

# 이 프로세스를 생성한 터미널에 로그인한 사용자
os.getlogin()
