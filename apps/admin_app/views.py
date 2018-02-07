from ..login_app.models import *
from django.shortcuts import render, HttpResponse, redirect

# from login_app.models import User
from django.contrib import messages 

def index(request):
    users = User.objects.exclude(admin=1).order_by('first_name')
    records = Record.objects.order_by('name')
    artists = Artist.objects.order_by('name')
    orders = Order.objects.all()
    context = {
        "users": users,
        "records": records,
        "artists": artists,
        "orders": orders
    }
    return render(request, 'admin_app/admin_portal.html', context)

def addrecord(request):
    artists = Artist.objects.order_by("name")
    context = {
        "artists": artists
    }
    return render(request, 'admin_app/addrecord.html', context)

def proccess_record(request):
    if len(request.POST['name']) < 1:
        messages.error(request, "Please enter title of the record")
        return redirect('/admin/addrecord')
    # if len(request.POST['artist']) < 1:
    #     messages.error(request, "Please enter artist of the record")
    #     return redirect('/admin/addrecord')
    if len(request.POST['genre']) < 1:
        messages.error(request, "Please enter genre of the record")
        return redirect('/admin/addrecord')
    if len(request.POST['price']) < 1:
        messages.error(request, "Please enter price of the record")
        return redirect('/admin/addrecord')
    if len(request.POST['description']) < 10:
        messages.error(request, "Please a description of the record longer than 10 characters")
        return redirect('/admin/addrecord')
    else:
        if len(request.POST['artist_name']) > 0:
            Record.objects.create(name=request.POST['name'], artist=request.POST['artist_name'], genre=request.POST['genre'], price=request.POST['price'], description=request.POST['description'], rec_image=request.POST['image'])
            Artist.objects.create(name=request.POST['artist_name'], bio="N/A", art_image="N/A", record=Record.objects.get(name=request.POST['name']))
            return redirect('/admin/admin_portal')
        else:
            Record.objects.create(name=request.POST['name'], artist=request.POST['artist_list'], genre=request.POST['genre'], price=request.POST['price'], description=request.POST['description'], rec_image=request.POST['image'])
            return redirect('/admin/admin_portal')

# def record_page(request, record_id):
#     return render(request, 'admin_app/record_page.html')

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        "user": user
    }
    return render(request, 'admin_app/userprofile.html', context)

def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.save()
    user.last_name = request.POST['last_name']
    user.save()
    user.email = request.POST['email']
    user.save()
    user.admin = request.POST['admin']
    user.save()
    return redirect('/admin/admin_portal')

def remove_record(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('/admin/admin_portal')

def remove_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/admin/admin_portal')

def edit_record_page(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        "record": record
    }
    return render(request, 'admin_app/edit_record_page.html', context)

def update_record(request, record_id):
    record = Record.objects.get(id=record_id)
    record.name = request.POST['name']
    record.save()
    record.artist = request.POST['artist_name']
    record.save()
    record.description = request.POST['description']
    record.save()
    record.genre = request.POST['genre']
    record.save()
    record.price = request.POST['price']
    record.save()
    record.rec_image = request.POST['image']
    record.save()
    return redirect('/admin/admin_portal')

def edit_artist_page(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    
    
    context = {
        "artist": artist,
       
        
    }
    return render (request, 'admin_app/edit_artist_page.html', context)

def update_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.name = request.POST['name']
    artist.save()
    artist.bio = request.POST['bio']
    artist.save()
    artist.art_image = request.POST['image']
    artist.save()
    return redirect('/admin/admin_portal')

def order_page(request, order_id):
    order = Order.objects.get(id=order_id)
    items = RecordItem.objects.filter(order=order_id)
    context = {
        "order": order,
        "items": items
    }
    return render(request, 'admin_app/order_page.html', context)

def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = request.POST['status']
    order.save()
    return redirect('/admin/admin_portal')


def logout(request):
    return redirect('/')