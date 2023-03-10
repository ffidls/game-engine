import FIRST_PART.DATAS.const
import FIRST_PART.MECHANICA.check_moving


class MOVING:
    def __init__(self):
        self.speed = FIRST_PART.DATAS.const.SPEED

    def new_possions_user(self, side, pos):
        if side == 'right':
            new_pos = (pos[0], pos[1] + self.speed)
        elif side == 'left':
            new_pos = (pos[0], pos[1] - self.speed)
        elif side == 'up':
            new_pos = (pos[0] - self.speed, pos[1])
        else:
            new_pos = (pos[0] + self.speed, pos[1])

        return new_pos if self.get_result(new_pos) else None

    def new_pos_dogs(self):  # for ii dogs
        pass

    def get_result(self, new_pos):
        checking = FIRST_PART.MECHANICA.check_moving.CHECKING(pos_user=new_pos, type_checking='people')
        return new_pos if checking.result() else None
