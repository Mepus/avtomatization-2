def fizz_buzz(n):
    for l in range(0, n):
        print (l)
        if (l % 3 == 0):
            print ("Fizz")
        if (l % 5 == 0):
            print ("Buzz")
        if (l % 3 == 0) and (l % 5 == 0):
            print ("FizzBuzz")
fizz_buzz(16)
