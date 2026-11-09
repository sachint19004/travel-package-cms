"use client";

import { useEffect, useState } from "react";

export default function PackageDetailsPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const [pkg, setPkg] = useState<any>(null);

  useEffect(() => {
    params.then((value) => {
      fetch(`http://127.0.0.1:8000/packages/${value.id}`)
        .then((res) => res.json())
        .then((data) => setPkg(data))
        .catch(console.error);
    });
  }, [params]);

  if (!pkg) {
    return <div style={{ padding: "2rem" }}>Loading...</div>;
  }

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f8fafc",
        padding: "40px",
      }}
    >
      <div
        style={{
          background: "white",
          padding: "30px",
          borderRadius: "16px",
          maxWidth: "900px",
          margin: "0 auto",
          boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
        }}
      >
        <h1>{pkg.title}</h1>

        <p>{pkg.description}</p>

        <hr />

        <h3>Trip Duration</h3>

        <p>
          {pkg.days} Days / {pkg.nights} Nights
        </p>

        <h3>Hotels</h3>

        <p>{pkg.hotels}</p>

        <h3>Inclusions</h3>

        <p>{pkg.inclusions}</p>

        <h3>Itinerary</h3>

        <pre>
          {JSON.stringify(pkg.itinerary, null, 2)}
        </pre>
      </div>
    </div>
  );
}