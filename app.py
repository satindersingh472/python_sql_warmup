import dbcreds
import mariadb

def sales_persons():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call sales_persons()')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    for result in results:
        print(result[0],': ' , result[1])
    pick_salesperson = input('Please pick one of the salesman by typing the number of the salesman : ')
    return pick_salesperson


def buy_something(argument1):
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call items()')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    for result in results:
        print(result[0],': ', result[1], result[2])
    while(True):
        pick_item = input('Please choose an item to buy from seller you choose:  ')
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute('call items_sale(?,?)',[argument1, pick_item])
        cursor.close()
        conn.close()
        print('Item number: ',pick_item, 'Purchased successfully')
        upsell =  input('Continue Shopping? (yes/no)')

        if upsell in ['yes']:
            continue
        else:
            print('Thanks for shopping')
            break

person =  sales_persons()
buy_something(person)
    
