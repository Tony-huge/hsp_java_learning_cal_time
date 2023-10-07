import pandas as pd

hsp_java = pd.read_csv("hspJava.txt")

df = pd.DataFrame(columns=['序号', '名称', '时间'])
for i in range(len(hsp_java)):
    if i % 3 == 0:
        df.loc[i // 3, '序号'] = hsp_java["韩顺平30天学java"][i]
    if i % 3 == 1:
        df.loc[i // 3, '名称'] = hsp_java["韩顺平30天学java"][i]
    if i % 3 == 2:
        df.loc[i // 3, '时间'] = hsp_java["韩顺平30天学java"][i]


def cal_time(num):  # 输入序列号Pxxx的号码xxx,例如P10，输入10。返回从P1到P10的总时长
    total_minutes = 0
    total_seconds = 0
    for i in range(num):
        # 使用 split 方法将时间字符串分割成分钟和秒
        minutes, seconds = map(int, df["时间"][i].split(':'))
        total_minutes += minutes
        total_seconds += seconds

    hours = (total_minutes + total_seconds // 60) // 60
    minutes = (total_minutes + total_seconds // 60) % 60
    seconds = total_seconds % 60
    print("P1到P{}的总时长为：{}小时{}分钟{}秒".format(num, hours, minutes, seconds))
    print("视频完成百分比为：{:.2f}%".format(100 * (total_minutes * 60 + total_seconds) / (199 * 3600 + 32 * 60 + 31)))


cal_time(443)
