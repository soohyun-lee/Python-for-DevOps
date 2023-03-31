import subprocess

# capture_output 파라미터 > 실행결과를 stdout과 stderr로 저장가능

# stdout
cp = subprocess.run(['ls', '-l'],
    capture_output=True,
    universal_newlines=True)
cp.stdout

print('--- stdout ---')
print(cp.stdout)

# stderr
cp_err = subprocess.run(['ls', '/doesnotexist'],
    capture_output=True,
    universal_newlines=True)
cp_err.stderr

print('--- stderr ---')
print(cp_err.stderr)

# check 파라미터 > Traceback 조회 가능
print('--- check(traceback) ---')
cp_err_check = subprocess.run(['ls', '/doesnotexist'],
    capture_output=True,
    universal_newlines=True,
    check=True)