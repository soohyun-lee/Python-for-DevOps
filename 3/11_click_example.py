#!/usr/bin/env python
"""
Command line tool using click
"""
import click

@click.group() # 최상위 그룹 생성
def cli(): # 최상위 그룹 역할의 함수 생성, click.group 메서드가 함수를 그룹으로 전환
    pass

@click.group(help='Ship related commands') # ships 명령을 보유할 그룹 만들기
def ships():
    pass

# ships 그룹을 최상위 그룹의 명령으로 추가 > cli 함수는 이제 add_command 메서드와 한 그룹
cli.add_command(ships)

# ships 그룹에 명령 추가. ships.command는 click.command 대신 사용
@ships.command(help='Sail a ship') 
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

@ships.command(help='List all of the ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")


@cli.command(help='Talk to a sailor') # cli 그룹에 명령 추가
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli() # 최상위 명령 호출