import re
set_number = int(input())
game_score = list()
set_score = list ()
mirko_wins = 0
slavko_wins = 0
match_result = 0

i=0
while i < set_number:
     game_score.append(input())
     set_score = re.findall(r'\d+', game_score[i])
     if int(set_score[0]) > int(set_score[1]):
         mirko_wins +=1
     elif int(set_score[0]) < int(set_score[1]):
         slavko_wins +=1
     i += 1

match_result = "{}:{}".format(mirko_wins,slavko_wins)
print(match_result)
