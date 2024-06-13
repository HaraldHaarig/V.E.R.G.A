from Tkinter_GUI.Login import Login
from API.GameAPI import getGame


def addToWishlist(title, login:Login): 
    steamid=login.getSteamId()
    connection=login.getConnection()

    with connection.cursor() as cur:
        sql="""INSERT INTO wishlist(gamenname,steamid) VALUES(%s,%s)"""
        cur.execute(sql,(title,steamid,))
        connection.commit()


def getWishlist(login:Login):
    steamid=login.getSteamId()
    connection=login.getConnection()
    title=[]
    img=[]
    details=[]

    with connection.cursor() as cur:
        sql="""SELECT gamenname FROM wishlist WHERE steamid=%s"""
        cur.execute(sql, (steamid,))
        rows=cur.fetchall()
        
        for row in rows:
            title.append(row[0])
            tempimg,tempdetails=getGame(row[0])
            img.append(tempimg)
            details.append(tempdetails)
        return img,title,details