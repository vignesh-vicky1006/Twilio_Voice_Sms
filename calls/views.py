from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse,Dial
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
import traceback



# Twilio Credentials
import os
from dotenv import load_dotenv
load_dotenv()

# TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
# TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
# def index(request):
#     return render(request, "calls/index.html")

@api_view(['POST'])
@permission_classes([AllowAny,])
def make_call(request):
    try:
        if request.method == "POST":
            phone_number = request.data.get("phone_number")
            message = request.data.get("message")
            if not phone_number:
                return JsonResponse({"error": "Phone number is required"}, status=400)

            if not phone_number.startswith("+"):
                return JsonResponse({"error": "Phone number must be in international format (e.g., +1234567890)"}, status=400)
            print(phone_number)
            try:
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                call = client.calls.create(
                    to=phone_number,
                    from_=TWILIO_PHONE_NUMBER,
                    # url="http://demo.twilio.com/docs/voice.xml",
                    twiml=f"<Response><Say>{message}.</Say></Response>"

                )
                return JsonResponse({"message": "Call initiated!", "call_sid": call.sid})

            except Exception as e:
                traceback.print_exc()
                return JsonResponse({"error": str(e)}, status=400)
    except:
        traceback.print_exc()
        return JsonResponse({"error": "Invalid request"}, status=400)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def send_sms(request):
    try:
        if request.method == "POST":
            phone_number = request.data.get("phone_number")
            message_body = request.data.get("message")

            if not phone_number or not message_body:
                return JsonResponse({"error": "Phone number and message are required"}, status=400)

            if not phone_number.startswith("+"):
                return JsonResponse({"error": "Phone number must be in international format (e.g., +1234567890)"}, status=400)

            try:
                client = Client(ACCOUNT_SID, AUTH_TOKEN)
                message = client.messages.create(
                    to=phone_number,
                    from_=TWILIO_PHONE_NUMBER,
                    body=message_body
                )

                return JsonResponse({"message": "SMS sent successfully!", "message_sid": message.sid})

            except Exception as e:
                traceback.print_exc()
                return JsonResponse({"error": str(e)}, status=400)
    except:
        traceback.print_exc()
        return JsonResponse({"error": "Invalid request"}, status=400)

