class IdentifyingWood:

    def check(self, s, t):
        i = 0
        j = 0
        
        while i < len(s):
            if s[i] != t[j]:
                print (s[i], t[j], s, t)
                s = s[:i] + s[i+1:]
                
            else:
                print ("else", s[i], t[j], s, t)
                if (j==len(t)-1):
                    break;
                j += 1
                i += 1

            

        if (t in s):
            return "Yep, it's wood."
        else:
            return "Nope."
