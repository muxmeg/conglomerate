init python:
    config.mouse = { 'default' : [ ('images/mouse.png', 0, 0)] }
    import random
    def dosv (*args):
        d = random.randint(0,15)
        dd = random.randint(0,9)
        if d == 0 and dd == 0:
            dd = random.randint(1,9)
        res = str(d) + '.' + str(dd)
        if d < 5:
            col = '#03fc28'
        elif d >= 5 and d < 10:
            col = '#f5d60c'
        else:
            col = '#fc2003'
        return Text(res, size=80, color=col, font='LCDNOVA.TTF'), 1
init:
    image doza = DynamicDisplayable(dosv)
screen dozimetr:
    add "d.png" pos(1500, 10)
    add "doza" pos(1530, 40)

define fade = Fade(0.5, 0.0, 0.5)
image bg black = "#000"
define d = dissolve

define sc = Character("Ученая", color="#FFFFFF")
define sg = Character("Школьница", color="#FFFFFF")
define rtn = Character("Возвращенец", color="#FFFFFF")
define om = Character("Старик", color="#FFFFFF")
define mrd = Character("Убийца", color="#FFFFFF")
define sales = Character("Продавец", color="#FFFFFF")
define nvle = Character('', color="#FFFFFF", kind=nvl)


label start:

    ""
    #Часть без дозметра
    show screen dozimetr
    ""
    #Часть с дозиметром
    hide screen dozimetr
    ""
    #Вторая часть без дозиметра
    return
