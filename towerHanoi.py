def towerHanoi(n,s,t,i):
    if n is 1:
        print ("Move disk " + "1 " + "from " + s + " to " + t)

    else:
        towerHanoi(n-1,s,i,t)
        print ("Move disk " + str(n) +" from " + s + " to " + t)
        towerHanoi(n-1,i,t,s)
       
towerHanoi(4,'s','t','i')