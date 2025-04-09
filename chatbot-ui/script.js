const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage("user", userText);
  input.value = "";

  appendMessage("bot", "Thinking...");

  try {
    const response = await fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: userText }),
    });

    const data = await response.json();

    // Replace placeholder response
    chatBox.lastChild.remove();
    appendMessage("bot", data.response);
  } catch (error) {
    chatBox.lastChild.remove();
    appendMessage("bot", "Oops! Something went wrong.");
  }
});

function appendMessage(sender, message) {
  const msgDiv = document.createElement("div");
  msgDiv.className = sender === "user" ? "user-msg" : "bot-msg";
  msgDiv.textContent = message;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
