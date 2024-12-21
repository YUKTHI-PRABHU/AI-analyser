import React, { useState } from "react";
import axios from "axios";
import "./FeedbackForm.css";

const FeedbackForm = ({ setAnalysisResult }) => {
    const [feedback, setFeedback] = useState("");

    const submitFeedback = async () => {
        try {
            const response = await axios.post("http://localhost:5000/analyze-feedback", { feedback });
            setAnalysisResult(response.data); // Pass the result to the parent component
            setFeedback(""); // Clear input field
        } catch (error) {
            console.error("Error submitting feedback:", error);
            alert("Error submitting feedback. Please try again.");
        }
    };

    return (
        <div className="feedback-container">
            {/* Fixed text in the top-right corner */}
            <div className="feedback-text">
                Intelligent Customer Feedback Analyzer
            </div>
            
            <div className="feedback-form">
                <h2>Submit Feedback</h2>
                <textarea
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    placeholder="Enter your feedback here..."
                />
                <button onClick={submitFeedback}>Submit</button>
            </div>
        </div>
    );
};

export default FeedbackForm;
