import random
import string
import sys


def answer_rand(input_list, num_chars):
    s = []
    chars = ''.join(input_list)
    if (num_chars % 2) == 0:
        for i in list:
            j = random.sample(chars, k=1)
            t = random.sample(chars, k=1)
            s.append(j)
            s.append(t)
    else:
        for i in range(1):
            j = random.sample(chars, k=1)
            s.append(j)
        for i in range(len(list) - 1):
            j = random.sample(chars, k=1)
            t = random.sample(chars, k=1)
            s.append(j)
            s.append(t)
    s = [item for sublist in s for item in sublist]
    return ''.join(s)

def char_rand(total_chars, num_chars):
    l = []
    chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(total_chars - num_chars):
        l.extend(random.sample(chars, k=1))
    return ''.join(l)

def listmix(first_list, second_list):
    g = []
    if len(first_list) > len(second_list):
        max = len(first_list)
        maxli = first_list
    elif len(first_list) == len(second_list):
        max = len(first_list)
        maxli = []
    else:
        max = len(second_list)
        maxli = second_list
       
    k = 0
    y = 1
    for i in range(max):
        try:
            g.extend(first_list[k])
            g.extend(second_list[k])
        except IndexError:
            g.extend(maxli[k])
        
        k += 1
        y += 1
    g = [item for sublist in g for item in sublist]
    return ''.join(g)

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
        password = listmix(u, f)
        password_str = ''.join(password)
        print('Here is your password. every other character is a random character while the 1st, 3rd, 5th, etc., characters are from your answers.:', password_str)
    elif x == 8 or x == 9:
        y = str(input("What is your name?: "))
        z = str(input("What is your city of birth?: "))
        t = [y, z]
        u = answer_rand(t, r)
        f = char_rand(x, r)
        password = listmix(u, f)
        password_str = ''.join(password)
        print('Here is your password: ', password_str)
    elif x >= 14 or x <= 16:
        y = str(input("What is your name?: "))
        z = str(input("What is your city of birth?: "))
        a = str(input("What is your favourite food?: "))    
        b = str(input("What kind of pet do you want(ex. dog, cat, etc.): "))
        t = [y, z, a, b]
        u = answer_rand(t, r)
        f = char_rand(x, r)
        password = listmix(u, f)
        password_str = ''.join(password)
        print('Here is your password: ', password_str)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
