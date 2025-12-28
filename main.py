from puppy import Puppy 
import check_input 

def main():
    """
    this function represents the puppy and take commands from the user.     
    """
    puppy = Puppy()
    print("Congratulations on your new puppy!")

    done = False 
    while not False:
        print("\nWhat would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")

        user_input = check_input.get_int_range("Enter Choice: ", 1 , 3)

        if user_input == 1:
            print(puppy.give_food())
        elif user_input == 2:
            print(puppy.throw_ball())
        elif user_input == 3:
            print("Goodbye!")
            break
main()
