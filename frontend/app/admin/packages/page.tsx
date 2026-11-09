"use client";

import { useEffect, useState } from "react";

export default function AdminPackagesPage() {
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
        background: "#f1f5f9",
        padding: "30px",
      }}
    >
      <h1
        style={{
          fontSize: "2.5rem",
          marginBottom: "20px",
        }}
      >
        Admin Dashboard
      </h1>

      <div
        style={{
          display: "flex",
          gap: "12px",
          marginBottom: "30px",
        }}
      >
        <a
          href="/admin/packages"
          style={{
            background: "#2563eb",
            color: "white",
            padding: "10px 20px",
            borderRadius: "8px",
          }}
        >
          📦 Packages
        </a>

        <a
          href="/admin/enquiries"
          style={{
            background: "#0f766e",
            color: "white",
            padding: "10px 20px",
            borderRadius: "8px",
          }}
        >
          📨 Enquiries
        </a>

        <a
          href="/packages"
          style={{
            background: "#7c3aed",
            color: "white",
            padding: "10px 20px",
            borderRadius: "8px",
          }}
        >
          🌍 Public Site
        </a>

        <a
          href="/"
          style={{
            background: "#475569",
            color: "white",
            padding: "10px 20px",
            borderRadius: "8px",
          }}
        >
          🏠 Home
        </a>
      </div>

      {packages.map((pkg) => (
        <div
          key={pkg.id}
          style={{
            background: "white",
            padding: "20px",
            marginBottom: "20px",
            borderRadius: "12px",
            boxShadow:
              "0 5px 15px rgba(0,0,0,0.1)",
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
        </div>
      ))}
    </div>
  );
}