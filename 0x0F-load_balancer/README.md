0x0F. Load balancer

# Load balancer

# Nginx Custom HTTP Header Configuration

This project involves configuring Nginx on web servers to include a custom HTTP header for tracking purposes. The custom header `X-Served-By` will indicate which server is handling the request. This is useful for monitoring and understanding load balancing.

## Overview

The `0-custom_http_response_header` script performs the following tasks:
1. Installs Nginx if it is not already installed.
2. Configures Nginx to add a custom header `X-Served-By` with the server's hostname.
3. Restarts Nginx to apply the changes.

## Script Details

### `0-custom_http_response_header`

- **Purpose**: Configures Nginx to add a custom HTTP response header indicating which server is responding to requests.
- **Location**: `0x0F-load_balancer/0-custom_http_response_header`

### Usage

1. **Ensure the script is executable**:
    ```bash
    chmod +x 0-custom_http_response_header
    ```

2. **Run the script**:
    ```bash
    ./0-custom_http_response_header
    ```

3. **Verify the custom header**:
    After running the script, use `curl` to check the header:
    ```bash
    curl -sI http://<server-ip> | grep X-Served-By
    ```

## Configuration

- **Nginx Configuration**: The script modifies `/etc/nginx/sites-available/default` to include the `add_header X-Served-By` directive in the `server` block.

## Requirements

- **Operating System**: Ubuntu 20.04 or later
- **Nginx Version**: Any version compatible with the script

## Notes

- Ensure that the server hostnames are properly configured (e.g., `249200-web-01` and `249200-web-02`).
- The script handles the installation and configuration of Nginx, so it should be run on a clean or newly provisioned server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

jayricka
