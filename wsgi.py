from dashboard import app

server = app.server

if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=10000)
