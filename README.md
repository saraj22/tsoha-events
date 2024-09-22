# Tapahtumasovellus

Sovelluksessa näkyy tietyllä alueella järjestettävät tapahtumat, joista voi lukea lisätietoa ja niiden järjestäjistä voi lukea arvioita. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen tapahtumien määrän. Aluetta painamalla käyttäjä näkee kaikki kyseisellä alueella järjestettävät tapahtumat aikajärjestyksessä
- Käyttäjä voi luoda uuden tapahtuman antamalla sille nimen, paikka- ja aikatiedot, aiheen sekä tarkemman selityksen
- Käyttäjä voi muokata luomansa tapahtuman tietoja
- Käyttäjä voi suorittaa haun tapahtumista aiheen perusteella
- Käyttäjä voi antaa arvion tapahtumasta sekä sen järjestäjästä ja lukea muiden antamia arvioita
- Käyttäjä voi seurata muita käyttäjiä, sekä nähdä heidän järjestämiä tapahtumia
- Ylläpitäjä voi lisätä ja poistaa tapahtumia
- Ylläpitäjä voi myös tarvittaessa poistaa annettuja arvioita tai käyttäjiä


Tällä hetkellä sovelluksessa toimii vasta sisäänkirjautuminen, uuden käyttäjän rekisteröinti sekä uloskirjautuminen.

Sovellus ei ole testattavissa Fly.iossa.
Sovellusta voi testata kloonaamalla tämän repositorion omalle koneelle ja siirtymällä sen juurikansioon. 
Luo sitten kansioon .env-tiedosto ja määritä sen sisällöksi: 



DATABASE_URL= tietokannan-paikallinen-osoite

import secrets

SECRET_KEY=secrets.token_hex(16)



Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt



Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql

Nyt voit käynnistää sovelluksen komennolla

$ flask run


