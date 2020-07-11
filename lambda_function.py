import json
import pymysql

#Creates MySQL connection
connection = pymysql.connect(host='internly-db.co952byay6uw.eu-west-2.rds.amazonaws.com',
                             user='admin',
                             password='tlc041!Durham',
                             db='veer_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
