class Test:
    my_name = "Dominic"

    @classmethod
    def wtf_is_this(cls):
        print(Test.my_name) #what's the point of using cls then?
        print(cls.my_name)

    @staticmethod
    def print_message(msg):
        print(msg)

    def idk(self):
        print("HI")

t = Test()
t.idk()