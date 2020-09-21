from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#Create your views here
from .models import Friends, TransactionIOU
from .serializers import FriendsSerializer, TransactionIOUSerializer

class FriendsView(APIView):
    ser_class = FriendsSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            user = {"user": ser.data}
            #print("user", user)
            return Response(user, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def get(self, request):
        x = []
        data = Friends.objects.values("friends_name").order_by("friends_name")
        #print("data", data)
        for user in data:
            x.append(user["friends_name"])
        #print("x", x)
        users = {"users": x}
        #print("users", users)
        ser = self.ser_class(data)
        return Response(users, status=status.HTTP_200_OK)

class TransactionIOUView(APIView):
    ser_class = TransactionIOUSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            transaction = {"iou": ser.data}
            print("iou", transaction)
            return Response(transaction, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    #in lieu of not knowing whether I could use url parametrization or not, I decided to hard-code things
    def get(self, request):
        summary_all = []
        names = TransactionIOU.objects.values("friends_id").distinct() 
        #print("names", names)
        for i in names:
            #print("i", i)
            name = i["friends_id"]
            #print("name", i["friends_id"])
            x_name = Friends.objects.filter(friends_id=name).values("friends_name")[0]["friends_name"]
            #print("x_name", x_name)
            data_lend = TransactionIOU.objects.filter(friends_id=name, iou_type="L").values("transactor_id", "iou_amount")
            #print("data", data_lend)
            sum_lend = []
            sum_borrow = []
            owes = {}
            owed_by = {}
            for iou in data_lend:
                lender_id = iou["transactor_id"]
                lender_name = Friends.objects.filter(friends_id=lender_id).values("friends_name")[0]["friends_name"]
                #print("lender_name", lender_name)
                owes[lender_name] = iou["iou_amount"]
                sum_lend.append(iou["iou_amount"])
            #print("owes", owes)
            #print("sum_lend", sum_lend)

            data_borrow = TransactionIOU.objects.filter(friends_id=name, iou_type="B").values("transactor_id", "iou_amount")
            #print("data", data_borrow)
            for iou_b in data_borrow:
                borrower_id = iou_b["transactor_id"]
                borrower_name = Friends.objects.filter(friends_id=borrower_id).values("friends_name")[0]["friends_name"]
                print("borrower_name", borrower_name)        
                owed_by[borrower_name] = iou_b["iou_amount"]
                sum_borrow.append(iou_b["iou_amount"])
            #print("owed_by", owed_by)
            #print("sum_borrow", sum_borrow)
            transaction_summary = {
                "name" : x_name,
                "owes" : owes,
                "owes_by": owed_by,
                "balance": sum(sum_borrow)-sum(sum_lend)
            }
            #print("transaction_summary", transaction_summary)
            summary_all.append(transaction_summary)
        return Response(summary_all, status=status.HTTP_200_OK)
