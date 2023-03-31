#!/usr/bin/env python
"""
Command line tool using argparse
"""
import argparse


def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")


def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")


def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)


if __name__ == '__main__':
    # 최상위 레벨 parser 생성
    parser = argparse.ArgumentParser(description='Maritime control')
    # 해당 파서 계층 아래에 어떠한 명령과도 사용할 수 있는 최상위 인수 추가
    parser.add_argument('--twice', '-t',
                        help='Do it twice',
                        action='store_true')

    # 서브파서 객체 생성, dest는 서브파서 선택에 사용될 속성의 이름
    subparsers = parser.add_subparsers(dest='func')
    # ships 서브파서 추가
    ship_parser =  subparsers.add_parser('ships', 
                                         help='Ship related commands')
    # ships 서브파서에 명령 추가. choices 파라미터는 해당 명령에서 선택 가능한 목록                                     
    ship_parser.add_argument('command',
                             choices=['list', 'sail'])

    # sailors 서브파서 추가
    sailor_parser = subparsers.add_parser('sailors',
                                          help='Talk to a sailor')
    # sailors 서브파서에 필요한 위치 인수 추가
    sailor_parser.add_argument('name',
                               help='Sailors name')
    sailor_parser.add_argument('--greeting', '-g',
                               help='Greeting',
                               default='Ahoy there')

    # 어느 서브파서가 func 값 확인에 사용됐는지 체크
    args = parser.parse_args()
    if args.func == 'sailors': 
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()
