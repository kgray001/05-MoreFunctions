###############################################################################
#
#   As you saw in the quiz for today's class, functions can call other
#   functions.
#
#   Go through this code line by line and predict what will be printed. Notice
#   how the first line that runs is actually the last line "main()", because it
#   is the first line that is not part of a definition. This line calls the
#   main() function which then gets the ball rolling.
#
#   Once you have made a prediction of what will print when this code runs, run
#   it for yourself.
#
#   If you are surpirsed by anything try to figure out why it did what it did.
#   If you get stuck please ask questions.
#
#   Once you understand this code, then move on to the next module.
#
###############################################################################

def main():
    hello("Snow White")
    goodbye("Bashful")
    hello("Grumpy")
    hello("Sleepy")
    hello_and_goodbye("Magic Mirror", "Cruel Queen")


def hello(friend):
    print(f"Hello, {friend} - how are things?")


def goodbye(friend):
    print(f"Goodbye, {friend} - see you later!")
    print('   Ciao!')
    print('   Bai bai!')


def hello_and_goodbye(person1, person2):
    hello(person1)
    goodbye(person2)


main()
# hello, snow white-how are things? goodbye bashful-see you later! Ciao! Bai Bai! hello grumpy-how are things? 
# hello sleepy-how are things? hello magic mirror-how are things? goodbye cruel queen-see you later! ciao! bai bai!