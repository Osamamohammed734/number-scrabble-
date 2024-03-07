# --------------------------  بسم الله الرحمن الرحيم   ---------------------------------

# CS112_A1_T2_2_20230718.py 

# Number scrabble : is played with the list of numbers between 1 and 9. Each player takes
#turns picking a number from the list. Once a number has been picked, it cannot be picked
#again. If a player has picked three numbers that add up to 15, that player wins the game.
#However, if all the numbers are used and no player gets exactly 15, the game is a draw.

# NAME : Osama Mohamed Hamed Sultan
# ID : 20230718

# ++++++++++++++++++++++++++  CONSTENTS  ++++++++++++++++++++++++++++++++++
counter_1 = 0
counter_2 = 0
listt = [1,2,3,4,5,6,7,8,9]
print(listt)
##
while True :
    if listt ==[]:
        print("##############  Draw  ##############")
#+++++++++++++++++++++++++++++  PLAYER_1 CODE  +++++++++++++++++++++++++++++++++++++
    player_1 =int(input("player_1 chose a number from the list above : "))
##
    while player_1 not in listt :
        player_1 =int(input("player_1 please chose a correct num : "))
##
    listt.remove(player_1)
    counter_1 = counter_1 + player_1
    print("NOW THE LIST IS : ",listt)
##
    if counter_1 == 15 :
        print ("############# player_1 winner ##############")
        break
##
    if listt ==[]:
        print("##############  Draw  ##############")
        break
#+++++++++++++++++++++++++++++++  PLAYER_2 CODE  +++++++++++++++++++++++++++++++++++++
    player_2 =int(input("player_2 chose a number from the list above : "))
    while player_2 not in listt :
        player_2 =int(input("player_2 please chose a correct num : "))
##
    listt.remove(player_2)
    counter_2 = counter_2 + player_2
    print("NOW THE LIST IS : ",listt)
##
    if counter_2 == 15 :
        print ("############# player_2 winner ##############")
        break