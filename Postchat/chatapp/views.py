from django.shortcuts import render
from .models import myUser
from .models import Post


def index(request):
    return render(request,'./index.html')

def login(request):
    name=request.POST.get("name")
    password=request.POST.get("password")
    try:
        user=myUser.objects.get(Name=name,Password=password)
        UserPosts = Post.objects.all()
        Response = render(request, 'Welcome.html', {
        "Name":name,
        "Password":password,
        "message": "Post Delivered Successfully!",
        "username": name,
        "data": UserPosts
       })

        # Response=render (request,"./welcome.html",{"user":{"Name":name,"Password":password,"data":UserPosts}})
        Response.set_cookie("username",name,max_age=60*60)
        return Response
    except myUser.DoesNotExist:
        return render(request, 'index.html', {
            "error": "Invalid username or password."
        })

    
def create(request):
    return render(request, 'create.html')

def register(request):
    name = request.POST.get("name")
    password = request.POST.get("password")

    if myUser.objects.filter(Name=name).exists():
        return render(request, "create.html", {
            "Heading": "This username is already taken.",
            "link": "create"
        })

    myUser.objects.create(Name=name, Password=password)
    return render(request, "index.html", {
        "Heading": "Thank you for registering!",
        "link": "/"
    })

def postview(request):
    username = request.COOKIES.get("username")
    return render(request, 'Post.html', {"username": username})

def postData(request):
    name=request.COOKIES.get("username")
    comment=request.POST.get("comment")
    postdata=request.FILES.get("post")
     
    if name and postdata:
        Post.objects.create(Name=name, comment=comment,postData=postdata)

    UserPosts = Post.objects.all()
    return render(request, 'welcome.html', {
        "message": "Post Delivered Successfully!",
        "username": name,
        "data": UserPosts
    })

def logout(request):
    response=render(request,'index.html')
    response.delete_cookie("username")
    return response
