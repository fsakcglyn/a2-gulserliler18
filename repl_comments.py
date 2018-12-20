k = 0
pre_comments = []
while 1>=0 :
    n = input("Enter your comment: ")
    pre_comments = pre_comments + [n]
    print("Previously entered comments:")
    k = k + 1
    z = 0
    y = z + 1
    if n == "quit":
        break
    while y <= len(pre_comments):
        print(y,".",pre_comments[z])
        z = z + 1
        y = z + 1
