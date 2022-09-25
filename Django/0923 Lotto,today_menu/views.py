from django.shortcuts import render
import random

def index(request):
    menus = [
        {"name": "피자","src":"https://w.namu.la/s/8c2aebf04d4c6e0ae24ebf3b3789cb064f353da40f0a2916630ee33cc34742414ac8427b8765569e84d615a24cac7bc389ada2e5c60579541ea8b41be9b22db66f14a3db5f981a2cc93bba229a752932915474cffbb7d3fe3cc41022e163a2b2b720c118309e131b9dbe8fdfda5c449b"},
        {"name": "치킨","src":"http://www.bhc.co.kr/upload/bhc/menu/410x271_view_%EC%B9%98%ED%90%81%EB%8B%B9%ED%95%9C%EB%A7%88%EB%A6%AC(0).png"},
        {"name": "라면","src":"https://health.chosun.com/site/data/img_dir/2021/10/26/2021102601968_0.jpg"},
        {"name": "밥","src":"https://folkency.nfm.go.kr/upload/img/20190304/20190304121119_t_.jpg"},
        {"name": "삼겹살","src":"https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg"},
        {"name": "초밥","src":"https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000881/img/basic/a0000881_main.jpg"},
        {"name": "냉면","src":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Dongmu_Bapsang_02.jpg/1200px-Dongmu_Bapsang_02.jpg"},
        {"name": "굶어","src":"https://cdn.ppomppu.co.kr/zboard/data3/2019/0220/m_20190220141945_hplxucsz.jpg"},
    ]    

    menu = random.choice(menus)

    context = {
        "menu" : menu
    }


    
  
    return render(request,'index.html',context)

def Lotto(request):
    Lotto_list=[]
    

    for _ in range(5):
        Lotto = random.sample(range(1,46),6)
        Lotto_list.append(Lotto)
        

    context = {
        "Lotto_list": Lotto_list,
     }


    return render(request,"Lotto.html",context)



