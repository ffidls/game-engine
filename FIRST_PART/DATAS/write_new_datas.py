def new_condition_anna(condition):
    file = open('FIRST_PART/DATAS/DATA_ANNA/condition_anna', 'w')
    print(condition, file=file)
    file.close()


def new_side_user(side):
    file = open('FIRST_PART/DATAS/DATA_ANNA/side_move', 'w')
    print(side, file=file)
    file.close()


def new_condition_kira(condition):
    file = open('FIRST_PART/DATAS/DATA_KIRA/condition', 'w')
    print(condition, file=file)
    file.close()


def new_count_location_dog(count):
    file = open('FIRST_PART/DATAS/DATAS_DOGS/count_location', 'w')
    print(count, file=file)
    file.close()


def new_inf_for_button(pos, name_house):
    file = open('FIRST_PART/DATAS/INF_BUTTONS', 'w')
    str_inf = f'True {pos[0]} {pos[1]} {name_house}' if pos is not None else 'False -1 -1 None'
    print(str_inf, file=file)
    file.close()


def new_inf_dialog(name_dialog, count):
    file = open('FIRST_PART/DATAS/INF_DIALOG', 'w')
    print(f"{name_dialog} {count}", file=file)
    file.close()


def new_num_location(num):
    file = open('FIRST_PART/DATAS/DATAS_LOCATIONS/count_now_location', 'w')
    print(num, file=file)
    file.close()


def new_condition(condition, new_data):
    file = open('FIRST_PART/DATAS/DATAS_DOGS/INF_CONDITION', 'w')
    if ')' in str(new_data):
        new_str = f'{condition}@{new_data[0]} {new_data[1]}'
    else:
        new_str = f'{condition}@{new_data}'
    print(new_str, file=file)
    file.close()


def new_count_sprite(count, name_people='ANNA'):
    file = open(f'FIRST_PART/DATAS/DATA_{name_people}/count_sprite', 'w')
    print(count, file=file)
    file.close()


def new_condition_game():
    file = open(f'FIRST_PART/DATAS/condition_game', 'w')
    print('end', file=file)
    file.close()
