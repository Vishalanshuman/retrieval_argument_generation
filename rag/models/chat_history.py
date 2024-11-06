import pinecone
from dotenv import load_dotenv
import os

# class ChatHistory:
#     def __init__(self, index_name='chat-history'):
#         load_dotenv()
#         self.api_key = os.getenv("PINECONE_API_KEY")
#         # Initialize Pinecone
#         pinecone.init(api_key=self.api_key)
#         self.index = pinecone.Index(index_name)

#     def upsert_message(self, chat_id, message, embedding):
#         """
#         Store a chat message in Pinecone.

#         Args:
#             chat_id (str): Unique identifier for the chat session.
#             message (str): The chat message to store.
#             embedding (list): The vector representation of the message.
#         """
#         self.index.upsert([(chat_id, embedding, {'message': message})])

#     def retrieve_chat_history(self, chat_id, limit=10):
#         """
#         Retrieve chat history for a given chat ID.

#         Args:
#             chat_id (str): Unique identifier for the chat session.
#             limit (int): Number of messages to retrieve.

#         Returns:
#             list: A list of chat messages retrieved from Pinecone.
#         """
#         response = self.index.query(
#             query=[chat_id],
#             top_k=limit,
#             include_metadata=True
#         )
#         return response['matches']

"""=========================================================LIST====================================================================="""
class ChatHistory:
    def __init__(self):
        self.history={}
    def upsert_message(self, chat_id, message, embedding):
        if chat_id not in self.history:
            self.history[chat_id] = []  # Create a new list for this chat_id if it doesn't exist
        self.history[chat_id].append({'message': message, 'embedding': embedding})

    def retrieve_chat_history(self, chat_id, limit=10):
        if chat_id in self.history:
            return self.history[chat_id][-limit:]  # Return the last 'limit' number of messages
        else:
            return []  # Return an empty list if no history exists for the chat_id
