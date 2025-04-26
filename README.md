# ASCII Art Streaming API

This is a FastAPI application created to test streaming responses over HTTP. It converts text into ASCII art using the `pyfiglet` library and streams the result with colors.

![Demo GIF](demo.gif)

## Running the Application

### Locally

1.  **Install dependencies:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    pip install -r requirements.txt
    ```

2.  **Run the FastAPI server:**

    ```bash
    uvicorn api:app --reload
    ```

### Using Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t ascii-art-api .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 ascii-art-api
    ```
    The application will be available at `http://localhost:8000`.

## API Endpoint

### `GET /{text}`

Streams ASCII art generated from the provided text.

- **URL Parameter:**
    - `text`: The text to convert to ASCII art. **Important:** This text must be Base64 encoded.

- **Example:**

    To display the ASCII art for the word "Hello", first Base64 encode it:

    ```python
    import base64
    text = "Hello"
    encoded_text = base64.b64encode(text.encode()).decode()
    print(encoded_text) # Output: SGVsbG8=
    ```

    Then, make a request to the endpoint using `curl` or a web browser: `http://localhost:8000/SGVsbG8=`

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): The web framework used.
- [Uvicorn](https://www.uvicorn.org/): The ASGI server.
- [Pyfiglet](https://github.com/pwaller/pyfiglet): For generating ASCII art text.

## Deployment

This application is configured for deployment using a `Procfile` (e.g., for Heroku) and a `render.yaml` (for Render). The `Dockerfile` allows for containerized deployment.
