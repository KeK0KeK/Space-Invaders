# Space-Invaders
Мой второй крупный проект в сфере программирования. Но первый залитый в GitHub. 
Проект представляет собой видеоигру "Space Invaders". Конечно, это не похоже на оригинал игры из-за некоторых моментов. 
Программа встречает пользователя открывшимся меню, где есть только две кнопки: "Новая игра" и "Выход". Первая кнопка запускает саму игру, где пользователь в виде пушки, должен уничтожить армию инопланетян. 
Роль игрока связана с уничтожением пришельцев. Для этого он может перемещаться по горизонтальной плоскости через кнопки A (влево) и D (вправо). Для уничтожения врагов у пушки есть снаряды в бесконечном количестве. Стреляя на кнопку SPACE игрок может как уничтожить их всех, либо они уничтожат его...
Инопланетяне, в отличии от оригинала, в этом проекте передвигаться строго сверху-вниз. Если хотя бы один инопланетянин коснётся пушки или долетит до земли (до конца экрана), то это засчитывается как победа инопланетян. Игрок же в этом случае проигрывает, но не сразу...
Игрок имеет некоторое количество "жизней" - попыток для уничтожения врагов. Однако, в проекте невозможно убить всех врагов - как только игрок сумеет уничтожить одну армию врагов, появится новая. В чём же тогда мотивация тратить свои силы и время в этой игре? "Мотивация быть самым быстрым и быть первым", - отвечу я.
В игре описан метод накопления очков. Каждый убитый враг вознаграждает тебя некоторым количеством очков. Каждая твоя игра (не попытка), накапливает с каждого врага все твои очки и сравнивает с лучшим счётом - счётом, который был получен кем-то до тебя. Ты же можешь стать тем, кто набьёт лучший счёт, который никто не сможет побить.
