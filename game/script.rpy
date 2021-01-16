init python:
    renpy.music.register_channel("d_sound", "sfx", True)
    config.mouse = { 'default' : [ ('images/mouse.png', 0, 0)] }
    import random
    def dosv (*args):
        d = random.randint(0,10)
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
init 0:
    image doza = DynamicDisplayable(dosv)
    ###Блок сборки спрайтов
    image alise_exmp = LiveComposite(
    #Что с размерами?
    (712, 1245),
    #Сборщику - убедиться в правильности пути
    (0,0), "images/alice/A/pose1.png",
    (0,0), "images/alice/A/br1.png",
    (0,0), "images/alice/A/ey1.png",
    (0,0), "images/alice/A/rt1.png"
    )
    ###Конец блока сборки спрайтов
screen dozimetr:
    add "d.png" pos(1500, 10)
    add "doza" pos(1530, 40)

define fade = Fade(0.5, 0.0, 0.5)
image bg black = "#000"
define d = dissolve
transform center:
        xalign 0.5 yalign -0.2

define sc = Character("Ученая", color="#FFFFFF")
define sg = Character("Школьница", color="#FFFFFF")
define rtn = Character("Возвращенец", color="#FFFFFF")
define om = Character("Старик", color="#FFFFFF")
define mrd = Character("Убийца", color="#FFFFFF")
define sales = Character("Продавец", color="#FFFFFF")
define guard = Character("Охранник", color="#FFFFFF")
define bf = Character("Такеши", color="#FFFFFF")
define nvle = Character('', color="#FFFFFF", kind=nvl)
define aka = Character("Акайо", color="#FFFFFF")
define sf = Character("Мари", color="#FFFFFF")



label start:

    ""
    #Часть без дозметра
    show screen dozimetr
    ""
    #Часть с дозиметром
    ###Убедиться в правильности пути
    play d_sound "audio/dozimetr.mp3"
    hide screen dozimetr
    ""
    #Вторая часть без дозиметра
    return
