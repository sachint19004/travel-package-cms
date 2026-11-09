"use client";

import { useEffect, useState } from "react";

export default function EnquiriesPage() {
  const [enquiries, setEnquiries] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/enquiries/")
      .then((res) => res.json())
      .then((data) => setEnquiries(data))
      .catch(console.error);
  }, []);

  return (
    <div
      style={{
        padding: "30px",
        background: "#f1f5f9",
        minHeight: "100vh",
      }}
    >
      <h1>AI Enquiry Inbox</h1>

      {enquiries.map((e) => (
        <div
          key={e.id}
          style={{
            background: "white",
            padding: "20px",
            marginTop: "20px",
            borderRadius: "12px",
            boxShadow: "0 5px 15px rgba(0,0,0,0.1)",
          }}
        >
          <h2>{e.name}</h2>

          <p>{e.email}</p>

          <p>{e.message}</p>

          <h4>AI Extraction</h4>

          <pre>
            {JSON.stringify(
              e.ai_extraction,
              null,
              2
            )}
          </pre>
        </div>
      ))}
    </div>
  );
}