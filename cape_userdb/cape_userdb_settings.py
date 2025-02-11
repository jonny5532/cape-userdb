# Copyright 2018 BLEMUNDSBURY AI LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Either 'sqlite' or 'mysql'
DB_TYPE = os.getenv('CAPE_USERDB_DATABASE_TYPE', 'sqlite')

# SQLite settings
DB_PATH = os.getenv('CAPE_USERDB_SQLITE_PATH', os.path.join(THIS_FOLDER, 'storage', 'capeusers.sqlite'))

# MySQL settings
DB_NAME = os.getenv('CAPE_USERDB_MYSQL_DATABASE', 'cape_userdb')
DB_HOST = os.getenv('CAPE_USERDB_MYSQL_HOST', '127.0.0.1')
DB_PORT = os.getenv('CAPE_USERDB_MYSQL_PORT', '3306')
DB_USER = os.getenv('CAPE_USERDB_MYSQL_USER', 'cape_userdb')
DB_PASS = os.getenv('CAPE_USERDB_MYSQL_PASS', 'REPLACEME')

DEFAULT_EMAIL = "answer@questions.mail"
DEFAULT_RESPONSE = "I'm sorry, we couldn't find a response"
DEFAULT_THRESHOLD = "MEDIUM"
