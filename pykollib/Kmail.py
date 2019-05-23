from .request import SendMessageRequest, kmail_get
from .util.decorators import logged_in


class Kmail(object):
    "This class represents a user's kmail box"

    def __init__(self, session):
        self.session = session

    @logged_in
    async def get(self):
        return await self.session.parse(kmail_get)

    @logged_in
    async def send(self, recipient, message=""):
        msg = {"userId": recipient, "text": message}

        await SendMessageRequest(self.session, msg).doRequest()
