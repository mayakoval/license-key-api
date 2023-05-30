# Key generator-validator

Key generator-validator is a FastAPI app for generating an encrypted license key and validating an issued key.

## Installation

Download the source code on your machine. This app uses [Python](https://www.python.org) and [FastAPI](https://fastapi.tiangolo.com/).

Use the package manager to install dependencies.

```bash
pip install -r requirements.txt
```

Create a local `.env` file in the source folder and populate it with the required keys.

## Usage

To start the app locally:

```bash
uvicorn main:app --reload
```

> **Note**  **API key** (access token) is mandatory for both requests.
  If using FastAPI interface, use Authorize button for providing API key.

Use FastAPI interface for accessing the endpoints or the following CURL on command line:

### Generating key

Update request body with the **user name** and name of **software package**.

```bash
curl -X 'POST' \
  'http://local-url/key-generator/' \
  -H 'accept: application/json' \
  -H 'access_token: secret' \
  -H 'Content-Type: application/json' \
  -d '{
  "full_name": "Your Name",
  "software_package": "package"
}'
```

### Validating key

**User name** and encrypted **license key** must be provided as a request body.
> **Note** User name is not case-sensitive.

```bash
curl -X 'POST' \
  'http://local-url/key-validator/' \
  -H 'accept: application/json' \
  -H 'access_token: secret' \
  -H 'Content-Type: application/json' \
  -d '{
  "full_name": "your name",
  "key": "encrypted-key"
}'
```

## Testing

From the project root file run the following command:

```bash
pytest
```
