from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login as l, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserWebsite, UpdateUserEdu, WriteBlog, ContactForm
from .models import *
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            l(request, user)
            a = UserSkill(user=request.user)
            a.C = 0
            a.Cpp = 0
            a.python = 0
            a.java = 0
            a.webdev = 0
            a.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'practise/signup.html', {'form': form})


def login(request):
    print(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            l(request, user)
            # Redirect to a success page.
            print(type(user))
            return redirect('home')
        else:
            return render(request, 'practise/login.html')
    else:
        return render(request, 'practise/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    frnd_list = Friend.objects.friends(request.user)
    frnd_rqst = Friend.objects.unread_requests(user=request.user)
    if request.method == 'POST':
        print(list(request.POST))


        c = list(request.POST)[1]
        print('c', c)
        if c == 'name':
            print(1)
            try:
                if request.user.userdetails:
                    print(request.POST['name'])
                    print(request.POST)
                    form1 = ContactForm(request.POST, request.FILES, instance=request.user.userdetails)
                    if form1.is_valid():
                        print('valid')

                        print('save')
                        form1.save()
                        return redirect('home')
            except:
                print(request.POST['name'])
                temp = UserDetails(user=request.user, name=request.POST['name'], phone=request.POST['phone'],
                                   address=request.POST['address'], Bio=request.POST['Bio'])
                temp.save()
                form1 = ContactForm(request.POST, request.FILES, instance=request.user.userdetails)
                if form1.is_valid():
                    print('valid')

                    print('save')
                    form1.save()
                    return redirect('home')
        if c == 'li':
            try:
                if request.user.userwebsite:
                    form2 = UpdateUserWebsite(request.POST, instance=request.user.userwebsite)
                    if form2.is_valid():
                        print('valid')

                        print('save')
                        form2.save()
                        return redirect('home')
            except:
                temp = UserWebsite(user=request.user)
                temp.save()
                form2 = UpdateUserWebsite(request.POST, instance=request.user.userwebsite)
                if form2.is_valid():
                    print('valid')

                    print('save')
                    form2.save()
                    return redirect('home')
        if c == 'TenName':
            try:
                if request.user.useredu:
                    form3 = UpdateUserEdu(request.POST, instance=request.user.useredu)
                    if form3.is_valid():
                        print('valid')

                        print('save')
                        form3.save()
                        return redirect('home')
            except:
                temp = UserEdu(user=request.user)
                temp.save()
                form3 = UpdateUserEdu(request.POST, instance=request.user.useredu)
                if form3.is_valid():
                    print('valid')

                    print('save')
                    form3.save()
                    return redirect('home')
        if c == 'post':
            temp = Blog(user=request.user)
            temp.save()
            # print(temp.id,Blog.objects.get(id=temp.id))

            form4 = WriteBlog(request.POST, request.FILES, instance=Blog.objects.get(id=temp.id))
            print(form4.errors)
            if form4.is_valid():
                print('valid')

                print('save')
                form4.save()
                return redirect('home')


    else:
        print("not post")
        try:
            form1 = ContactForm(instance=request.user.userdetails)
        except:
            form1 = ContactForm()
        try:
            form2 = UpdateUserWebsite(instance=request.user.userwebsite)
        except:
            form2 = UpdateUserWebsite()
        try:
            form3 = UpdateUserEdu(instance=request.user.useredu)
        except:
            form3 = UpdateUserEdu()

        form4 = WriteBlog()

        a = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'frnd_list':frnd_list, 'frnd_rqst':frnd_rqst}
        return render(request, 'practise/home.html', a)


def cquiz(request):
    if request.method == 'POST':
        s = 0
        for i in range(1, 6):
            if (request.POST[str(i)] == 'a'):
                s = s + 10
        try:

            c = UserSkill.objects.get(user=request.user)
            c.C = s
            c.save()
        except:
            a = UserSkill(user=request.user)
            a.C = s
            a.save()

        return redirect('home')
    return render(request, 'practise/cquiz.html')
def cpp(request):
    if request.method == 'POST':
        s = 0
        for i in range(1, 6):
            if (request.POST[str(i)] == 'a'):
                s = s + 10
        try:

            c = UserSkill.objects.get(user=request.user)
            c.Cpp = s
            c.save()
        except:
            a = UserSkill(user=request.user)
            a.Cpp = s
            a.save()

        return redirect('home')
    return render(request, 'practise/cpp.html')

def java(request):
    if request.method == 'POST':
        s = 0
        for i in range(1, 6):
            if (request.POST[str(i)] == 'a'):
                s = s + 10
        try:

            c = UserSkill.objects.get(user=request.user)
            c.java = s
            c.save()
        except:
            a = UserSkill(user=request.user)
            a.java = s
            a.save()

        return redirect('home')
    return render(request, 'practise/java.html')

def python(request):
    if request.method == 'POST':
        s = 0
        for i in range(1, 6):
            if (request.POST[str(i)] == 'a'):
                s = s + 10
        try:

            c = UserSkill.objects.get(user=request.user)
            c.python = s
            c.save()
        except:
            a = UserSkill(user=request.user)
            a.python = s
            a.save()

        return redirect('home')
    return render(request, 'practise/python.html')

def webdev(request):
    if request.method == 'POST':
        s = 0
        for i in range(1, 6):
            if (request.POST[str(i)] == 'a'):
                s = s + 10
        try:

            c = UserSkill.objects.get(user=request.user)
            c.webdev = s
            c.save()
        except:
            a = UserSkill(user=request.user)
            a.webdev = s
            a.save()

        return redirect('home')
    return render(request, 'practise/webdev.html')


def search(request):
    if request.method == 'GET':
        x = request.GET.get('search1')
        a = User.objects.filter(username__iexact=x)
        b = User.objects.filter(username__istartswith=x[0:3])
        c = User.objects.filter(username__iendswith=x[len(x) - 1:len(x) - 1:-1])
        records = (a | b | c).distinct()

        print(records)
        return render(request, 'practise/search.html', {'record': b})


def otherprofile(request, name):
    o = User.objects.get(username=name)
    print(o.pk)

    param = {'o': o}
    return render(request, 'practise/otherprofile.html', param)


def sendfr(request, myid):
    try:
        other_user = User.objects.get(pk=myid)
        Friend.objects.add_friend(
            request.user,  # The sender
            other_user,  # The recipient
            message='Hi! I would like to add you')
        return redirect('home')
    except:
        return redirect('home')







def acceptreq(request, myid):
    friend_request = FriendshipRequest.objects.get(id=myid)
    print("accepted")
    friend_request.accept()
    return redirect('home')


def cancelreq(request, myid):
    friend_request = FriendshipRequest.objects.get(id=myid)
    print("cancel")
    friend_request.reject()
    return redirect('home')


def rmvfrnd(request, myid):
    other_user = User.objects.get(pk=myid)
    Friend.objects.remove_friend(request.user, other_user)
    return redirect('home')
