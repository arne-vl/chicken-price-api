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
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_SCHEMA`
