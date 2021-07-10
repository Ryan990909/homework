Student_Id = input('請輸入號碼： ')
Chinese_Score = int(input('請輸入國文科目成绩： '))
Math_Score = int(input('請輸入數學科目成绩： '))
English_Score = int(input('請輸入英語科目成績： '))
All_Score = Chinese_Score + Math_Score + English_Score
Average_Score = All_Score / 3
Chinese_Percent =  Chinese_Score / All_Score *100
print('%s的平均成績為%.2f' %(Student_Id,Average_Score))
print('%s的國文成績占總成績的百分比為：%.2f' %(Student_Id,Chinese_Percent))
