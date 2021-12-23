import os 
path = os.getcwd()
for i in os.popen('ls'):
    try: 
        if len(os.listdir(f"{path}/{i[:-1]}")):
            os.system(f"rmdir {path}/{i[:-1]}")
    except NotADirectoryError:
        pass