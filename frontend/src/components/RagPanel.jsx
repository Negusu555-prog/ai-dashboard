import { useState } from "react"


function RagPanel() {
    const [question, setQuestion] = useState("")
    const [file, setFile] = useState(null)
    const [answer, setAnswer] = useState("")

async function handleSubmit() {
  const formData = new FormData()
  formData.append("file", file)
  formData.append("question", question)

  const response = await fetch("http://localhost:8000/rag/ask", {
    method: "POST",
    body: formData
  })

  const data = await response.json()
  setAnswer(data.answer)
}
    return (
    <div className="bg-white rounded-xl shadow p-6 w-full max-w-xl">
        <h2 className="text-2xl font-bold mb-4">RAG — שאל את המסמך</h2>
        <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full border rounded-lg p-2 mb-4"
        />

        <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="כתוב שאלה..."
        className="w-full border rounded-lg p-2 mb-4"
        />      
        <button className="bg-blue-600 text-white px-4 py-2 rounded-lg" onClick={handleSubmit}>
        שלח
        </button>
        {answer && <p className="mt-4 text-gray-700">{answer}</p>}
    </div>
    )
}


export default RagPanel

