import httplib2

from oauth2client.client import (
    AccessTokenCredentials, AccessTokenCredentialsError)
from social.strategies.utils import get_current_strategy


class APIClient(object):
    """Handles refresh of access token"""
    def __init__(self, user):
        self._google_auth = user.social_auth.first()
        self._http = self._get_http(self._google_auth.access_token)

    def execute(self, service_request):
        try:
            return service_request.execute(http=self._http)
        except AccessTokenCredentialsError:
            self._google_auth.refresh_token(get_current_strategy())
            self._http = self._get_http(self._google_auth.access_token)
            return service_request.execute(http=self._http)

    def _get_http(self, access_token):
        credentials = AccessTokenCredentials(
            access_token,
            'my-user-agent/1.0')
        return credentials.authorize(httplib2.Http(cache=".cache"))


def parse_email(msg_data):
    return {
        'id': msg_data['id'],
        'subject': parse_header(msg_data, 'Subject'),
        'date': parse_header(msg_data, 'Date'),
        'from': parse_header(msg_data, 'From'),
        'snippet': msg_data['snippet'],
    }


def parse_header(msg_data, header_name):
    headers = [
        h for h in msg_data['payload']['headers']
        if h['name'] == header_name
    ]
    if headers:
        return headers[0]['value']
