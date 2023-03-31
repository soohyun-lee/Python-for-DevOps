#!/usr/bin/env python
"""
Command line tool using fire
"""
import fire


class Ships(): # ships 명령을 위한 클래스 정의
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")


def sailors(greeting, name): # sailors는 하위 명령이 없으므로 함수로 정의될 수 있음
    message = f'{greeting} {name}'
    print(message)


class Cli(): # 최상위 그룹 역할을 하는 클래스 정의. 클래스 속성으로 sailors함수와 Ships 추가

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == '__main__':
    fire.Fire(Cli) # 최상위 그룹 역할을 하는 클래스를 fire.Fire로 호출