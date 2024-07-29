DEFAULT_CONFIG = {
    "read_path": "file:///app/data/original/",
    "anonymizer_config": [
        {
            "method": "sha256",
            "parameters": {
                "column_name": "first_name"
            }
        },
        {
            "method": "replace",
            "parameters": {
                "column_name": "last_name",
                "replace_to": "****"
            }
        },
        {
            "method": "replace_with_regex",
            "parameters": {
                "column_name": "address",
                "replace_from_regex": "R\d",
                "replace_to": "*"
            }
        }
    ],
    "sink_path": "file:///app/data/anonymize/"
}

# docker run -v "$(pwd)/download:/app" demyst
