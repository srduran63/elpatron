bind = "0.0.0.0:10000"
workers = 4
threads = 2
timeout = 120

# Remove fcntl usage
def when_ready(server):
    # Optional: Add Windows-specific initialization here
    pass