#!/usr/bin/env python
"""
Simple command line tool using sys.argv
"""
import sys

def say_it(greeting, target):
    message = f'{greeting} {target}'
    print(message)

# 현재 명령줄에서 실행중인지 확인 후,
# greeting와 target의 기본값 설정
if __name__ == '__main__':
    greeting = 'Hello'
    target = 'Joe'

    # 인수에 --help 문자열이 있는지 확인
    # 있다면, 도움말 출력 후 프로그램 종료
    if '--help' in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()

    # --name 인수 뒤에 이어지는 값의 위치 파악 후
    # 인수 리스트의 길이를 파악하여 해당 인수 뒤에 값이 없다면 길이가 부족하다고 판단
    if '--name' in sys.argv:
        # Get position after name flag
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            # print(len(sys.argv))
            # print(name_index)
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        # Get position after greeting flag
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    # 인수에 따라 수정된 값 출력
    say_it(greeting, name)