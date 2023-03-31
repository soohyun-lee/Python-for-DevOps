#!/usr/bin/env python
"""
Command line tool using argparse
"""
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input') # 메시지와 함께 parser 객체 생성
    parser.add_argument('message', # 도움말 메세지와 위치 기반 명령 추가
                        help='Message to echo')
        
    parser.add_argument('--twice', '-t', # 옵션 인수 추가
                        help='Do it twice',
                        action='store_true') # 옵션 인수에 boolean 값 저장

    args = parser.parse_args() # 파서를 사용해 인수 파싱

    print(args.message) # 이름을 통해 인숫값에 접근, 옵션 인수의 이름에는 --가 제거되어있음
    if args.twice:
        print(args.message)
