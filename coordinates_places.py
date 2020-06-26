#!/usr/bin/python2.7

import rospy
from std_msgs.msg import String
global akhil
global n
n=0


def traffic():
        global pub

        global akhil
        global n 

        global pub5

        sen=akhil
        ss="my task is "+sen
        
        pub5.publish(ss)
        
	v=['get','grasp','take','pick','deliver','put','place','tell','say','go','navigate','enter','find']
	pl=['exit','table','counter','kitchen','bedroom','living','corridor','office','dinning','bar','sink','hall','']
	po =['','6.728 0.024++','5.846 3.647+-','','4.150 3.339+-','','','','','','0.579 -2.09','2.1 3.1+-','']
        
        i=0
               
	j=0
	k=0
	verbs=['','','','','','']
	place=['','','','','','']
	person=['','','','','','']
	vas=['','','']
        words = akhil.split()
	print words
	while(i<len(words)):
   	    j=0
            
    	    while(j<len(v)):
                
        	if(words[i]==v[j]):
         
         		verbs[k]=v[j]
         		
         		k=k+1
         		break
       		j=j+1
    	   # print i   
    	    i=i+1
 
	i=0	
	k=0

	while(i<len(words)):
    	   j=0
           
    	   while(j<len(pl)):
                
       		if(words[i]==pl[j]):
         
         		place[k]=pl[j]
         		print po[j]
         		k=k+1
                        pub.publish(po[j])
         		break
       		j=j+1
    		#print i   
    	   i=i+1 



        print vas
        print place
        print verbs


        i=0
        

def traff(data):
    global n
    print "hiii"
    n=n+1
    traffic()
    
def akhil(data):
    global akhil
    akhil=data.data
    print data.data
    traffic()
    
    




def listener():
    global pub
    
    global pub5
    
    rospy.init_node('traffic1',anonymous=True)
    pub5 = rospy.Publisher('/recognized_speech', String, queue_size=10)
    
    rospy.Subscriber('/key',String,akhil)
    pub = rospy.Publisher('/posision', String, queue_size=10)
    
    rospy.spin()
    
    
    
    




if __name__=='__main__':
   listener()

