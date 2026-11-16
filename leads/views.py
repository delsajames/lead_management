from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from leads.serializers import LeadSerializer
from leads.models import Lead
from accounts.permissions import IsOwner

# Create your views here.
class LeadListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        qs=Lead.objects.filter(created_by=request.user)

        serializer_instance=LeadSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data=request.data

        serializer_instance=LeadSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(created_by=request.user)

            return Response(serializer_instance.data)

        else:    

            return Response(serializer_instance.errors)


class LeadRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]      

    permission_classes=[IsOwner]  


    def get(self,request,pk=None):

        lead_object=get_object_or_404(Lead,id=pk)

        self.check_object_permissions(request,lead_object)

        serializer_instance=LeadSerializer(lead_object)

        return Response(data=serializer_instance.data)

    def patch(self,request,pk=None):

        form_data=request.data

        lead_object=get_object_or_404(Lead,id=pk)

        self.check_object_permissions(request,lead_object)

        serializer_instance=LeadSerializer(data=form_data,instance=lead_object,partial=True)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)


    def put(self,request,pk=None):

        form_data=request.data

        lead_object=get_object_or_404(Lead,id=pk)

        self.check_object_permissions(request,lead_object)

        serializer_instance=LeadSerializer(data=form_data,instance=lead_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        lead_object=get_object_or_404(Lead,id=pk)   

        self.check_object_permissions(request,lead_object)

        lead_object.delete() 

        response_data={"message":"deleted"}

        return Response(data=response_data)