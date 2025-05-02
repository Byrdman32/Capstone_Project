

# In general if this is a container keep the address to '0.0.0.0' to allow access from outside the container.
# If you want to test locally set it to '127.0.0.1' or 'localhost'
API_ADDRESS = '0.0.0.0'

# MAKE SURE THAT IF YOU CHANGE THIS PORT THAT THE PORT IS FORWARDED IN DOCKER
# Check docker-compose.yml to see this.
API_PORT = 9000

DB_CONFIG = {
    'DB_HOST': 'postgres',
    'DB_PORT': 5432,
    'DB_NAME': 'mydatabase',
    'DB_USER': 'testuser',
    'DB_PASSWORD': 'testpassword',
}