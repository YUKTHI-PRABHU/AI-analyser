import React from "react";
import "./FeedbackAnalysis.css";

const FeedbackAnalysis = ({ analysisResult }) => {
    return (
        <div className="feedback-analysis">
            <h2>Feedback Analysis</h2>
            {analysisResult ? (
                <div>
                    <div>"{analysisResult.feedback}"</div>
                    <div>Sentiment: {analysisResult.sentiment}</div>
                </div>
            ) : (
                <p>No feedback analyzed yet.</p>
            )}
        </div>
    );
};

export default FeedbackAnalysis;
