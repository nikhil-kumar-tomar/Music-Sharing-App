from django.shortcuts import HttpResponseRedirect,render
from .forms import * 
from django.conf import settings
from .miscellaneous import object_creator,object_exists,object_remove
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .business_logic import allowed_music_view
# Create your views here.

def home(request):
    context={}
    if request.user.is_authenticated:
        context={
            "data":allowed_music_view(request),
            "authenticated":True,
            "content":settings.MEDIA_URL,
        }
    return render(request,"music_platform/home.html",context)
def root(request):
    return HttpResponseRedirect("/home/")
def registration(request):
    form=user_create()
    if request.method=="POST":
        form=user_create(request.POST)
        if object_exists(factor={'email':request.POST["email"]},model="User") or object_exists(factor={'username':request.POST["username"]},model="User"):
            messages.error(request,"Email or Username Already Exists, Please use a different email")
            return HttpResponseRedirect("/registration/")
        if form.is_valid():
            form.save()
            messages.success(request,"Signed-Up Succesfully")
            return HttpResponseRedirect("/login/")
    context={
        'form':form,
    }
    return render(request,"music_platform/registration.html",context)
def logins(request):
    form=user_sign()
    if request.method=="POST":
        users=authenticate(username=request.POST["email"],password=request.POST["password"])
        if users != None:
            login(request,users)
            messages.success(request,f"Welcome {request.user.first_name}, You have Logged In Succesfully")
            return HttpResponseRedirect("/")
        else:
            messages.error(request,"Email/Password does not exist")
            return HttpResponseRedirect("/login/")
    context={
        "form":form,
        }
    return render(request,"music_platform/login.html",context)
def logouts(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Successfully Logged Out")
        return HttpResponseRedirect("/login/")
    else:
        messages.error(request,"Logout failed, Not logged in")
        return HttpResponseRedirect("/login/")
    
def music_upload(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=music_upload_form(request.POST,request.FILES,{"owner_email":request.user.id})
            if form.is_valid():
                inst=form.save(commit=False)
                inst.owner_email_id=request.user.email
                inst.save()
                if request.POST["music_type"]=="protected":
                    return HttpResponseRedirect(f"/upload_music_protected_access_allowed_{inst.id}")
                else:
                    messages.success(request,"File Uploaded Successfully")
            else:
                messages.error(request,"File did not upload Successfully")
        context={"form":music_upload_form}
        return render(request,"music_platform/music_upload.html",context)
    else:
        return HttpResponseRedirect("/login/")

def music_upload_protected_allows(request,music_id):
    if object_exists(factor={"id":music_id},model="music_uploads_model"):
        context={"music_id":music_id}
        if request.method=="POST":
                # Only emails that are registered and are not the same as email of the uploading user are allowed
                allowed_emails=[x for x in request.POST["protect_emails"].split(',') if object_exists({"email":x},model="User") and x!=request.user.email] 
                try:
                    [object_creator(factor={"email_id":x,"music_id_id":music_id},model="protected_accessors") for x in allowed_emails]# assigining every allowed email to music_id
                except Exception as e:
                    if e.args[0]!=1062:# if exception is not due to duplication
                        messages.error(request,"File did not upload Successfully")
                        object_remove(factor={"id":music_id},model="music_uploads_model")
                        return HttpResponseRedirect("/upload_music/")
                messages.success(request,"File Uploaded Successfully")
                return HttpResponseRedirect("/upload_music/")
        return render(request,"music_platform/protected_allows.html",context)
    else:
        return HttpResponseRedirect("/home/")