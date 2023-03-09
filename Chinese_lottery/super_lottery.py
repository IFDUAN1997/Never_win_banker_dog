import random
"""模拟中国体育彩票 -- '超级大乐透' """
"""Try to simulate Chinese lottery game -- 'The super lottery' """

num_play = 1000000  # 设置投注次数

"""后边的不用改了, 直接run, 开始摇号！"""
i1, i2, i3, i4, i5, i6, i7, i8, i9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(num_play):
    # Generate the winning number
    winning_front = random.sample(range(1, 36), 5)
    winning_back = random.sample(range(1, 13), 2)
    winning_number = winning_front + winning_back

    # Generate the player number
    player_front = random.sample(range(1, 36), 5)
    player_back = random.sample(range(1, 13), 2)
    player_number = player_front + player_back

    # Check if the player is a winner
    if player_number == winning_number:
        prize = "First Prize"
        i1 += 1
    elif player_front == winning_front and len(set(player_back) & set(winning_back)) == 1 :
        prize = "Second Prize"
        i2 += 1
    elif player_front == winning_front:
        if len(set(player_back) & set(winning_back)) == 0:
            prize = "Third Prize"
            i3 += 1
        else:
            prize = "No Prize"
    elif len(set(player_front) & set(winning_front)) == 4 and len(set(player_back) & set(winning_back)) == 2:
        prize = "Fourth Prize"
        i4 += 1
    elif len(set(player_front) & set(winning_front)) == 4 and len(set(player_back) & set(winning_back)) == 1:
        prize = "Fifth Prize"
        i5 += 1  
    elif len(set(player_front) & set(winning_front)) == 3 and len(set(player_back) & set(winning_back)) == 2:
        prize = "Sixth Prize"
        i6 += 1
    elif len(set(player_front) & set(winning_front)) == 4 and len(set(player_back) & set(winning_back))== 0:
        prize = "Seventh Prize"
        i7 += 1
    elif (len(set(player_front) & set(winning_front)) == 3 and len(set(player_back) & set(winning_back))== 1) or (len(set(player_front) & set(winning_front)) == 2 and len(set(player_back) & set(winning_back))== 2):
        prize = "Eighth Prize"
        i8 += 1
    elif (len(set(player_front) & set(winning_front)) == 3 and len(set(player_back) & set(winning_back)) == 0) or (len(set(player_front) & set(winning_front)) == 2 and len(set(player_back) & set(winning_back)) == 1) or (len(set(player_front) & set(winning_front)) == 1 and len(set(player_back) & set(winning_back)) == 2) or (len(set(player_front) & set(winning_front)) == 0 and len(set(player_back) & set(winning_back)) == 2):
        prize = "Ninth Prize"
        i9 += 1
    else:
        prize = "No Prize"

    # Print the results
    print("Winning Number: ", sorted(list(winning_front)), "+", sorted(list(winning_back)))
    print("Player Number: ", sorted(list(player_front)), "+", sorted(list(player_back)))
    print("Prize: ", prize)

print("There are {} times 1st prize".format(i1))
print("There are {} times 2nd prize".format(i2))
print("There are {} times 3rd prize".format(i3))
print("There are {} times 4th prize".format(i4))
print("There are {} times 5th prize".format(i5))
print("There are {} times 6th prize".format(i6))
print("There are {} times 7th prize".format(i7))
print("There are {} times 8th prize".format(i8))
print("There are {} times 9th prize".format(i9))
print("in {} plays".format(num_play))
