#!/usr/bin/env python

#Dependencias necesarias:
import time, datetime, twitter

#Generamos variables para dia, fecha y hora
day = datetime.datetime.today().weekday()
z = time.strftime("%H:%M:%S", time.localtime())
y = time.strftime("%d-%m-%Y", time.localtime())

#Validamos los dias de la semana y el horario
# Lunes = 0
# Martes = 1
# Miercoles = 2
# Jueves = 3
# Viernes = 4

if (day == 0 or day == 1 or day == 2 or day == 3 or day == 4) and (z >= "08:00" and z <= "17:59"):

# Colocamos las credenciales obtenidas en twitter developers
    twitter_handle = 'cuenta de twitter a enviar mensajes'
    consumer_key = "coloque aqui el consumer_key"
    consumer_secret = "coloque aqui el consumer_secret"
    access_token_key = "coloque aqui el access_token_key"
    access_token_secret = "coloque aqui el access_token_secret"

    api = twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret)

    ##Enviar tweet publico:
    tweetPublico = "Hola " - twitter_handle + "! son las " + str(z) + " del dia de hoy: " + str(y) + ", voy a enviarte un mensaje cada hora."
    
    ##########################################
    ## Enviar Mensaje Directo:
    msgDirecto = "Hola " + twitter_handle + ", este es un mensaje directo. Enviado: " + t

    ##########################################
    ## Validaciones:

    if (tweetPublico):
        status = api.PostUpdate(tweetpublico)
        print "se envio el tweet!!!"
    else
        print "No habia tweet para enviar..."
    
    if (msgDirecto):   
        t = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
        send_msg = api.PostDirectMessage(msg, user_id=None, screen_name=twitter_handle)    
        print "Mensaje Directo enviado!!!"
    else
        print "No habia Mensaje Directo para enviar..."
else:
    print "No estoy en el horario de lun-vie de 8am - 5pm"
## Dev
