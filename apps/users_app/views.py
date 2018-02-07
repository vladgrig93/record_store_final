from django.shortcuts import render, HttpResponse, redirect
from ..login_app.models import *
from xml.etree import ElementTree
import stripe
import requests
import json


stripe.api_key = "sk_test_h5SNwnBXX4FmHVQNxEy6ZLJu"



def index(request):
    if len(Artist.objects.all())<1:
        Record.objects.create(name='Club hits 2017', artist="Tiesto", rec_image="https://pbs.twimg.com/profile_images/815327700810285057/25nr1B16.jpg", price=20, genre='EDM', description='best of tiesto')
        Artist.objects.create(name='Tiesto', bio='Tijs Michiel Verwest, better known by his stage name Tiesto, is a Dutch DJ and record producer', 
        art_image="https://images-na.ssl-images-amazon.com/images/I/C1blmwzSGfS._SL1000_.png", record=Record.objects.last())
        
        Record.objects.create(name='All Eyez on Me', artist='Tupac', rec_image='https://static.gigwise.com/community/105571/all-eyez-on-me-20-qd3-remembers-2pac-his-seminal-death-row-debut-vts41ruk', price=20, genre='Rap', description='Latest studio album by Tupac')
        Artist.objects.create(name='Tupac', bio='Shakur began his career as a roadie, backup dancer, and MC for the alternative hip hop group Digital Underground, eventually branching off as a solo artist', art_image="http://www.billboard.com/files/media/tupac-bw-portrait-photofest-billboard-1548.jpg", record=Record.objects.last()) 
        
        Record.objects.create(name='Toxicity', artist=
        "System of a Down", rec_image='https://images-na.ssl-images-amazon.com/images/I/61Wt2PvyIhL.jpg', price=20, genre='Rock', description='2nd album by SOAD!')
        Artist.objects.create(name='System of a Down', bio='In June 1998, System of a Down released their debut album, System of a Down. They enjoyed moderate success as their first singles "Sugar" and "Spiders" became radio favorites and the music videos for both songs were frequently aired on MTV', art_image='http://assets.blabbermouth.net/media/systemofadown2014band_638.jpg',record=Record.objects.last()) 

        Record.objects.create(name='Hotel California', artist="Eagles", rec_image='https://cps-static.rovicorp.com/3/JPG_500/MI0003/501/MI0003501116.jpg?partner=allrovi.com', price=20, genre='Rock', description='Best of the eagles') 
        Artist.objects.create(name='Eagles', bio='The Eagles are an American rock band formed in Los Angeles in 1971. The founding members were Glenn Frey (lead guitar, lead vocals), Don Henley (drums, lead vocals), Bernie Leadon (guitars, vocals) and Randy Meisner (bass guitar, vocals)', art_image='http://media.cleveland.com/popmusic_impact/photo/-46c2bc7924ed54bd.jpg',record=Record.objects.last())

        Record.objects.create(name='Generationwhy', artist="Zhu", rec_image='https://images.genius.com/113fed86b1d0b579a00aeb54631b11cf.1000x1000x1.jpg', price=20, genre='EDM',description='Zhu is fire')
        Artist.objects.create(name='Zhu', bio="Zhu's success carried over into 2017, where he was a featured performer in Ultra Music Festival 2017 in Miami on the live stage on March 24, 2017. His performance was positively received.", art_image='http://dailytrojan.com/wp-content/uploads/2016/09/zhu-720x340.jpg',record=Record.objects.last())
        
        Record.objects.create(name='Issa Album', artist="21 Savage", rec_image='http://images.genius.com/c882a112b55acb3623fa4b0e4d9bd37c.1000x1000x1.jpg', price=20, genre='Rap', description='horrible')
        Artist.objects.create(name='21 Savage', bio='Shayaa Bin Abraham-Joseph (born October 22, 1992), better known by his stage name 21 Savage, is an American rapper from Atlanta, Georgia.', art_image='https://upload.wikimedia.org/wikipedia/commons/0/03/Rapper_21_Savage.jpg', record=Record.objects.last())
        
        Record.objects.create(name='Jazz Masters Collection', artist="Duke Ellington", rec_image='http://direct.rhapsody.com/imageserver/images/Alb.218913062/600x600.jpg', price=20, genre='Jazz', description='best of Duke Ellington')
        Artist.objects.create(name='Duke Ellington', bio='Greatest hits by legendary Tiesto!', art_image='https://upload.wikimedia.org/wikipedia/commons/a/af/Duke_Ellington_-_publicity.JPG', record=Record.objects.last())

        #greg's
        Record.objects.create(name="DAMN", artist="Kendrick Lamar", description="Arguably the best Hip-Hop record of 2017", genre="Rap", price="20", rec_image="http://www.onthecomeuptv.com/wp-content/uploads/2017/06/Damn.jpg")
        Artist.objects.create(name="Kendrick Lamar", bio="n/a", art_image="https://ticketcrusader.com/wp-content/uploads/2017/04/kendrick-lamarr.jpg", record=Record.objects.last())

        Record.objects.create(name="Slim Shady LP", artist="Eminem", description="Debut LP from Eminem", genre="Rap", price="25", rec_image="http://images.genius.com/21bba30244f10169c83d757be797fe0a.999x999x1.jpg")
        Artist.objects.create(name="Eminem", bio="n/a", art_image="http://img2-ak.lst.fm/i/u/arO/ec0ad2dba67a4dc2a49a3abdd9f5f03a", record=Record.objects.last())

        Record.objects.create(name="Vol. 4", artist="Black Sabbath", description="Classic Metal record from the pioneers of the genre", genre="Rock", price="25", rec_image="https://images-na.ssl-images-amazon.com/images/I/71KZqP%2B9hmL._SL1425_.jpg")
        Artist.objects.create(name="Black Sabbath", bio="n/a", art_image="http://img2-ak.lst.fm/i/u/arO/580ab07bac4344c29ffe3aa9b36d3e6c", record=Record.objects.last())

        Record.objects.create(name="Rated R", artist="Queens of the Stone Age", description="Amazing sophmore LP from QOTSA", genre="Rock", price="25", rec_image="http://images.genius.com/0fe9029ab2384a9c8fb40786895695c4.1000x1000x1.png")
        Artist.objects.create(name="Queens of the Stone Age", bio="n/a", art_image="http://www.metalinjection.net/wp-content/uploads/2017/04/queens_of_the_stone_age_01.jpg", record=Record.objects.last())

        Record.objects.create(name="Animal Magic", artist="Bonobo", description="Debut LP from Bonobo. More hip-hop oriented beats than his later materiral", genre="EDM", price="20", rec_image="https://ninjatune.net/images/releases/animal-magic-main.jpg")
        Artist.objects.create(name="Bonobo", bio="n/a", art_image="http://www.freundevonfreunden.com/wp-content/uploads/bonobos-latest-album-explores-our-changing-cultural-landscape/Freunde-von-Freunden-Bonobo-1-1600x1067.jpg", record=Record.objects.last())

        Record.objects.create(name="Endroducing", artist="DJ Shadow", description="The timeless Debut LP from one of the greatest producers of all time", genre="EDM", price="35", rec_image="https://images-na.ssl-images-amazon.com/images/I/71wdyiHw-iL._SL1087_.jpg")
        Artist.objects.create(name="DJ Shadow", bio="n/a", art_image="https://www.undergroundhiphop.com/wp-content/uploads/2017/04/DJ-Shadow.jpg", record=Record.objects.last())

        Record.objects.create(name="Mannish Boy: The Best Of", artist="Muddy Waters", description="A Muddy Waters best of complilation", genre="Blues", price="40", rec_image="https://images-na.ssl-images-amazon.com/images/I/71AwKHJkj0L._SL1200_.jpg")
        Artist.objects.create(name="Muddy Water", bio="n/a", art_image="https://www.biography.com/.image/t_share/MTE4MDAzNDEwNzE5NTA3OTgy/muddy-waters-9525002-1-402.jpg", record=Record.objects.last())

        Record.objects.create(name="The Rockin' Chair Album", artist="Howlin Wolf", description="Classic record from one of the best the blues game as ever seen.", genre="Blues", price="35", rec_image="https://images-na.ssl-images-amazon.com/images/I/71u-Dft6OdL._SL1086_.jpg")
        Artist.objects.create(name="Howlin Wolf", bio="n/a", art_image="https://i.ytimg.com/vi/Xs6cTV1L7UQ/maxresdefault.jpg", record=Record.objects.last())

        Record.objects.create(name="Monk's Dream", artist="Thelonious Monk", description="Class jazz record. Must have for any collector", genre="Jazz", price="25", rec_image="https://i.ytimg.com/vi/wqHe50_tBVc/maxresdefault.jpg")
        Artist.objects.create(name="Thelonious Monk", bio="n/a", art_image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Thelonious_Monk%2C_Minton%27s_Playhouse%2C_New_York%2C_N.Y.%2C_ca._Sept._1947_%28William_P._Gottlieb_06191%29.jpg/1200px-Thelonious_Monk%2C_Minton%27s_Playhouse%2C_New_York%2C_N.Y.%2C_ca._Sept._1947_%28William_P._Gottlieb_06191%29.jpg", record=Record.objects.last())

        Record.objects.create(name="Lullabies Of Birdland", artist="Ella Fitzgerlad", description="Amazing record from the queen of jazz", genre="Jazz", price="40", rec_image="http://www.qualityrecords.com.au/Images/Ella%20Fitzgerald%20-%20Lullabies%20of%20Birdland.jpg")
        Artist.objects.create(name="Ella Fitzgerlad", bio="n/a", art_image="https://www.biography.com/.image/t_share/MTE4MDAzNDEwNTIyNTA2NzY2/ella-fitzgerald-9296210-1-402.jpg", record=Record.objects.last())

        Record.objects.create(name="Cowboys From Hell", artist="Pantera", description="Do you like riffs? Why don't you have this already", genre="Metal", price="30", rec_image="https://images.genius.com/823a0c5b7d12b62dc6938203980ae611.993x1000x1.jpg")
        Artist.objects.create(name="Pantera", bio="n/a", art_image="https://iscale.iheart.com/v3/url/aHR0cDovL2ltYWdlLmloZWFydC5jb20vaW1hZ2VzL3JvdmkvMTA4MC8wMDAxLzM5MS9NSTAwMDEzOTEzMTkuanBn", record=Record.objects.last())

        Record.objects.create(name="Slaughter of the Soul", artist="At The Gates", description="Timeless melodic death metal record", genre="Metal", price="30", rec_image="http://www.leastworstoption.com/wp-content/uploads/1385119252_606f92426903ec9d4b3151d3ad02267b.jpg")
        Artist.objects.create(name="At The Gates", bio="n/a", art_image="http://distortedsoundmag.com/wp-content/uploads/2017/03/Band-Photo-At-The-Gates.jpg", record=Record.objects.last())
    
    records=Record.objects.all()
    artists=Artist.objects.all()
    context={'records': records, 'artists':artists}
    return render(request, 'users_app/user_portal.html', context)

def category(request, artist_record_genre):
    request.session['genre']=artist_record_genre
    display=Artist.objects.record=Record.objects.filter(genre=artist_record_genre)
    context={'display':display}
    return render(request, 'users_app/categories.html', context)

def artist(request, artist_id):
    artist=Artist.objects.get(id=artist_id)
    context={'artist':artist}
    return render(request, 'users_app/artist.html', context)

def record(request, artist_record_id):

    record=Record.objects.get(id=artist_record_id)
    youtube = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q="+record.artist+" "+record.name+"&type=video&key=AIzaSyD1p01u8hMTqxtWZMMrNdH0jbO153a4fRg")
    json_data = json.loads(youtube.text)
    youtubeid = json_data['items'][0]['id']['videoId']
    print youtubeid
    context={'record':record,
    'youtube': youtubeid}
    return render(request, 'users_app/records.html', context)

def addrecord(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    saved_list = request.session['cart']
    recordobject = {"id":request.POST['recordid'], "quantity":request.POST['quantity']}
    saved_list.append(recordobject)
    request.session['cart'] = saved_list
    return redirect('/user/cart')
    
def displaycart(request):
    listofrecords = []
    listofpreviousorders = []
    totalprice = 0

    if not 'cart' in request.session:
        request.session['cart'] = []

    for record in request.session['cart']:
        recordobj = Record.objects.get(id=record['id'])
        recordobj_q = record['quantity']
        newrecordobj = {'record':recordobj, 'quantity':recordobj_q}
        listofrecords.append(newrecordobj)
    for recordobj in listofrecords:
        itemprice = recordobj['record'].price*int(recordobj['quantity'])
        totalprice+=itemprice
    user = User.objects.get(id=request.session['id'])
    previousorders = Order.objects.filter(user = user)
    
    for order in previousorders:
        recorditems = order.orderItems.all()
        for recorditem in recorditems:
            listofpreviousorders.append(recorditem)


    context = {
        "listofrecords":listofrecords,
        "totalprice":totalprice,
        "listorders":listofpreviousorders,
    }
    return render(request, 'users_app/cart.html', context)


def removeitem(request):
    recordid = request.POST['record_to_be_deleted']
    recordq = request.POST['record_quantity']
    saved_list = request.session['cart']
    for item in saved_list:
        if ((item['id'] == recordid )and (item['quantity']==recordq)):
            saved_list.remove(item)
            request.session['cart'] = saved_list
            return redirect('/user/cart')
    return redirect('/user/cart')

def processpayment(request):
    token = request.POST['stripeToken']
    totalprice = request.POST['totalprice']
    charge = stripe.Charge.create(
        amount=int(totalprice)*100,
        currency = "usd",
        description="Record Purchase from recordstore.com",
        source=token,
    )
    user = User.objects.get(id=request.session['id'])
    saved_list = request.session['cart']
    thisorder = Order.objects.create(status=0,user=user)
    for item in saved_list:
        recorditem = RecordItem.objects.create(order = thisorder, record = Record.objects.get(id=item['id']), quantity = item['quantity'])
    del request.session['cart']
    return redirect('/user/displayconfirmation')


def search(request):
    noartist = False
    norecord = False
    if request.POST['search'] == "":
        return render(request, "users_app/searchresults.html")
    records = Record.objects.filter(name__startswith=request.POST['search'])
    artists = Artist.objects.filter(name__startswith=request.POST['search'])
    if not records:
        norecord = True
    if not artists:
        noartist = True
    return render(request, "users_app/searchresults.html", {"records":records, "artists": artists, "header1":"Records:", "header2":"Artists:", "noartist":noartist,"norecord":norecord})

    return render(request, 'users_app/user_portal.html')
def settings(request):
    user = User.objects.filter(id = request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'users_app/user_profile.html', context)

def confirm(request):
    artists = Artist.objects.all()
    context = {
        "artists": artists
    }
    return render(request, 'users_app/confirmation.html', context)

def update(request, user_id):
    user = User.objects.get(id = user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    request.session['first_name']=user.first_name
    return redirect ('/user/settings')
