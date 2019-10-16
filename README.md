# pytweet
Aplicación hecha en python para enviar tweets de lunes a viernes (de 8am a 5pm)

### Dependencias:

Para ejecutar este script necesitaras:
- Crear una aplicacion en twitter para desarrolladores (https://developer.twitter.com/en/apps)
- Copiar y pegar los siguentes valores en el archivo **mytweet.py**:
	1. consumer_key
    2. consumer_secret
    3. access_token_key
    4. access_token_secret
- Instalar **python-twitter** en el equipo donde se ejecutara (https://github.com/bear/python-twitter)
- Modificar los campos twitter_handle, tweetPublico y mensajeDirecto

### Primeras pruebas:

Para ejecutarlo, es necesario escribir el siguiente comando en la terminal:
```
$ python pytweet.py
```

En caso de no mostrar ningun error, mostrara en pantalla: 

```
$ se envio el tweet!!!
```

Adiconalmente, en caso de haber escrito un mensaje directo, se mostrara:

```
$ Mensaje Directo enviado!!!
```
