# 🐔 Chicken Price API
Een eenvoudige API om de huidige marktprijs van braadkippen per kilo op te halen. De prijzen worden elk uur vernieuwd voor zowel Deinze als ABC Markt.

## 📌 Functionaliteiten

    /current-price → Haal de meest recente kippenprijs op.
    /update → Forceer een handmatige update van de prijzen.

## 🚀 Snelle Start
1. Start de API met onderstaand Docker Compose.
```yaml
version: "3"

services:
    chicken-price-api:
        image: ghcr.io/arne-vl/chicken-price-api:latest
        ports:
            - 8000:8000
        volumes:
            - ./chicken-price-scraper:/data
```
2. De API is toegankelijk op poort 8000.
3. Gebruik de endpoints om actuele prijzen op te halen of een update te forceren.

## 🔄 Automatische Updates
De API ververst de prijzen automatisch elk uur, zodat je altijd up-to-date bent met de laatste marktinformatie.

Voor vragen of verbeteringen, open een issue of draag bij aan het project! 🐓

## 💾 Opslaan in Database
Er is de mogelijkheid om de data op te slaan in een PostgreSQL database, hiervoor gebruik je volgende environment variabelen:

| Naam            | Standaard    | Beschrijving                                           |
| --------------- | ------------ | ------------------------------------------------------ |
| DB_NAME         |              | De naam van de Postgres Database                       |
| DB_USER         |              | De naam van de Postgres gebruiker die verbinding maakt |
| DB_PASSWORD     |              | Het wachtwoord voor de Postgres gebruiker              |
| DB_HOST         |              | De host van de Postgres instantie                      |
| DB_PORT         | 5432         | De poort waarop toegang tot Postgres                   |
| DB_SCHEMA       | public       | Het schema waarin de gegevens worden opgeslagen        |
| DB_ABC_TABLE    | abc_price    | De naam voor de tabel met ABC prijsnoteringen          |
| DB_DEINZE_TABLE | deinze_price | De naam voor de tabel met Deinze prijsnoteringen       |
