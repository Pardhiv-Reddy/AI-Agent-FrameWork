from models.models import Message
class Conversation:
    def __init__(self,prompt,max_messages):
        self._messages = []
        self._system_prompt = prompt
        self._summary =  None
        self._max_messages = max_messages
    def add_user(self,topic):
        self._messages.append(Message(
            role="user",
            content=topic
        ))
    def add_assistant(self,reply):
        self._messages.append(Message(
            role="assistant",
            content=reply
        ))
    def system(self):
        return Message(
            role="system",
            content=self._system_prompt
        )
    def needs_summary(self)->bool:
        return len(self._messages)>self._max_messages
    def clear(self):
        self._messages.clear()
    def build_messages(self):
        temp_list = []
        temp_list.append(self.system())
        temp_list.extend(self._messages)
        return temp_list