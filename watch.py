import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import json
import websocket

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
		print "Got it!"
		f=open("/home/anuja/hubot/1.txt","r+")
		content=f.read()
		content = content.split()
		cont = ""
		arrsize = len(content)
		for i in range(2,arrsize):
			cont=cont+content[i]+" "

		#print(cont)

		ws = websocket.WebSocket()
		uri = 'ws://' + sys.argv[1] + ':8181/core'
		ws.connect(uri)
		message = {'type': 'recognizer_loop:utterance',
			   'data': {'utterances': [cont]}
		}

		print("Sending " + json.dumps(message) + " to " + uri + "...")
		result = ws.send(json.dumps(message))
		print(result)
		time.sleep(10)

		result1= ws.recv()
		print(result1)

		ws.close()


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
