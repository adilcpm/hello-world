import time
def fibinocci(num):
    first=1
    second=1

    for i in range(num):

        yield first
        time.sleep(1)
        first,second = second,first+second

for num in fibinocci(10):
    print(num)
