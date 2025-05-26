class BotUpdate:   #Последняя версия бота
    def __init__(self, version, update):
        self.version = version
        self.update = update
    def last_update(self):
        return f"Последняя версия клиента: ({self.version}), дата апдейта: {self.update}"


