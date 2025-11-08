"""
Secure version of main.py demonstrating proper secret management.

This file shows how to properly handle secrets using environment variables
instead of hardcoding them in the source code.
"""
import os
import sys


def get_secret(secret_name):
    """
    Safely retrieve a secret from environment variables.
    
    Args:
        secret_name: Name of the environment variable
        
    Returns:
        The secret value
        
    Raises:
        ValueError: If the secret is not found
    """
    secret = os.getenv(secret_name)
    if not secret:
        raise ValueError(
            f"Required environment variable '{secret_name}' is not set.\n"
            f"Please set it in your .env file or environment."
        )
    return secret


def main():
    """Main entry point of the application."""
    print("Hello, World!")
    
    # Example of secure secret handling
    # Uncomment below to use in production:
    # try:
    #     payment_gateway_key = get_secret('PAYMENT_GATEWAY_KEY')
    #     print("Payment gateway configured successfully")
    #     # Use the key for actual payment processing
    # except ValueError as e:
    #     print(f"Configuration error: {e}", file=sys.stderr)
    #     sys.exit(1)


if __name__ == "__main__":
    main()
