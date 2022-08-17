from django.shortcuts import render,redirect

from invoice.models import  AddProduct, UserRegistration

# Create your views here.
def user_login(request):
    error=''
    if request.method=='POST':
        user_email=request.POST['u_email']
        user_pass=request.POST['u_pass']
        user_data=UserRegistration.objects.filter(email=user_email,password=user_pass).exists()
        if user_data:
            Metro_user=UserRegistration.objects.get(email=user_email,password=user_pass)
            request.session['User_id']=Metro_user.id
            return redirect('add_product')
        else:
            error="Invalied username or password"
    return render(request, 'user_app/user_login.html')

def sign_up(request):
    if request.method=="POST":
        user_fname=request.POST["f_name"]
        user_lname=request.POST["l_name"]
        user_email=request.POST["e_mail"]
        user_phone=request.POST["p_hone"]
        user_pass=request.POST["pass"]
        sign=UserRegistration(fname=user_fname,lname=user_lname,email=user_email,phone=user_phone,password=user_pass)
        sign.save()   
    return render(request, 'user_app/sign_up.html')

def add_product(request):
    product=""
    if request.method=="POST":
        p_name=request.POST["pname"]
        p_desc=request.POST['desc']
        p_cat=request.POST['cat']
        p_subcat=request.POST["subcat"]
        p_wgt=request.POST["wgt"]
        p_unit=request.POST["unit"]
        p_qty=request.POST["qty"]
        p_amt=request.POST["amt"]
        stock=AddProduct(pname=p_name,desc=p_desc,cat=p_cat,sub_cat=p_subcat,weight=p_wgt,unit=p_unit,qty=p_qty,amount=p_amt)
        stock.save()
        product=AddProduct.objects.all()
    return render(request,'user_app/add_product.html',{'prod':product})

def billing(request):
    product=AddProduct.objects.all()
    return render(request,'user_app/billing.html',{'prod':product})

def bill(request):
    contact=AddProduct.objects.get(id=id)
    if request.method=='POST':
        contact.reply=request.POST['rply']
        contact.save()
        return redirect('complaints')
    return render(request,{'c':contact})