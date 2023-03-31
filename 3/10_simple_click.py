#!/usr/bin/env python
"""
Simple Click example
"""
import click

# click.command > 함수가 명령줄 접근에 노출되어야함
# click.option > 같은 이름의 함수 파라미터(greeting,name)을 연결하여 인수로 추가

@click.command()
@click.option('--greeting', default='Hiya', help='How do you want to greet?')
@click.option('--name', default='Tammy', help='Who do you want to greet?')
def greet(greeting, name):
    print(f"{greeting} {name}")


if __name__ == '__main__':
    greet()