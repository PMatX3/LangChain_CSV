import React, { useState } from "react";
import axios from "axios";

const JobSearch = () => {
  const [jobs, setJobs] = useState([]);
  const [technologies, setTechnologies] = useState(["React", "Node.js"]); // Example: React.js repo

  const searchJobs = async () => {
    const keywords = technologies.join(" ");
    const jobResults = await axios.get(`https://api.indeed.com/ads/apisearch`, {
      params: {
        publisher: "YOUR_INDEED_PUBLISHER_ID",
        q: keywords, // Search for jobs that match the technologies
        format: "json",
        v: "2",
      },
    });
    setJobs(jobResults.data.results); // Store the job results
  };

  return (
    <div>
      <h1>Job Search for React.js Projects</h1>
      <button onClick={searchJobs}>Search Jobs</button>
      
      <div>
        {jobs.length > 0 ? (
          <ul>
            {jobs.map((job, index) => (
              <li key={index}>
                <h3>{job.jobtitle}</h3>
                <p>{job.company}</p>
                <p>{job.snippet}</p>
                <a href={job.url} target="_blank" rel="noopener noreferrer">
                  Apply Now
                </a>
              </li>
            ))}
          </ul>
        ) : (
          <p>No jobs found. Try searching again!</p>
        )}
      </div>
    </div>
  );
};

export default JobSearch;
