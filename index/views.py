from django.db.models import Q
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from index.models import *


def index(request, pIndex=1):
    films = Films.objects.all().order_by('name')
    mywhere = []
    kw = request.GET.get("kw", None)
    if kw:
        films = films.filter(Q(person__contains=kw) | Q(name__contains=kw))
        mywhere.append('keyword' + kw)
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(films, 15)  # 以每页9条数据分页
    maxpagex = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpagex:
        pIndex = maxpagex
    if pIndex < 1:
        pIndex = 1

    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码表信息
    context = {"data": list2, "plist": plist, "pIndex": pIndex, "max_pages": maxpagex, 'mywehere': mywhere}
    return render(request, 'index/index.html', context)


def detail(request, id):
    try:
        film = Films.objects.get(pk=id)
        return render(request, 'index/detail.html', {"data": film})
    except:
        return HttpResponseRedirect('/')


def star(request):
    user = request.session['name']['name']
    user = Users.objects.get(name=user)
    if request.method == "GET":
        film_id = request.GET.get('film_id', None)
        del_id = request.GET.get('del_id', None)
        print(film_id, user, del_id)
        if film_id:
            sel = Start.objects.filter(user=user, name__id=film_id)
            if sel:
                pass
            else:
                Start.objects.create(user=user, name=Films.objects.get(id=film_id))

        if del_id:

            try:
                film = Start.objects.get(id=del_id)
                film.delete()
            except Start.DoesNotExist:
                pass
    star_list = Start.objects.filter(user__name=user).order_by('-time')
    data = {"data_list": star_list}
    return render(request, 'index/star.html', data)


def logout(request):
    if 'name' in request.session:
        del request.session['name']

    return HttpResponseRedirect('/login/')


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            user = Users.objects.filter(name=name, password=password)
            if user:
                try:
                    name = Users.objects.get(name=name, password=password)
                except Exception as e:
                    print(e)
                request.session['name'] = {"name": name.name, "photo": str(name.photo)}
                return HttpResponseRedirect('/')
            else:
                msg = "账号或密码错误！"
                return render(request, 'index/login.html', {"msg": msg})
        except Users.DoesNotExist:
            return HttpResponseRedirect('/login/')

    else:
        return render(request, 'index/login.html')


def password_update(request):
    if request.method == "POST":
        name = request.session['name']
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_1"]

        try:
            stu = Users.objects.get(name=name['name'])
        except Exception as e:
            print(e)
        if stu.password == password_1:
            stu.password = password_2
            stu.save()
            return HttpResponseRedirect("/login/")
        else:
            msg = "账号或密码错误！"
            return render(request, 'index/pswd_update.html', {"msg": msg})
    else:
        return render(request, 'index/pswd_update.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        photo = request.FILES.get('photo')
        try:
            stu = Users.objects.filter(is_active=True, name=name)
        except Exception as e:
            print(e)
        if stu:
            msg = '用户已存在！'
            return render(request, 'index/register.html', {"msg": msg})
        else:
            try:
                stu = Users.objects.create(
                    name=name,
                    password=password,
                    phone=phone,
                    email=email,
                    photo=photo
                )
            except Exception as e:
                print(e)
            msg = "注册成功！"
            return render(request, 'index/login.html', {"msg": msg})

    return render(request, 'index/register.html')
