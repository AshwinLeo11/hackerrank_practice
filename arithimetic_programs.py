# excercise 1 :

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# excercise 2 :

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# if else excercise 3 :

if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n%2==0:
        if n in range (2,6):
            print("Not Weird")
        elif n in range (6,21):
            print("Weird")
        else:
            print("Not Weird")
            




