import { useState, useEffect } from "react";

const MetricsPanel = () => {
  // 1. useState-ים
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // 2. פונקציה שמביאה נתונים
  const fetchMetrics = async () => {
    try {
      const response = await fetch("http://localhost:8000/metrics");
      
      if (!response.ok) {
        throw new Error(`שגיאה: ${response.status}`);
      }
      
      const data = await response.json();
      setMetrics(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // 3. useEffect — יפעיל את fetchMetrics
  useEffect(() => {
    fetchMetrics();
    const interval = setInterval(fetchMetrics, 10000);
    return () => clearInterval(interval);
  }, []);

  // 4. return — מה מוצג על המסך

  if (loading) return (
    <div className="bg-gray-900 border border-gray-700 rounded-xl p-6">
      <p className="text-gray-400">טוען מדדים...</p>
    </div>
  );

  if (error) return (
    <div className="bg-gray-900 border border-red-500 rounded-xl p-6">
      <p className="text-red-400">⚠️ שגיאה: {error}</p>
    </div>
  );

  return (
    <div className="bg-gray-900 border border-gray-700 rounded-xl p-6">
      <h2 className="text-white text-xl font-semibold mb-4">
        📊 System Metrics
      </h2>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        
        <div className="bg-gray-800 border border-blue-500 rounded-lg p-4">
          <p className="text-gray-400 text-sm">RAG Requests</p>
          <p className="text-blue-400 text-2xl font-bold mt-1">
            {metrics.rag_requests}
          </p>
        </div>

        <div className="bg-gray-800 border border-purple-500 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Agent Requests</p>
          <p className="text-purple-400 text-2xl font-bold mt-1">
            {metrics.agent_requests}
          </p>
        </div>

        <div className="bg-gray-800 border border-green-500 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Avg Latency</p>
          <p className="text-green-400 text-2xl font-bold mt-1">
            {metrics.avg_latency_ms} <span className="text-sm">ms</span>
          </p>
        </div>

        <div className="bg-gray-800 border border-red-500 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Errors</p>
          <p className="text-red-400 text-2xl font-bold mt-1">
            {metrics.error_count}
          </p>
        </div>

      </div>
    </div>
  );

};

export default MetricsPanel;