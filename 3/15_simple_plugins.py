#!/usr/bin/env python
import fire
import pkgutil
import importlib

def find_and_run_plugins(plugin_prefix):
    plugins = {}
     
    # 플러그인 발견 및 적재
    print(f"Discovering plugins with prefix: {plugin_prefix}")
    for _, name, _ in  pkgutil.iter_modules(): # pkgutil.iter_modules가 sys.path에서 사용 가능한 전체 모듈을 반환
        if name.startswith(plugin_prefix): # 이 모듈이 제시한 플러그인 접두사를 사용하는지 확인
            module = importlib.import_module(name) # importlib을 사용해 해당 모듈 로드 후 dict에 저장
            plugins[name] = module

    # 플러그인 실행
    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run() # 해당 플러그인의 run 메서드 호출

if __name__ == '__main__':
    fire.Fire()


