import hashlib
import json
import os
import random
import secrets
import urllib
import urllib.parse
import urllib.request
from datetime import datetime
from email.policy import default
import requests
from flask import Flask, flash, make_response, redirect, render_template,request, session, url_for
from flask_login import LoginManager, UserMixin, current_user, login_user,logout_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from PIL import Image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SECRET_KEY'] = '5791628b21sb13ce0c676dfde280ba245'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

proxies = {
#   "http": os.environ['QUOTAGUARDSTATIC_URL']
  "http": "http://6xg7ny82rmedub:vl88kl66mb8fqxoa01p0bovi1v5iv5@us-east-static-06.quotaguard.com:9293",
}

login_manager = LoginManager(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(10), nullable=True)
    description = db.Column(db.String(), nullable = False)
    image =  db.Column (db.String(), default='default.jpg')
    trending = db.Column (db.Boolean, default = False)
    category = db.Column(db.String(), nullable=False)
    # user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
def __repr__(self): 
    return f"Item('{self.name}', '{self.category}', )"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(), nullable = False)
    image =  db.Column (db.String(), default='default.jpg')
    category = db.Column(db.String(), nullable=True)
    organiser = db.Column(db.String(), nullable=True)
    startDate = db.Column(db.String(), nullable=True)
    organiser = db.Column(db.String(), nullable=True)
    
    def __repr__(self): 
        return f"Item('{self.name}', '{self.category}', )"

    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=True)
    phoneNumber = db.Column(db.String(), nullable=True)
    numberOfTickets = db.Column(db.String(), nullable = True)
    typeOfTickets =  db.Column (db.String(), default='default.jpg')
    paid = db.Column(db.Boolean, default=False, nullable=True)
    paymentId = db.Column(db.String(), nullable=True)
    startDate = db.Column(db.String(), nullable=True)
    event = db.Column(db.String(), nullable=True)
    
    def __repr__(self): 
        return f"Customer('{self.name}', 'Paid: {self.paid}', )"


    
class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=True)
    phoneNumber = db.Column(db.String(), nullable=True)
    movie = db.Column(db.String(), nullable = True)
    movieConfirm =  db.Column (db.String(), nullable = True)
    talanku = db.Column(db.Boolean, default=False, nullable=True)
    probability = db.Column(db.String(), nullable=True)
    startDate = db.Column(db.String(), nullable=True)
    event = db.Column(db.String(), nullable=True)
    
    def __repr__(self): 
        return f"Movie('{self.movie}', 'Probability: {self.probability}',  )"

class Transactions(db.Model):
    tablename = ['Transactions']

    id = db.Column(db.Integer, primary_key=True)
    candidate = db.Column(db.String, nullable=False)
    candidateName = db.Column(db.String)
    award = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.String)
    account = db.Column(db.String)
    ref = db.Column(db.String)
    paid = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"Transaction(': {self.id}', 'Amount:{self.amount}', 'Candidate:{self.candidate}', 'Paid:{self.paid}')"



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
    items = db.Column(db.String(), nullable=True)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable = False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15))
    stock = db.relationship('Item', backref='author', lazy=True)

def __repr__(self):
    return '<User %r' % self.username


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def __repr__(self):
    return '<Category %r' % self.name


