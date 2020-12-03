from .import bp as shop
from .models import Product, Category
from flask import jsonify, request

@shop.route('/products', methods=['GET'])
def products():
    return jsonify([p.to_dict() for p in Product.query.all()])

@shop.route('/product/<int:id>', methods=['GET'])
def single_product(id):
    """
    [GET] /api/product/<id>
    """
    p = Product.query.get(id)
    return jsonify(p.to_dict())

@shop.route('/product/create', methods=['POST'])
def create_product():
    data = request.json
    post = Product()
    post.from_dict(data)
    post.save()
    return jsonify(post.to_dict()), 201

@shop.route('product/edit/<int:id>', methods=['PUT'])
def edit_product(id):
    """
    [PUT/PATCH] /api/product/edit/<id>
    """
    data = request.json
    p = Product.query.get(id)
    p.from_dict(data)
    db.session.commit()
    return jsonify(p.to_dict())
    #    ;l;Skdl;AS
@shop.route('/product/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    """
    [DELETE] /api/product/delete/<id>
    """
    p = Product.query.get(id)
    p.remove()
    return jsonify([p.to_dict() for p in Product.query.all()])
# SHOP ROUTES

# SHOP CATEGORY ROUTES
@shop.route('/categories', methods=['GET'])
def categories():
    return jsonify([c.to_dict() for c in Category.query.all()])

@shop.route('/category/<int:id>', methods=['GET'])
def single_category(id):
    """
    [GET] /api/category/<id>
    """
    p = Category.query.get(id)
    return jsonify(p.to_dict())

@shop.route('/category/create', methods=['POST'])
def create_category():
    data = request.json
    c = Category()
    c.from_dict(data)
    c.save()
    return jsonify(c.to_dict()), 201

@shop.route('category/edit/<int:id>', methods=['PUT'])
def edit_category(id):
    """
    [PUT/PATCH] /api/category/edit/<id>
    """
    data = request.json
    p = Category.query.get(id)
    p.from_dict(data)
    db.session.commit()
    return jsonify(p.to_dict())
    
@shop.route('/category/delete/<int:id>', methods=['DELETE'])
def delete_category(id):
    """
    [DELETE] /api/category/delete/<id>
    """
    p = Category.query.get(id)
    p.remove()
    return jsonify([p.to_dict() for p in Category.query.all()])

@shop.route('/test', methods=['POST'])
def test():
    data = request.json
    print(data)
    return "Success", 201