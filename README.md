# FastAPI Deploy Info App

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

```bash
podman build -t bgdep-color .
```
