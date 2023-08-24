from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# # get method
# @api_view()
# def hello_world(request):
#     return Response({'msg':'This is GET reqsuest'})
 

# # get method
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'This is GET reqsuest})
 
 
 
# # post request
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This is POST reqsuest'})
 
 
# get and post request
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg':'This is GET reqsuest','data':request.data})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is POST request','data':request.data})
 