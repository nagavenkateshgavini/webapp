## Create new user
```commandline
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;
```

## Drop user
```commandline
DROP USER 'username'@'host';
```

## Create DB
```commandline
CREATE DATABASE application CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
- The utf8mb4 character set is an extension of the utf8 character set in MySQL. The term "utf8mb4" stands for "UTF-8 Multibyte 4-byte," indicating that it supports the full range of Unicode characters, including those that require 4 bytes for representation.
- The utf8mb4_unicode_ci collation is a specific collation for the utf8mb4 character set in MySQL. It is designed to provide a case-insensitive and accent-insensitive comparison of Unicode characters.