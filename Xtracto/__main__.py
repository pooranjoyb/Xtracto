import os
if __name__ == '__main__':
    os.chdir("Xtracto")
    os.system('python -m flask --app main --debug run')