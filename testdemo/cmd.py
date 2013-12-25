import cmd
cmd.Cmd.__init__(self)
self.app_key = app_key
self.app_secret = app_secret
self.current_path = ''
self.prompt = "Dropbox> "
self.api_client = None
