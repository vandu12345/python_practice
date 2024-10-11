def abc():
    deff()
    print("Hi")


def deff():
    xyz()
    print("Hello")

def xyz():
    print("gelo")


abc()

if __name__ == "__main__":  
    print ("File1 is being run directly") 
else:  
    print ("File1 is being imported") 