print(r'''
*******************************************************************************
                           _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'                                                        
                                                              .-" .-. "-.
                                                            _/ '=(0.0)=' \_
                                                          /`   .='|m|'=.   `\
                                                          \________________ /
                                                      .--.__///`'-,__~\\\\~`
                                                     / /6|__\// a (__)-\\\\
                                                     \ \/--`((   ._\   ,)))
                                                     /  \\  ))\  -==-  (O)(
                                                    /    )\((((\   .  /)))))
                                                   /  _.' /  __(`~~~~`)__
                                                  //"\\,-'-"`   `~~~~\\~~`"-.
                                                 //  /`"              `      `\
*******************************************************************************
''')
print("Welcome to Treasure Island ... Are you a hero to fight Mr.Jack and get the treasure!")
print("Your mission is to find the treasure.")
user_choice = input('You\'re are the hero here so where do you want to go "Left" or "Right" \n Please choose one to start the adventure \n')

# Ensure that whatever is written is matching the needed scenario 'Left' Or 'Right'
if user_choice.lower() == "left":
    # Continue the game
    user_choice2= input('You\'ve come to Mr.Helper... Do you want to "fight" or you will "Swim" away? \n').lower()
    if user_choice2 == "swim":
        # Continue the game (Choose a door)
        user_choice3 = input('You\'re close to the treasure! Quick, pick a door: "Yellow" , "Red" or "Blue" '
                             '— and hope it’s not the one with the hungry dragon! \n').lower()
        if user_choice3 == "red":
            print("You had chosen a room full of fire ... Enjoy it 'Game Over!' ")
        elif user_choice3 == "yellow":
            print("You Found the treasure.... Yay 🥳")
        elif user_choice3 == "blue":
            print("You enter a room full of Avengers you got busted 🦸‍♂️... Game Over!")

        else:
            print("You had chosen a door that is not exist 🤷‍. Game Over!")

    else:
        print("You picked a fight, lost the battle, and… oops, you’re toast. GAME OVER!")


# Right path or Anything else the game is over!
else:
    print("A Kill-shot by Captain Jack Sparrow… Game Over! You're no hero!")
