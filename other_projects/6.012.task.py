import random, bext

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(OBJECT_PRONOUNS)
    place = random.choice(PLACES)
    return f'Ты не поверишь, что в {state} {noun} нашли в {pronoun} {place}.'

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    return f'Крупные компании ненавидят {pronoun}! Смотри как это делают {noun} в {state}.'

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS)
    when = random.choice(WHEN)
    return f'Без этого {noun} и {pluralNoun} убьют тебя {when}.'

def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f'Убивают ли миллениалы {noun} индустрию?'

def main():
    bext.clear()
    print('Наш веб-сайт должен заставлять людей смотреть рекламу обманом!')
    print()
    while True:
        response = input('Введите количество заголовков для кликбейта, которые необходимо сгенерировать: ')
        print()
        if not response.isdecimal():
            print('Вы ввели не цифры.')
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 4)

        if clickbaitType == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()

        print(headline)
    print()


OBJECT_PRONOUNS = ['её', 'его', 'их']
PERSONAL_PRONOUNS = ['Она', 'Он', 'Они']
STATES = ['Московской области', 'Чукотке', 'Ставропольском крае', 'Крыме', 'Владимирской области', 'Тульской области', 'Чеченской республике', 'Белгородской области', 'Республике Татарстан', 'Республике Коми']
NOUNS = ['спортсмен(ы)', 'клоун(ы)', 'доктор(а)', 'родитель(и)', 'кошка(и)', 'собака(и)', 'курица(ы)', 'робот(ы)', 'серийный(е) убийца(ы)', 'телефонный(е) экстрасенс(ы)']
PLACES = ['дом(е)', 'чердак(е)', 'банковской депозитной ячейке', 'школа(е)', 'подвал(е)', 'рабочем месте', 'магазине пончиков', 'бункер(е)']
WHEN = ['скоро', 'в этом году', 'сегодня позже', 'прямо сейчас', 'на следующей неделе']

if __name__ == '__main__':
    main()