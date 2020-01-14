import langid
import os
import xlsxwriter
FileList=[]
Findpath = "D:/langid.py-master/数据/"   #所要处理的文件夹路径
FileNames=os.listdir(Findpath)
# 创建工作簿
file_name = "result.xlsx"
workbook = xlsxwriter.Workbook(file_name)
# 创建工作表
worksheet = workbook.add_worksheet('sheet1')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def dircount(DIR):
    return len(os.listdir(DIR))
count = dircount("D:/langid.py-master/数据/")
number=0
for fn in FileNames:
    fullfilename=os.path.join(Findpath,fn)      #获得文件夹路径下面的文件名
    fin = open(fullfilename,'r',encoding='utf-8')                #打开该文件
    ch = 0
    en = 0
    x=0
    toid=0
    for eachLine in fin:
        line = eachLine.strip().encode('utf-8').decode('utf-8','ignore')    #每行读取内容
        id = line[0:10]
        #print(id)
        if is_number(id):
            toid=int(id)
        lineTuple = langid.classify(line)                   #判断每行内容属于什么语种
        if lineTuple[0]=="zh":                              #langid.classify(line)的输出结果是一个二元组，二元组的第一项表示该文本所属的语系，如：ch中文，en英文，mr日文
            ch = ch+1
        elif lineTuple[0]=="en":
            en = en +1
        else:
            x = x+1


    n=ch+en+x
    a1=ch/n
    a2=en/n
    a3=x/n
    d = {'中文（ch）: ': a1, '英语（en）: ': a2, '其它（x）: ': a3, }
    t = sorted(d.items(), key=lambda item: item[1], reverse=True)

    print(*t, sep=' ')

    worksheet.write_row(number, 0, [toid, str(t[0][0])+str(t[0][1]), str(t[1][0])+str(t[1][1]),str(t[2][0])+str(t[2][1])])
    number=number+1

    fin.close()

workbook.close()
