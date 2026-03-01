class DynamicArray:
    def __init__(self, initial_capacity=8):
        """
        Create a dynamic array with a fixed-size backing storage.

        initial_capacity = how many elements we can store before resizing
        """

        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be greater than 0")

        # Total number of elements the storage can currently hold
        self.total_storage_capacity = initial_capacity

        # Number of elements actually stored in the array
        self.current_number_of_elements = 0

        # Fixed-size storage (this is the "real array" underneath)
        self.storage_array = [0] * self.total_storage_capacity
    
    # -----------------------------------------------------------
    # BASIC INFORMATION
    # -----------------------------------------------------------    
        def size(self):
            """
            Return how many elements are currently in the array    
            """
            return self.current_number_of_elements
        
        def capacity(self):
            """
            Return how many elements can fit before resizing
            """
            return self.total_storage_capacity
        
        def is_empty(self):
            """
            Return True if no elements are stored
            """
            return self.current_number_of_elements == 0
        
    # -----------------------------------------------------------
    # ACCESS ELEMENTS
    # -----------------------------------------------------------         
        def get(self, index_to_access):
            """
            Retrieve element at given index
            """
            self._ensure_index_is_valid(index_to_access)

            return self.storage_array[index_to_access]

        def set(self, index_to_modify, new_value):
            """
            Replace the value at a given index.
            """

            self._ensure_index_is_valid(index_to_modify)

            self.storage_array[index_to_modify] = new_value

    # -----------------------------------------------------------
    # ADD ELEMENTS : add new element to end of dynamic array
    # -----------------------------------------------------------  
        def append(self, value_to_add):
        
            # If storage is full, increase capacity
            if self.current_number_of_elements == self.total_storage_capacity:
                self.increase_storage_capacity()

            # Place the new element at the next free position
            self.storage_array[self.current_number_of_elements] = value_to_add

            # Increase amount of stored elements
            self.current_number_of_elements += 1

    # -----------------------------------------------------------
    # REMOVE ELEMENTS : remove element at specific index
    # -----------------------------------------------------------   
        # All elements to the right of index shift LEFT one position

        def remove_at(self, index_to_remove):
            self._ensure_index_is_valid(index_to_remove)

            # Shift elements left to fill the gap
            for position in range(
                index_to_remove,
                self.current_number_of_elements - 1
            ):
                self.storage_array[position] = self.storage_array[position + 1]

            # Reduce the element count
            self.current_number_of_elements -= 1

            # Optional cleanup: clear the now-unused slot
            self.storage_array[self.current_number_of_elements] = 0

            # Optional shrink if mostly empty (common optimization)
            if (
                self.current_number_of_elements > 0
                and self.current_number_of_elements
                <= self.total_storage_capacity // 4
            ):
                self._decrease_storage_capacity()

    

    # -----------------------------------------------------------
    # INTERNAL RESIZING OPERATIONS
    # -----------------------------------------------------------

        def _increase_storage_capacity(self):
            """
            Double the storage capacity when full.
            """

            new_capacity = self.total_storage_capacity * 2

            new_storage_array = [0] * new_capacity

            # Copy elements into new storage
            for index in range(self.current_number_of_elements):
                new_storage_array[index] = self.storage_array[index]

            self.storage_array = new_storage_array
            self.total_storage_capacity = new_capacity

        def _decrease_storage_capacity(self):
            """
            Halve the storage capacity when mostly empty.
            """

            new_capacity = self.total_storage_capacity // 2

            new_storage_array = [0] * new_capacity

            # Copy existing elements
            for index in range(self.current_number_of_elements):
                new_storage_array[index] = self.storage_array[index]

            self.storage_array = new_storage_array
            self.total_storage_capacity = new_capacity

    # -----------------------------------------------------------
    # HELPER VALIDATION
    # -----------------------------------------------------------

        def _ensure_index_is_valid(self, index):
            """
            Check that index is within the range of stored elements.
            """

            if index < 0 or index >= self.current_number_of_elements:
                raise IndexError("Index out of bounds")

        # -----------------------------------------------------------
        # STRING REPRESENTATION
        # -----------------------------------------------------------

        def __str__(self):
            """
            Show only the stored elements, not unused capacity.
            """

            visible_elements = self.storage_array[
                : self.current_number_of_elements
            ]

            return str(visible_elements)