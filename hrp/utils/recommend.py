import math
from operator import itemgetter

from django.db.models import Q

from hrp.models import JobIntent, Position, BrowsingHistory, BaseModel


# def load_data(file_path):
#     f = open(file_path, "r", encoding="utf-8")
#     train_set = {}
#     limit = 0
#     for line in f:
#         user_id, position_id, rating = line.strip().split(",")
#         train_set.setdefault(user_id, {})
#         train_set[user_id][position_id] = rating
#         limit = limit + 1
#         if limit > 10000:  # 取10000条数据
#             break
#     f.close()
#     return train_set


# 基于用户的协同过滤推荐算法
class Recommend:
    def __init__(self, intent: JobIntent):
        filter_positions = None
        if intent.job_intent_min_wages == 0:
            filter_positions = Position.objects.filter((Q(position_tags__icontains=intent.job_intent_type) |
                                                        Q(position_region__icontains=intent.job_intent_region) |
                                                        Q(position_education__icontains=intent.job_intent_education)) &
                                                       Q(position_state=BaseModel.text2state("正常")))
        else:
            filter_positions = Position.objects.filter((Q(position_tags__icontains=intent.job_intent_type) |
                                                        Q(position_min_wages__lte=intent.job_intent_min_wages) |
                                                        Q(position_max_wages__gte=intent.job_intent_max_wages) |
                                                        Q(position_region__icontains=intent.job_intent_region) |
                                                        Q(position_education__icontains=intent.job_intent_education)) &
                                                       Q(position_state=BaseModel.text2state("正常")))
        train_set = {}
        uid_pid = BrowsingHistory.objects.all().values('user__user_id', 'position__position_id')
        for query in uid_pid:
            user_id = query["user__user_id"]
            position_id = query["position__position_id"]
            train_set.setdefault(user_id, {})
            train_set[user_id][position_id] = 1
        self.data_set = train_set
        self.filter_positions = filter_positions
        self.recommend_position_ids = {}

    def run(self, user_id, k):
        user_set = self.calc_user_sim()
        user_similar = self.user_similarity(user_set)
        self.recommend_position_ids = self.recommend(user_id, user_similar, k)
        # 包含概率的字典{}列表, {'id':概率}
        return self.recommend_position_ids

    # 建立岗位-用户的倒排列表
    def calc_user_sim(self):
        item_users = dict()
        for user, items in self.data_set.items():
            for position_id in items:
                if position_id not in item_users:
                    item_users[position_id] = set()
                item_users[position_id].add(user)

        # print("岗位-用户倒排列表: ", item_users)
        return item_users

    def user_similarity(self, user_set):
        # 稀疏矩阵
        c = dict()
        # 累加矩阵
        n = dict()
        for position_id, users in user_set.items():
            for u in users:
                n.setdefault(u, 0)
                # 每个职位下用户出现一次就加一次，就是计算每个岗位有多少用户浏览。
                n[u] += 1
                for v in users:
                    if u == v:
                        continue
                    c.setdefault(u, {})
                    c[u].setdefault(v, 0)
                    c[u][v] += 1 / math.log(1 + len(users))

        # print("稀疏矩阵: ", c)
        # 相似度矩阵
        w = dict()
        for u, related_users in c.items():
            for v, cuv in related_users.items():
                w.setdefault(u, {})
                w[u].setdefault(v, 0)
                w[u][v] = cuv / math.sqrt(n[u] * n[v])

        # print("用户相似度: ", w)
        return w

    def recommend(self, user_id, w, k):
        rvi = 1
        positions = dict()
        related_user = []
        interacted_items = self.data_set[int(user_id)]

        for co_user, item in w.items():
            if co_user == user_id:
                for user_id, score in item.items():
                    related_user.append((user_id, score))
                break

        # print("与user用户相似度: ", related_user)
        for v, wuv in sorted(related_user, key=itemgetter(1), reverse=True)[0:k]:
            for i in self.data_set[v]:
                if i in interacted_items:  # 如果用户已经喜欢  则不需要推荐
                    continue
                if i not in positions.keys():
                    positions[i] = 0
                positions[i] += wuv * rvi

        # print(positions)
        return positions

    def get_recommend_positions(self):
        if len(self.recommend_position_ids) > 0:
            position_ids = self.recommend_position_ids.keys()
            positions = Position.objects.filter(position_id__in=position_ids)
            return positions
        return None

    def get_filter_positions(self):
        return self.filter_positions
