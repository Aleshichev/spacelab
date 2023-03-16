TORTOISE_ORM = {
    "connections": {"default": "sqlite://sql_app.db"},
    "apps": {
        "models": {
            "models": ["database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}