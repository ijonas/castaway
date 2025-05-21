# Address Book

To make the use of castaway a more pleasant experience for end users we want to create an Address Book, which will translate human-readable names such as Alice, Bob, and Charlie to their EVM addresses such as 0x57B6611dE36d8C093cA1c01E054dB301d8e092F5.

We're going to store the Address Book in a locally held SQLite database in the ./db folder, eg. ./db/address_book.sqlite.

We'll need to add sqlite and sqlalchemy as dependencies so we can manage our data access in a Python-typed manner.

Our Address Book schema will be simple, consisting of a list of Address records, each with a `name` and `evm_address` field.

Our Address Book should implement standard CRUD functionality.
