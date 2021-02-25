from flask import Flask, render_template, url_for, request, send_file
from flask_table import Table, Col
import set_get
import webbrowser
import call_api

app = Flask(__name__)
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

@app.route("/", methods=['POST', 'GET'])
def page1():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        set_get.set(a=stock_name, b=start_date, c=end_date)
        cur_stats, title_stats = new_function()
        graph = "file:///home/yuvraj/PycharmProjects/SMAP/notebooks/graph.png"
        return render_template('page2.html', cur_stats = cur_stats, title_stats = title_stats, graph = graph)
    else:
        return render_template("page1.html")


@app.route('/analysis_report/')
def analysis_report():
    webbrowser.open(
        url="http://localhost:8888/notebooks/PycharmProjects/SMAP/notebooks/stock_analysis.ipynb")
    cur_stats, title_stats = new_function()
    graph = "file:///home/yuvraj/PycharmProjects/SMAP/notebooks/graph.png"
    return render_template("page2.html", cur_stats = cur_stats, title_stats = title_stats, graph = graph)


@app.route('/prediction_report/')
def prediction_report():
    webbrowser.open(
        url="http://localhost:8888/notebooks/PycharmProjects/SMAP/notebooks/stock_prediction.ipynb")
    cur_stats, title_stats = new_function()
    graph = "file:///home/yuvraj/PycharmProjects/SMAP/notebooks/graph.png"
    return render_template("page2.html", cur_stats = cur_stats, title_stats = title_stats, graph = graph)


@app.route('/graph_frame/')
def graph_frame():
    if request.args.get('type') == '1':
        filename = 'graph.png'
    else:
        filename = 'graph.png'
    return send_file(filename, attachment_filename='graph.png')

def new_function():
    cur_sutats = call_api.current_stats(set_get.stock_name)
    title_stats = call_api.stock_title(set_get.stock_name)
    return cur_sutats, title_stats

if __name__ == "__main__":
    app.run(debug=False)
