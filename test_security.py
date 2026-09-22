from app.core.security import (
    hash_password,
    verify_password
)


def main():
    original_password = "Kaarya@123"

    hashed_password = hash_password(
        original_password
    )

    print("Original Password:", original_password)
    print("Hashed Password:", hashed_password)

    correct_result = verify_password(
        original_password,
        hashed_password
    )

    wrong_result = verify_password(
        "WrongPassword",
        hashed_password
    )

    print("Correct Password:", correct_result)
    print("Wrong Password:", wrong_result)


if __name__ == "__main__":
    main()