from django.db import models

# Create your models here.

TransactionType = (
    ("L", "Lending"),
    ("B", "Borrowing"),
)

#saving a record of users
class Friends(models.Model):
    friends_id  = models.AutoField(primary_key=True)
    friends_name = models.CharField(max_length=100, unique=True)
    friends_record = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "friends_users"
        managed = True

#transaction iou records
class TransactionIOU(models.Model):
    iou_id = models.AutoField(primary_key=True)
    friends_id = models.ForeignKey(Friends, on_delete=models.CASCADE)
    transactor_id = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name="transactor")
    iou_amount = models.FloatField()
    iou_record = models.DateTimeField(auto_now=True)
    iou_type = models.CharField(max_length=1, choices=TransactionType)

    class Meta:
        db_table = "transaction_iou"
        managed = True

# #creating a Base model for inheritance of IOU table
# class IOUTable(models.Model):
#     iou_id = models.AutoField(primary_key=True)
#     friends_id = models.ForeignKey(Friends, on_delete=models.CASCADE)
#     iou_amount = models.FloatField()
#     # iou_record = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# #creating an inherited model of lending by the friend to another from the table 
# class AsLendingIOU(IOUTable):
#     borrower_id = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name="borrower")

#     class Meta:
#         db_table = "lender_to"
#         ordering = ["iou_id"]
#         managed = True

# #creating an inherited model of borrowing by the friend from another from the table
# class AsBorrowerIOU(IOUTable):
#     lender_id = models.ForeignKey(Friends, on_delete=models.CASCADE, related_name="lender")

#     class Meta:
#         db_table = "borrower_from"
#         ordering = ["iou_id"]
#         managed = True
    