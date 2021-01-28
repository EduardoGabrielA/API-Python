"""
import boto3

client = boto3.client('translate', region_name="us-east-1")
text = "hola, mi nombre es Eduardo Gabriel"
result = client.translate_text(Text=text, SourceLanguageCode="auto", 
    TargetLanguageCode="en")
print(result['TranslatedText'])
"""
import os
import json
import boto3

from todos import decimalencoder

dynamodb = boto3.resource('dynamodb')

client = boto3.client('translate', region_name="us-east-1")

def translate(event, context): #event, context
    # TODO implement
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    toTraduce = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    lenguajeAtraducir = event['pathParameters']['language']
    
    #client
    text = "hola, mi nombre es Eduardo Gabriel"
    
    """
    result = client.translate_text(Text=toTraduce, SourceLanguageCode="auto", 
        TargetLanguageCode=lenguajeAtraducir)
    #print(result['TranslatedText'])
    """
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(text)#, toTraduce['Item']['text']
                           #cls=decimalencoder.DecimalEncoder)
    }

    return response
"""
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
"""
