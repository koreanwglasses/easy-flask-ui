import os
from multiprocessing import Process, Queue
from flask import Flask, request, send_from_directory
import gevent.pywsgi

DIR = os.path.dirname(os.path.realpath(__file__))

MODE = (os.environ.get('MODE') or 'PROD').upper()


class WebInterface:
    def __init__(self):
        self.event_queue = Queue()
        self.process = Process(target=self._run, args=(self.event_queue,))

    def start(self):
        self.process.start()

    def events(self):
        while True:
            event = self.event_queue.get()
            yield event

    @staticmethod
    def _run(event_queue: Queue):
        app = Flask(__name__, static_url_path='',
                    static_folder=f'{DIR}/web')

        @app.route('/')
        def index():
            return app.send_static_file('index.html')

        @app.route("/api/start", methods=["GET", "POST"])
        def api_start():
            event_queue.put("a")
            return "did action a!", 200

        @app.route("/api/stop", methods=["GET", "POST"])
        def api_stop():
            event_queue.put("b")
            return "did action b!", 200

        if MODE == 'DEV':
            print('Starting server in DEV mode...')
            app.run(port=4000, debug=True)
        else:
            print('Starting server in PROD mode...')
            app_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 80), app)
            app_server.serve_forever()


wi = WebInterface()
wi.start()

for event in wi.events():
    print(event)
    if event == "b":
        break
