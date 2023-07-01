# Miley Malware Scanner

Miley is a proof of concept malware scanner built for scanning container images, as well as local files.

Miley works by taking file hashes from the container/directory, and querying the hashes against a malware databse, [Malware Bazaar](https://bazaar.abuse.ch/).

This tool was created to satisfy classwork for Dakota State University's CSC-842 Security Tool Development.

Demo video: [here](https://youtu.be/crDHKCgIqW8)

<img src="images/miley_cli.png" alt="miley-cli" width="600" height=auto/>

## Prerequisites

- Python 3 interpreter
- Pip3
- Docker for container scanning

## Usage

**Install Miley**

```bash
pip install miley

miley --help
```

**Scan a hash (MD5, SHA-1, or SHA-256)**

```bash
miley --hash f617abd6a9ccb98e34a6e32184004d5a08ea11d198fca9fed88b04b9dfc96de2
```

**Scan a directory for malware**

```bash
miley --path /path/to/directory/
```

**Scan a remote container image**

```bash
miley --img alpine:latest
```

## Future Work

If I were to maintain this program going forward, I would:

- speed up the program
- support additional malware databases, such as Virus Total
- add a GUI

## Why is it named Miley?

Miley is my beloved family dog, who passed away in 2023 due to old age.

Miley was always good at detecting and alerting to potentially dangerous situations, despite being blind.

I wrote this tool with her memory at the forefront of my mind.

<img src="images/miley.png" alt="miley" width="400" height=auto/>

