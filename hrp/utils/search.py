import os
import re
import time

import jieba
import jieba.posseg
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 相对于manage.py的路径
# 加载自定义字典库
jieba.load_userdict("./hrp/utils/search/dict.txt")
# jieba.load_userdict("./utils/search/dict.txt")
# jieba.load_userdict("./search/dict.txt")
jieba.initialize()


def get_file_list(root_path):
    file_path_list = []
    walk = os.walk(root_path)
    for root, dirs, files in walk:
        for name in files:
            filepath = os.path.join(root, name)
            file_path_list.append(filepath)
    return file_path_list


def read_train_data():
    _train_x = []
    _train_y = []
    file_list = get_file_list("./hrp/utils/search/question/")
    # 遍历所有文件
    for one_file in file_list:
        # 获取文件名中的数字
        num = re.sub(r'\D', "", one_file)
        # 如果该文件名有数字，则读取该文件
        if str(num).strip() != "":
            # 设置当前文件下的数据标签
            label_num = int(num)
            # 读取文件内容
            with(open(one_file, "r", encoding="utf-8")) as fr:
                data_list = fr.readlines()
                for one_line in data_list:
                    word_list = list(jieba.cut(str(one_line).strip()))
                    # 将这一行加入结果集
                    _train_x.append(" ".join(word_list))
                    _train_y.append(label_num)
    return _train_x, _train_y


train_x, train_y = read_train_data()


class SearchJob:
    def __init__(self, question=""):
        self.question = question
        self.processed_question = ""
        self.word_with_type = []
        self.result = -1

    def preprocess_question(self):
        processed_question = re.sub("[.!/_,$%^*(\"\')]+|[—()?【】“”！，。？、~@#￥%…&*（）《》；‘’{}]+",
                                    "", self.question).lower().replace("-", "到") \
            .replace(">", "大于").replace("<", "小于").replace(" ", "")
        tmp_list = []
        word_with_type = []
        for word, word_type in jieba.posseg.cut(processed_question):
            word_type_dict = {"word": word, "type": word_type}
            word_with_type.append(word_type_dict)
            if word_type in ["ns", "jb", "m"]:
                tmp_list.append(word_type)
            else:
                tmp_list.append(word)
        self.word_with_type = word_with_type
        self.processed_question = "".join(tmp_list)

    def train(self):
        tv = TfidfVectorizer()
        train_data = tv.fit_transform(train_x).toarray()
        clf = MultinomialNB(alpha=0.01)
        clf.fit(train_data, train_y)
        question = [" ".join(list(jieba.cut(self.processed_question)))]
        tmp_data = tv.transform(question).toarray()
        self.result = clf.predict(tmp_data)[0]

    def run(self, question=None):
        start = time.time()
        if question:
            self.question = question
        self.preprocess_question()
        self.train()
        print("累计用时：", time.time() - start)
        print("原始问题为：", self.question)
        print("处理后问题为：", self.processed_question)
        print("匹配模板：", self.result)
        return self.word_with_type, self.result

# if __name__ == '__main__':
#     st = ""
#     print("-------------------------------------")
#     search = SearchJob("北京")
#     temp = SearchTemplate()
#     temp.run(search.run(st))
