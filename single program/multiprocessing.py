import multiprocessing
import requests
def downloadfile(url,name):
    respose = requests.get(url)

    open(f"file{name}.jpg","wb").write(respose.content)

url = "https://picsum.photos/2000/3000"

for i in range(5):
    downloadfile(url,i)