# HashBuster


**HashBuster** is a powerful and easy-to-use command-line tool for hashing strings and cracking hashes using wordlist attacks. Whether you need to generate hashes for security purposes or crack existing hashes for penetration testing, HashBuster has you covered.

## 🚀 Features

- **Hash Generation**: Generate hashes for strings using multiple algorithms
- **Hash Cracking**: Crack hashes using wordlist-based attacks
- **Multiple Algorithms**: Support for MD5, SHA1, SHA224, SHA256, SHA384, and SHA512
- **Automatic Algorithm Detection**: Automatically detects hash type based on length
- **Robust Error Handling**: Comprehensive error handling for various edge cases
- **Simple CLI Interface**: User-friendly command-line interface with clear arguments

## 📋 Supported Hash Algorithms

| Algorithm | Hash Length | Example |
|-----------|-------------|---------|
| MD5       | 32 chars    | `5d41402abc4b2a76b9719d911017c592` |
| SHA1      | 40 chars    | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| SHA224    | 56 chars    | `730e109bd7a8a32b1cb9d9a09aa2325d2430587ddbc0c38bad911525` |
| SHA256    | 64 chars    | `2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae` |
| SHA384    | 96 chars    | `ca737f1014a48f4c0b6dd43cb177b0afd9e5169367544c494011e3317dbf9a509cb1e5dc1e85a941bbee3d7f2afbc9b1` |
| SHA512    | 128 chars   | `9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043` |

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pro-yash-jects/HashBuster.git
   cd hashbuster
   ```

2. **Ensure Python 3.6+ is installed:**
   ```bash
   python --version
   ```

3. **No additional dependencies required** - HashBuster uses only Python standard library modules.

## 📖 Usage

HashBuster offers two main functionalities: **hashing strings** and **cracking hashes**.

### Basic Syntax
```bash
python main.py [OPTIONS]
```

### Command-Line Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--algo` | Hash algorithm to use (md5, sha1, sha224, sha256, sha384, sha512) | For hashing |
| `--w` | String to hash | For hashing |
| `--hash` | Hash to crack | For cracking |
| `--list` | Path to wordlist file | For cracking |

## 💡 Examples

### 1. Hashing a String

Generate an MD5 hash:
```bash
python main.py --algo md5 --w "hello"
```
Output:
```
Algorithm: md5
Hash: 5d41402abc4b2a76b9719d911017c592
```

Generate a SHA256 hash:
```bash
python main.py --algo sha256 --w "password123"
```
Output:
```
Algorithm: sha256
Hash: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

### 2. Cracking a Hash

Crack an MD5 hash using a wordlist:
```bash
python main.py --hash 5d41402abc4b2a76b9719d911017c592 --list wordlist.txt
```
Output:
```
Hash type: md5
Hash cracked: hello
```

Crack a SHA1 hash:
```bash
python main.py --hash aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d --list common_passwords.txt
```

### 3. Creating a Wordlist

Create a simple wordlist file for testing:
```bash
echo -e "password\nhello world\n123456\nadmin\ntest" > wordlist.txt
```

## 🔧 How It Works

### Hash Generation Process
1. Takes user input string and algorithm choice
2. Uses Python's `hashlib` library to generate the hash
3. Returns the hexadecimal representation of the hash

### Hash Cracking Process
1. **Algorithm Detection**: Automatically determines the hash type based on its length
2. **Wordlist Processing**: Reads the provided wordlist file line by line
3. **Hash Comparison**: Generates hash for each word and compares with target hash
4. **Result Output**: Returns the plaintext when a match is found

### Algorithm Detection Logic
```python
hash_lengths = {
    "md5": 32,
    "sha1": 40,
    "sha224": 56,
    "sha256": 64,
    "sha384": 96,
    "sha512": 128
}
```

## ⚠️ Error Handling

HashBuster includes comprehensive error handling for:

- **Missing Arguments**: Ensures required argument combinations are provided
- **Unsupported Algorithms**: Validates hash algorithms before processing
- **File Not Found**: Handles missing wordlist files gracefully
- **Permission Errors**: Manages file access permission issues
- **Encoding Issues**: Handles Unicode decode errors in wordlist files
- **Invalid Hash Format**: Validates hash format using regex patterns

## 🎯 Use Cases

- **Security Testing**: Test password strength by attempting to crack hashes
- **Penetration Testing**: Hash cracking during security assessments
- **Digital Forensics**: Recover plaintext from discovered hash values
- **Educational Purposes**: Learn about different hashing algorithms
- **Development**: Generate hashes for testing and development

## 📁 Project Structure

```
hashbuster/
├── main.py          # Main application script
├── hashes.py        # Hash functions and utilities
├── README.md        # Project documentation
└── wordlist.txt     # Sample wordlist (optional)
```



## 🤝 Contributing

We welcome contributions from the community! HashBuster is an open-source project that thrives on collaboration and continuous improvement.

### How to Contribute

1. **Fork the Repository**
   ```bash
   git fork https://github.com/pro-yash-jects/HashBuster.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Add new hash algorithms
   - Improve error handling
   - Enhance performance
   - Add new features
   - Fix bugs
   - Improve documentation

4. **Test Your Changes**
   ```bash
   python main.py --algo md5 --w "test"
   python main.py --hash [test_hash] --list [test_wordlist]
   ```

5. **Commit and Push**
   ```bash
   git commit -m "Add your descriptive commit message"
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**

### Areas for Contribution

- **🔐 New Hash Algorithms**: Add support for additional hashing algorithms (Blake2, Argon2, etc.)
- **⚡ Performance Optimization**: Implement multi-threading for faster hash cracking
- **🎨 GUI Interface**: Create a graphical user interface
- **📊 Progress Indicators**: Add progress bars for long-running operations
- **🔍 Advanced Features**: Dictionary attacks, rule-based attacks, rainbow tables
- **📝 Documentation**: Improve documentation, add tutorials, create examples
- **🧪 Testing**: Add unit tests and integration tests
- **🐛 Bug Fixes**: Identify and fix bugs
- **🎯 CLI Improvements**: Enhance command-line interface with better options


## 🎉 Acknowledgments

- Thanks to all contributors who help improve HashBuster
- Python community for excellent standard library support
- Security research community for insights and feedback

---

**Ready to start cracking?** Clone the repository and start using HashBuster today! Don't forget to ⭐ star the repository if you find it useful!

```bash
git clone https://github.com/pro-yash-jects/HashBuster.git
cd hashbuster
python main.py --help
```
