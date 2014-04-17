class TaroString:
    def getAnswer(self, S):
        got_c = False
        got_a = False
        got_t = False
        
        for elem in S:
            if elem=='C' and not got_c:
                got_c = True
            elif elem=='C' and got_c:
                return 'Impossible'
            
            if elem=='A' and not got_a:
                got_a = True
            elif elem=='A' and got_a:
                return 'Impossible'
            
            if elem=='T' and not got_t:
                got_t = True
            elif elem=='T' and got_t:
                return 'Impossible'
            
            if (elem=='A' or elem=='T') and not got_c:
                return 'Impossible'
            if elem=='T' and not got_a:
                return 'Impossible'
            
        
        if got_c and got_a and got_t:
            return 'Possible'
        else:
            return 'Impossible'