# diploma

### ИГРА 
### космическое сражение  

![IMAGE](https://github.com/SimonaSoloduha/diploma/blob/main/image_for_readme/Снимок%20экрана%202021-07-22%20в%2016.21.57.png)

## Установка необходимого ПО
Установка необходимых пакетов: pip install astrobox

Разработка диплома ведется на ЯП Python с применением
практик объектно-ориентированного программирования.

## Запуск игры
Для запуска игры необходимо запустить файл game.py 

## Основные положения 
Диплом реализуется в виде игры-модели, в которой надо писать код поведения объектов.

Поле игры - ограниченное космическое пространство, видимое на экране. Координаты объектов отсчитываются от левого нижнего угла экрана.

В центре поля - несколько астероидов с содержащимся в них ресурсом - фантастическим материалом элериумом.  Астероид содержит от 100 до 200 единиц элериума.

Космобаза расположена с краю экрана - это “порт приписки” дронов. Космобаза неподвижна и может хранить большое количество элериума (по крайней мере, весь элериум из всех астероидов поля игры).

Дрон-сборщик может летать по всему полю, собирать элериум
из астероидов и выгружать его в трюмы космобазы. Дрон может хранить и перевозить до 100 единиц элериума. 

## Цель игры 

собрать весь элериум за минимальное время.

## Описание программной модели

Напрямую, мышкой/клавиатурой, дроном управлять нельзя. Нужно писать код в классе-наследнике astrobox.core.Dron.

Чтобы начать какое-либо действие - надо вызвать метод дрона. Например, чтобы отправить дрон в путь надо вызвать метод-действие self.move_at(). 

В определенные моменты времени (например, при  достижении цели полета) будет вызвано соответствующее событие ( self.on_stop_at_asteroid() для события “дрон подлетел к астероиду”)

Для анализа ситуации в поле игры у дрона есть множество атрибутов - своё положение, положения астероидов, кол-во элериума в астероидах, и т.д.


## Методы дрона

turn_to(obj) - повернуться к объекту/точке
move_at(obj) - двигаться к объекту/точке
stop() – остановиться
load_from(obj) - загрузить элериум от объекта в трюм
unload_to(obj) - разгрузить элериум из трюма в объект
distance_to(obj) - рассчет расстояния до объекта/точки
near(obj) - дрон находится рядом с объектом/точкой

## События дрона 

on_born - рождение
on_stop_at_asteroid - дрон прилетел к астероиду
on_stop_at_mathership - дрон прилетел к космобазе
on_stop_at_point - дрон прилетел к точке-цели
on_load_complete - процесс загрузки элериума завершен
on_unload_complete - процесс разгрузки элериума завершен


## Атрибуты дрона 

coord - координаты собственного местоположения
direction - курс корабля
my_mathership - космобаза приписки
asteroids - список всех астероидов на поле
payload - кол-во элериума в трюме
free_space - свободного места в трюме
fullness - процент загрузки
is_empty - трюм пустой
is_full - трюм полностью забит элериумом

## Атрибуты астероида и космобазы

coord - координаты местоположения
payload - кол-во элериума

## Управление игрой 

Выход из игры: клавиша Q или закрытие окна игры.

Режим отладки: клавиша D. Выход из режима отладки:
клавиша D.

В режиме отладки: шаг игры - клавиша S, несколько
шагов игры подряд - зажатая клавиша G.

Замер производительности FPS: клавиша F.

