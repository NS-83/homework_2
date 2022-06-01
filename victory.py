# Год рождения Пушкина -1799
# Год рождения Лермонтова - 1814
# Год рождения Гоголя - 1809
# Год рождения Тютчева - 1803
# Год рождения Некрасова - 1821

NUMBER_OF_QUESTIONS = 5

while True:
    right_answers = 0
    wrong_answers = 0
    born_year = input('Введите год рождения Пушкина: ')
    if born_year == '1799':
        right_answers += 1
    else:
        wrong_answers += 1
    born_year = input('Введите год рождения Лермонтова: ')
    if born_year == '1814':
        right_answers += 1
    else:
        wrong_answers += 1
    born_year = input('Введите год рождения Гоголя: ')
    if born_year == '1809':
        right_answers += 1
    else:
        wrong_answers += 1
    born_year = input('Введите год рождения Тютчева: ')
    if born_year == '1803':
        right_answers += 1
    else:
        wrong_answers += 1
    born_year = input('Введите год рождения Некрасова: ')
    if born_year == '1821':
        right_answers += 1
    else:
        wrong_answers += 1
    right_answers_percent = right_answers / NUMBER_OF_QUESTIONS * 100
    wrong_answers_percent = wrong_answers / NUMBER_OF_QUESTIONS * 100
    print(f'Количество правильных ответов: {right_answers}')
    print(f'Количество ошибок: {wrong_answers}')
    print(f'Процент правильных ответов: {right_answers_percent}')
    print(f'Процент ошибок: {wrong_answers_percent}')
    continue_answer = None
    while continue_answer != 'да' and continue_answer != 'нет':
        continue_answer = input('Сыграть ещё раз? (да/нет) ')
    if continue_answer == 'нет':
        break
