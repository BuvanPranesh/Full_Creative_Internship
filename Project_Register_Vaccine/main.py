@app.route('/booking')
def book():
    id1 = int(request.args.get('id'))
    register(id1)
    return render_template('register.html')



@app.route('/booking')
def book():
    id1 = int(request.args.get('id'))
    register1(id1)
    return render_template('register.html')