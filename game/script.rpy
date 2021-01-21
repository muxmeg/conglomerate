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
        if random.randint(0,1) and d > dd:
            d -= dd
        elif random.randint(0,1) and d > dd:
            d -= dd
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

init:
 $ close_eyes = ImageDissolve("images/eyes.png", 3.0, 50, reverse=True)
 $ open_eyes = ImageDissolve("images/eyes.png", 3.0, 50, reverse=False)
transform g:
 xalign 0.6
 yalign 1.0
 zoom 0.75
transform gr:
 xalign 0.7
 yalign 1.0
 zoom 0.75
transform gl:
 xalign 0.25
 yalign 1.0
 xzoom -0.75
 yzoom 0.75

define sc = Character("Элис", color="#FFFFFF", what_drop_shadow = (2, 1,), who_drop_shadow = (2, 1,))
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
default f1 = 0
default f2 = 0
default f3 = 0
default f4 = 0
default result = 2
default f = 1

#тестинг деда по нажатию g
screen g:
  key "g" action Jump("start_oldMan")
#



label start:

show screen g
show bg snowfield with d
"Пожалуйста,выберете героя повествования"
if f1 and f2 and f3 and f4 and f:
    $ f = 0
    $ renpy.notify("Поздравляем, вам открыт рут старика!")
    # renpy.imagemap is deprecated, use screens instead
    $ result = renpy.imagemap("cho3.png", "cho4.png", [
        (1, 1, 350, 1080, 1),
        (350, 1, 660, 1080, 2),
        (661, 1, 940, 1080, 5),
        (941, 1, 1515, 1080, 3),
        (1516, 1, 1919, 1080, 4)
    ], focus="imagemap")
elif f1 and f2 and f3 and f4:
  $ result = renpy.imagemap("cho3.png", "cho4.png", [
    (1, 1, 350, 1080, 1),
    (350, 1, 660, 1080, 2),
    (661, 1, 940, 1080, 5),
    (941, 1, 1515, 1080, 3),
    (1516, 1, 1919, 1080, 4)
    ], focus="imagemap")
else:
  $ result = renpy.imagemap("cho1.png", "cho2.png", [
    (1, 1, 535, 1080, 1),
    (535, 1, 940, 1080, 2),
    (940, 1, 1395, 1080, 3),
    (1395, 1, 1920, 1080, 4)
    ], focus="imagemap")
if result == 1:
    jump start_returner
if result == 2:
    jump start_schoolgirl
if result == 3:
    jump start_scientist
if result == 4:
    jump start_murderer
if result == 5:
    jump start_oldMan

    return
