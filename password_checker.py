#!/usr/bin/env python3
"""Password Strength Checker - evaluates password strength offline.

Checks length, character variety, entropy, common passwords and
repeated / sequential patterns. Nothing is sent over the network.
"""
import argparse
import getpass
import math
import re
import string

COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345", "qwerty",
    "azerty", "abc123", "111111", "123123", "admin", "letmein", "welcome",
    "monkey", "dragon", "football", "iloveyou", "motdepasse", "soleil",
    "password1", "qwerty123", "000000", "1234", "sunshine", "princess",
}

SEQUENCES = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "azertyuiop",
             "qwertyuiop", "asdfghjkl", "qsdfghjklm", "zxcvbnm", "wxcvbn"]


def charset_size(pw: str) -> int:
    size = 0
    if any(c.islower() for c in pw):
        size += 26
    if any(c.isupper() for c in pw):
        size += 26
    if any(c.isdigit() for c in pw):
        size += 10
    if any(c in string.punctuation for c in pw):
        size += len(string.punctuation)
    if any(ord(c) > 127 or c == " " for c in pw):
        size += 32
    return size


def entropy_bits(pw: str) -> float:
    size = charset_size(pw)
    return len(pw) * math.log2(size) if size else 0.0


def has_sequence(pw: str, min_len: int = 4) -> bool:
    low = pw.lower()
    for seq in SEQUENCES:
        for s in (seq, seq[::-1]):
            for i in range(len(s) - min_len + 1):
                if s[i:i + min_len] in low:
                    return True
    return False


def has_repeats(pw: str, min_len: int = 3) -> bool:
    return re.search(r"(.)\1{%d,}" % (min_len - 1), pw) is not None


def evaluate(pw: str) -> dict:
    tips = []
    score = 0

    if pw.lower() in COMMON_PASSWORDS:
        return {"score": 0, "label": "Very weak", "entropy": round(entropy_bits(pw), 1),
                "tips": ["This is one of the most common passwords - change it!"]}

    if len(pw) >= 16:
        score += 3
    elif len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters.")

    classes = sum([
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in string.punctuation for c in pw),
    ])
    score += max(classes - 1, 0)
    if classes < 3:
        tips.append("Mix lowercase, uppercase, digits and symbols.")

    if has_sequence(pw):
        score -= 1
        tips.append("Avoid sequences like 'abcd', '1234' or 'azerty'.")
    if has_repeats(pw):
        score -= 1
        tips.append("Avoid repeated characters like 'aaa'.")

    ent = entropy_bits(pw)
    if ent >= 80:
        score += 1

    score = max(0, min(score, 6))
    labels = ["Very weak", "Weak", "Weak", "Medium", "Strong", "Strong", "Very strong"]
    if not tips:
        tips.append("Great password! Store it in a password manager.")
    return {"score": score, "label": labels[score], "entropy": round(ent, 1), "tips": tips}


def main():
    parser = argparse.ArgumentParser(description="Check how strong a password is (offline).")
    parser.add_argument("password", nargs="?", help="password to test (omit to type it hidden)")
    args = parser.parse_args()
    pw = args.password or getpass.getpass("Password: ")
    r = evaluate(pw)
    bar = "#" * r["score"] + "-" * (6 - r["score"])
    print(f"Strength : [{bar}] {r['label']} ({r['score']}/6)")
    print(f"Entropy  : {r['entropy']} bits")
    for t in r["tips"]:
        print(f" - {t}")


if __name__ == "__main__":
    main()
