"use client";

import { useEffect, useState } from "react";

export default function PackagesPage() {
  const [packages, setPackages] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/packages/")
      .then((res) => res.json())
      .then((data) => setPackages(data))
      .catch(console.error);
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Travel Packages</h1>

      {packages.map((pkg) => (
        <div
          key={pkg.id}
          style={{
            border: "1px solid #ddd",
            padding: "1rem",
            marginBottom: "1rem",
            borderRadius: "8px",
          }}
        >
          <h2>{pkg.title}</h2>

          <p>{pkg.description}</p>

          <p>
            {pkg.days} Days / {pkg.nights} Nights
          </p>

          <a href={`/packages/${pkg.id}`}>
            View Details
          </a>
        </div>
      ))}
    </div>
  );
}