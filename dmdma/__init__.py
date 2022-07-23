from flask import Flask

# Import the views and create the app
import dmdma.views
app = views.create_app()



if __name__ == '__main__':
    # Run application
    app.run()