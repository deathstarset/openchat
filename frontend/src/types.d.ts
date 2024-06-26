type AiResponse = {
  model: string;
  createdAt: string;
  response: string;
  done: boolean;
};

type ChatChunk = {
  type: "prompt" | "response";
  content: string;
};

type Conversation = {
  id: string;
  createdAt: Date;
};

enum Sender {
  user = "user",
  bot = "bot",
}

type Message = {
  id: string;
  conversationId: string;
  content: string;
  sender: Sender;
  createdAt: Date;
};
type AddMessage = {
  conversationId: string;
  content: string;
  sender: Sender;
};

type AiResponse = {
  created_at: Date;
  done: boolean;
  model: string;
  response: string;
};
