import requests,random,time

cookies = open('cookies.txt','r').readlines()
sess = requests.session()
def checkaccs():
 for i in cookies:
  try:
   i = i.strip()
   cookies = {'.ROBLOSECURITY': i}
   response = sess.get(url='https://www.roblox.com/my/account/json',cookies=cookies)
   friends = sess.get(url='https://friends.roblox.com/v1/my/friends/count',cookies=cookies)
   friends = friends.json()
   response = response.json()
   print('UserId:' , response['UserId'] , '| Username:',response['Name'],'| Friends:',friends['count'])
  except:
    print(i)
input("Press Enter To Continue")
checkaccs()
