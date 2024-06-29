from flask import Blueprint, request, jsonify
from app.model.post import Post

post_bp = Blueprint('post_controller', __name__, url_prefix='/posts')

@post_bp.route('/')
def list_posts():
    try:
        posts = Post.get_all()
        return jsonify({"posts": posts})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@post_bp.route('/<int:post_id>')
def view_post(post_id):
    try:
        post = Post.get_by_id(post_id)
        if post is None:
            return jsonify({"error": "Post not found"}), 404
        return jsonify({"post": post})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@post_bp.route('/create', methods=['POST'])
def create_post():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        created_by = request.json.get('created_by')
        content = request.json.get('content')
        if not created_by or not content:
            return jsonify({"error": "Missing 'created_by' or 'content'"}), 400
        post_id = Post.create(created_by, content)
        return jsonify({"post_id": post_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@post_bp.route('/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "Missing 'content'"}), 400
        post = Post.get_by_id(post_id)
        if post is None:
            return jsonify({"error": "Post not found"}), 404
        Post.update(post_id, content)
        return jsonify({"post": post})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@post_bp.route('/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    try:
        post = Post.get_by_id(post_id)
        if post is None:
            return jsonify({"error": "Post not found"}), 404
        Post.delete(post_id)
        return jsonify({"post_id": post_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500