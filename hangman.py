import help_list
import random

global selected_word
global user_play
selected_word = random.choice(help_list.country)
user_play = "".join(['_' if char != "" else "" for char in selected_word]) 

def wrong(wrongs):
    print(help_list.frames[wrongs])

def check_words(selected,user):
    if selected == user:
        return True
    else:
        return False

def won():
    print('you won! ')
def lost():
    print('you lost')

global guessed_wrong
guessed_wrong = 0
global guessed_chars
guessed_chars = []
print(user_play)
while(guessed_wrong < len(user_play)):
    if check_words(selected_word, user_play):
        won()
        break
    else:
        pass
    
    g_char = str(input('what character would you think is in word?'))
    if g_char in guessed_chars:
        print("you have guessed!!")
        continue
    else:
        guessed_chars.append(g_char)
    replaced = 0
    for index,char in enumerate(selected_word):
        if str(char) == g_char:
            user_play = user_play[:index] + g_char + user_play[index+1:]
            replaced += 1
    if replaced == 0:
        print('wrong guess')
        guessed_wrong += 1
        wrong(guessed_wrong-1)
        continue
    else:
        print(user_play)
else:
    lost()




