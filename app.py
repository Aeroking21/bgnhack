from webapp import create_app

# Calling the function create_app() in __init__.py to return the app, then stored in app
app = create_app()

# Only running the web server if the file is run directly
if __name__ == '__main__':
    # Starting the web server, set debug to false or remove it later
    app.run(debug=True)
