import pyautogui as pg
import webbrowser as wb
import time as t


name = pg.prompt("What is your name? ")
if name== "Julia":
    wb.open("https://venturemom.com/wp-content/uploads/2016/08/vanessaandjulia.jpg")
    pg.alert("I love your name!")
    t.sleep (2)

elif name=="Cassidy":
    pg.alert("cool name")
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US761&biw=681&bih=647&tbm=isch&sa=1&ei=dgzbW6TPE6qd_QaTkKKgCA&q=french+bulldog+puppies&oq=french+bulldog&gs_l=img.1.1.0l10.21216.29481..31440...6.0..0.69.1530.30......0....1..gws-wiz-img.......0i24j0i10i24j0i67j0i30j0i8i30.wC3KwloqiXk#imgrc=jCAcLfGsVZg1OM:")
    t.sleep (3)

elif name== "Peter":
    pg.alert("I dislike that name")
    wb.open("https://images-na.ssl-images-amazon.com/images/I/61FYUKHqDnL._SX355_.jpg")
    t.sleep (4)
elif name == "Emily":
    pg.alert ("Emily is a cool name")
    wb.open("https://www.google.com/search?q=cat&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJ7Zyn8vneAhUQn-AKHVXHDaEQ_AUIDygC&biw=1315&bih=647#imgrc=FvRC4kFUyJvc2M:")

elif name == "Jurgis":
    pg.alert ("HIT IT JURGI")

elif name == "Carter":
    pg.alert ("Carter is a cool name")
    wb.open("https://www.google.com/search?q=hockey+stick&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj7kPTJ8vneAhWOMd8KHZ0wC2QQ_AUIDigB&biw=1315&bih=647#imgrc=v-pbD9G58U_FEM:")
 
elif name == "Annabelle":
    pg.alert ("Annabelle is a cool name")

else:
    pg.alert("What is your name" + name)


food = pg.prompt("What is your favorite food? ")
if food == "hotdogs":
    pg.alert(" hotdogs are okay")
    wb.open("https://www.google.com/search?q=hot+dog+cartoon&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQjfOu8_neAhUjVt8KHc4eDmEQ_AUIDigB&biw=1315&bih=647#imgrc=1TnuetPDBJftFM: ")

elif food == "ice cream":
    pg.alert("ice cream is my fav")    
    wb.open(" https://minimalistbaker.com/wp-content/uploads/2015/06/AMAZING-Vegan-Cherry-Pie-ICE-CREAM-10-ingredients-simple-methods-SO-delicious-vegan-recipe-icecream-dessert-cherry.jpg")
    t.sleep("5")

elif food== "pasta":
    pg.alert (" J'adore pasta!")
    wb.open("https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/2/4/1/RX-FNM_030111-Lighten-Up-012_s4x3.jpg.rend.hgtvcom.616.462.suffix/1382539856907.jpeg ")
    t.sleep(4)
elif food == "brownies":
    pg.alert("YUM")
    wb.open("https://www.wellplated.com/wp-content/uploads/2016/02/One-Bowl-Brownies-with-cocoa-powder.jpg")

elif food == "pizza":
    pg.alert(" pizza is okay")

elif food == "nutella":
    pg.alert("WHAT HAPPENS IF SOMEONES ALERGIC") 
 
    t.sleep (3)
else:
    pg.alert ("Your favorite food is" + food)


sport = pg.prompt("What sport do you like to play?")

if sport== "hockey":
    pg.alert("hockey is the best!")
    wb.open("https://www.youtube.com/watch?v=v9EtLGwrJ58")
    t.sleep (6)

elif sport == "horse back riding":
    pg.alert ("horse back riding is my fav")
    wb.open ("https://www.youtube.com/watch?v=Q0D3TgWr-ag")
    t.sleep (6)
elif sport == "lax":
    pg.alert ("I love lax")
    wb.open ("https://www.youtube.com/watch?v=tmgqaBo3x3I ")
    t.sleep (6)
elif sport == "soccer":
    pg.alert ("I hate soccer")
    wb.open ("https://www.youtube.com/watch?v=hDm22pMfvEQ ")
    t.sleep (6)

elif sport == "water polo":
    pg.alert ("I love water polo")

elif sport == "fortnite":
    pg.alert (" I LOVE NINGAS STREAMS")
    wb.open ("https://www.youtube.com/watch?v=M3KEl7lsMd8 ")
    t.sleep (6)

else:
       pg.alert ("Your favorite sport is" + sport)

movie = pg.prompt("What is you favorite movie?")

if movie== "Winnie the Poo":
    pg.alert ("LOVE THAT MOVIE")
    wb.open ("https://lumiere-a.akamaihd.net/v1/images/c94eed56a5e84479a2939c9172434567c0147d4f.jpeg")
    t.sleep (4)
elif movie == "Frozen":
    pg.alert ("ICYYYYYYYY")
    wb.open ("https://lumiere-a.akamaihd.net/v1/images/image_b349f970.jpeg ")
    t.sleep (4)
elif movie == "Game night":
    pg.alert ("I love that movie")

elif movie == "Hunger Games":
    pg.alert ("Catniss")

elif movie == "Instant Family":
    pg.alert (" That made me cry")


else:
       pg.alert ("Your favorite movie is" + movie)

color = pg.prompt("What is your fav color?")

if movie== "blue":
    pg.alert ("THAT IS MY FAV COLOR TOO")
    wb.open ("data:image/jpeg;base64,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")
    t.sleep (2)
elif movie == " yellow":
    pg.alert ("THAT IS KATES FAV COLOR")

elif movie == "red":
    pg.alert ("ahhh that is the color of blood")

elif movie == "purple":
    pg.alert ("purple is a pretty color")

elif movie == "green":
    pg.alert (" HEALTHY")

elif movie == "pink":
    pg.alert ("I love pink")


else:
       pg.alert ("Your favorite color is" + color)







