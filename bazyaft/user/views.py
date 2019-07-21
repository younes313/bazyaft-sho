# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage


from .serializers import UserSignupEmailSerializer


class UserSignupEmail(APIView):
    serializer_class = UserSignupEmailSerializer()

    def post(self, request, format=None):
        serializer = UserSignupEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            dic = serializer.data
            dic.update({'status':'101'})
            # print(serializer.data)
            email = EmailMessage('email_subject', "message", to=['younesmoradi313@gmail.com',])
            email.send()
            return Response(dic, status=status.HTTP_201_CREATED)
        else:
            dic = dict({'status': [] })
            try:
                dic["status"].extend( serializer.errors["non_field_errors"] )
            except:
                pass
            try:
                for err in serializer.errors['email'] :
                    if str(err) == "user email with this email already exists.":
                        dic['status'].append('102')
                    if str(err) ==  "Enter a valid email address.":
                        dic['status'].append('103')
                    if str(err) == "Ensure this field has no more than 100 characters.":
                        dic['status'].append('104')
                    if str(err) == "This field may not be blank.":
                        dic['status'].append('105')
            except:
                pass
            try:
                for err in serializer.errors['password']:
                    if str(err) == "Ensure this field has at least 6 characters.":
                        dic['status'].append('110')
                    if str(err) ==  "This field may not be blank.":
                        dic['status'].append('112')
                    if str(err) == "Ensure this field has no more than 30 characters.":
                        dic['status'].append('111')
            except:
                pass
            return Response(dic , status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
