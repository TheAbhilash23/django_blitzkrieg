
class ModelDetails:

    def __init__(
            self,
            pascal_model_name: str,
            fields: [str],
            # db_table: str,
            app_name: str,
    ):
        self.pascal_model_name = pascal_model_name
        self.fields = fields
        # self.db_table = db_table
        self.app_name = app_name
