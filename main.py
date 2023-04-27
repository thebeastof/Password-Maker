import random
import string
import sys


def answer_rand(list, num_chars):
    s = []

    if (num_chars % 2) == 0:
        for i in list:
            j = random.sample(i, k=2)
            s.append(j)
    else:
        j = random.sample(i, k=1)
        s.append(j)
        for i in range(len(list) - 1):
            j = random.sample(i, k=2)
            s.append(j)
    return s

def char_rand(total_chars, num_chars):
    l = []
    chars = string.ascii_letters + string.digits
    for i in range(total_chars - num_chars):
        l.append(random.choice(chars))
    return l

def listmix(first_list, second_list):
    g = []
    if len(first_list) > len(second_list):
        max = len(first_list)
        maxli = first_list
    elif len(first_list) == len(second_list):
        max = len(first_list)
    else:
        max = len(second_list)
        maxli = second_list
       
    x = 0
    y = 1
    for i in range(max):
        try:
            g.append(first_list[x])
            g.append(second_list[x])
        except IndexError:
            g.append(maxli[x])
        
        x += 1
        y += 1

    return str(g)

def main():
    x = int(input("How many characters do you want your password to be(must be 8-16 characters for the program to work)?: "))
    r = x//2

    if x >= 10 and x <= 13:
        y = str(input("What is your name?: "))
        z = str(input("What is your city of birth?: "))
        a = str(input("What is your favourite food?: ")) 
        t = [y, z, a]
        u = answer_rand(t, r)
        f = char_rand(x, r)
        print(listmix(u, f))
    if x == 8 or x == 9:
        y = str(input("What is your name?: "))
        z = str(input("What is your city of birth?: "))
        t = [y, z]
        u = answer_rand(t, r)
        f = char_rand(x, r)
        print(listmix(u, f))
    if x >= 13 or x <= 16:
        y = str(input("What is your name?: "))
        z = str(input("What is your city of birth?: "))
        a = str(input("What is your favourite food?: "))    
        b = str(input("What kind of pet do you want(ex. dog, cat, etc.): "))
        t = [y, z, a, b]
        u = answer_rand(t, r)
        f = char_rand(x, r)
        print(listmix(u, f))
    if x > 16 or x < 8:
        sys.exit()


if __name__ == "__main__":
    main()
