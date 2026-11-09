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
        padding: "30px",
        background: "#f1f5f9",
        minHeight: "100vh",
      }}
    >
      <h1 style={{ marginBottom: "20px" }}>
        Package Management
      </h1>

      {packages.map((pkg) => (
        <div
          key={pkg.id}
          style={{
            background: "white",
            padding: "20px",
            marginBottom: "20px",
            borderRadius: "12px",
            boxShadow: "0 5px 15px rgba(0,0,0,0.1)",
          }}
        >
          <h2>{pkg.title}</h2>

          <p>{pkg.description}</p>

          <p>
            {pkg.days} Days / {pkg.nights} Nights
          </p>

          <p>{pkg.hotels}</p>
        </div>
      ))}
    </div>
  );
}