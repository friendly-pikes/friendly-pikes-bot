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
    
    channels = {
        "main": {
            "staff_commands": 1477520001165430938,
            "audit": 1477498994082185350,
        },
        "test": {
            "staff_commands": 1478352488301072477,
            "audit": 1478387549662875689
        }
    }

    role_ids = {
        "seperators": {
            "main": {
                "vanity": 1477780961935491226
            },
            "test": {
                "vanity": 1478032301685211298
            }
        },
        "roles": {
            "main": {
                "cute": 1477781229599199434,
                "shortie": 1477781226910912563,
                "smol": 1477781211622539326,
                "explode": 1477803664407003340,
                "tall": 1478069476284039180
            },
            "test": {
                "cute": 1477749083404767364,
                "shortie": 1477749159997214863,
                "smol": 1477749196366020780,
                "explode": 1478033086196482241,
                "tall": 1478069476284039180
            }
        },
    }

    ignore_radar_ids = {
        "cute": [
            1262124659814695005, # Victor / Pixie / Pivor or whatever
            1450968328821670040 # TKO
        ],
        "gay": [
            1000478105128947773, # 𝐳𝐦𝐢ę𝐤ł𝐲 𝐛𝐢𝐬𝐳𝐤𝐨𝐩
            1449593053492023467 # Kooddoger
        ]
    }

    forced_radar_ids = [
        1257541858809217035
    ]
