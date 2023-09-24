class MyContextManager:
    def __enter__(self):
        # Initialize and set up resources
        print("Entering the context")
        return self  # You can return an object that will be available in the `with` block

    def __exit__(self, exc_type, exc_value, traceback):
        # Clean up and release resources
        print("Exiting the context")
        # You can handle exceptions here if needed

# Using the custom context manager
with MyContextManager() as cm:
    # Inside the context
    print("Doing something")

# Outside the context
