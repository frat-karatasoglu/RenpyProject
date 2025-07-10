define r = Character(_("Джо"), color="#0c30cc")
define s = Character(_("Сенсэй"), color="#0c30cc")
define m = Character(_("Монстр"), color="#0c30cc")


# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_background
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show joe normal

    # These display lines of dialogue.

    r "Добро пожаловать. Я Джо."

    r "Мы начинаем здесь хорошие историю. Вы готовы к этой истории?"

    r "Эта история не для тех, кто не любит приключений. Если вы не хотите присоединиться к приключению Джо, теперь хорошая возможность выйти."

menu:

    "Я готов. Итак, начнем!":

        jump hazir

    "Нет, я не люблю приключения":

        jump cikis

label hazir:

        scene bg_background

"Джо унаследовал загадочную карту от своего давно потерянного деда. Карта показывает потерянное сокровище. Чтобы получить карту, Джо должен отправиться в город своего деда и найти Сенсэя"
"Тогда мы начинаем давай поедем в город!"

menu:

    "Поехать в город":

        jump sehir

    "Нет, иди домой":
        jump cikis

label sehir:
    scene bg_town with fade
    show joe normal at left with moveinbottom
    r "Я наконец-то в городе, мне нужно найти Сенсзй"
"Идите сенсей домой, чтобы получить карту"

menu:

    "Пойти к нему домой":

        jump home

label home:
scene bg_home with fade
show joe normal at left with moveinbottom
r "Я думаю, это должен быть дом, все, кого я просил, показали сюда,надеюсь,Я надеюсь, что это правильный дом"

menu:

     "Входи в дом":

        jump inhome

label inhome:
scene bg_inhome with fade
show sensei normal at right with moveinright
show joe normal at left with moveinleft
s "Добро пожаловать в внук моего старого друга, я ждал тебя."
s "Мне так жаль слышать, что у вас есть карта, я думаю, что ты уже знаешь"
r "Я знаю, что пришел за картой"
s "Это путешествие будет очень трудным для тебя, сынок,это сокровище охраняет очень могущественный монстр"
s "Единственный способ получить сокровище - это убить монстра волшебным мечом"
s "Волшебный меч воткнут в камень глубоко в темном лесу"
s "Удачи тебе в этом путешествии"
r "Спасибо, сэр"
hide sensei normal
hide joe normal
"Джо идет в темный лес за мечом..."

menu:

   "Идти в темный лес":

       jump road

label road:
scene bg_road with fade
show joe normal at left with moveinleft
"Джо продолжает двигаться впередr"
scene bg_darkforest
show joe normal at left with moveinleft
r "Я наконец-то добрался до темного леса"

menu:

     "Идти в темный лес без страха.":

        jump temles

     "Если боишься идти в лес, иди домой":

        jump cikis

label temles:
scene bg_sword with fade
"Там меч взглянул на Иону во всей славе ее, и если бы ее сердце было чистым, то это был бы ее меч"
r "Этот меч, который мой дед давал мне, когда я был маленьким, я могу победить зверя и принести мир в мою деревню"
"Джо думает об этом и без труда вытаскивает меч из скалы и достигает конца леса в конце этой дороги двумя разными путями встречает нашего героя"
jump hazine



label hazine:
    scene bg_forest
show joe normal at left with moveinright
menu:
    r "Джо приходится выбирать между двумя разными путями."

    "Северная дорога":


        jump north

    "Южная дорога":

        jump south

label north:
     scene bg_river
"Джо, выбирает свой путь на север и должен пересечь реку."
show joe normal at right with moveinleft
r  "Боже мой, это выглядит так опасно, ну давай попробуем пересечь реку"
hide joe
scene bg_nehir
"Джо, пытаясь пересечь реку, он падает в ручей и падает в воду. У него есть выбор, чтобы избавиться от."
menu:
    "Придерживаться течения":
         "Дерево было сухим, поэтому ты сломался и утонул."
         jump cikis
    "Продолжать плавать со всей своей силой":
         "Джо поплыл изо всех сил и достиг берега"
         "Достигнув берега, он видит пещеру и движется к ней"
         jump south
label south:
     scene bg_cave
"Джо идёт в пещеру"
"Когда Джо входит в пещеру, он должен выбрать между двумя дорожками в пещере"
menu:
    "Проходить через световой туннель":
         scene bg_closed
         "Вы вышли из пещеры, потому что вошли в тоннель света. Дверь таинственной пещеры была закрыта. Пути назад больше нет..."
         menu:
             "иди домой":
              jump cikis
    "Пройти через страшный темный туннель":
         "Джо достает карту от своего деда, чтобы узнать, куда ему нужно идти"
         jump treasure

label treasure:
     scene bg_map
     "Перемещается, глядя на карту"
     scene bg_caveroad
     show joe normal at left
     r "Надеюсь, что я на правильном пути"
     r "Я продолжу идти немного дальше"
     scene bg_gold
     show joe o2 at left with moveinbottom
     r "Не могу поверить, сколько там золота"
     "Страшный голос слышен, и хранитель сокровищ замечает джону"
     show monster at right with moveinright
     m "Разве ты не знаешь, что это сокровище охраняется существом вроде меня, и что никто, кто сюда заходит, не выживает"
     "Джо внезапно достает нож и бросает на него свой сюрприз, говоря:"
     menu:
        "Я пришел убить тебя и забрать все сокровища":
         show joe sword at right with moveinleft
         hide monster
         "Джо убивает монстра волшебным мечом одним ударом."
         "Наш герой забирает сокровище и возвращается в деревню"
         menu:
             "Назад в деревню":
                 jump final
        "Я хочу заключить с тобой сделку":
         scene bg_tomb
         "Наш герой думал, что сможет заключить сделку с лжецом и хитрым монстром, но в тот момент, когда он обернулся, монстр проглотил его одним укусом"
         jump cikis
label final:
    scene bg_town
    show joe normal at left with moveinleft
    show sensei normal at right with moveinright
    s "Я знал, что ты вернешься"
    s "Ты спас деревню от этого монстра, а деревню от страданий"
    r "Спасибо, сенсей. это честь для меня"
    scene bg_final
    ""
label cikis:
return
