class MicroStrings:
    def makeMicroString(self, A, D):
        a = ''
        i = 0
        result = []
        while (A-i*D>=0):
            result += [A-i*D]
            i +=1
        l = len(result)
        for j in range(l):
            a += str(result[j])
        
        return a