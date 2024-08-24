from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import socket
import platform
import logging
import os

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_info(request: Request):
    try:
        # Get local IP and port
        local_ip = request.client.host
        local_port = request.url.port

        # Get remote IP and port
        remote_ip = request.headers.get("host").split(":")[0]
        remote_port = request.url.port

        # Connection ID (just an example, usually you'd use a more sophisticated method)
        connection_id = hash(f"{local_ip}:{local_port}-{remote_ip}:{remote_port}")

        # Get request host and path
        request_host = request.headers.get("host")
        request_path = request.url.path

        # Get system information
        arch = platform.machine()
        rid = platform.system() + " " + platform.release()
        framework = "FastAPI"
        hostname = socket.gethostname()
        background_color = os.getenv("BACKGROUND_COLOR", "white")
        # Log the request details
        logging.info(f"Request from {remote_ip}:{remote_port} to {local_ip}:{local_port}")

        # Render the HTML template with the system information
        return templates.TemplateResponse("index.html", {
            "request": request,
            "local_ip": local_ip,
            "local_port": local_port,
            "remote_ip": remote_ip,
            "remote_port": remote_port,
            "connection_id": connection_id,
            "request_host": request_host,
            "request_path": request_path,
            "arch": arch,
            "rid": rid,
            "framework": framework,
            "hostname": hostname,
            "background_color": background_color,
        })
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": "An error occurred while processing your request."}

# Add a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Graceful shutdown handling
@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application is shutting down...")

