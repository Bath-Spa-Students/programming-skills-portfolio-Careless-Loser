# Define a function named make_shirt with default arguments for size and message.
def make_shirt(size='large', message='Programming Excellence'):
    """Summarize the shirt that's going to be made."""
    # Print a description of the t-shirt, including size and message.
    print(f"\nCreating a {size} t-shirt.")
    print(f'It will feature the message: "{message}"')

# Call the function with different size and message values.
make_shirt()  # Using defaults for size and message.
make_shirt(size='medium')  # Specifying size while keeping default message.
make_shirt('small', 'Elegant Code Matters')  # Custom size and message.
