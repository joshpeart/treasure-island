import os

os.system('clear')

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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
input("Press 'Enter' to Continue")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
os.system('clear')
print("You are walking along the island on a very sunny hot day.")
direction=input("You have arrived at a fork in the road.  Which direction should you travel?  Type 'Left' to turn left.  Type 'Right' to turn right: ").lower()

os.system('clear')

if direction == "left":
    print('''

                                                            ---\=,__,>,_`-.     |
       :  |  `"""V#######,,_ `-  ""##################' --z--;" /_/  `. `.   |
          |          `/"""".`|`|| } }|.""""""""|"""""  --'//`/'  `    \  '. |
    :          :      |:     ||   |  |  :   :  |   :   ,_\---_\._   :  `.\ |/
                   :  /  :   |  |   || :  :      :    //--'> ___ ``-,_   \  \
         `"^            :  ` ||   || |   :  :         '=-`',' / `-, __`-. |
      :    :          : :  : |  |    ||    :     ---  //7;<\     / ,--._ ` |
         .,      :        :  |   ||| || '       :     -/;\'/` -='/|(    \ \
        %#'            :    `| |||    |  :   :      :  // '\   // | `    | |
    :         :   `'   :  :  || # | |||    :            `    .        :  | 
                         :   | ||#|#| | ':    :    :             :       ` 
         '#"      :   :    : | ||,|, ||   :      /        :           |:  ||
  ""'                    :  \\|\ X XX///`      :|   :    |   :      : |   |
''')
    action=input("You find a walking path along a river and eventually see a beautiful waterfall.  This is where you are to be meeting your fellow adventurer 'Chip Baskets' but he is not here yet.  Its quite hot outside today. What do you want to do?  Type 'Wait' to remain where you are until he arrives or type 'Swim' to take a dip in the water: ").lower
    os.system('clear')
    if action == "wait":
        transition=input("You take a short nap and awake to your friend 'Chip' arriving.  He tells you that the treasure is up a little further along the river.  The two of you journey on.  Press 'Enter' to continue")
        door=input("You and Chip come across a castle that has 3 doors.  Chip says that behind one of these doors is the treasure and behind the other two is the fate of death.  Which door shall you open?  Type 'Red' for the red door, type 'Blue' for the blue door, or type 'Yellow' for the yellow door").lower()

        if door == "yellow":
            print('''

                  ."`".		      '."""""""""""""""""`.
              .-./ _=_ \.-.	        `.       ...       `
             {  (,(oYo),) }}	          `.    /@  `.       `.
             {{ |   "   |} }	           .'"":_    :"""""".'|
             { { \(---)/  }}	         .'//)/) `  (/)/)).'  |
             {{  }'-=-'{ } }	       .'/)_/""   __ ""\.'  ^ |
             { { }._:_.{  }}	      |"""(((""""((("""|    | |
             {{  } -:- { } }	      |    ""     ""   |  U | |
       jgs   {_{ }`===`{  _}	      |  High Quality  |  P  .'
            ((((\)     (/))))	      |___ Bananas_____|   .'

Congratulations!  You found the treasure!  A lifetime supply of 'High Quality Bananas'!  And it is revealed that you are indeed a Gorilla.  Hoping you would have found gold?  Not this Gorilla.  And you lived happily ever after.
''')
        elif door == "red":
            transition=input("Chip opens the red door and the two of you walk down a long hallway.  The door closes behind you.  Press 'Enter' to continue: ")
            print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 You hear a click and all of a sudden flames shoot up from the floor.  You and Chip try to escape through the red door but it is locked.  GAME OVER!!!''')  
        else:
                print('''
                                             ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
   -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
    -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```               

You open the blue door and out jumps a gigantic demon with long claws that devours both you and Chip.  GAME OVER!!! 
''')
    else:
        print('''
                                    _
                                    (_)
              |    .
          .   |L  /|   .          _
      _ . |\ _| \--+._/| .       (_)
     / ||\| Y J  )   / |/| ./
    J  |)'( |        ` F`.'/        _
  -<|  F         __     .-<        (_)
    | /       .-'. `.  /-. L___       
    J \      <    \  | | O\|.-'  _   
  _J \  .-    \/ O | | \  |F    (_) 
 '-F  -<_.     \   .-'  `-' L__    
__J  _   _.     >-'  )._.   |-'  
`-|.'   /_.           \_|   F    
  /.-   .                _.<     
 /'    /.'             .'  `\    
  /L  /'   |/      _.-'-\
 /'J       ___.---'\|
   |\  .--' V  | `. `
   |/`. `-.     `._)
      / .-.\
      \ (  `\
       `.\
''')
        print("You jump into the water.  The water feels cool and feels nice on this hot day.  A female blowfish takes a liking to you.  The blowfish also happens to have magical powers which she uses to cast a spell on you.  You are transformed into a handsome blowfish.  The two of you marry and have little blowfish children.  GAME OVER!!!")
else:
    print('''
************************************
       ---_ ......._-_--.
      (|\ /      / /| \  \
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\
       `/'\__/      \ _ _ \*\
      /^|            \ _ _ \*
     '  `             \ _ _ \
                       \_)
************************************
''')
    print("You fall into a deep, dark hole.  You light your torch and see in front of you a deadly, poisonous snake.  It bites you and you die.  GAME OVER!!!")
