from app import app
from flask import request
import stress.stress as s
import os, psutil

@app.route('/')
def hello_world():
    return '<b>CPU Load:</b> <a href="/cpu?cores=2">2 Cores</a></br><b>Mem Load:</b> <a href="/mem?use=512">512 MB Use</a>'

@app.route('/cpu')
def stress_cpu():
    cores=request.args.get('cores')
    s.stress_processes(int(cores))
    cpup = psutil.cpu_percent()
    return 'Starting CPU on '+str(cores)+' Cores' + ' of '+str(os.cpu_count())+' Cores<br/>Avg CPU Usage across '+str(psutil.cpu_count())+' Cores:'+str((cpup)/psutil.cpu_count())+' %<br>Total CPU Usage:'+str(cpup)+' %'

@app.route('/cpu_usage')
def cpu_usage():
    cpup = psutil.cpu_percent()
    return 'Avg CPU Usage across '+str(psutil.cpu_count())+' Cores:' + str((cpup)/psutil.cpu_count()) + ' %<br>Total CPU Usage:'+str(cpup)+' %'

@app.route('/mem')
def stress_mem():
    use = request.args.get('use')
    app.secret_key = [0] * int(((int(use) / 8) * (1024 ** 2)))
    return 'Starting Mem Usage of '+str(use)+' MB on Total Capacity'+str(psutil.virtual_memory()[0]/(1024*1024))+' MB'

@app.route('/mem_usage')
def mem_usage():
    return 'Current Memory Usage :' + str(psutil.virtual_memory()[2]) + '% of Total Capacity :'+str(psutil.virtual_memory()[0]/(1024*1024)) + ' MB<br/>'