from forms import *


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    print(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/items', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    # form_picture.save(picture_path)
    print ("The picture name is" + picture_fn)
    return picture_fn

def save_picture_to_firebase(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    print(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/items', picture_fn)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    print ("The picture name is" + picture_fn)
    return picture_fn

src="../static/items/92f33ab490e95eca.jpg"

def searchitem(searchquery):
    items = Item.query.all()
    search = searchquery.split()
    foundItems = []
    print(items)
    print(search)
    for s in range(len(search)):
        # This is the word in the search bar
        print(search[s])
        for i in range(len(items)):
            print("Searching for " + search[s] + " in " + items[i].name)
            # Picks a specific item from the Database
            item_string = str(items[i].name.split()).lower()
            itemsArray = items[i].name.split()
            print(item_string)
            # Counts how many words are in that list
            item_string_count = len(items[i].name.split())
            print(item_string_count)
            # Good Code
            if item_string_count != 1:
                print("More than 1 word: " + str(item_string))
                for c in range(item_string_count):
                    item_sub_string = itemsArray[c].lower()
                    item_sub_string = item_sub_string.replace("[", "")
                    item_sub_string = item_sub_string.replace("'", "")
                    item_sub_string = item_sub_string.replace("]", "")
                    print("Item Sub String: " + item_sub_string)
                    if search[s] == item_sub_string:
                        print("found")
                        print(items[i].id)
                        foundItems.append(items[i].id)
            else:
                print("It is one word")
                item_string = item_string.replace("[", "")
                item_string = item_string.replace("'", "")
                item_string = item_string.replace("]", "")
                if search[s] == item_string:
                    print("found")
                    print(items[i].id)
                    foundItems.append(items[i].id)
                    print("We found the ff:" + str(foundItems))
            # End of Good code

            # else:
            #     print(type(search[s]))
            #     print(len(search[s]))
            #     print(type(str(items[i].name.split())))
            #     print(len(str(items[i].name.split())))
            #     res = str(items[i].name.split())    
            #     x = res.replace("[", "")
            #     y = x.replace("'", "")
            #     z = y.replace("]", "")
            #     print("Not found")
                # print(items[i].name.split())
    return foundItems

# searchResults = []
# queryResult = search('case')
# print("Found" + str(queryResult))
# for f in queryResult:
#     item = Item.query.get_or_404(f)
#     searchResults.append(item)
#     print(searchResults)





@app.route('/search', methods=['POST'])
def search():
    piw = request.args.get('q')
    print(piw)
    items = Item.query.all()
    # totalitems = Item.query.all().count()
    results = []
    # for i in items:
        # words = i.split()
        # for word in splits:
            # print(word)
    return render_template('results.html', items = items, search = 'iPhone')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/shop<string:userid>')
def shop(userid):

    print(userid)
    return render_template('shop.html')

@app.route('/allitems')
def allitems():
    items = Item.query.all()
    return render_template('allitems.html', items = items)


@app.route("/searchal/<string:searchquery>", methods=['POST','GET'])
def searchal(searchquery):
    searchResultsArray = []
    searchresults = (searchitem(searchquery))
    print("Home" + str(searchresults))
    for i in searchresults:
        item = Item.query.get_or_404(i)
        print(item)
        searchResultsArray.append(item)
    return render_template('searchal.html', search=searchquery, items=searchResultsArray)

# def replace_all(text, dic):
#     for i, j in dic.iteritems():
#         text = text.replace(i, j)
#     return text

@app.route('/', methods=['POST','GET'])
def start():
    session['cart'] = []
    return render_template('splash.html')

@app.route('/easypill', methods=['POST','GET'])
def easypill():
    api_key = "aniXLCfDJ2S0F1joBHuM0FcmH" #Remember to put your own API Key here
    phone = "0204716768" #SMS recepient"s phone number
    message = "You have a new order please go to your dashboard and check it out"
    sender_id = "PrestoSl" #11 Characters maximum
    send_sms(api_key,phone,message,sender_id)

    data = request.data
    print(data)
    return 'Easy Pill Webhooks URL'


@app.route("/voip/<string:params>", methods=['POST','GET'])
def voip(params):
    print(params)
    with open('readme.txt', 'w') as f:
        f.write(params)
    return render_template('voip.html', textfile=params)

# def addToCard(addToCart):
#     print ("add to cart thing")
#     return redirect(url_for('index'))

@app.route("/hello/<string:itemId>", methods=['POST','GET'])
def index(itemId):
    if itemId != 0: 
        # flash(f'Added to cart.')
        cart = session['cart']
        print(cart)
    form = Search()
    items = Item.query.order_by(Item.id.desc()).limit(20).all()
    home = 'home'
    if form.validate_on_submit():
        searchquery = form.search.data
        searchquery = searchquery.lower()
        print(searchquery)
        return redirect(url_for('searchal', searchquery = searchquery)) 
    return render_template('index.html', items = items, home=home, form=form, cart=session['cart'])

@app.route('/hello', methods=['POST','GET'])
def home():
    form = Search()
    session['cart'] = []
    events = Event.query.order_by(Event.id.desc()).limit(20).all()
    home = 'home'
    shoppingCart = session['cart']
    print(type(shoppingCart))
    if form.validate_on_submit():
        searchquery = form.search.data
        searchquery = searchquery.lower()
        print(searchquery)
        return redirect(url_for('searchal', searchquery = searchquery)) 
    return render_template('index.html', events = events, home=home, form=form, cart=shoppingCart)

@app.route('/testing')
def testing():
    return render_template('grid.html')

@app.route('/delivery', methods=['POST','GET'])
def delivery():
    form = DeliveryForm()
    if form.validate_on_submit():
        newOrder = Order(name = form.username.data, phone=form.phone.data, price=form.price.data, location=form.location.data, items=form.items.data)
        db.session.add(newOrder)
        db.session.commit()
        print(newOrder)
        params = "New Order id: " + str(newOrder.id) + '\n' + str(newOrder.phone) +'\n' + "Location: " +newOrder.location + '\n' + newOrder.items + '\n' + 'Total: Ghc' +  newOrder.price
        try:
            sendtelegram(params)
        except:
            print("Well that didsnt work...")
        return redirect(url_for('reciept', orderId=newOrder.id))
    return render_template('delivery.html',form=form)

@app.route('/cart', methods=['POST','GET'])
def cart():
    shoppingCart = session['cart']
    print(shoppingCart)
    items = []
    for i in shoppingCart:
        theItem = Item.query.get_or_404(i)
        print(theItem)
        items.append(theItem)
    print(items)
    if request.method == 'POST':
        print("request.data")
        print(request.form.get('items'))
        # params = request.form.get('items')
        # sendtelegram(params)
        return redirect(url_for('delivery'))
    return render_template('myitems.html', items=items)



@app.route('/remove/<int:id>')
def remove(id):
    print(id)
    shoppingCart = session['cart']
    try:
        theItem = Item.query.get_or_404(id)
        flash(' ' + theItem.name + ' has been deleted','danger')
        shoppingCart.remove(id)
        session['cart'] = shoppingCart
    except:
        flash(f'There was a problem, please try again.', 'danger')
        print('close error')
    if len(shoppingCart) < 1:
        # flash(f'Please add to your cart', 'warning')
        return redirect(url_for('index'))
    return redirect(url_for('cart'))

@app.route('/updateCart/<int:itemId>')
def updateCart(itemId):
    print(itemId)
    shoppingCart = session['cart']
    # Checks for duplication
    for i in shoppingCart:
        print(i)
        if i == itemId:
            flash(f'This item has been added to the cart.','warning')
            return redirect(url_for('home'))
    addedItem = Item.query.filter_by(id=itemId).first()
    # print("added " + addedItem)
    shoppingCart.append(itemId)
    print(shoppingCart)
    session['cart'] = shoppingCart
    flash(f' '+addedItem.name+ ' has been added to the cart.','success')
    return redirect(url_for('index', itemId=itemId))

@app.route('/preview/<int:itemid>')
def preview(itemid):
    print(session['cart'])
    item = Item.query.filter_by(id=itemid).first()
    vendor = User.query.filter_by(id = item.vendor).first()
    vendorname = vendor.username
    return render_template('preview.html', item=item, vendorname=vendorname, vendor=vendor)

@app.route('/show/<string:category>')
def show(category):
    items = Item.query.filter_by(category = category).all()
    print(items)
    return render_template('show.html', items=items, category=category)

@app.route('/additem', methods=['POST','GET'])
def additem():
    form = ItemForm()
    if form.validate_on_submit():
        pic = 'default.png'
        pictures = 'default.png'
        # if form.picture.data:
        #     print('YO!!!!!!!!! IT IS OVER HERE!!!')
            # pic = save_picture(form.picture.data)   
        # if form.other_pictures.data:
        #     for picture in form.other_pictures.data:
        #         pictures = []
        #         picture = save_picture(form.picture.data)
        #         pictures.append(picture)
        #         print (pictures)
        new_item = Item(name = form.name.data, category=form.category.data, price = form.price.data, image=form.link.data, description = form.description.data, vendor = current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash(f'New Item has been added', 'success')
        # x = datetime.now()
        # today = x.strftime("%Y/%m/%d")
        # time = x.strftime("%H:%M:%S")
        params = "New Item Added\n" + form.name.data + '\n' + "By " + current_user.username + " "
        sendtelegram(params)
        return redirect(url_for('account'))
    elif not form.is_submitted():
        print(form.errors)
        flash('There was a problem, please try again.','danger')
    return render_template('additemcopy.html', form=form)

def sendtelegram(params):
    url = "https://api.telegram.org/bot5367664024:AAEpnGU1Fa0qh0SCSB_TlJgmSfU2DdTz9bA/sendMessage?chat_id=-603441321&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content


@app.route('/makepayments/<string:account>/<string:amount>/<string:candidateId>/<string:network>', methods=['GET', 'POST'])
def makePayment(account, amount, customerId, network):
    test = True
    print(account, str(amount), customerId, str(network))

    # PaymentThingyDontFuckingTouch!
    username = "Pr3t0_gen"
    apiKey = ",)gnxTU_"
    key = str(random.randint(1000,9999))
    hashedApiKey = hashlib.md5(apiKey.encode())
    strHashedApiKey = str(hashedApiKey.hexdigest())
    userCredentials = username + key + strHashedApiKey
    print(type(userCredentials))
    usercred = hashlib.md5(userCredentials.encode())
    vodePayment = False
    # Okay,THankFuckingYou❤️!

    # TODO :change candidate to customer!
    # try:
    newTransaction = Transactions(candidate = customerId, account=account, award="tca", amount = float(amount))
    db.session.add(newTransaction)
    db.session.commit()
    print(newTransaction)
    sendtelegram("New transaction created:" + str(newTransaction.id) + " awaiting payment of "+ str(newTransaction.amount)+"and refernece.")
# except:
    # votingAlert("Create transaction was unsuccessful")

    if test == True:
        amount = 0.20

    if network == 'OT':
        payBy = 'VODAFONE'
        vodePayment = 'TRUE'

    elif network == 'VODAFONE':
        payBy = 'VODAFONE'
        vodePayment = 'TRUE'

    elif network == 'TIGO':
        payBy = 'AIRTELTIGO'
    
    elif network == 'AIRTEL':
        payBy = 'AIRTELTIGO'

    elif network == 'AIRTELTIGO':
        payBy = 'AIRTELTIGO'

    elif network == 'MTN':
        payBy = 'MTN'
    
    elif network == 'MTNGH' :
        payBy = 'MTN'

    else:
        print(str(network) + " Is not registered in switch statemenet")


    phoneNumber = "233"+ str(account[-9:])
    print(phoneNumber)


    print('WEBHOOK_VERIFIED')
    print(payBy)
    # stagingCallBack = "https://tca-staging.herokuapp.com/ussdconfirm/"+str(newTransaction.id)
    liveCallBack = "http://prestoussd.herokuapp.com/ussdconfirm/"+str(newTransaction.id)
    print(liveCallBack)
    endpoint = "http://api.nalosolutions.com/payplus/api/"

    # if vodePayment == True:
    data ={ 
        "merchant_id": "NPS_000153",
        "secrete": usercred.hexdigest(), 
        "key": key, 
        "order_id": str(customerId)+"-"+str(newTransaction.amount)+"TCA-PRS",
        "customerName": str(customerId)+"tca", 
        "amount": str(amount), 
        "item_desc": "TickedFor - :"+str(customerId) , 
        "customerNumber": str(phoneNumber), 
        "isussd":1,
        "newVodaPayment": vodePayment,
        "payby":payBy, 
        "callback": liveCallBack
        }
    
    headers = {
        'Content-Type': 'application/json'
    }

    json_object = json.dumps(data) 
    print(data)

    r = requests.post(endpoint, data=json_object, headers=headers, proxies=proxies)
    print(r.content)
    content = r.content

    content = json.loads(content)


    invoiceNo = content['InvoiceNo']
    newTransaction.ref = str(invoiceNo)
    db.session.commit()

    print(r.status_code)
    print(r.headers)
    return r.content
     

@app.route('/test', methods=['POST','GET'])
def test():
    return render_template('asdf.html')


@app.route('/ussdconfirm/<string:id>', methods=['GET', 'POST'])
def ussdconfirm(id):
    test = True
    print(request)
    json_content = {}
    response = make_response({"Response": "OK"})
    response.headers = {'Content-Type': 'application/json'}
    try:
            print(request.form)
            content = request.form  # ImmutableMultiDict(text, "")
            text = list(content.keys())[0]  # '{"Source":{"ReportTime":"2022-...
            json_content = json.loads(text)
            print(json_content)
    except:
        print("request.form - didnt work")

    if test == True:
        print("THIS IS A TEST VALUE!!!!")
        status = 'PAID'
        transactionId = Transactions.query.get_or_404(id).ref
        
    else:
        # votingAlert(json_content)
        status = json_content["Status"]
        transactionId = json_content["InvoiceNo"]
        
    if status == 'PAID':
        transaction = Transactions.query.filter_by(ref = transactionId).first()
        print(transaction)
        customer = Customer.query.get_or_404(transaction.candidate)
        # send_sms(" have" + str(transaction.ref) + " has been paid!")
        # print(transaction)
        

        if transaction:
            if transaction.paid == False:
                # votingAlert("USSD: New Vote for of "+ str(transaction.amount)+" for " + candidate.name)
               
                customer.paid = True
                transaction.paid = True
                # TODO newTicket!
                # db.session.add(newVote)
                # db.session.commit()
                phoneNumber = "0"+ str(transaction.account[-9:])
                print(phoneNumber)
                # votingChannel(transaction.amount + " votes have been bought for " + candidate.name + " from " + transaction.account)
                # votingAlert("Vote id: " + newVote.id + " is successful " )
                # votingAlert("Successfully updated " + candidate.name + " votes to " + str(candidate.votes) + "\n Vote Id: " + str(newVote.id))
                send_sms(phoneNumber, "Hello " + str(customer.name) + "\n" + "You have succesfully purchased " + str(customer.numberOfTickets) + " ticket(s) for " + str(customer.event) + " Your ticket code is: PRSXA3258BVGFM", "PrestoSl")
                print(" --------------------------------------------------------------------- ")
                # except:
                    # votingAlert("Attempt to update " + str(transaction.amount) + " votes for "+ candidate.name +" was unsuccessful.")
            else:
                print("This transaction has already been recorded.")
        else:
            print("There is no transaction with that id" + str(id))
    else:
        print("Nalo Payment " + transactionId + "has failed, kpotor!")
   
    return response

    return response


# @app.route('/ussdconfirm/<string:id>', methods=['GET', 'POST'])
# def ussdconfirm(id):
#     print(request)
#     json_content = {}
#     response = make_response({"Response": "OK"})
#     response.headers = {'Content-Type': 'application/json'}
#     try:
#             print(request.form)
#             content = request.form  # ImmutableMultiDict(text, "")
#             text = list(content.keys())[0]  # '{"Source":{"ReportTime":"2022-...
#             json_content = json.loads(text)
#             print(json_content)
#     except:
#         print("request.form - didnt work")
    
#     if test == True:
#         print("THIS IS A TEST VALUE!!!!")
#         status = 'PAID'
#         transactionId = Transactions.query.get_or_404(id).ref
        
#     else:
#         # votingAlert(json_content)
#         status = json_content["Status"]
#         transactionId = json_content["InvoiceNo"]
        
#     if status == 'PAID':
#         transaction = Transactions.query.filter_by(ref = transactionId).first()
#         # send_sms(" have" + str(transaction.ref) + " has been paid!")
#         # print(transaction)
        

#         if transaction:
#             if transaction.paid == False:
#                 # votingAlert("USSD: New Vote for of "+ str(transaction.amount)+" for " + candidate.name)
               
#                 candidate.votes = int(updatedVotes)
#                 newVote = Votes(candidateId = str(candidate.id), name = str(candidate.name), amount = str(transaction.amount), ref=str(transaction.id))
#                 transaction.paid = True
#                 db.session.add(newVote)
#                 db.session.commit()
#                 phoneNumber = "0"+ str(transaction.account[-9:])
#                 print(phoneNumber)
#                 votingChannel(transaction.amount + " votes have been bought for " + candidate.name + " from " + transaction.account)
#                 # votingAlert("Vote id: " + newVote.id + " is successful " )
#                 votingAlert("Successfully updated " + candidate.name + " votes to " + str(candidate.votes) + "\n Vote Id: " + str(newVote.id))
#                 send_sms(phoneNumber, "Congratulations! You have successfully bought " + str(transaction.amount) + " vote(s) for " + str(candidate.name) + "transactionId: PRS" +id + "NLO"+str(transaction.ref)  , "TCA")
#                 print(" --------------------------------------------------------------------- ")
#                 # except:
#                     # votingAlert("Attempt to update " + str(transaction.amount) + " votes for "+ candidate.name +" was unsuccessful.")
#             else:
#                 votingAlert("This transaction has already been recorded.")
#         else:
#             votingAlert("There is no transaction with that id" + str(id))
#     else:
#         print("Nalo Payment " + transactionId + "has failed, kpotor!")
   
#     return response



def checkForPollSession(sessionId):
 # Search db for a session with that Id
    session = Poll.query.filter_by(sessionId = sessionId).first()
    # If there is none, create one
    if session == None :
        print("Session " + sessionId + " is not in the database.")
        #  create session!
        # print("sessionId " + getSession.sessionId + " has been found")
        newSession = Poll(sessionId = sessionId)
        db.session.add(newSession)
        db.session.commit()
        print(sessionId + " session has been created")
        session = newSession
    print(session)
    return session


@app.route('/naloussd', methods=['GET', 'POST'])
def ticketPoll():
    print(request.json)
    sessionId = request.json['SESSIONID']
    # menu = request.json['USERDATA']
    print(sessionId)
    msisdn = request.json['MSISDN']
    mobileNetwork = request.json['NETWORK']
    extension = '148'
    data = request.json['USERDATA']
    print(data)

    poll = checkForPollSession(sessionId)
    if poll:
        print(poll)
        # TODO : Fill the fields for repr for poll.
        # If a poll has an event.
        if poll.event == None:
            poll.event = "A Night Under The Stars"
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Welcome to the poll for A Night Under The Stars powered by talanku.com. \n Press 1 to continue",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        elif poll.startDate == None:
            poll.startDate = datetime.now()
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Which of these movies would you like to see \n 1. Black Panther  \n 2. Cruella \n 3. This Lady Called Life \n 4. Black Widow \n 5. Fatherhood ",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        elif poll.movie == None:
            poll.movie = data
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Have you used talanku.com before? \n 1.Yes \n 2.No",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        elif poll.talanku == None and data == 1:
            poll.talanku = True
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"On a scale of 1 to 10, how was the service?!",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        elif poll.talanku == None and data == 2:
            poll.talanku = False
            poll.probability = 0
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Thank you for your input. Poll results will go live on Friday! \n Visit talanku.com for more information",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        elif poll.probability == None:
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Thank you for your input. Poll results will go live on Friday! \n Visit talanku.com for more information",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp 

       

        else:
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Oops, if you are seeing this, then Nana Kweku Really FuckUp on this USSD",
                "MSGTYPE":False
            }
            resp = make_response(response)
            return resp

            
        # Type Of Ticket
        # Number Of Tickets
        # Name
        # PhoneNumber
        # PaymentId



# @app.route('/naloussd', methods=['GET', 'POST'])
def naloussd():
    print(request.json)
    sessionId = request.json['SESSIONID']
    # menu = request.json['USERDATA']
    print(sessionId)
    msisdn = request.json['MSISDN']
    mobileNetwork = request.json['NETWORK']
    extension = '148'
    data = request.json['USERDATA']
    print(data)

    customer = checkForSession(sessionId)
    if customer:
        print(customer)
        # TODO : Fill the fields for repr for customer.
        # If a customer has an event.
        if customer.event == None:
            customer.event = "Welcome to the poll for A Night Under The Stars powered by talanku.com \n "
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Welcome to the poll for A Night Under The Stars. Press 1 to continue. \n powered by talanku.com",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        if customer.typeOfTickets == None:
            if data == 1:
                customer.typeOfTickets = "Regular"
                db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Hello, Welcome to PrestoVotes. How many " + customer.typeOfTickets + " tickets would you like to buy",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp


        elif customer.numberOfTickets == None:
            customer.numberOfTickets = data
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Please enter your name.",
                "MSGTYPE":True
            }
            resp = make_response(response)
            return resp

        elif customer.name == None:
            customer.name = data
            db.session.commit()
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Hi "+ data+" you are attempting to buy. " +  customer.numberOfTickets + " " + customer.typeOfTickets + " tickets. \n Please wait while we trigger payment for " + customer.numberOfTickets,
                "MSGTYPE":False
            }
            makePayment(msisdn, customer.numberOfTickets, customer.id, mobileNetwork)
            resp = make_response(response)
            return resp
        else:
            response = {
                "USERID": "prestoGh",
                "MSISDN":msisdn,
                "MSG":"Oops, if you are seeing this, then Nana Kweku Really FuckUp on this USSD",
                "MSGTYPE":False
            }
            resp = make_response(response)
            return resp

            
        # Type Of Ticket
        # Number Of Tickets
        # Name
        # PhoneNumber
        # PaymentId


@app.route('/reciept/<int:orderId>', methods=['POST','GET'])
def reciept(orderId):
    session['cart'] = []
    order = Order.query.get_or_404(orderId)
    return render_template('reciept.html', order=order)  

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        checkUser = User.query.filter_by(phone = form.phone.data).first()
        if checkUser:
            flash(f'This Number has already been used','danger')
            return redirect (url_for('register'))
        else:
            new_user = User(username = form.username.data, phone = form.phone.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            params = "New Account Created for " + new_user.username
            sendtelegram(params)
            flash (f'Account for ' + form.username.data + ' has been created.', 'success') 
            user = User.query.filter_by(phone = form.phone.data).first()
            login_user(user, remember=True)
            return redirect (url_for('index'))
    else:
        print(form.errors)
        flash (f'There was a problem', 'danger')
    return render_template('register.html',  form=form)

@app.route('/account')
def account():
    user = current_user
    return render_template('account.html', user=user)

@app.route('/allusers')
def allusers():
    allusers = User.query.all()
    return render_template('allusers.html', allusers=allusers)

@app.route('/categories')
def categories():
    return render_template('cat.html')

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         # Login and validate the user.
        # user should be an instance of your `User` class
        user = User.query.filter_by(phone=form.phone.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            print ("Logged in:" + user.username + " " + user.phone)
            print(form.password.data)
            return redirect(url_for('index'))
        else:
            flash(f'Incorrect details, please try again', 'danger')
    return render_template('login.html', form=form)

@app.route('/bookmarks')
def bookmarks():
    return 'Done'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/myitems')
def myitems():
    items = Item.query.filter_by(vendor = current_user.id).all()
    print(items)
    user = current_user
    return render_template('adminitems.html', items = items, user=user)

@app.route('/<int:phone>/<int:itemId>')
def item(phone, itemId):
    user = User.query.filter_by(phone = phone).first()
    item = Item.query.filter_by(id=itemId).first()
    return 'hmmmm'


@app.route('/update/<int:itemid>', methods=['POST','GET'])
def update(itemid):
    form = ItemForm()
    item = Item.query.filter_by(id = itemid).first()
    update = True
    print(item)
    if request.method == 'GET':
        print(item.image)
        form.name.data = item.name
        form.price.data = item.price
        form.description.data = item.description
        form.picture.data = item.image 
        form.link.data = item.image
        form.category.data = item.category 
    if request.method == 'POST':
        if form.validate_on_submit():
            prevPicture = item.image
            print(item.image)
            print(prevPicture)
            print("Posting new remote")
            # item = Item(name = form.name.data, description = form.description.data, price = form.price.data, image = form.link.data)
            item.name = form.name.data
            item.price = form.price.data
            item.image = form.link.data
            item.description = form.description.data
            item.category = form.category.data
            db.session.commit()
            flash(f'Your Item has been updated', 'success')
            return redirect(url_for('account'))
        else:
            flash(f'There is a problem', 'danger')
                 
    return render_template('additemcopy.html', form=form, item=item, update=update)

@app.route('/delete/<int:itemid>', methods=['POST','GET'])
def delete(itemid):
    Item.query.filter_by(id = itemid).delete()
    db.session.commit()
    return redirect(url_for('myitems'))

@app.route('/admin/delete/<string:itemid>', methods=['POST','GET'])
def admindelete(itemid):
    Item.query.filter_by(id = itemid).delete()
    db.session.commit()
    return redirect(url_for('allitems'))



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sendmessage')
def sendmessage():
    api_key = "aniXLCfDJ2S0F1joBHuM0FcmH" #Remember to put your own API Key here
    phone = "0592865541" #SMS recepient"s phone number
    message = "You have been verified. You can now sell on talanku.com"
    sender_id = "Tnsghana" #11 Characters maximum
    send_sms(api_key,phone,message,sender_id)
    flash (f'Account has been verified','success')
    return redirect('dashboard')

def send_sms(phone,message,sender_id):
    params = {"key":"aniXLCfDJ2S0F1joBHuM0FcmH","to":phone,"msg":message,"sender_id":sender_id}
    url = 'https://apps.mnotify.net/smsapi?'+ urllib.parse.urlencode(params)
    content = urllib.request.urlopen(url).read()
    print (content)
    print (url)


@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template("users.html", users = users)


# Request Body
@app.route('/orders', methods=['GET', 'POST'])

# Function
def orders():
    # Query is initialized to a variable - orders
    orders = Order.query.all()

    # new array is initiales
    allOrders = []

    # Iterate through the list returned by the query
    for order in orders:

        # Converting to json
        newResponse = {
            "orderId":order.id,
            "price":order.price,
            "location":order.location,
            "phone":order.phone
        }
        # After every iteration, we upload to the arra
        allOrders.append(newResponse)

    # We print all orders
    print(allOrders)

    # Make a response, this parses the data to a readable format
    response = make_response(allOrders)
    # Return the response. Which is recieved by the client.
    return response


@app.route('/neworder', methods=['GET', 'POST'])
def neworder():
    print(request.json["name"])
    print(request.json["price"])
    print(request.json["location"])
    print(request.json["phone"])


    # THis is how you create a new entry to your db.
    newOrder = Order(name = request.json['name'], phone = request.json['phone'], price=request.json['price'], location = request.json['location'])
    # You add to your session
    db.session.add(newOrder)
    # Commits the data to storage if all checks are passed.
    db.session.commit()

    newResponse = {
        "orderId": newOrder.id,
        "name":newOrder.name,
        "phone":newOrder.phone,
        "price":newOrder.price,
        "location":newOrder.location
    }

    response = make_response(newResponse)
    return response

@app.route('/getorder/<int:id>', methods=['GET', 'POST'])
def getorder(id):
    order = Order.query.get_or_404(id)
    print(order)
    jsonOrder = {
        "orderId":order.id,
        "price":order.price,
        "location":order.location,
        "phone":order.phone,
    }

    response = make_response(jsonOrder)
    return response

@app.route('/deleteOrder/<int:id>', methods=['GET', 'POST', 'DELETE'])
def deleteOrder(id):

    try:
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()
        response = "Order Id: " + str(id) + " was deleted successfully!"

    except:
        response = "Order Id: " + str(id) + " was not deleted!!"
   
    return make_response(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)