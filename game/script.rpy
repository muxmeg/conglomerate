label splashscreen:
    scene red_flags with Dissolve(5.0)
    with Pause(5)
    scene bg campfire with Dissolve(5.0)
    with Pause(1)
    return

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
        return Text(res, size=80, color=col, font='LCDNOVA.TTF'), 5
    def fire(*args):
        d = random.randrange(1,4)
        dd = random.randrange(1,2)
        return [d, dd]
        fire()
init:
    image mm animated:
        "images/bg/bg campfire.jpg" with dissolve
        pause fire()[0]
        "images/bg/bg campfire2.jpg" with dissolve
        pause fire()[1]
        repeat
init:
    image mm animated b:
        "images/bg/bg campfire.jpg" with dissolve
        pause fire()[0]
        "images/bg/bg campfire2.jpg" with dissolve
        pause fire()[1]
        repeat
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
transform left:
        xalign 0.1 yalign -0.2
transform right:
        xalign 0.95 yalign -0.2
transform very_right:
        xalign 1.15 yalign -0.2

define sc = Character("Ученая", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define sg = Character("Киоко", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define rtn = Character("Модору", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define om = Character("Старик", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define mrd = Character("Китамура", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define sales = Character("Продавец", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define guard = Character("Охранник", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define bf = Character("Такеши", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define nvle = Character('', color="#FFFFFF", kind=nvl, what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define aka = Character("Акайо", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define sf = Character("Мари", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define un = Character("Незнакомец", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
define unf = Character("Незнакомка", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))



label start:

    return
