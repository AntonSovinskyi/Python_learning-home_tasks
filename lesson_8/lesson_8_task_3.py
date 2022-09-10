"""Create a function called make_operation, which takes in a simple
 arithmetic operator as a first parameter (to keep things simple let it only
 be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
 as the second parameter. Then return the sum or product of all the numbers
  in the arbitrary parameter.


  """


def make_operation(arg_, *args):
    if arg_ == '+':
        return sum(args)

    elif arg_ == '-':
        subt = args[0]
        for i in range(len(args) - 1):
            subt -= args[i + 1]
        return subt

    elif arg_ == '*':
        mult = 1
        for j in args:
            mult *= j
        return mult

    else:
        print('Ooops, something wrong. Try again.')


print(make_operation('%', 5, 5, -10, -20))
