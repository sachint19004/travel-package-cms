"use client";

import { useEffect, useState } from "react";

export default function EnquiriesPage() {
  const [enquiries, setEnquiries] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/enquiries/")
      .then((res) => res.json())
      .then((data) => {
        setEnquiries(data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Enquiry Inbox</h1>

      {enquiries.map((e) => (
        <div
          key={e.id}
          style={{
            border: "1px solid #ddd",
            padding: "1rem",
            marginBottom: "1rem",
          }}
        >
          <h2>{e.name}</h2>
          <p>{e.email}</p>
          <p>{e.message}</p>

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