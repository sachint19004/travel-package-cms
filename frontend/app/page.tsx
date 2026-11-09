export default function HomePage() {
  return (
    <div
      style={{
        padding: "4rem",
        textAlign: "center",
      }}
    >
      <h1>AI Powered Travel Package CMS</h1>

      <p>
        Travel Package Management Platform
      </p>

      <br />

      <a href="/packages">
        Browse Packages
      </a>

      <br />
      <br />

      <a href="/admin/packages">
        Admin Packages
      </a>

      <br />
      <br />

      <a href="/admin/enquiries">
        Admin Enquiries
      </a>
    </div>
  );
}