from app import create_app
from app import cli, db

from app.blueprints.shop.models import Product, Category

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_context():
    return dict(Product=Product, Category=Category, db=db)