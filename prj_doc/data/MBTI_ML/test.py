import sys

print ("HELLO" + sys.argv[1])

def testprint(a):
    a = sys.argv[1]
    # print(a)

    return a

print(testprint(sys.argv[1]))