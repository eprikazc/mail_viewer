from apiclient import discovery
from django.shortcuts import render
from django.http import JsonResponse

from core.google_api_utils import APIClient, parse_email


def home(request):
    return render(request, 'core/home.html')


def email(request):
    emails_to_retrieve = 100
    emails = {}

    def email_fetched(request_id, response, exception):
        emails[response['id']] = parse_email(response)

    api_client = APIClient(request.user)
    service = discovery.build('gmail', 'v1')
    res = api_client.execute(
        service.users().messages().list(userId='me', maxResults=emails_to_retrieve))
    ordered_message_ids = []
    batch = service.new_batch_http_request(callback=email_fetched)
    for message in res['messages']:
        batch.add(
            service.users().messages().get(userId='me', id=message['id']))
        ordered_message_ids.append(message['id'])
    api_client.execute(batch)
    emails_list = [emails[msg_id] for msg_id in ordered_message_ids]
    return JsonResponse({'messages': emails_list})
