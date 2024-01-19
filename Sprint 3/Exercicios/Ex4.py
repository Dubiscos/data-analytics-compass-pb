for x in range(2,101):
    primo = 1
    for i in range(2,x):
        if(x % i == 0):
            primo = 0
    if (primo == 1):
        print(x)
