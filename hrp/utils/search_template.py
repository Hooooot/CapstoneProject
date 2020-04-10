from django.db.models import Q

from hrp.models import Position, BaseModel


class SearchTemplate:
    def __init__(self, word_with_type=None, index=None):
        self.word_with_type = word_with_type
        self.index = index
        self.template = {
            0: self.position,
            1: self.wages,
            2: self.wages_gt,
            3: self.wages_lt,
            4: self.wages_bt,
            5: self.address,
            6: self.position_address,
            7: self.position_wages,
            8: self.position_wages_gt,
            9: self.position_wages_lt,
            10: self.position_wages_bt,
            11: self.wages_address,
            12: self.wages_gt_address,
            13: self.wages_lt_address,
            14: self.wages_bt_address,
            15: self.position_wages_address,
            16: self.position_wages_gt_address,
            17: self.position_wages_lt_address,
            18: self.position_wages_bt_address,
            19: self.company,
        }

    def run(self, word_with_type=None, index=None):
        if word_with_type:
            self.word_with_type = word_with_type
        if index:
            self.index = index
        return self.template[int(self.index)]()

    # 0
    def position(self):
        word_with_type = self.word_with_type
        _type = ''
        for word_type in word_with_type:
            if word_type["type"] == "jb":
                _type = word_type["type"]
                break
        res = Position.objects.filter(position_tags__icontains=_type, position_state=BaseModel.text2state("正常"))
        return res

    # 1
    def wages(self):
        num_start, num_end = self.check_num()
        res = Position.objects.filter(Q(position_min_wages__lte=num_start) & Q(position_max_wages__gte=num_start),
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 2
    def wages_gt(self):
        num_start, num_end = self.check_num()
        res = Position.objects.filter(position_min_wages__lte=num_start,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 3
    def wages_lt(self):
        num_start, num_end = self.check_num()
        res = Position.objects.filter(position_max_wages__gte=num_start,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 4
    def wages_bt(self):
        num_start, num_end = self.check_num()
        res = Position.objects.filter(position_min_wages__lte=num_start, position_max_wages__gte=num_end,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 5
    def address(self):
        address = self.check_address()
        res = Position.objects.filter(position_region__icontains=address,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 6
    def position_address(self):
        position = self.check_job()
        address = self.check_address()
        res = Position.objects.filter(position_region__icontains=address, position_tags__icontains=position,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 7
    def position_wages(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        position = self.check_job()
        res = Position.objects.filter(Q(position_min_wages__lte=num_end) & Q(position_max_wages__gte=num_end),
                                      position_tags__icontains=position, position_state=BaseModel.text2state("正常"))
        return res

    # 8
    def position_wages_gt(self):
        num_start, num_end = self.check_num()
        position = self.check_job()
        res = Position.objects.filter(position_min_wages__lte=num_start,
                                      position_tags__icontains=position, position_state=BaseModel.text2state("正常"))
        return res

    # 9
    def position_wages_lt(self):
        num_start, num_end = self.check_num()
        position = self.check_job()
        res = Position.objects.filter(position_max_wages__gte=num_start,
                                      position_tags__icontains=position, position_state=BaseModel.text2state("正常"))
        return res

    # 10
    def position_wages_bt(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        position = self.check_job()
        res = Position.objects.filter(Q(position_min_wages__lte=num_start) & Q(position_max_wages__gte=num_end),
                                      position_tags__icontains=position, position_state=BaseModel.text2state("正常"))
        return res

    # 11
    def wages_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        res = Position.objects.filter(Q(position_min_wages__lte=num_end) & Q(position_max_wages__gte=num_end),
                                      position_region__icontains=address, position_state=BaseModel.text2state("正常"))
        return res

    # 12
    def wages_gt_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        res = Position.objects.filter(position_min_wages__lte=num_start,
                                      position_region__icontains=address, position_state=BaseModel.text2state("正常"))
        return res

    # 13
    def wages_lt_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        res = Position.objects.filter(position_max_wages__lte=num_end,
                                      position_region__icontains=address, position_state=BaseModel.text2state("正常"))
        return res

    # 14
    def wages_bt_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        res = Position.objects.filter(Q(position_min_wages__lte=num_start), Q(position_max_wages__gte=num_end),
                                      position_region__icontains=address, position_state=BaseModel.text2state("正常"))
        return res

    # 15
    def position_wages_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        position = self.check_job()
        res = Position.objects.filter(Q(position_min_wages__lte=num_start) & Q(position_max_wages__gte=num_end),
                                      position_tags__icontains=position, position_region__icontains=address,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 16
    def position_wages_gt_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        position = self.check_job()
        res = Position.objects.filter(position_min_wages__lte=num_end,
                                      position_tags__icontains=position, position_region__icontains=address,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 17
    def position_wages_lt_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        position = self.check_job()
        res = Position.objects.filter(position_max_wages__gte=num_end,
                                      position_tags__icontains=position, position_region__icontains=address,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 18
    def position_wages_bt_address(self):
        num_start, num_end = self.check_num()
        if num_start > num_end:
            num_start, num_end = num_end, num_start
        address = self.check_address()
        position = self.check_job()
        res = Position.objects.filter(position_min_wages__lte=num_start, position_max_wages__gte=num_end,
                                      position_tags__icontains=position, position_region__icontains=address,
                                      position_state=BaseModel.text2state("正常"))
        return res

    # 19
    def company(self):
        pass

    # 分析语句，获取两个数字
    def check_num(self):
        word_with_type = self.word_with_type
        num_start = 0
        num_end = 0
        to_flag = False
        for word_type in word_with_type:
            if word_type["word"] in ["和", "到"]:
                to_flag = True
                continue
            if word_type["type"] == "my":
                return 0, 0
            if word_type["type"] == "m":
                if word_type["word"] not in ["万", "千", "百"]:
                    try:
                        if to_flag:
                            num_end = int(word_type["word"])
                        else:
                            num_start = int(word_type["word"])
                    except ValueError as e:
                        print("捕获异常，转化的不是数字", e)
                else:
                    if word_type["word"] == "万":
                        if to_flag:
                            if num_end > 0:
                                num_end = num_end * 10000
                            else:
                                num_end = 10000
                        else:
                            if num_start > 0:
                                num_start = num_start * 10000
                            else:
                                num_start = 10000
                    elif word_type["word"] == "千":
                        if to_flag:
                            if num_end > 0:
                                num_end = num_end * 1000
                            else:
                                num_end = 1000
                        else:
                            if num_start > 0:
                                num_start = num_start * 1000
                            else:
                                num_start = 1000
                    elif word_type["word"] == "百":
                        if to_flag:
                            if num_end > 0:
                                num_end = num_end * 100
                            else:
                                num_end = 100
                        else:
                            if num_start > 0:
                                num_start = num_start * 100
                            else:
                                num_start = 100

            elif word_type["type"] == "eng":
                if word_type["word"] in ["k", "w"]:
                    if word_type["word"] == "w":
                        if to_flag:
                            if num_end > 0:
                                num_end = num_end * 10000
                            else:
                                num_start = 10000
                        else:
                            if num_start > 0:
                                num_start = num_start * 10000
                            else:
                                num_start = 10000
                    elif word_type["word"] == "k":
                        if to_flag:
                            if num_end > 0:
                                num_end = num_end * 1000
                            else:
                                num_start = 1000
                        else:
                            if num_start > 0:
                                num_start = num_start * 1000
                            else:
                                num_start = 1000
        return num_start / 1000, num_end / 1000

    # 返回查到的地址
    def check_address(self):
        word_with_type = self.word_with_type
        for word_type in word_with_type:
            if word_type["type"] == "ns":
                return word_type["word"]
        return None

    # 返回查到的工作岗位
    def check_job(self):
        word_with_type = self.word_with_type
        for word_type in word_with_type:
            if word_type["type"] == "jb":
                return word_type["word"]
        return None
