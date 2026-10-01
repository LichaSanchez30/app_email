from pathlib import *

url = Path(r'/home/licha-sanchez-30/Escritorio/todasLasFC')

for fc in url.iterdir():
    print(fc.suffix)

