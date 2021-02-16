import datetime
import logging
from bs4 import BeautifulSoup
import requests
from azure.data.tables import TableServiceClient
import os
import random
import azure.functions as func

#Get the connection string to the Azure Table Storage
tableConnectionString = os.environ['CUSTOMCONNSTR_tableConnectionString']

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    #Create Azure Tabel Service connection, form connection string
    table_service_client = TableServiceClient.from_connection_string(conn_str=tableConnectionString)
    #Connect to the right table
    table_client = table_service_client.get_table_client(table_name="scraperdata")

    
    #Let's fetch a html page
    page = requests.get("http://nos.nl")

    #Parse the page with BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    #Loop through all main articles
    for article in soup.find_all('li', class_="cb-mab"):
        #Find the title of the article
        title = article.find('h2').getText()
        print(title)

        #Create a Table Service entity
        tableEntity = {
            'PartitionKey':'title',
            'RowKey':'test' + str(random.randint(0,10000)),
            'Title':title
        }

        #Save the entity in azure table storage
        entity = table_client.create_entity(entity=tableEntity)
        print(entity)
    
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
