import ast

from google.cloud import secretmanager


def get_secret_value_dict(project_id="", secret_id="", version_id="latest"):
    """
    Retrieve the value of a specified secret from Google Cloud Secret Manager and return it as a dictionary.

    This function uses the SecretManagerServiceClient from the google-cloud-secret-manager library to
    access a specified version of a secret from a specific Google Cloud project. The secret value is
    expected to be a JSON string, which is loaded into a dictionary before being returned.

    Args:
        project_id (str, optional): The ID of the Google Cloud project where the secret is stored.
                                     Defaults to an empty string.
        secret_id (str, optional): The ID of the secret to be retrieved.
                                   Defaults to an empty string.
        version_id (str, optional): The version of the secret to be retrieved.
                                    Defaults to "latest".

    Returns:
        dict: A dictionary containing the JSON-decoded value of the secret.

    Raises:
        google.api_core.exceptions.GoogleAPICallError: If the request for accessing the secret value fails.
        json.JSONDecodeError: If the secret value cannot be decoded into JSON.

    Example:
        >>> get_secret_value_dict("my-project", "my-secret")
        {'key1': 'value1', 'key2': 'value2'}
    """
    client = secretmanager.SecretManagerServiceClient()

    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # secret_value = {'key1': 'value1', 'key2': 'value2'}
    # return secret_value
    response = client.access_secret_version(request={"name": secret_name})
    secret_value = ast.literal_eval(response.payload.data.decode("UTF-8"))

    return secret_value