<script>
  let userInput = "";
  let chatLog = [];

  async function sendMessage() {
    if (!userInput.trim()) return;

    chatLog = [...chatLog, { role: "user", text: userInput }];

    const res = await fetch("/impersonator_backend/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_message: userInput })
    });

    const data = await res.json();
    chatLog = [...chatLog, { role: "bot", text: data.reply }];
    userInput = "";
  }
</script>

<main>
  <h1>Christian Conservative Vaccine Chatbot</h1>

  <div class="chat-box">
    {#each chatLog as msg}
      <div class={msg.role === "user" ? "user" : "bot"}>
        <strong>{msg.role === "user" ? "You" : "Bot"}:</strong> {msg.text}
      </div>
    {/each}
  </div>

  <input bind:value={userInput} on:keydown={(e) => e.key === "Enter" && sendMessage()} placeholder="Ask a question..." />
  <button on:click={sendMessage}>Send</button>
</main>

<style>
  main { max-width: 600px; margin: auto; padding: 1rem; font-family: sans-serif; }
  .chat-box { margin-bottom: 1rem; border: 1px solid #ccc; padding: 1rem; height: 300px; overflow-y: auto; }
  .user { text-align: right; margin-bottom: 0.5rem; }
  .bot { text-align: left; margin-bottom: 0.5rem; }
  input { width: 80%; padding: 0.5rem; }
  button { padding: 0.5rem; }
</style>
