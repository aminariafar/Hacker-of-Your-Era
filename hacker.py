from PIL import Image
from io import BytesIO
import requests
import json
from requests.sessions import Session

def getCaptcha():

    global ses
    global digits
    captcha, res = "", True

    getc=ses.get("http://utproject.ir/bp/image.php")
    capFile = BytesIO(getc.content)
    capImg = Image.open(capFile)
    capArray = capImg.convert("L").load()
    capArray = [ [ capArray[i,j] for j in range(40)] for i in range(200)]

    digList= [0]*5
    for i in range(5):
        digList[i] = capArray[i*40:(i+1)*40]

    for j in range(5):
        for i in range(10):
            if digits[i]==digList[j]:
                captcha += str(i)
                break

    return captcha

def passwordSearch ( captcha ):

    global ses
    low, high = 0, 10**20 -1
    mid = (low+high)//2
    
    while low <= high:

        response = ses.post("http://utproject.ir/bp/login.php",data={"username":"610300017",
        "password":f"{mid}","captcha":captcha()})
        stat = json.loads(response.content)['stat']
        if stat==0:
            return mid
        elif stat==-1:
            low = mid+1
            mid = (low+high)//2
        elif stat==1:
            high = mid-1
            mid = (low+high)//2

ses=Session()

digits = [0]*10
for i in range(10):
    digitReq = requests.get(f"http://utproject.ir/bp/Numbers/{i}.jpg")
    digitFile = BytesIO(digitReq.content)
    digitImg= Image.open(digitFile)
    digitArray = digitImg.convert("L").load()
    digitArray = [ [ digitArray[k,j] for j in range(40)] for k in range(40)]
    digits[i] = digitArray

password = passwordSearch( getCaptcha() )

print(610300017)
print(password)