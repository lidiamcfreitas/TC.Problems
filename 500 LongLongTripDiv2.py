class LongLongTripDiv2:
    
    def isAble(self,D,T,B):
        if (T>D):
        	return "Impossible"
        	
        P_i = D%B + D//B
	
        if (T-P_i>=0 and ((T-P_i) % (-1 + B) == 0)):
            return "Possible"
	
        else:
            return "Impossible"