# azure-functions-scraper

We designed this project to demo 3 key concepts:

1. Azure Functions
1. GitHub Actions and Workflows
1. ARM Templates

### The App

This repo contains an Azure Function app written in Python, that scrapes the Dutch news site, [NOS.nl](https://nos.nl/) for new articles. It grabs the article titles on the homepage, and stores them to Azure Table service. We're using a Timer Trigger, so the function runs every X minutes.

### To Deploy It

To make deployment of our function app easy and repeatable, we're using an ARM Template. ARM Templates allow us to declare which resources we want to spin up in Azure, and are Azure's native method of handling Infrastructure-as-Code. 
