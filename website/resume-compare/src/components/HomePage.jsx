import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Import CSS file for styling

function HomePage() {
  return (
    <div className="home-container">
      <h1 className="heading">Welcome to Launchpad!</h1>
      <p className="description">Streamline your hiring process with our innovative HR comparison tool. Simply input your job description and attach resumes, and let our powerful algorithm find the best candidate for the job. Save time and resources by identifying top talent efficiently and effectively.</p>
      <p className="description">Looking for your next career opportunity? Our user recommendation feature matches your resume with suitable job openings, helping you take the next step in your professional journey with ease.</p>
      <p className="description">Experience the future of recruitment with Launchpad. Get started today and unlock the potential of seamless hiring and career advancement. <Link to="/signup" className="link">Sign Up</Link> now!</p>
    </div>
  );
}

export default HomePage;
