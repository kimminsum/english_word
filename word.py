from typing import NamedTuple

# structure
class User(NamedTuple):
    li: list
    running: bool

def start():
    lines = word.readlines()
    for line in lines:
        var.li.append(line.rstrip())

def judge(contry, enorkor): # enorkor == 1 write kor
    for i in range(len(var.li)//2):
        print(var.li[i*2+(enorkor-1)])
        answer = str(input('***write down %s plz***\n' % (contry)))
        if answer == var.li[i*2+(enorkor%2)]:
            print('!!!You correct!!!')
        elif answer != var.li[i*2+(enorkor%2)]:
            print('The answer is ***%s***' % var.li[i*2+(enorkor%2)])

if __name__ == '__main__':
    var = User(li=[], running=True) # var setting
    word = open('word.txt', 'r', encoding="UTF8") # open the korean file
    start()
    while var.running:
        selection = str(input('***select KOR or EN***\n')) # write 1 == write kor
        if selection == 'KOR': # write kor and correct en
            judge(contry='KOREAN', enorkor=1)
        elif selection == 'EN': # write en and correct kor
            judge(contry='ENGLISH', enorkor=2)
        else:
            pass
    word.close()