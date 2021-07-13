score = []
while True:
    str_score = input('輸入你的數學成績：')
    if str_score == '':
        maximum = max(score)
        minimum = min(score)
        summation = sum(score)
        y = summation/4
        print("最高分",maximum)
        print("最低分",minimum)
        print('總分',summation)
        print("平均",y)
    else:
        score.append(float(str_score))