﻿
# ⚔️ Attack Machine

![](https://github.com/realaskaer/Scroll/blob/master/data/preview.png)

## Общая информация

Очень мощный инструмент в умелых руках. Практически полностью автоматизирован. С помощью этой тачки, вы сможете управлять 
фермой под любое количество аккаунтов во всех поддерживаемых сетях. Все настройки простые и понятные, ничего лишнего.
> Путь осилит идущий, а софт осилит любой деген🕵️

**Подробная [статья](https://teletype.in/@realaskaer/attackmachine) по работе с этим зверем**

## Основные особенности 

* **Автоматическая работа большинства модулей
  (не нужно настраивать каждый модуль отдельно)**
* **Автоматическое определение кошелька в Starknet**
* **Поддержка прокси (включая мобильные)**
* **Поддержка работы с базой данных (Google реализация)**
* **Rhino / LayerSwap / Orbiter (все L2 сети)**
* **Защита от Price Impact на всех DEX**
* **Рандомизация сумм/задержек/количества транзакций**
* **Плотнейшее логирование, даже ваш чих залогируется**
* **Полная статистика всех аккаунтов в таблице**
* **Автоматическая/ручная генерация маршрута**
* **Сохранение процесса для аккаунтов**
* **Gas чекер, Повторитель (при ошибках в модулях)**
* **Сбор не отработавших кошельков**
* **Сохранение логов в файлы по дням**
* **Софт знает дату дропа (WHEN?)**
* **Параллельный запуск**
* **Асинхронный ООП код**
* **EIP-1559**

***❗Благодаря настройке `AMOUNT_PERCENT` софт сам решает, какое количество и какие токены будут применяться для работы модулей.
Машина учитывает % только для нативного токена `ETH`, остальные токены(включая LP токены) обмениваются или выводятся из пулов на 100% от их баланса.


## 🧩Модули

    1.  OKX             (Депозит / Вывод / Сбор средств с субАккаунтов)                                       
    2.  LayerSwap       (Bridge по любым направлениям)
    3.  Orbiter         (Bridge по любым направлениям)    
    4.  Rhino           (Bridge по любым направлениям)   
    5.  Native bridge   (офф. мост Bridge / Withdraw)   
    6.  Upgrade Wallet  (обновление кошелька Starknet)
    7.  Deploy Wallet   (деплой кошелька Starknet)
    8.  Merkly          (Refuel во все сети из L2)
    9.  Bungee          (Refuel во все сети из zkSync, Base)
    10. Mute            (Свапы между стейблами и ETH + ввод и вывод ликвидности)                       
    11. SyncSwap        (Свапы между стейблами и ETH + ввод и вывод ликвидности)                         
    12. Maverik         (Свапы между стейблами и ETH + ввод и вывод ликвидности)             
    13. Velocore        (Свапы между стейблами и ETH)
    14. SushiSwap       (Свапы между стейблами и ETH)
    15. Uniswap         (Свапы между стейблами и ETH)
    16. XYfinance       (Свапы между стейблами и ETH)                                   
    17. Rango           (Свапы между стейблами и ETH)                                      
    18. OpenOcean       (Свапы между стейблами и ETH)                               
    19. 1inch           (Свапы между стейблами и ETH)                                                  
    20. zkSwap          (Свапы между стейблами и ETH)  
    21. Rango           (Свапы между стейблами и ETH)                                    
    22. SpaceFI         (Свапы между стейблами и ETH)   
    23. WooFI           (Свапы между стейблами и ETH)          
    24. veSync          (Свапы между стейблами и ETH)
    25. iZumi           (Свапы между стейблами и ETH)   
    26. PancakeSwap     (Свапы между стейблами и ETH)
    27. Velocore        (Свапы между стейблами и ETH)
    28. AVNU            (Свапы между стейблами и ETH)    
    29. Protoss         (Свапы между стейблами и ETH)
    30. SithSwap        (Свапы между стейблами и ETH)
    31. mySwap          (Свапы между стейблами и ETH)
    32. 10kSwap         (Свапы между стейблами и ETH)
    33. JediSwap        (Свапы между стейблами и ETH)
    34. EraLend         (Ввод и вывод ликвидности + вкл/выкл collateral)        
    35. Basilisk        (Ввод и вывод ликвидности + вкл/выкл collateral)
    36. ReactorFusion   (Ввод и вывод ликвидности + вкл/выкл collateral)
    37. zkLend          (Ввод и вывод ликвидности + вкл/выкл collateral)  
    38. LayerBank       (Ввод и вывод ликвидности + вкл/выкл collateral)  
    39. ZeroLend        (Ввод и вывод ликвидности)
    40. Nostra          (Ввод и вывод ликвидности)
    41. ZNS             (Минт домена для zkSync)
    42. ENS             (Минт домена для zkSync)
    43. Safe (Gnosis)   (Создание сейфа на zkSync и Base)
    44. MailZero        (Минт Free NFT)
    45. Zerius          (Минт / бридж NFT + Refuel во все сети из L2)
    46. Tevaera         (Минт двух NFT)
    47. Omnisea         (Создание коллекции)
    48. Starknet ID     (Минт Starknet identity)
    49. StarkStars      (Минт рандомной NFT)
    50. zkStars         (Минт рандомной NFT)
    51. Dmail           (Отправка сообщений)
    52. L2Telegraph     (Отправка сообщений + минт и брижд во все сети)
    53. Sending ETH to random addresses (Отправка пыли в ETH на рандомные адресса)
    54. Wrap/Unwrap ETH


## ♾️Основные функции

1.  **🤖Запуск прогона всех аккаунтов с автоматической генерацией маршрутов из Google таблицы**

    Если вы подготовили таблицу и включили сервисы на Google Cloud API, софт будет самостоятельно генерировать маршруты для всех аккаунтов по вашим настройкам и данным из таблицы.
    В гайде по настройке вы сможете найти разделе **Google SpreadSheet**, там подробно описано и прикреплен видео гайд, как все настроить. Очень полезная вещь, если под вашим контролем находиться более нескольких сотен аккаунтов.

2.  **🚀Запуск прогона всех аккаунтов по подготовленным классическим маршрутам**

    После генерации маршрута (Пункт #3 функций), софт запустит выполнение маршрутов для всех аккаунтов. Все варианты работы смотрите в разделе **Настройка софта**  

3.  **📄Генерация классических роутов для каждого аккаунта**

    Классический генератор, работает по дедовской методике. Вам нужно указать списки модулей в настройке `CLASSIC_ROUTES_MODULES_USING` и при запуске этой функции софт соберет вам маршрут по этой настройке. Поддерживается 
    `None` как один из модулей в списке, при его попадании в маршрут, софт пропустит этот список.

4. **💾Создание файла зависимостей ваших и OKX кошельков**

    Создает файл JSON, где привязываются ваши адреса к кошелькам OKX. Сделал для вашей безопасности. Софт сопоставляет
    к каждой строке в `OKX address` эту же строку в `Private Key` и если вы ошиблись, то всегда можно проверить это в 
    файле `okx_withdraw_list.json`, во избежания пересечений кошельков.

5. **✅Проверка всех прокси на работоспособность**

    Быстрая проверка прокси(реально быстрая, как с цепи срывается)

6. **📊Получение статистики для каждого аккаунта**

    Практически моментальное получение всей статистики по аккаунтам, даже если их больше 100 штук(не забудьте про прокси). Сделаны все необходимые
    поля. *На 02.12.2023 поддерживается только для zkSync*

7. **⏰WHEN?**

    Без комментариев

## 📄Ввод своих данных

### Все нужные данные необходимо указать в таблицу `accounts_data` в папке `/data`. Для каждого проекта необходим свой отдельный в лист. 
   1. **Name** - имена ваших аккаунтов, каждое название должно быть уникальным
   2. **Private Key** - приватные ключи от кошельков
   3. **Proxy** - прокси для каждого аккаунта. Если их будет меньше, софт будет брать их по кругу. Если прокси мобильные, то можно указать просто одну проксю.
   4. **OKX address** - адреса пополнения OKX. Для каждого кошелька необходимо указать адрес, иначе вывод не сработает.
   5. **Private Key EVM** - приватные ключи от EVM кошельков. Чтобы сделать бридж в Starknet необходим EVM кошелек. Можете их не указывать, но бриджи работать не будут.

Вы можете установить пароль на вашу таблицу и включить настройку `EXCEL_PASSWORD = True`. При активации пароля, софт будет требовать его ввести для дальнейшей работы. Полезно при работе на сервере.

## ⚙️Настройка софта

>Крайне рекомендую ознакомиться с этой **[статьей](https://teletype.in/@realaskaer/attackmachine)**, с ее помощью вы сможете настроить любую деталь в софте.

Все настройки вынесены в файл `settings.py`. Заходим в него и видим подробное описание каждого раздела.
Самые важные настройки продублирую здесь. 

1. Раздел `API KEYS`. Получите все API ключи. В разделе есть ссылки на сайты, где это нужно сделать
2. Раздел `GENERAL SETTINGS`. Внимательно прочитайте все описания и проставьте необходимые значения
3. Далее сверху вниз настройте все модули. К каждому модулю есть описание

### 📚Основные параметры

* `GLOBAL_NETWORK` - устанавливает основную сеть для работы софта
* `SOFTWARE_MODE` - определяет режим работы софта (параллельный или последовательный). Параллельный способен одновременно
крутить очень больше количество аккаунтов (необходимы прокси для аккаунтов, максимум 5-7 аккаунтов на 1 проксю, если проксей будет мало, то работа софта станет нестабильной из-за лимитов RPC). Последовательный режим работает как ручной прогон. Условно: депозит на аккаунт -> прохождение маршрута ->
вывод на OKX и так по кругу, для всех аккаунтов
* `ACCOUNTS_IN_STREAM` - устанавливает количество кошельков в потоке при асинхронном запуске (`SOFTWARE_MODE = 1`)
* `WALLETS_TO_WORK` - определяет какие кошельки будут работать. Варианты работы: Одиночный, Выборка, От Х до У, Все сразу. Подробнее в настройках.
* `SAVE_PROGRESS` - включает сохранение прогресса для аккаунтов
* `TELEGRAM_NOTIFICATIONS` - включает уведомления в Telegram
* `SOURCE_CHAIN_ZERIUS`, `SOURCE_CHAIN_MERKLY`, `DESTINATION_MERKLY_DATA`, `DESTINATION_BUNGEE_DATA`, `DESTINATION_BUNGEE_DATA` и `DESTINATION_ZERIUS` - определяют исходящий / входящий блокчейн(куда делаем refuel/бридж) и минимальную/максимальную
сумму для refuel. Также можно выбрать несколько сетей, софт выберет одну случайную.
* `AMOUNT_PERCENT`, `LIQUIDITY_AMOUNT`, `TRANSFER_AMOUNT` - благодаря этим параметрам, софт понимает, сколько % от вашего баланса ему необходимо использовать в модулях
в свапах, депозитах на лендинги и добавлении ликвидности. Более подробно описал [**здесь**](https://github.com/realaskaer/zkSync#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D0%BE%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8)
* `MIN_BALANCE` - устанавливает минимальный баланс для аккаунта, опустившись за который, софт будет выдаться ошибку о
недостаточном балансе на аккаунте `Insufficient balance on account!`
* `GAS_CONTROL` - включает/выключает контроль газа для каждого шага в маршруте
* `GAS_MULTIPLIER` - множитель газа, рекомендуемые значения: Starknet - 1.2 до 1.5 Остальные сети - 1. Этот параметр умножается на газ лимит, чтобы 
увеличить шанс успешного завершения транзакции.
* `MAXIMUM_RETRY` - количество повторных попыток при ошибках в модулях
* `PRICE_IMPACT` - определяет максимальный % для защиты от Price Impact. Если Price Impact будет больше, то модуль прекратит свап.
* `UNLIMITED_APPROVE` - выбор между бесконечными и точными апрувами
* `SLEEP_MODE` и `SLEEP_TIME_STREAM` - включает/выключает режим сна после каждого модуля и между аккаунтами. Включив параллельный режим софта и
выключив эту настройку, вы сможете лицезреть скорость данного аппарата
* `EXCEL_PASSWORD` - включает запрос пароль от таблицы с данными от аккаунтов
* `EXCEL_PAGE_NAME` - название листа в таблице с данными от аккаунтов

## 🤛🏻Реферальная программа

Внутри файла `сonfig.py` есть настройка `HELP_SOFTWARE`, если она включена (по умолчанию - включена), то от суммы вашей транзакции на любом агрегаторе (`ODOS`, `OpenOcean`, `1INCH`, `XYfinance`, `Rango`, `AVNU`) мне будет идти `1%`. Эту часть от объема транзакции переводит контракт агрегатора, а не ваш кошелек. Поэтому вы не будете иметь дел с моим кошельком.
Чтобы выключить эту функции, укажите значение `False` 


## 🛠️Установка и запуск проекта

> Устанавливая проект, вы принимаете риски использования софта для добывания денег(потерять жопу, деньги, девственность).

Как только вы скачаете проект, **убедитесь**, что у вас Python 3.10.11

Установка проекта

```bash
  git clone https://github.com/realaskaer/AttackMachine.git
```

Для установки необходимых библиотек, пропишите в консоль

```bash
  pip install -r requirements.txt
```

Запуск проекта

```bash
  cd attackmachine
  python main.py
```

## 🔗 Ссылки на установку Python и PyCharm

 - [Установка PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
 - [Установка Python](https://www.python.org/downloads/windows/) (Вам нужна версия 3.10.11)

## 🧾FAQ

#### Есть ли дрейнер в софте?

> Нет, но перед запуском любого софта, необходимо его проверять 

#### Что делать, если ничего работает?

> Сначала, прочитать README, если не получилось с первого раза, попытаться еще раз.

## ❔Куда писать свой вопрос?

- [@askaer.foundation](https://t.me/askaer) - мой канал в телеграм  
- [@askaer.chat](https://t.me/askaerchat) - ответы на любой вопрос
- [@askaer](https://t.me/realaskaer) - **при обнаружении бомбы в коде**  

## ❤️‍🔥Donate (Any EVM)

### `0x000000a679C2FB345dDEfbaE3c42beE92c0Fb7A5`
> Спасибо за поддержку❤️1111111
