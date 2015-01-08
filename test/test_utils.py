# Copyright 2015 Leon Sixt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import tempfile
from unittest import TestCase
from bernet.utils import download, sha256_file


class TestUtils(TestCase):
    def test_download(self):
        encoding = 'utf-8'
        with tempfile.NamedTemporaryFile("w+b") as server_file:
            server_file.write("Hello World!".encode(encoding))
            server_file.flush()
            with tempfile.NamedTemporaryFile("w+b") as f:
                download("file://" + server_file.name, f)
                f.seek(0)
                bytes = f.read()
                self.assertEqual(bytes.decode(encoding),  "Hello World!")

    def test_sha256_file(self):
        with tempfile.NamedTemporaryFile("w+b") as f:
            sha256sum = sha256_file(f)
            self.assertEqual(sha256sum,
                             hashlib.sha256("".encode("utf-8")).hexdigest())
            self.assertEqual(
                sha256sum,
                "e3b0c44298fc1c149afbf4c8996fb92427ae41e"
                "4649b934ca495991b7852b855")
