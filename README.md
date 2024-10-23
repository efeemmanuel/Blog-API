# Blog API

A simple blog API built with Django REST Framework that allows users to create posts and comments. This project includes token authentication and custom permissions to restrict access to owners of the posts and comments.

## Features

- Create, retrieve, update, and delete blog posts.
- Create, retrieve, update, and delete comments on posts.
- Token-based authentication for user access.
- Custom permissions to restrict editing access to owners only.

## Technologies Used

- Django
- Django REST Framework
- SQLite 
- Django Auth (for user management)

API Endpoints
Authentication:
POST /api-token-auth/
Obtain an authentication token.

Posts:

GET /posts/ - List all posts.
POST /posts/ - Create a new post.
GET /posts/{id}/ - Retrieve a specific post.
PUT /posts/{id}/ - Update a specific post.
DELETE /posts/{id}/ - Delete a specific post.
Comments:

GET /comments/ - List all comments.
POST /comments/ - Create a new comment.
GET /comments/{id}/ - Retrieve a specific comment.
PUT /comments/{id}/ - Update a specific comment.
DELETE /comments/{id}/ - Delete a specific comment.
Custom Permissions
The API includes a custom permission class (IsOwnerOrReadOnly) that allows only the owners of posts and comments to edit or delete them. All users can read posts and comments.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
