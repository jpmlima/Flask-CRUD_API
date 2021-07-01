#!/usr/bin/env python
from config import app
from controllers.user_controller import bp_user
from controllers.login_controller import bp_login


app.register_blueprint(bp_user)
app.register_blueprint(bp_login)


if __name__ == '__main__':
    app.run()
    

