from message import Message


class MessagePool:
    """пул шаблонов сообщений"""

    def __init__(self, *games):
        self.pool = {}
        for game in games:
            self.pool.setdefault(game, Message())

    def acquire(self, game):
        """забрать инициализированный объект сообщения"""
        try:
            return self.pool.pop(game)
        except:
            raise Exception('Не удалось получить шаблон сообщения из словаря')

    def release(self, game, message):
        """вернуть шаблон сообщения в пул"""
        message.reset()
        self.pool.setdefault(game, message)

