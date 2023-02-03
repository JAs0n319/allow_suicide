from mcdreforged.api.all import *

def kill(server: ServerInterface,player: str):
    if player != '(Console)':
        server.execute('kill '+player)

def player_name(is_player: bool,player: str):
    if is_player:
        return player
    else:
        return '(Console)'

def on_load(server: PluginServerInterface, old):
    server.register_help_message('!!kill','自杀')
    server.register_command(
        Literal('!!kill')
        .runs(lambda src: kill(server,player_name(src.is_player,src.player)))
    )