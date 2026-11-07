from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password

db = SessionLocal()

existing = (
    db.query(User)
    .filter(
        User.email == "admin@travelcms.com"
    )
    .first()
)

if not existing:

    admin = User(
        name="System Admin",
        email="admin@travelcms.com",
        password_hash=hash_password(
            "Admin@123"
        ),
        role="ADMIN"
    )

    db.add(admin)

    db.commit()

    print("Admin created")

else:
    print("Admin already exists")