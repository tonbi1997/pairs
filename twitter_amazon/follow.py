#!/usr/bin/env python
# coding: utf-8


import tweepy
import const
from Twitter import Twitter
import re

def main():
    api = Twitter().getApi()
    with open('followCandidate.txt') as f:
        l = f.readlines()
        print(type(l))
        print(l)
    f.close()

    followList=[]
    for user in l:
        match = re.search(r'[a-zA-Z0-9]*', user)
        followList.append(match.group(0))
    
    print(followList)

    for i in range(1):
        try:
            api.create_friendship(followList[i])
        except:
            print('followed')
        followList.pop(i)
    with open('followCandidate.txt', 'w') as f:
        for user in followList:
            f.write("%s\n" % user)
            
    f.close()

if __name__ == '__main__':
    main()
