# Change the value of DEBUG on line 6 to turn logging on or off

class debug():
    def log(*msg):

        DEBUG = True

        if DEBUG:
            print(*msg)
            