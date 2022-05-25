from flask import Flask, request, redirect, render_template
from functions.sqlquery import sql_delete, sql_query, sql_query2, sql_edit_insert

app = Flask(__name__)
warehouses=sql_query("SELECT name FROM warehouse order by name")

@app.route('/item_database')
def item_database():
    results = sql_query(''' SELECT * FROM data_table''')
    warehouses=sql_query("SELECT name FROM warehouse order by name")
    return render_template('sqldatabase.html', results=results, warehouses=warehouses)

@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def item_datainsert():
    if request.method == 'POST':
        track_num = request.form['track_num']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        warehouse = request.form['warehouse']
        sql_edit_insert(''' INSERT INTO data_table (item_name,track_num,quantity,warehouse) VALUES (?,?,?,?) ''', (item_name,track_num,quantity,warehouse) )
    results = sql_query(''' SELECT * FROM data_table''')

    return render_template('sqldatabase.html', results=results, warehouses=warehouses)
    
@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def item_datadelete():
    if request.method == 'GET':
        t_num = request.args.get('t_num')
        i_name = request.args.get('i_name')
        sql_delete(''' DELETE FROM data_table where item_name = ? and track_num = ?''', (i_name,t_num) )
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('sqldatabase.html', results=results, warehouses=warehouses)

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def item_editlink():
    if request.method == 'GET':
        et_num = request.args.get('et_num')
        ei_name = request.args.get('ei_name')
        eresults = sql_query2(''' SELECT * FROM data_table where item_name = ? and track_num = ?''', (ei_name,et_num))
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('sqldatabase.html', eresults=eresults, results=results, warehouses=warehouses)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def item_dataedit():

    if request.method == 'POST':
        old_track_num = request.form['old_track_num']
        old_item_name = request.form['old_item_name']
        track_num = request.form['track_num']
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        warehouse = request.form['warehouse']
        sql_edit_insert(''' UPDATE data_table set item_name=?,track_num=?,quantity=?,warehouse=? WHERE item_name=? and track_num=? ''', (item_name,track_num,quantity,warehouse,old_item_name,old_track_num) )
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('sqldatabase.html', results=results, warehouses=warehouses)

@app.route('/insert_warehouse',methods = ['POST', 'GET']) #this is when user submits an insert
def wh_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        name = request.form['name']
        sql_edit_insert(''' INSERT INTO warehouse (name) VALUES (?) ''', (name,) )
    results = sql_query(''' SELECT * FROM warehouse''')
    return render_template('warehouse.html', results=results)

@app.route('/warehouse')
def wh_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM warehouse''')
    return render_template('warehouse.html', results=results)

@app.route('/delete_warehouse',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete_w():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        name = request.args.get('name')
        sql_delete(''' DELETE FROM warehouse where name = ?''', (name,) )
    results = sql_query(''' SELECT * FROM warehouse''')
    return render_template('warehouse.html', results=results)

@app.route('/query_edit_warehouse',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink_w():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        name = request.args.get('name')
        eresults = sql_query2(''' SELECT * FROM warehouse where name = ?''', (name,))
        print('[+]', name, eresults)
    results = sql_query(''' SELECT * FROM warehouse''')
    return render_template('warehouse.html', eresults=eresults, results=results)

@app.route('/edit_warehouse',methods = ['POST', 'GET']) #this is when user submits an edit
def wh_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_name = request.form['old_name']
        name = request.form['name']
        sql_edit_insert(''' UPDATE warehouse set name=? WHERE name=?''', (name,old_name) )
    results = sql_query(''' SELECT * FROM warehouse''')
    return render_template('warehouse.html', results=results)

@app.route('/',methods = ['POST', 'GET'])
def render_main():
    return render_template('main.html')


# Only runs the web server if this file is explicitly ran
if __name__ == "__main__":
    app.run(host='0.0.0.0')

