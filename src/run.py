import cherrypy

class Landing(object):
    @cherrypy.expose
    def index(self):
        return '<html><body>scripted landing</body></html>'

# The config.update is optional, but this will prevent scaling issues in a moment
cherrypy.config.update({
    'server.socket_host': '0.0.0.0', # 127.0.0.1 is default
    'server.socket_port': 80, # 8080 is default
    'server.thread_pool': 100, # 10 is default
    'tools.trailing_slash.on': False # True is default
})

if __name__ == "__main__":
    cherrypy.quickstart(Landing(), '/', "run.conf")
