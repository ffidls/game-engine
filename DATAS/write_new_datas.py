def new_inf_for_button(pos, name_house):
    file = open('DATAS/INF_BUTTONS', 'w')
    str_inf = f'True {pos[0]} {pos[1]} {name_house}' if pos is not None else 'False -1 -1 None'
    print(str_inf, file=file)

    file.close()

