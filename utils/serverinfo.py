from utils.default import CustomContext

class ServerInfo():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def main_or_test_server(self, ctx: CustomContext):
        if ctx.guild.id == self.server_ids["test"]:
            return "test"
        return "main"
    
    server_ids = {
        "main": 1414222707570118656,
        "test": 1438414082448425111
    }
    