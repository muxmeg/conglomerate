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

label start_schoolgirl:
 play music "audio/Homeless at the Ruins.mp3" fadeout 1.6 fadein 1.6
 scene bg city_road  with d
 show sf side hands_down closed sad smile at gr with d
 sf " Как тут тихо. И вокруг никого никого. "
 show sg front hands_down_scarf open sad happy at gl with d
 sg "А как же полицейские на дороге?"
 show sf front hands_down open calm smile at gr with d
 sf " Ну… Они там были, а тут вообще никого. "
 pause 1.6
 show sf side hands_up open raised frown at gr with d
 sf " И почему ты решилась на это путешествие?"
 show sg front hands_down_scarf closed calm smile at gl with d
 sg "Не знаю. Наверно потому, что мы давно никуда ходили вместе."

 hide sg
 hide sf
 with d

 "Дома глядели на пустынные улицы выбитыми стёклами. Покинутые в спешке, оставленные на растерзание природе."
 "Без людей они быстро пришли в негодность и стали памятником человеческих амбиций."
 "Пугающая пустота знакомых пейзажей отпечатывалась в сознании. Ведь когда-то тут была жизнь."
 "Она не кипела, как в столице, но она была. Кафе, магазинчики, частные дома и квартиры. Жизнь текла своим чередом. "
 "Но всё изменилось в один день."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " А давно это случилось?"
 show sf front hands_down open calm frown at gr with d
 sg "Почти десять лет назад."
 sf " Сколько же всего произошло с тех пор. Почему сюда никто не вернулся?"
 sg " Нельзя. Слишком опасно."
 sf " Не знаю. По-моему всё безопасно."

 hide sg
 hide sf
 with d

 "Авария пришла, когда её не ждали. Землетрясение вызвало сильные волны, которые обрушились на прибрежные территории."
 "Системы безопасности были нарушены. В считанные часы всё вышло из под контроля."
 "Сначала эвакуировались только ближайшие районы. Три километра, потом десять, а затем расширили и до двадцати."
 "Тех, кто жил дальше, попросили не выходить из жилищ."
 "Паника охватила население. Они спешно покидали опасную территорию, оставляя нажитое имущество. "
 "Говорят, кому-то пришлось переезжать больше шести рпз из-за того, что зону эвакуации постоянно расширяли. "
 "Про больницы страшно вспоминать."
 "Кто-то погиб в пути, кто-то вскоре после, кто-то из-за недостатка медицинской помощи."

 show sf front hands_down wide_open calm frown at gr with d
 show sg side hands_down_scarf open calm shout at gl with d
 sg " Подожди, у тебя шарф развязался."
 show sf side hands_down closed calm smile at gr with d
 show sg side hands_down_scarf open calm smile at gl with d
 " Остановилась и заново повязала свой шарф. Розовая ткань не только прекрасно смотрелась, но и хорошо грела."
 show sg side hands_up_scarf closed calm smile at gl with d
 "Именно поэтому мы когда-то выбрали эти шарфики."
 show sg front hands_down_scarf wide_open calm smile at gl with d
 sf " Ой, только сейчас заметила. Ты тоже в нём. "
 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm shout at gl with d
 sg " Я без него на улицу не выхожу."
 show sf front hands_down open calm smile at gr with d
 show sg front hands_down_scarf closed calm smile at gl with d
 sf "  Здорово! Мы настоящие шарфные подружки."
 hide sg
 hide sf
 with d
 pause 1.6
 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d
 sg " Мне кажется, нам стоит остановиться где-то здесь. Скоро станет темно. Да и есть немного хочется "
 show sf front hands_down open raised shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 sf " Но мы только только пришли. Давай хотя бы до следующей деревни дойдём."
 show sf side hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 "Мари ткнула пальцем в карту, которую я держала перед собой."
 show sf front hands_down open calm shout at gr with d
 sf " Вот, эта не так далеко. "
 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open sad shout at gl with d
 sg " По дороге слишком долго, нам придётся идти через лес."
 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open sad frown at gl with d
 sf " Трусишка Киоко! Трусишка Киоко! Боиться идти через лес."
 show sf front hands_down closed calm smile at gr with d
 show sg front hands_down_scarf open angry speak at gl with d
 sg " Я не… не боюсь. Просто хотела остаться на ночь в доме. А если мы не успеем, то нам придётся спать в лесу."
 show sf side hands_up calm smile at gr with d
 show sg front hands_down_scarf open angry speak at gl with d
 sf " Спать в палатке. Под открытым небом. В пустом пустом лесу. {p=0.8} Так романтично."
 hide sg
 hide sf
 with d
 show bg city_crossroads with d

 "Не знаю почему, но я всегда представляла себе это место, как старую выцветшую фотографию."
 "Чёрно-белый снимок, застывший во времени. Будто трагедия захотела сохранить на память ужас, который она учинила."
 "Но в действительности это место живо. "
 "Да, оно не блещет огнями ночного города или бескрайней палитрой зелёных оттенков вековых лесов. Но живёт. "
 "Природа забрала себе покинутое человеком место, дабы вновь восстановить. Новый виток цикла уничтожения и возрождения."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 sf " Ты сказала что-нибудь родителям?"
 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open shout at gl with d
 sg " Да."
 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 sf " И что же? Что ты пойдёшь гулять по закрытым территориям?"
 show sf front hands_down open calm smile at gr with d
 show sg front hands_down_scarf closed calm shout at gl with d
 sg " Нет конечно. Я сказала, что побуду у тебя. "
 show sf side hands_up closed calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 "Мари развернулась и пригрозила мне пальцем."
 show sf side hands_up open angry frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 sf " Айайай, врать родителям не хорошо, Киоко."
 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm sout at gl with d
 sg " А ты что сказала?"
 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm smile at gl with d
 sf " Что побуду у тебя."
 hide sg
 hide sf
 with d
 show bg woods_campfire_road with d
 play music "audio/Campfire.mp3" fadeout 1.6 fadein 1.6

 "Пейзаж сменился на более спокойный. Место, когда-то у них отобранное, вновь заняли животные. "
 "Пустой пустой лес встречал нас распростёртыми ветвями. Здесь снег лежал толстым слоем и приятнее хрустел под ногами . "
 play sound "audio/sound/snow.mp3"
 "Здесь птицы летали над головой. Здесь даже пробежала лисичка. "
 "Даже я не до конца понимаю, как решилась на это путешествие. Но услышав согласие от Мари, я поняла - это мой  шанс. "
 "Ведь в пути нужен попутчик, а в жизни – друг. "
 "У этого путешествия есть очень важная цель. Я уже очень давно хочу признаться ей в кое чём и здесь нам точно никто не помешает."


 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 sf " Киоко, а почему ты выбрала нашу старшую школу? Ведь были и поближе к твоему дому. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d
 sg " Ты первая выбрала, где будешь учиться. Вот я и подумала, что подруга лучше знает что нам подойдёт."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d
 sf " Получается ты выбрала школу, потому что её выбрала я?"

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d
 sg " Получается так."

 hide sg
 hide sf
 with d
 show bg woods_campfire_day with d

 "Солнце скрывалось за листвой. до деревни мы не дошли и пока не стало слишком поздно, решили развести костёр. "
 "Оставив рюкзаки мы начали собирать хворост."

 show sf side hands_down open angry shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Собирай сухие палки, иначе мы костёр не разведём."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Набрав достаточное количество, я вернулась к рюкзакам. Мари уже принесла немного хвороста и, видимо, ушла собирать дальше. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Я слышала скрип снега совсем близко и не переживала за подругу."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Теперь спички. И… {p=0.8} почти готово."
 # play sound "audio/sound/snowball.mp3"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Попала! Попала!"
 "Так вот зачем она ушла. Не продолжать собирать ветки, а подготовить снежную засаду."
 sg " Мариии!"

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "А лучшая снежная защита, это снежное нападение. Оставив костёр на потом, я принялась кидаться снежками в ответ. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 play sound "audio/sound/snowball.mp3"
 sf " Тебе просто повезло!"
 play sound "audio/sound/snowballplay.mp3"
 pause 1.6
 sf " Ну вот. Теперь я вся мокрая."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " А мне холодно."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Мари посмотрела на кучку палок, которые так и не были зажжены, а потом на меня."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Потому что нужно было разводить костёр. Тогда не пришлось бы мёрзнуть."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Нужно было меня не отвлекать. "

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Нужно… Нужно… "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Мне показалось, она поняла, что именно из-за неё костёр всё ещё не горит."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Нужно было не отвлекаться."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Но только показалось."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Хорошо, ты победила. Я разжигаю костёр, а ты ставишь палатки. Идёт?"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Палатку. Как ставиться твоя я не знаю. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d


 # pause 3.2
 scene bg woods_campfire_night with d
 play music "audio/Anaemia.mp3" fadeout 1.6 fadein 1.6

 "Разобравшись с костром и палатками мы принялись за еду. В рюкзаках было достаточно сладостей, "
 "но начался совместный ужин с бенто. Рис, рыба, овощи. Кажется ещё теплые. "
 "После долгой прогулки любая еда будет казаться особенно вкусной. А эта была просто божественна."
 sf " Закончилась."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Я просто люблю пить."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Получив флягу Мари принялась жадно пить содержимое. Я хотела её остановить, ведь у нас не так много воды с собой и если тратить запасы такими темпами, "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "то до конца путешествия может не хватить, но думаю ничего страшного, если Мари попьёт чуть больше чем могла бы."

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Ухх, хорошо пошла."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Ко мне вернулась на половину опустевшая фляга. Убрав её и другие вещи обратно в рюкзак, я полезла к себе в палатку. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Тушим костёр?"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Зачем? Ничего страшного не случится, если он потухнет, когда мы уснём, а спать будет теплее."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Спальных мешков было бы достаточно."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Ночь опустилась на лес. Тёплый свет костра тянулся к холодной луне. Маленькие огоньки заблестели на небе.  "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d



 "Вот оно, можно коснуться пальцами, пересчитать каждую каждую звёздочку. Такое же, как дома. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Всё это место будто изнанка, последствия, которые оставляет после себя человеческая жизнь, а небо всё равно такое же как дома. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d


 sf " Киоко, как думаешь, в тебя кто-нибудь влюблён?"

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Ещё не потухшее пламя выхватила из темноты мои покрасневшие щёчки. Надеюсь Мари этого не заметила."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Не знаю… Быть может кто-то из старых друзей. А в тебя?"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Думаю да."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " И кто же это?"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Тоже кто-то из старых друзей. "

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " И… И давно ты знаешь, об этой влюблённости?"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Не очень. Но я не думаю отвечать ему взаимностью."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Ему?!"

 show sf front hands_down open calm shout at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 sf " Давай я тебе завтра расскажу. Хорошо? Спокойной ночи."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Спокойной ночи."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm frown at gl with d

 "Зарывшись поглубже в спальный мешок, Мари быстро уснула. Я поспешила последовать за ней."

 show sf front hands_down open calm frown at gr with d
 show sg front hands_down_scarf open calm shout at gl with d

 sg " Завтра утром я ей обязательно во всём признаюсь признаюсь."
 hide sg
 hide sf
 with d


 play music "audio/Daiichi.mp3" fadeout 1.6 fadein 1.6
 scene black with close_eyes
 pause 3.2
 scene bg woods_campfire_night with open_eyes

 # show sf front hands_down open calm frown at gr with d
 # show sg front hands_down_scarf open calm frown at gl with d


 sf " Киоко!"
 # hide sg with d
 # hide sg with d
 "Всё произошло так быстро, я даже не успела понять. "
 "Ночь. "
 "Звёзды. "
 "Мы ложимся спать. "
 "И вот… "
 "Я выбралась из спального мешка так быстро, как только смогла. "
 "И только когда мои глаза полностью открылись, стало понятно почему кричит Мари."
 pause 1.6
 # show bg pig1
 "Кабан."
 "Страшный дикий кабан. "
 "Он пришёл чтобы забрать нашу еду?! "
 "Или избавить свою территорию от нас?!"
 "Я не знаю. "
 "Не было времени думать."
 "Схватив рюкзак, я привлекала его внимание и помчалась прочь."
 play sound "audio/sound/run.mp3"
 "Бежала."
 "Бежала без оглядки. "
 "Сквозь кусты, деревья, усилившийся снег."
 "Пока наконец не упёрлась в болото."

 show bg lake_storm with d

 "Большое, на сколько хватало глаз. "
 "Эту топь не обойти."
 "Особенно, когда тебя загнали в ловушку."
 "Небольшой островок земли выдававшийся в топь был абсолютно пустым. "
 "Ни деревьев, ни даже кустов."
 "С одной стороны трясина, с другой разъярённый звёрь."
 "Он визжал, хрюкал и бил копытом землю. "
 play sound "audio/sound/pig.mp3"
 # show bg pig2
 "Была, не была."
 play sound "audio/sound/jump.mp3"
 "Островок земли."
 "За ним ещё и ещё один."
 "Прыжок за прыжком я удалялась от берега."
 "На сколько глубока топь? "
 "Как далеко кабан? "
 "Где Мари?"
 "Не сейчас."
 "Потом."
 "Сейчас надо убежать как можно дальше."
 play sound "audio/sound/jump.mp3"
 "Усилившийся снегопад превращал болото в ровную белую гладь. "
 "Становилось всё труднее находить островки земли. "
 "Они всё меньше выделялись на белом покрове."
 "Нога соскользнула и я потеряла равновесие. "
 "Холодная, густая, мерзкая жижа обволокла ноги. "
 sg " Нет!"
 sg " Я не могу!"
 sg " Надо идти дальше!"
 "Слёзы, проступившие на глазах, потекли ручьём. "
 "Ситуация становилась всё хуже и хуже."
 play sound "audio/sound/snowwater.mp3"

 play music "audio/Death.mp3" fadeout 1.6 fadein 1.6

 "Обессиленная, я выбралась на другой берег. "
 "И сразу же села на землю. "
 "Снег не прекращал падать, засыпая всё вокруг."
 sg " Мариии!"
 sg " МАРИИИ!"
 "Я кричала. "
 "Кричала изо всех оставшихся сил. "
 "Но никто не отвечал."
 show bg night_sky with d
 sg " Неужели…"
 sg " Неужели она убежала."
 sg " А я? "
 sg " Как же я?"
 pause 3.2
 "Стало слишком холодно. Лишившись тепла костра и палатки, можно было очень быстро окоченеть. "
 "И даже адреналин, так активно ускоряющий сердцебиение, не помощник в таких условиях. "
 "Неподалёку хватало домов, которые могли защитить от ветра и снега. "
 "Просто необходимо укрыться в одном из них."
 sg " Нет."
 "Иначе просто занесёт снегом."
 sg " Пускай."
 "И ты хочешь умереть здесь? "
 "Умереть вот так?"
 sg " Да…"
 sg " Так будет лучше."
 "Кому?"
 "Тем кто найдёт тело?"
 "Твоим родителям?"
 "Друзьям?"
 "Близким?"
 "Мари?"
 sg " Всем."
 sg " Всем будет лучше, если я просто умру."


 scene black with close_eyes
 pause 3.2
 # play sound "audio/sound/crybabycry.mp3"

 play music "audio/Homeless at the Ruins.mp3" fadeout 1.6 fadein 1.6

 "Я помню, как мы впервый раз встретились."
 "Из-за переезда, мне пришлось поменять школу."
 "Класс дружелюбно принял меня, но в нём уже сформировались круги общения и ни в один меня не взяли."
 "Было грустно слышать дружелюбные приветствия, а потом весь день проводит в одиноком молчании. "
 "Всё изменилось, когда в класс вернулась Мари. Болезнь заставила её пропустить месяц учёбы. "
 "По её возвращению весь класс не мог дождаться, когда вновь сможет пообщаться с ней, но первым, с кем она заговорила, была я."
 "Тёплые воспоминания ускользающей жизни."
 "Они грели душу. "
 "А вместе с ней и всё тело."
 "Обволакивающим, мягким, шерстяным теплом."
 scene bg farm_night with open_eyes
 om " Эхх… Ещё бы чуть-чуть и на одного снеговика было бы больше. Хорошо, что тёплое одеяло нашлось."
 sg " А… Вы кто?"
 om " Думаю это сейчас не так важно. Сначало нужно тебя согреть и высушить."
 om " Ты же не хочешь простудиться?"
 "Я помотала головой.  "
 om " Вот и хорошо."
 "Старичок протянул руку и помог подняться. "
 "Кажется, силы окончательно покинули меня."
 om " Ничего не забыла?"
 sg " Нет."
 om " А шарф?  Вон тот. Не будем доставать?"
 "Он указал на розовый кусок ткани, лежавший на поверхности топи. "
 "Оставшись там, после моего падения, шарф заносился снегом, постепенно скрываясь с моих глаз."
 sg " Обойдусь без него."
 om " Как знаешь."
 scene bg black with d
 stop music  fadeout 5
 pause 1.6
 om " Я, кстати, Фуджимото."
 sg " Киоко."
 om " И что же ты здесь делаешь одна Киоко?"
 sg " Думаю это сейчас не так важно..."

 window hide
 pause(2)
 window auto
 jump start_oldMan
