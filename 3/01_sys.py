import sys

# 현재 아키텍쳐의 바이트 순서 확인
sys.byteorder

# 파이썬 객체의 크기를 바이트 단위로 반환
sys.getsizeof(1)

# 기반 OS 확인 (uname)
sys.platform

# 파이썬 버전 조회
sys.version_info.major

print(sys.byteorder)
print(sys.getsizeof(1))
print(sys.platform)
print(sys.version_info.major)

# 파이썬 버전을 감지하여 3.7 / 3 / 그 이하 별 문구 출력
if sys.version_info.major < 3:
    print("You need to update your Python version")
elif sys.version_info.major < 7:
    print("You are not running the latest version of Python")
else:
    print("All is good.")