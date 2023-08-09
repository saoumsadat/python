str = input("Enter string: ");
num = int(input("Enter iteration time: "));

for x in range(0, num):
    print("%d %s" % (x + 1, str));