import { useState } from "react"

function AgentPanel() {
  const [task, setTask] = useState("")
  const [result, setResult] = useState("")

async function handleSubmit() {
  const response = await fetch("http://localhost:8000/agent/research", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task: task })
  })
  const data = await response.json()
  setResult(data.result)
}
return (
  <div className="bg-white rounded-xl shadow p-6 w-full max-w-xl">
    <h2 className="text-2xl font-bold mb-4">Agent — Research</h2>
    <input
      type="text"
      value={task}
      onChange={(e) => setTask(e.target.value)}
      placeholder="כתוב משימת research..."
      className="w-full border rounded-lg p-2 mb-4"
    />
    <button
      onClick={handleSubmit}
      className="bg-purple-600 text-white px-4 py-2 rounded-lg"
    >
      חקור
    </button>
    {result && <p className="mt-4 text-gray-700">{result}</p>}
  </div>
)
}

export default AgentPanel