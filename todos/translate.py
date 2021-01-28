import os
import json
import boto3

from todos import decimalencoder

dynamodb = boto3.resource('dynamodb')

client = boto3.client('translate', region_name="us-east-1")

def translate(event, context):
    # Creando variable table 
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    toTraduce = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    lenguajeAtraducir = event['pathParameters']['language']
    
    # Traduciendo petición de DynamoDB
    result = client.translate_text(Text=toTraduce['Item']['text'], SourceLanguageCode="auto", 
        TargetLanguageCode=lenguajeAtraducir)
    
    # create a response.... EN caso de querer solo el texto usar: result['TranslatedText']
    response = {
        "statusCode": 200,
        "body": json.dumps(result) 
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
