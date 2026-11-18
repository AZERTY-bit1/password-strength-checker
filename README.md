# 🔐 Password Strength Checker

![tests](https://github.com/AZERTY-bit1/password-strength-checker/actions/workflows/tests.yml/badge.svg)
![python](https://img.shields.io/badge/python-3.8%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)

An **offline** tool that tells you how strong a password is and how to improve it. Nothing is ever sent over the internet.

## ✨ Features

- Length and character-variety scoring
- Entropy estimation (bits)
- Detection of the most common passwords (`123456`, `azerty`...)
- Detection of sequences (`abcd`, `1234`, `azerty`) and repeats (`aaa`)
- Clear tips to make the password stronger

## 🚀 Usage

No installation needed - only Python 3.8+.

```bash
git clone https://github.com/AZERTY-bit1/password-strength-checker.git
cd password-strength-checker
python password_checker.py            # type it hidden
python password_checker.py 'azerty123'
```

## 📸 Example output

```
Strength : [#-----] Weak (1/6)
Entropy  : 46.5 bits
 - Mix lowercase, uppercase, digits and symbols.
 - Avoid sequences like 'abcd', '1234' or 'azerty'.
```

## 🧪 Tests

```bash
python -m unittest discover -s tests -v
```

## ⚠️ Disclaimer

This is a **defensive / educational** tool. Only use it on systems and data you own or are allowed to check.

## 📄 License

MIT - see [LICENSE](LICENSE).
