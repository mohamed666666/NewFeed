# Flask Post API

This project is a simple Flask API for managing posts. It includes endpoints for creating, retrieving, updating, and deleting posts.

## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/mohamed666666/newfeed_test/.git
    cd newfeed_test
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Database Connection**
    - Update the `app/config.py` file with your MySQL database configuration.

## Running the Project

To run the project locally on port 5000:
```bash
python main.py



API Endpoints

You can use Postman or any other API testing tool to interact with the API.
Get All Posts

    URL: http://127.0.0.1:5000/posts/
    Method: GET
    Description: Retrieves all posts from the database.

Create a Post

    URL: http://127.0.0.1:5000/posts/create
    Method: POST
    Description: Creates a new post.
    Request Body (JSON):

    json

    {
        "created_by": 1,
        "content": "Hello, this is the first post from our API"
    }

Get Post by ID

    URL: http://127.0.0.1:5000/posts/<post_id>
    Method: GET
    Description: Retrieves a post by its ID.

Update Post Content

    URL: http://127.0.0.1:5000/posts/<post_id>/edit
    Method: POST
    Description: Updates the content of a post.
    Request Body (JSON):

    json

    {
        "content": "Updated content for the post"
    }

Delete a Post

    URL: http://127.0.0.1:5000/posts/<post_id>/delete
    Method: POST
    Description: Deletes a post by its ID.
