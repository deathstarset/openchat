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
