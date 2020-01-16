import os
import jieba
import jieba.posseg as pseg
import numpy
fout = open("Result.txt",'w',encoding='utf-8')
fin = open('C:/Users/41104/Desktop/a.txt' ,'r',encoding='utf-8')
#fenci="'1510 屯門市中心巴士總站暫停服務\n\n因應屯門一帶最新交通情況，九巴及龍運以下路線改道：\n52X, 60M, 60X, 12点11M, 61X, 259D, 261, 263, 961, A33X, E33',服务"
#words = pseg.cut(fenci,use_paddle=True)
# words = pseg.cut(fenci)
count=0

def judge(e):
    if e>0:
        return 1
    else:
        return 0

# for word, flag in words:
#     if flag == 'v':
#         v=v+1
#     print('%s %s' % (word, flag))

for eachLine in fin:
    # 1时间2地点3人物
    n = 0  # 普通名词
    nr = 0  # 人名3
    nz = 0  # 其他专名
    a = 0  # 形容词
    m = 0  # 数量词
    c = 0  # 连词
    #
    f = 0  # 方位名词2
    ns = 0  # 地名2
    v = 0  # 普通动词
    ad = 0  # 副形词
    q = 0  # 量词
    u = 0  # 助词
    #
    s = 0  # 处所名词
    nt = 0  # 机构名2
    vd = 0  # 动副词
    an = 0  # 名形词
    r = 0  # 代词
    xc = 0  # 其他虚词
    #
    t = 0  # 时间1
    nw = 0  # 作品名
    vn = 0  # 名动词
    d = 0  # 副词
    p = 0  # 介词
    w = 0  # 标点符号

    x = 0

    line = eachLine.strip().encode('utf-8').decode('utf-8','ignore')
    words =pseg.cut(line)
    for word, flag in words:
        if flag == 'n':
            n= n+1
        elif flag=='nr':
            nr= nr+1
        elif flag=='nz':
            nz= nz+1
        elif flag=='a':
            a= a+1
        elif flag=='m':
            m= m+1
        elif flag=='c':
            c= c+1
        elif flag=='f':
            f= f+1
        elif flag=='ns':
            ns= ns+1
        elif flag=='v':
            v= v+1
        elif flag=='ad':
            ad= ad+1
        elif flag=='q':
            q= q+1
        elif flag=='u':
            u= u+1
        elif flag=='s':
            s= s+1
        elif flag=='nt':
            nt= nt+1
        elif flag=='vd':
            vd= vd+1
        elif flag=='an':
            an= an+1
        elif flag=='r':
            r= r+1
        elif flag=='xc':
            xc= xc+1
        elif flag=='t':
            t= t+1
        elif flag=='nw':
            nw= nw+1
        elif flag=='vn':
            vn= vn+1
        elif flag=='d':
            d= d+1
        elif flag=='p':
            p= p+1
        elif flag=='w':
            w= w+1
        else:
            x=x+1
    count = judge(t)+judge(judge(nt)+judge(f)+judge(ns))+judge(nr)
    print(count)

    if count>=2:
        fout.write(line+ '\n')

fin.close()

fout.close()