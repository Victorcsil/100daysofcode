# DAY 4 PROJECT
import random


shapes = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "paper": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

while True:
    input_player = input("Choose between rock, paper, and scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    if input_player == "rock" and computer == "scissors":
        print(shapes[input_player])
        print(f"Computer chose {computer}")
        print(shapes[computer])
        print("You win!")
    elif input_player == "scissors" and computer == "paper":
        print(shapes[input_player])
        print(f"Computer chose {computer}")
        print(shapes[computer])
        print("You Win!")
    elif input_player == "paper" and computer == "rock":
        print(shapes[input_player])
        print(f"Computer chose {computer}")
        print(shapes[computer])
        print("You Win!")
    elif input_player == computer:
        print(shapes[input_player])
        print(f"Computer chose {computer}")
        print(shapes[computer])
        print("It's a draw!")
    else:
        print(shapes[input_player])
        print(f"Computer chose {computer}")
        print(shapes[computer])
        print("You lost!")