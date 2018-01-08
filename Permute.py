import itertools
import sys
import csv
import json
import logging
import os
from flask import Flask, request, render_template, url_for, send_from_directory


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>', methods = ['GET', 'POST'])
def send_static(path):
    return send_from_directory('static', path)

# @app.route('/template', methods=['GET', 'POST'])
# def block_retriever():
#     app.logger.debug('This block of code was reached. congrats')
#     block1 = request.form['block1']
#     block2 = request.form['block2']
#     block3 = request.form['block3']
#     block4 = request.form['block4']
#     block5 = request.form['block5']
#     block6 = request.form['block6']
#     block7 = request.form['block7']
#     block8 = request.form['block8']

#     retrieved = block1 + ',' + block2 + ',' + block3 + ',' + block4 + ',' + block5 + ',' + block6 + ',' + block7 + ',' + block8
#     return retrieved



@app.route('/results', methods = ['GET', 'POST'])
def index_post():
    app.logger.debug('This block of code was reached. congrats')
    block1 = request.form['block1']
    block2 = request.form['block2']
    block3 = request.form['block3']
    block4 = request.form['block4']
    block5 = request.form['block5']
    block6 = request.form['block6']
    block7 = request.form['block7']
    block8 = request.form['block8']

    mylist = [block1, block2, block3, block4, block5, block6, block7, block8]

    mylist1 = []

    for x in mylist:
        if x != "":
            mylist1.append(x)

    if all(v == "" for v in mylist):
        return render_template('landing.html')
    else:
         # global valued
        valued = list(itertools.permutations(mylist1))

        with open ('filelanding.csv', 'w', newline='') as f_in:
            writing = csv.writer(f_in, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writing.writerows(valued)
            # json.dump(ret, f)
        return render_template('landing.html')
    # ret = '</br>'.join(', '.join(elems) for elems in valued)
    # ret = '\n'.join(', '.join(elems) for elems in valued)
    # return ret
    # return jsonify(valued)

    # for elems in valued
    #     part = []
    #     for





def rowcleaner():
    with open ('filelanding.csv', 'r', newline='') as f_in, open('fileoutput.csv', 'w') as f_out:
        writer = csv.writer(f_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        for row in csv.reader(f_in, delimiter=','):
            if row[0] != "a":
                writer.writerow(row)


# , open('announcer.csv', 'r') as ref
# def setclassadder():




# @app.route('/')
# def tester():
#     return url_for(index)







# sys.stdout = open("Test.txt", "w")
# print (value)
# print ("Test")

if __name__ == "__main__":
    app.debug = True
    app.run()


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


print (index_post)
rowcleaner()
# print (tester)


# filename  = open("Test.txt","w")
# sys.stdout = filename
