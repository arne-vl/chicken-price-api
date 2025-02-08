# Wa staan de kiekes?
Bekijk snel de huidige marktprijs van braadkippen per kilo.
Zowel Deinze als ABC markt.
Wordt elk uur vernieuwd.

<a href="https://hub.docker.com/r/arnevl/chicken-price-api" target="_blank">
  <img alt="Static Badge" src="https://img.shields.io/badge/docker%20-%20chicken--price--api%20-%20blue?color=blue">
</a>

## Installatie docker-compose:
```yaml
version: "3"

services:
  chicken-api:
    image: arnevl/chicken-price-api:latest
    ports:
      - 8000:8000
    volumes:
      - ./chicken-price-scraper:/data
```

## Methods
`/price` : ophalen laatste prijs
`/update` : manueel updaten
