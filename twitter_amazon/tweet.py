#!/usr/bin/env python
# coding: utf-8


import tweepy
import const

class Twitter:
    def __init__(self):
        self.CK=const.CK
        self.CS=const.CS
        self.AT=const.AT
        self.AS=const.AS

    def getApi(self):
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.AS)
        api=tweepy.API(auth)
        return api





import random
def getUrl():
    path='affiUrl.txt'
    with open(path,'r') as f:
        urlList = f.readlines()
        f.close()
    print(urlList)
    size=len(urlList)
    delFig=random.randint(0,size-1)
    url=urlList[delFig]
    urlList.pop(delFig)
    
    with open(path, 'w') as f:
        for url in urlList:
            f.write("%s" % url)
            
    url.replace('\n','')
    return str(url)



def main():
    url=getUrl()
    print(url)
    api=Twitter().getApi()
    api.update_status(url)

if __name__ == '__main__':
    main()




