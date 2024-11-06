
# FastAPI PDF Upload and Question-Answering API

This is a FastAPI project that provides two main features:
1. **Upload PDF Documents** - Allows users (specifically admins) to upload PDF documents, which are then saved to the server and recorded in the database.
2. **Ask Questions** - Users can ask questions, and the system will provide answers by utilizing stored documents and chat history to generate contextually relevant answers.

## Features

- **PDF Upload**
  - Upload PDF files (only PDFs allowed).
  - Store PDF files in a designated folder on the server.
  - Record document metadata (filename, file path, and user ID) in the database.

- **Question Answering**
  - Allows users to ask questions.
  - Provides context-aware answers using stored documents and previous chat history.
  - Stores user questions and answers in the database for future reference.

## Requirements

- Python 3.x
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (or another database)
- Additional libraries: `python-multipart`, `uvicorn`, `requests`, etc.

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create the database (if not already created):
   ```bash
   # Create your SQLite database file if it doesn't exist
   touch DB.sqlite
   ```

## Environment Variables

- `DOCUMENTS_FOLDER`: Directory to save uploaded PDF files.
- Ensure you have a database connection configured (SQLite is used in this example).

## Endpoints

### `/upload-pdf`

- **Method**: `POST`
- **Description**: Uploads a PDF document.
- **Request Body**: Multipart file upload (`file: UploadFile`).
- **Response**: A `DocumentRecordOut` object with document metadata.

#### Example:
```bash
POST /upload-pdf
Content-Type: multipart/form-data
File: <pdf_file>
```

Response:
```json
{
  "id": 1,
  "filename": "example.pdf",
  "file_path": "/path/to/example.pdf",
  "user_id": 1
}
```

### `/ask`

- **Method**: `POST`
- **Description**: Allows the user to ask a question, and provides a context-aware answer.
- **Request Body**:
  - `question`: The question object.
  - **Example**:
    ```json
    {
      "question": "What is the purpose of the uploaded PDFs?"
    }
    ```

- **Response**:
  - Returns a JSON object containing the user's question and the generated answer.
  
#### Example:
```bash
POST /ask
Content-Type: application/json
Body: 
{
  "question": "What is the purpose of the uploaded PDFs?"
}
```

Response:
```json
{
  "question": "What is the purpose of the uploaded PDFs?",
  "answer": "The PDFs are used to store and retrieve document information."
}
```

## Dependencies

- `FastAPI` - Framework for building APIs.
- `Uvicorn` - ASGI server for running the FastAPI app.
- `SQLAlchemy` - ORM for interacting with the database.
- `Pydantic` - Data validation library.
- `python-multipart` - To handle file uploads.
- `requests` - For making HTTP requests.

## Running the Application

To run the FastAPI application, use Uvicorn:
```bash
uvicorn main:app --reload
```

This will start the development server at `http://127.0.0.1:8000`.

## Database Setup

The project uses an SQLite database by default, but it can be adapted to other databases like PostgreSQL or MySQL. Ensure that your database is set up and connected properly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
