from livereload import Server


def main():
    server = Server()
    # Watch common editable assets
    server.watch('*.html')
    server.watch('*.css')
    server.watch('*.js')
    server.watch('assets/**')

    # Serve the current workspace root on port 5500
    server.serve(root='.', port=5500, open_url_delay=1)


if __name__ == '__main__':
    main()
