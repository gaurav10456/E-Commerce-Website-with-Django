from django.shortcuts import render, HttpResponse, redirect
from .models import Contact 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Blogpost 


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')
    

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})


def blog(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/blog.html',
                  {'myposts': myposts})


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    query = request.GET['query']
    if len (query)>70:
        myposts = Blogpost.objects.none()
    else:
        mypostsTitle = Blogpost.objects.filter(title__icontains=query)
        mypostsContent = Blogpost.objects.filter(chead0__icontains=query)
        mypostsaAuthor = Blogpost.objects.filter(author__icontains=query)
        myposts = mypostsTitle.union(mypostsContent).union(mypostsaAuthor)
    if myposts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'myposts': myposts, 'query': query}
    return render(request, 'blog/search.html', params)

def add(request):
    return render(request, 'blog/add.html')

def browse(request):
    return render(request, 'blog/browse.html')


def apply(request):
    myposts = Blogpost.objects.all()
    if request.method=='POST':
        temp=request.POST['templa']
        if len(temp)==0:
            return HttpResponse({'<script>alert("add template first ..")</script>'})
        else:
            print(temp)
            with open('blog/templates/blog/basic.html', 'w+') as file:
                file.write(temp)
                response = HttpResponse(content_type='text/plain')
            
            return render(request,'blog/blog.html',{'myposts': myposts})


def handleSignup(request):
    if request.method == "POST":
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous inputs
        #username should be 10 character
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('blogHome')

        # alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('blogHome')
        
        #password should match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('blogHome')


        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your BlogPost account has been successfully created")
        return redirect('blogHome')


    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == "POST":
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user) 
            messages.success(request, "Successfully Logged In")
            return redirect('blog')

        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('blogHome')


    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('blogHome')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.warning(request, "Please fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent.")
    return render(request, 'blog/contact.html')

def createblogpost(request):
    if request.method=='POST':
        title = request.POST['title']
        author = request.POST['author']
        chead0 = request.POST['chead0']
        head1 = request.POST['head1']
        chead1 = request.POST['chead1']
        head2 = request.POST['head2']
        chead2 = request.POST['chead2']
        date2=request.POST['date']
        thumb=request.POST['filename']

        print(title, author, chead0, head1, chead1, head2, chead2, date2)
        if len(title)<2 or len(author)<2 or len(chead0)<2 or len(head1)<2 or len(chead1)<2 or len(head2)<2 or len(chead2)<2:
            messages.warning(request, "Please fill the form correctly.")
        else:
            blog=Blogpost(title=title, author=author, chead0=chead0, head1=head1, chead1=chead1, head2=head2, chead2=chead2, pub_date=date2, thumbnail=thumb)
            blog.save()
            messages.success(request, "Your BlogPost has been Create successfully.")
    return render(request, 'blog/createblogpost.html')


