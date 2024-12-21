import React, { useState } from "react";
import FeedbackForm from "./components/FeedbackForm";  // Adjusted path
import FeedbackAnalysis from "./components/FeedbackAnalysis";  // Adjusted path
import "./App.css";

const App = () => {
    const [analysisResult, setAnalysisResult] = useState(null);

    return (
        <div className="App">
            <FeedbackForm setAnalysisResult={setAnalysisResult} />
            <FeedbackAnalysis analysisResult={analysisResult} />
        </div>
    );
};

export default App;
