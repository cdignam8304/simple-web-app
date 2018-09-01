# NOTES
# =====
# A simple web app.
# By default, app will run on port 8080, but can change
# port by running, e.g.:
# python code.py 1234
# to run on port 1234.

import web

# tell web.py to look for templates in templates directory:
render = web.template.render("templates/")

# defines which class relates to which url:
urls = (
        # "/(.*)", "index",
        "/home/(.*)", "index",
        "/challenge", "challenge",
        "/challenge2", "challenge2"
        )

# classes:

class index:
    def GET(self, name):
        
        # OPTION 1: Hard-code a variable to be passed to the template:
        # name = "Chris" # this variable will be passed to html template.
        # 'index' is the name of the template and 'name' is the variable passed to it.
        # return render.index(name)

        # OPTION 2: Allow user to input a variable:
        # user inputs name variable via the url: e.g. /Chris
        i = web.input(name=None)
        return render.index(name)


class challenge:
    
    def GET(self):
        num_tiles = 9
        return render.challenge(num_tiles)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

