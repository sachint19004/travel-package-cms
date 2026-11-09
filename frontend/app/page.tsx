export default function HomePage() {
  return (
    <div>
      <section
        style={{
          minHeight: "100vh",
          background:
            "linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%)",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          color: "white",
          textAlign: "center",
          padding: "2rem",
        }}
      >
        <h1
          style={{
            fontSize: "6rem",
            fontWeight: "bold",
            marginBottom: "1rem",
            letterSpacing: "2px",
          }}
        >
          ✈️ Travel Package CMS
        </h1>

        <p
          style={{
            fontSize: "1.5rem",
            maxWidth: "700px",
            lineHeight: "1.8",
            marginBottom: "2rem",
          }}
        >
          AI Powered Travel Management Platform
          for Modern Travel Consultants
        </p>

        <div
          style={{
            display: "flex",
            gap: "1rem",
            flexWrap: "wrap",
            justifyContent: "center",
          }}
        >
          <a
            href="/packages"
            style={{
              background: "#ffffff",
              color: "#1e3a8a",
              padding: "14px 28px",
              borderRadius: "10px",
              fontWeight: "bold",
            }}
          >
            Browse Packages
          </a>

          <a
            href="/admin/packages"
            style={{
              background: "#2563eb",
              color: "white",
              padding: "14px 28px",
              borderRadius: "10px",
              fontWeight: "bold",
            }}
          >
            Admin Dashboard
          </a>
        </div>
      </section>

      <section
        style={{
          padding: "5rem 2rem",
          background: "#f8fafc",
        }}
      >
        <h2
          style={{
            textAlign: "center",
            fontSize: "2.5rem",
            marginBottom: "3rem",
          }}
        >
          Platform Features
        </h2>

        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(auto-fit,minmax(250px,1fr))",
            gap: "20px",
            maxWidth: "1200px",
            margin: "0 auto",
          }}
        >
          <div
            style={{
              background: "white",
              padding: "2rem",
              borderRadius: "16px",
              boxShadow:
                "0 10px 20px rgba(0,0,0,0.08)",
            }}
          >
            <h3>📦 Package CMS</h3>
            <p>
              Create, edit and manage
              travel packages with version history.
            </p>
          </div>

          <div
            style={{
              background: "white",
              padding: "2rem",
              borderRadius: "16px",
              boxShadow:
                "0 10px 20px rgba(0,0,0,0.08)",
            }}
          >
            <h3>🤖 AI Extraction</h3>
            <p>
              Gemini automatically extracts
              destination, budget and travellers.
            </p>
          </div>

          <div
            style={{
              background: "white",
              padding: "2rem",
              borderRadius: "16px",
              boxShadow:
                "0 10px 20px rgba(0,0,0,0.08)",
            }}
          >
            <h3>🎯 Smart Recommendations</h3>
            <p>
              AI suggests best-fit packages
              based on customer enquiries.
            </p>
          </div>

          <div
            style={{
              background: "white",
              padding: "2rem",
              borderRadius: "16px",
              boxShadow:
                "0 10px 20px rgba(0,0,0,0.08)",
            }}
          >
            <h3>📨 Enquiry Inbox</h3>
            <p>
              Track customers and AI-enhanced
              travel requests in one place.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}