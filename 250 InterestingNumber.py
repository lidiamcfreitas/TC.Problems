class InterestingNumber:
    def isInteresting(self, x):
        dic = {}
        l = len(x)
        for i in range(l):
            if x[i] not in dic:
                dic[x[i]] = [i]
            else:
                if (type(dic[x[i]]) != list):
                    return 'Not interesting'
                else:
                    if i-dic[x[i]][0]-1!=eval(x[i]):
                        return 'Not interesting'
                    dic[x[i]] = 0
        for elem in dic:
            if type(dic[elem])== list:
                return 'Not interesting'
        return 'Interesting'