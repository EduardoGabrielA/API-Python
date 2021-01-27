"""
import boto3

client = boto3.client('translate', region_name="us-east-1")
text = "hola, mi nombre es Eduardo Gabriel"
result = client.translate_text(Text=text, SourceLanguageCode="auto", 
    TargetLanguageCode="en")
print(result['TranslatedText'])
"""

import json
import boto3

def lambda_handler(event, context): #event, context
    # TODO implement
    client = boto3.client('translate', region_name="us-east-1")
    text = "hola, mi nombre es Eduardo Gabriel"
    lenguajeAtraducir = "fr"
    
    result = client.translate_text(Text=text, SourceLanguageCode="auto", 
        TargetLanguageCode=lenguajeAtraducir)
    print(result['TranslatedText'])
    
    capturaRoute = event['pathParameters']['language']
    
    return {
        'statusCode': 200,
        'body': json.dumps(capturaRoute)
    }

"""
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
"""
