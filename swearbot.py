import random
swear=open("foo.txt","r")
comeback=open("comebacks.txt","r")
s=swear.readlines()
c=comeback.readlines()
flag=1
for i in range(0,len(s)):
    s[i]=s[i].lower()
while flag==1:
    str=input("Insult me: ")
    str=str+'\n'
    if str in s:
        i=random.randint(0,len(c))
        print(c[i])
    q=input("Give up? (y/n)")
    if q=="y":
        flag=0
    elif q=="n":
        flag==1
    else:
        q=input("Give up? (y/n)")
