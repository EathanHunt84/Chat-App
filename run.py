from chatapp import create_app, Socketio
import socket

def get_private_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Attempt to connect to an external server to determine the local IP
        s.connect(('10.254.254.254', 1))  # This IP address is just a dummy address
        private_ip = s.getsockname()[0]
    except Exception:
        private_ip = '127.0.0.1'  # Fallback to localhost if the connection fails
    finally:
        s.close()
    return private_ip


app = create_app()


Socketio.run(app, host= "0.0.0.0", port=5000) 