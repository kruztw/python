#!/usr/bin/env python3

from hashlib import sha256

print(sha256(b'hello world').hexdigest())
