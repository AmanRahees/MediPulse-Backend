from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from doctors.permissions import *
from bookings.models import *
from bookings.serializers import *
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

class BookingAPI(APIView):
    permission_classes = [isPatient]
    def post(self, request):
        required_fields = ['email', 'payment_method_id', 'appointment_slot', 'amount', 'doctor', 'patient']
        missing_fields = [field for field in required_fields if not request.data.get(field)]
        
        if missing_fields:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.data.get('email', None)
        payment_method_id = request.data.get('payment_method_id', None)
        amount = request.data.get('amount', None)
        slot_id = request.data.get('appointment_slot', None)

        try:
            slot = Slots.objects.get(id=slot_id)
        except Slots.DoesNotExist:
            return Response({"error": "Slot does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        if slot.is_booked:
            return Response({"error": "Slot is already booked"}, status=status.HTTP_409_CONFLICT)
        
        try:
            customer_data = stripe.Customer.list(email=email).data
            if len(customer_data) == 0:
                customer = stripe.Customer.create(
                        email=email, 
                        payment_method=payment_method_id
                    )
            else:
                customer = customer_data[0]
            payment_intent = stripe.PaymentIntent.create(
                amount=amount, currency='inr',
                payment_method=payment_method_id, 
                receipt_email=email,
                customer=customer,
            )
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid():
                appointment = serializer.save()
                BookingPayments.objects.create(
                    appointment=appointment,
                    transaction_id=payment_intent.id,
                    amount=appointment.amount
                )
                slot.is_booked = True
                slot.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
