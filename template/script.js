 // Navigate from home page to result page with prompt
  async function goToResult() {
   const prompt = document.getElementById("prompt").value;
    const res = await fetch("https://127.0.0.1:8000/send-prompt", {
     method: "POST",
     headers: { "Content-Type": "application/json" },
     body: JSON.stringify({ text: prompt })
   });
   if (!prompt) return alert("Please enter a prompt!");
   localStorage.setItem("userPrompt", prompt);
   window.location.href = "result.html";
 }

// Go back home
function goHome() {
  window.location.href = "index.html";
}

//Load result page
async function loadResult() {
  const outputDiv = document.getElementById("output");
  const prompt = localStorage.getItem("userPrompt");
  if (!prompt) {
    outputDiv.innerHTML = "<p style='color:red;'>❌ No prompt found.</p>";
    return;
  }

   outputDiv.innerHTML = `<p class="loading">⏳ Generating text, audio & video for: <b>${prompt}</b></p>`;

  try {
    const response = await fetch("http://127.0.0.1:8000/generate?prompt=" + encodeURIComponent(prompt), {
      method: "POST"
    });

     if (!response.ok) throw new Error("Backend error");

     // Backend sends back a video file
     const blob = await response.blob();
     const url = URL.createObjectURL(blob);

     outputDiv.innerHTML = `
       <h2>📜 Generated Text</h2>
       <pre>${prompt}</pre>

       <h2>🔊 Audio</h2>
       <audio controls src="${url}"></audio>

       <h2>🎥 Video</h2>
       <video controls src="${url}"></video>
     `;
   } catch (err) {
    outputDiv.innerHTML = `<p style="color:red;">❌ Error: ${err.message}</p>`;
  }
}

