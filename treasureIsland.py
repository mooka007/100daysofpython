print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

                                                    .mMMMMm.
                                               .mMMMMMMMMMMMm
          ....                               .mMMMMMMMMMMMMMM.
       .mMMMMMm.                           .mMMMMMMMMMMMMMMMM'
     .mMMMMMMMM)                          .MMMMMMMMMMMMMMM/'
   (MMMMMMMMMM/                          .MMMMMMMMMMMM"'
  mMMMMMMMMMM/                           (MMMMMMMMM"'
 /MMMMMMMMMM/                            |MMMMMMMM/
 MMMMMMMMMM/                             MMMMMMMM/
(MMMMMMMMMM(                            /MMMMMMM/                        
 MMMMMMMMMM|                            |MMMMMM"
 \MMMMMMMMM\              .mmmm..      |MMMMM`
  \MMMMMMMMMM.          .mMMMMMMMMm..mMMMm.MM/
   \MMMMMMMMM\.       mMMMMMMMMMMMMMMMMMMMMMm`
     \MMMMMMMMM.    .mMMMMMMMM"""MMMMMMMMMMMMMm
      `?MMMMMMMMm  mMMMMMMMM"'    "MMMMMMMMMMMMm.
        `"MMMMMMMm/MMMMMMM/'        \MMMMMMMMMMMM.
          `\MMMMM/MMMMMM"'           `MMMMMMM"""Mm.
            `\MM/MMMMMM/             `MMMM"'   '\M.
              ./MMMMMM/'               `"'        '\
              /MMMMMMM'                             \
             /MMMMMMM/                              `,
            /MMMMMMMM                                |
           .MMMMMMMMM                                )
           (MMMMMMMM|                                |
           |MMMMMMMM|.                               )
           |MMMMMMMMM|          oOo    oOo.         .'                  
           |MMMMMMMMM|         (OOOo   OOOO.        /
           (MMMMMMMMM\          OOOO.  OOOO).      '
           \MMMMMMMMMM         `OOOO   `OOO'      /
     x..   `\MMMMMMMMMm         `OO"    _"'__    ./Mm._______
     \MMMmm.MM"'     '\           ..**"""""***. <"""",MMMM/'  .
      \MMMMMM'                   .**"     ,'****        ')mMMMM'
       `\MMM(                    (**.__.******"'         )MMM/
      xmm>MMM\                   `********""'           )M/'
       `\MMMMMm,                    """                ,'M'
            `-"Mm.                                   ./"'
                  `\.                              ,/'
                     `\.                       _,/'
                        `.        /`     _,-/"'
                         M\      ( \   /'
                         MMm.     `'  /
                         MMMMm.     ,'
                         MMMMMMMmmmMM                                                                                   
                         MMMMMMMmmmMM
                         MMMMMMMMMMMM
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ')
if choice1 == "right":
    print("Game Over! ")
elif(choice1 == "left"):
    choice2 = input('You\'re at ac crossroad, what do you want to do "swim" or wait : ')
    if choice2 == "swim":
        print("Game Over! ")
    elif( choice2 == "wait"):
        choice3 = input('You\'re at a crossdoor, which color of door do you like ? "Red", "Blue" or "Yellow" : ')
        if choice3 == "Red" or choice3 == "Blue":
            print ("Congratulations, Game Over!")
        else:
            print ('Sorry, But you win !.')
