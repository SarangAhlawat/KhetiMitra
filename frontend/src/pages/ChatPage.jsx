import ChatAssistant
from "../components/ai/ChatAssistant";

import PageWrapper
from "../components/ui/PageWrapper";

export default function ChatPage() {

  return (
    <PageWrapper>

    <div className="p-6 bg-gray-100 min-h-screen">

      <h1 className="text-2xl font-bold mb-4">

        AI Farming Assistant

      </h1>

      <ChatAssistant />

    </div>
    </PageWrapper>

  );
}