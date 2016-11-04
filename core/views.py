from apiclient import discovery
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from core.google_api_utils import APIClient, parse_email


def home(request):
    return render(request, 'core/home.html')


class EmailList(APIView):  # using DRF is a requirement

    def get(self):
        emails_list = self.batch_retrieve_emails(100)
        return Response({'messages': emails_list})

    def batch_retrieve_emails(self, emails_to_retrieve):
        emails = {}
        ordered_message_ids = []

        def email_fetched(request_id, response, exception):
            emails[response['id']] = parse_email(response)

        api_client = APIClient(self.request.user)
        service = discovery.build('gmail', 'v1')
        res = api_client.execute(
            service.users().messages().list(userId='me', maxResults=emails_to_retrieve))
        batch = service.new_batch_http_request(callback=email_fetched)
        for message in res['messages']:
            batch.add(
                service.users().messages().get(userId='me', id=message['id']))
            ordered_message_ids.append(message['id'])
        api_client.execute(batch)
        return [emails[msg_id] for msg_id in ordered_message_ids]
