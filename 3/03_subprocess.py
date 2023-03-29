import subprocess

cp = subprocess.run(['ls', '-l'],
    capture_output=True,
    universal_newlines=True)
cp.stdout
print(cp.stdout)


cp_err = subprocess.run(['ls', '/doesnotexist'],
    capture_output=True,
    universal_newlines=True)
cp_err.stderr
print(cp_err.stderr)

cp_err_check = subprocess.run(['ls', '/doesnotexist'],
    capture_output=True,
    universal_newlines=True,
    check=True)
