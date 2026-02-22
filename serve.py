#!/usr/bin/env python3
from livereload import Server

server = Server()
# Watch key files and folders for changes
server.watch('index.html')
server.watch('styles.css')
server.watch('assets/')

# Serve the current directory on all interfaces so host can access it
server.serve(root='.', host='0.0.0.0', port=8000)
