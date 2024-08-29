
# FastAPI Deploy Info App !!!

**FastAPI Deploy Info App** is a simple FastAPI application that displays system and request information on a webpage. The background color of the webpage can be dynamically configured via an environment variable, making it suitable for deployment scenarios such as Blue/Green deployment.

## Features

- Displays system information such as local/remote IP, ports, connection ID, architecture, runtime ID, and hostname.
- Background color of the webpage can be set via the `BACKGROUND_COLOR` environment variable.
- Designed for Blue/Green deployment strategies.

## Getting Started

### Prerequisites

- Podman (or Docker) installed on your system.
- Python 3.12 or later (if running locally).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jemaltahir/bgdep-color.git
   cd bgdep-color
   ```

2. Build the container image using Podman:

   ```bash
   podman build -t fastapi-deploy-info-app .
   ```

### Running the Application

You can run the application with different background colors by passing the `BACKGROUND_COLOR` environment variable.

#### Example 1: Blue Deployment

```bash
podman run -d -p 8080:8080 --env BACKGROUND_COLOR="blue" fastapi-deploy-info-app
```

This command runs the application on port `8080` with a blue background.

#### Example 2: Yellow Deployment

```bash
podman run -d -p 8081:8080 --env BACKGROUND_COLOR="yellow" fastapi-deploy-info-app
```

This command runs the application on port `8081` with a yellow background.

### Accessing the Application

After running the containers, you can access the application in your browser:

- For the blue deployment: `http://localhost:8080`
- For the yellow deployment: `http://localhost:8081`
