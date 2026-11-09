"use client";

import { useEffect, useState } from "react";

export default function PackageDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const [pkg, setPkg] = useState<any>(null);

  useEffect(() => {
    params.then((value) => {
      fetch(
        `http://127.0.0.1:8000/packages/${value.id}`
      )
        .then((res) => res.json())
        .then((data) => setPkg(data))
        .catch(console.error);
    });
  }, [params]);

  if (!pkg) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>{pkg.title}</h1>

      <p>{pkg.description}</p>

      <p>
        {pkg.days} Days / {pkg.nights} Nights
      </p>

      <h3>Hotels</h3>

      <p>{pkg.hotels}</p>

      <h3>Inclusions</h3>

      <p>{pkg.inclusions}</p>
    </div>
  );
}