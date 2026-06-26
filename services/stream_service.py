class StreamService:

    messages = []

    @classmethod
    def send(cls, message):

        print(message)

        cls.messages.append(message)

    @classmethod
    def get_messages(cls):

        return cls.messages

    @classmethod
    def clear(cls):

        cls.messages = []