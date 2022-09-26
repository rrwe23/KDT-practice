from django.shortcuts import render
import random

# Create your views here.


def index(request):

    context = {}

    return render(request, "index.html", context)


def is_odd_even(request, number):
    context = {"number": number}

    return render(request, "is_odd_even.html", context)


def index2(request):
    name = request.GET.get("name")
    somethings = ["말", "돼지", "소", "군인", "모기", "성직자", "도둑"]
    imgs = {
        "말": "https://cdn.britannica.com/96/1296-050-4A65097D/gelding-bay-coat.jpg",
        "돼지": "data:image/jpeg;base64,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",
        "소": "https://cdn.britannica.com/55/174255-050-526314B6/brown-Guernsey-cow.jpg",
        "군인": "https://images.unsplash.com/photo-1541514431288-76b3c5aa474e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8c29pbGRlcnxlbnwwfHwwfHw%3D&w=1000&q=80",
        "모기": "https://images.theconversation.com/files/482160/original/file-20220831-18-wa7ab4.jpg?ixlib=rb-1.1.0&rect=0%2C45%2C6006%2C3962&q=45&auto=format&w=926&fit=clip",
        "성직자": "https://t3.ftcdn.net/jpg/01/01/03/72/360_F_101037235_Y0xakKrzTrSy8gYFIxOCkPRIp6xJbjY0.jpg",
        "도둑": "data:image/jpeg;base64,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",
    }

    something = random.choice(somethings)

    context = {"name": name, "something": something, "img": imgs.get(something)}

    return render(request, "index2.html", context)


def judge(request, id):
    if id % 2 == 0:
        res = "짝수"
    else:
        res = "홀수"

    context = {"res": res, "id": id}
    return render(request, "judge.html", context)


def calculator(request, num1, num2):
    res_sum = num1 + num2
    res_sub = num1 - num2
    res_mul = num1 * num2
    res_div = num1 // num2

    context = {
        "sum": res_sum,
        "sub": res_sub,
        "mul": res_mul,
        "div": res_div,
        "num1": num1,
        "num2": num2,
    }
    return render(request, "calculator.html", context)


def lorem(request):
    return render(request, "lorem.html")


def loremShow(request):
    cnt_para = int(request.GET.get("para"))
    cnt_words = int(request.GET.get("words"))

    # lorems = [[] for _ in range(cnt_para)]
    lorems = [[] for _ in range(cnt_para)]
    ran_words = [
        "바나나",
        "짜장면",
        "사과",
        "바나나",
        "딸기",
    ]

    for i in range(len(lorems)):
        while len(lorems[i]) < cnt_words:
            word = random.choice(ran_words)
            lorems[i].append(word)

    context = {"lorems": lorems}
    return render(request, "lorem-show.html", context)
