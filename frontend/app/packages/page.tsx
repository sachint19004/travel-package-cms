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
    <div
      style={{
        minHeight: "100vh",
        background: "#f8fafc",
        padding: "40px",
      }}
    >
      <h1
        style={{
          fontSize: "3rem",
          marginBottom: "30px",
          textAlign: "center",
        }}
      >
        Explore Travel Packages
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit,minmax(320px,1fr))",
          gap: "20px",
        }}
      >
        {packages.map((pkg) => (
          <div
            key={pkg.id}
            style={{
              background: "white",
              borderRadius: "16px",
              padding: "24px",
              boxShadow: "0 10px 25px rgba(0,0,0,0.1)",
            }}
          >
            <h2>{pkg.title}</h2>

            <p>{pkg.description}</p>

            <p>
              <strong>
                {pkg.days} Days / {pkg.nights} Nights
              </strong>
            </p>

            <p>{pkg.hotels}</p>

            <a
              href={`/packages/${pkg.id}`}
              style={{
                display: "inline-block",
                marginTop: "12px",
                background: "#2563eb",
                color: "white",
                padding: "10px 20px",
                borderRadius: "8px",
              }}
            >
              View Package
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}