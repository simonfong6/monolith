from .posts import posts


def register_sub_site(app, prefix="/api"):
    app.register_blueprint(posts, url_prefix=f'{prefix}/posts')
