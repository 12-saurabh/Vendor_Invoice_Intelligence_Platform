import bcrypt

hashed = b"$2b$12$JGNHHtht6tVV3hCUKWHl0.kcqUMvAH2DR6YAxxvkKF0D42yO633SO"

password = b"admin123"


print(
    bcrypt.checkpw(
        password,
        hashed
    )
)