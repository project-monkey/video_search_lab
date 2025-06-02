import importlib.util

def main():
    # 测试
    packages= ["torch","faisee"]
    for package in packages:
        if importlib.util.find_spec(package):
            print(f"{package} 已安装 (通过 importlib 检测)")
        else:
            print(f"{package} 未安装 (通过 importlib 检测)")

if __name__ == "__main__": 
    main()