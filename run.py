from chatapp import create_app, Socketio

app = create_app()


Socketio.run(app, host="192.168.41.188", port=5000) 