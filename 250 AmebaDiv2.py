class AmebaDiv2:
    def simulate(self,X,A):
        for i in X:
            if i==A:
                A=A*2
        
        return A