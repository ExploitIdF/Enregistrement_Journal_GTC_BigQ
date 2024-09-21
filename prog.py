import pandas as pd, numpy as np
import glob, re,datetime
from google.cloud import bigquery
from google.cloud import storage
client = bigquery.Client()
clientST=storage.Client()

blobs = clientST.list_blobs('gtc-test')

table_id='tunnels-dirif.GTC.Consignations'
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("Horodate", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("Metier", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("Equipement", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("Ouvrage", bigquery.enums.SqlTypeNames.STRING),   
        bigquery.SchemaField("Libelle", bigquery.enums.SqlTypeNames.STRING),    
         bigquery.SchemaField("Evenement", bigquery.enums.SqlTypeNames.STRING),    
         bigquery.SchemaField("Variable", bigquery.enums.SqlTypeNames.STRING),    
         bigquery.SchemaField("Operateur", bigquery.enums.SqlTypeNames.STRING),
    ],
    skip_leading_rows=1,
    write_disposition="WRITE_APPEND",
)
for blob in blobs:
    print(blob.name)
    uri=uri='https://storage.googleapis.com/gtc-test/' +blob.name
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config


    )   
    load_job.result()  
destination_table = client.get_table(table_id)
print("{} enregistrements envoyés".format(destination_table.num_rows))
