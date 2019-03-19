def login(request):
    form =AuthenticationForm()
    if request.user.is_authenticated():
        if request.user.is_premium:
            return redirect("/home/")# or your url name
        if request.user.is_normal:
            return redirect("/home/")# or your url name
        if request.user.is_superpremium:
            return redirect("/superhome/")    


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            if request.user.is_premium:
                return redirect("/home/")# or your url name
            if request.user.is_normal:
                return redirect("/home/")# or your url name
            if request.user.is_superpremium:
            	return redirect("/superhome/")    
        else:
            messages.error(request, 'Error wrong username/password')
    context = {}
    context['form']=form

    return render(request, 'login.html', context)

@user_passes_test(lambda u: u.is_normal)
def NormalHome(request):
    context = {}
    return render(request, 'home.html', context)

@user_passes_test(lambda u: u.is_premium)
def PremiumHome(request):
    context = {}
    return render(request, 'home.html', context)

@user_passes_test(lambda u: u.is_superpremium)
def SuperHome(request):
    context = {}
    return render(request, 'superhome.html', context)