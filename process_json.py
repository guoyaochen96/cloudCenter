import json
import random


def random_choice(seq, prob):
    '''
    功能：
        按给定概率prob，从seq中选取元素。可重复k次
    注意
        1. seq, prob长度要相等
        2. prob的概率和要等于1
        3. k 表示重复选取的次数，默认为1次
        4. 结果返回list
        5. 用到了random模块的random()函数
    例子：
        >>> random_choice(['a','b','c','d'], [0.4, 0.15, 0.1, 0.35])
        ['d']
        >>> random_choice('abcd', [0.4, 0.15, 0.1, 0.35], k=5)
        ['d','d','b','a','d']
    '''

    p = random.random()
    for i in range(len(seq)):
        if sum(prob[:i]) < p <= sum(prob[:i+1]):
            return seq[i]



def random_name():
    attributes = ["user_type", "gender", "name", "location", "transaction_type", "transaction_mode",
                       "Transaction channel", "spending"]

    last_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛' \
           '奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康' \
           '伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵' \
           '席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗' \
           '丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫' \
           '乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄' \
           '印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂' \
           '濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘' \
           '匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相' \
           '查后荆红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳' \
           '淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木' \
           '巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生' \
           '岳帅缑亢况郈有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福'
    first_name = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清' \
           '飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善' \
           '厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家' \
           '致树炎德行时泰盛秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环' \
           '雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶' \
           '怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑筠柔竹霭凝晓欢霄枫芸菲寒欣滢伊亚宜可姬舒影荔枝思丽秀' \
           '飘育馥琦晶妍茜秋珊莎锦黛青倩婷宁蓓纨苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希'
    addrs_dict = {"黄浦区":["外滩街道", "南京东路街道", "半淞园路街道", "小东门街道", "老西门街道", "豫园街道", "打浦桥街道", "淮海中路街道",
                         "瑞金二路街道", "五里桥街道"],
                  "徐汇区":["湖南路街道", "天平路街道", "枫林路街道", "徐家汇街道", "斜土路街道",
                        "长桥街道", "漕河泾街道", "康健新村街道", "虹梅路街道", "田林街道", "凌云路街道", "龙华街道", "华泾镇"],
                  "长宁区":["华阳路街道", "新华路街道", "江苏路街道", "天山路街道", "周家桥街道", "虹桥街道", "仙霞新村街道",
                        "程家桥街道", "北新泾街道", "新泾镇"],
                  "静安区":["江宁路街道", "静安寺街道", "南京西路街道", "曹家渡街道",
                        "石门二路街道", "天目西路街道", "北站街道", "宝山路街道", "芷江西路街道", "共和新路街道", "大宁路街道", "彭浦新村街道",
                        "临汾路街道", "彭浦镇"],
                  "浦东新区":["潍坊新村街道", "陆家嘴街道", "塘桥街道", "周家渡街道", "东明路街道", "洋泾街道",
                    "上钢新村街道", "沪东新村街道", "金杨新村街道", "浦兴路街道", "南码头路街道", "花木街道", "川沙新镇", "合庆镇", "曹路镇",
                    "高东镇", "高桥镇", "高行镇", "金桥镇", "张江镇", "唐镇", "北蔡镇", "三林镇", "惠南镇", "新场镇", "大团镇", "周浦镇",
                    "航头镇", "康桥镇", "宣桥镇", "祝桥镇", "泥城镇", "书院镇", "万祥镇", "老港镇", "南汇新城镇"]}
    X = random.choice(last_name)
    M = "".join(random.choice(first_name) for i in range(2))
    name = X+M
    user_type = random_choice(["个人", "商户"], [0.95, 0.05])
    gender = random.choice(["男", "女"])

    if user_type == "商户":
        gender = "0"
        name = "超商"
    distinct = random.choice(list(addrs_dict.keys()))
    position = distinct + "." + random.choice(addrs_dict[distinct])
    return user_type, gender, name,  position


def random_transaction(user_type):
    transaction_type = random.choice(["转账", "消费"])
    transaction_mode = random.choice(["刷脸", "扫码", "POS机"])
    transaction_channel = random.choice(["云闪付", "支付宝", "微信", "银行卡"])
    spending = random.randint(100, 501)
    spending = str(spending)
    if user_type == "商户":
        spending = "0"
        transaction_type = "0"
        transaction_mode = "0"
        transaction_channel = "0"
    return transaction_type, transaction_mode, transaction_channel, spending


class User:
    def __init__(self, user_type, gender, name, spending, position):
        self.user_type = user_type
        self.gender = gender
        self.name = name
        # self.job = job
        self.spending = spending
        self.position = position


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        json_data = json.load(f)


def generate_json(filename, n):
    with open(filename, "a", encoding="utf-8") as fp:
        for i in range(n):
            pass


if __name__ == '__main__':
    print(type(random_name()))
