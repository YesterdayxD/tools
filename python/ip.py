import os

# check ip 

for i in range(130,160):
    f=os.popen("ping -w 1 -c 1 10.7.11.{}".format(i)).read()
    #print(f)
    #print(f.find("100% packet loss"))
    if f.find("0 received")!=-1:
        print("10.7.11.{}".format(i))
