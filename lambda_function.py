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
    cursor.execute("SELECT * FROM veer_db.river_levels")
    result = cursor.fetchall()
    datetimelist = []
    for row in result:
        datetimelist.append((row['datetime'],row['height']))
        #print(row['datetime'])
    maxind = datetimelist.index(max(datetimelist))
    to_print = datetimelist[maxind]
    print(to_print)
    return {
        'statusCode': 200,
        'body': json.dumps({'datetime': str(to_print[0]), 'height': str(to_print[1])})
    }
