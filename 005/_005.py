﻿#Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». На главную роль нужен актёр обладающий всеми тремя качествами. Определите, сколько есть претендентов на главную роль.

a={'Илья', 'Федор', 'Семен', 'Олег', 'Лев', 'Антон', 'Артем', 'Боря', 'Демьян'}
b={'Илья', 'Георгий', 'Лев', 'Демьян', 'Антон', 'Владислав', 'Боря' 'Стас', 'Марк', 'Влад'}
c={'Федор', 'Георгий', 'Олег', 'Демьян', 'Артем', 'Елисей', 'Боря', 'Стас', 'Влад'}
print(a.intersection(b).intersection(c))