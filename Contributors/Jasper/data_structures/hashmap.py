class HashMap:
    def __init__(self, initial_bucket_count=8):
        """
        Create a hash map with a fixed number of buckets.

        Buckets = containers that store key-value pairs.
        """

        if initial_bucket_count <= 0:
            raise ValueError("Bucket count must be greater than 0")

        # Total number of buckets
        self.total_number_of_buckets = initial_bucket_count

        # Number of key-value pairs stored
        self.total_number_of_entries = 0

        # Load factor threshold (when to resize)
        self.maximum_allowed_load_factor = 0.75

        # Create buckets (each bucket starts empty)
        self.bucket_array = [[] for _ in range(self.total_number_of_buckets)]

    # -------------------------------------------------------
    # CORE HASH FUNCTION
    # -------------------------------------------------------

    def _calculate_bucket_index_for_key(self, key):
        """
        Convert key into bucket index using Python's hash().
        """

        raw_hash_value = hash(key)

        bucket_index = raw_hash_value % self.total_number_of_buckets

        return bucket_index

    # -------------------------------------------------------
    # INSERT OR UPDATE
    # -------------------------------------------------------

    def put(self, key, value):
        """
        Insert a key-value pair into the hash map.
        If key already exists, update its value.
        """

        bucket_index = self._calculate_bucket_index_for_key(key)

        bucket = self.bucket_array[bucket_index]

        # Check if key already exists
        for entry_index in range(len(bucket)):
            existing_key, existing_value = bucket[entry_index]

            if existing_key == key:
                # Update value
                bucket[entry_index] = (key, value)
                return

        # If key not found, add new entry
        bucket.append((key, value))

        self.total_number_of_entries += 1

        # Resize if load factor exceeded
        if self._current_load_factor() > self.maximum_allowed_load_factor:
            self._resize_and_rehash()

    # -------------------------------------------------------
    # RETRIEVE
    # -------------------------------------------------------

    def get(self, key):
        """
        Retrieve value associated with key.
        Raise KeyError if not found.
        """

        bucket_index = self._calculate_bucket_index_for_key(key)

        bucket = self.bucket_array[bucket_index]

        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value

        raise KeyError("Key not found")

    # -------------------------------------------------------
    # REMOVE
    # -------------------------------------------------------

    def remove(self, key):
        """
        Remove key-value pair from map.
        """

        bucket_index = self._calculate_bucket_index_for_key(key)

        bucket = self.bucket_array[bucket_index]

        for entry_index in range(len(bucket)):
            existing_key, existing_value = bucket[entry_index]

            if existing_key == key:
                del bucket[entry_index]
                self.total_number_of_entries -= 1
                return

        raise KeyError("Key not found")

    # -------------------------------------------------------
    # LOAD FACTOR
    # -------------------------------------------------------

    def _current_load_factor(self):
        """
        Load factor = entries / buckets
        """

        return (
            self.total_number_of_entries
            / self.total_number_of_buckets
        )

    # -------------------------------------------------------
    # RESIZE
    # -------------------------------------------------------

    def _resize_and_rehash(self):
        """
        Double bucket count and rehash all keys.
        """

        old_bucket_array = self.bucket_array

        new_bucket_count = self.total_number_of_buckets * 2

        self.bucket_array = [[] for _ in range(new_bucket_count)]

        self.total_number_of_buckets = new_bucket_count
        self.total_number_of_entries = 0

        # Reinsert all entries
        for bucket in old_bucket_array:
            for key, value in bucket:
                self.put(key, value)

    # -------------------------------------------------------
    # UTILITIES
    # -------------------------------------------------------

    def size(self):
        return self.total_number_of_entries

    def __str__(self):
        all_entries = []

        for bucket in self.bucket_array:
            for key, value in bucket:
                all_entries.append(f"{key}: {value}")

        return "{" + ", ".join(all_entries) + "}"