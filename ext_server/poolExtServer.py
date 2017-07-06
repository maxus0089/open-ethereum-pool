import MySQLdb
from time import time
from bottle import get, run, request

db = MySQLdb.connect(host='localhost', user='admin', passwd='iS_p0FgHm-i6X-8xly9G8g')


@get('/worker_upd')
def inf_worker_update():
    worker_name = request.GET['worker_name']
    with db.cursor() as cur:
        now = int(time())
        cur.execute('INSERT INTO worker_journal (worker_name, last_activity) VALUES '
                    '(?,?) ON DUPLICATE KEY UPDATE last_activity = ?',
                    (worker_name, now, now))


@get('/hashrate_upd')
def inf_worker_hr():
    worker_name = request.GET['worker_name']
    hashrate = request.GET['hashrate']
    with db.cursor() as cur:
        cur.execute('INSERT INTO worker_journal (worker_name, hashrate) VALUES '
                    '(?,?) ON DUPLICATE KEY UPDATE hashrate = ?',
                    (worker_name, hashrate, hashrate))

run(server='paste', port=1520, host='0.0.0.0')
