import random
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

outcomes=['HEAD','TAIL']

head_img=mpimg.imread("./heads_image_resized.jpg")
tail_img=mpimg.imread('./tails_image_resized.jpg')

def show_img(result):
    if result=='H':
        plt.imshow(head_img)
        axis=plt.gca()
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        plt.show()
    else:
        plt.imshow(tail_img)
        axis=plt.gca()
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        plt.show()

def repeat():
    continuation=input("Do You Wish to Flip/Toss the Coin Again? Enter Yes or No: ")
    if continuation[0].lower()=='y':
        gameplay()
    else:
        print("\n\nThank You for Playing. We hope to See You Soon")

def gameplay():
    while True:
        start=input("Press 'F' on the Keyboard to Flip a Coin/Toss a Coin or alternatively, Press 'S' on the Keyboard to Stop the Game: ")
        if start.lower()=='f':
            print("The Coin has been Tossed. We wish you All The Best for Guessing ...")
        else:
            print("\n\nYou have Chosen to Stop the Game. Run the Code to Start Playing Again.")
            break
        user_guess=input("Guess Heads or Tails: ")
        user_guess_short=user_guess[0].upper()

        result=random.choice(outcomes)    

        if user_guess_short=='H' and result[0]=='H':
            print(f"Your Guess is HEADS \n AND \nThe Computer Generated Outcome is HEAD")
            print("\n\nCONGRATS! You are Eligible to Play the Next Round\n")
            show_img(result[0])
            repeat()
            break
        elif user_guess_short=='T' and result[0]=='T':
            print(f"Your Guess is TAILS \n AND \nThe Computer Generated Outcome is TAIL")
            print("\n\nCONGRATS! You are Eligible to Play the Next Round\n")
            show_img(result[0])
            repeat()
            break
        else:
            print(f"Your Guess is {user_guess.upper()} \n AND \nThe Computer Generated Outcome is {result}")
            print("\n\nSorry, You are not Eligible to Play the Next Round\n")
            repeat()
            break

gameplay()
