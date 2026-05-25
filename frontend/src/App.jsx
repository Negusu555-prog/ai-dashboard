import RagPanel from "./components/RagPanel"
import AgentPanel from "./components/AgentPanel"
import MetricsPanel from "./components/MetricsPanel"

function App() {
  return (
  <div className="min-h-screen bg-gray-100 flex items-center justify-center p-10">
    <RagPanel />
    <AgentPanel/>
    <MetricsPanel/>
  </div>
  )
}

export default App