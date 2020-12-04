from .import bp as blog
from .models import BlogPost
from flask import jsonify
from app.auth import token_auth


@blog.route('/', methods=['GET'])
def index():
    return jsonify([p.to_dict() for p in BlogPost.query.all()])

@blog.route('/<int:id>', methods=['GET'])
def single_post(id):
    """
    [GET] /blog/<id>
    """
    p = BlogPost.query.get(id)
    return jsonify(p.to_dict())

@blog.route('/product/create', methods=['POST'])
@token_auth.login_required
def create_product():
    data = request.json
    post = Product()
    post.from_dict(data)
    post.save()
    return jsonify(post.to_dict()), 201

@blog.route('product/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_product(id):
    """
    [PUT/PATCH] /api/product/edit/<id>
    """
    data = request.json
    p = Product.query.get(id)
    p.from_dict(data)
    db.session.commit()
    return jsonify(p.to_dict())

@blog.route('/product/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_product(id):
    """
    [DELETE] /api/product/delete/<id>
    """
    p = Product.query.get(id)
    p.remove()
    return jsonify([p.to_dict() for p in Product.query.all()])