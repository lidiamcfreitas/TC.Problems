class Time:
    def whatTime(self, seconds):
        return "{}:{}:{}".format(seconds//3600 % 60,seconds//60 % 60,seconds % 60)
