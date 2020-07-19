from django.http import JsonResponse
import json
from . import models
from django.db.models import Q
import time
from django.contrib.auth import authenticate
from rest_framework import response
from django.shortcuts import render

# Create your views here.
def index(requests):
    

    if requests.method == "POST":
        # Do validation stuff here
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        print("+++++", body)
        user = authenticate(username=body['username'])
        print("(((((",user)
        try: 
            o = models.Booking(username=body['username'], moviename=body['moviename'], eventname=body['eventname'], timing=body['timing'],cost=body['cost'],seat=body['seat'],seatclass=body['seatclass'])
            o.save()
            return JsonResponse({'statusCode':201, 'data':body  })
        except Exception as e:
            return JsonResponse({'statusCode':400, 'message':str(e)  })
    elif requests.method == "DELETE":
        print("Delteeeeeeeeeee")
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        print("+++++",body)
        try: 
            # o = models.Booking(username=body['username'], moviename=body['moviename'], eventname=body['eventname'], timing=body['timing'],cost=body['cost'],seat=body['seat'],seatclass=body['seatclass'])
            models.Booking.objects.get(id=body['id']).delete()
            # o.delete()
            # requests.DELETE(body['username'])
            return JsonResponse({'statusCode':201, 'data':body  })
        except Exception as e:
            return JsonResponse({'statusCode': 400, 'message': str(e)})
    elif requests.method == "PUT":
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        print("EDITTTTTTTTT", body)
        try:
            models.Booking.objects.filter(id=body['id']).update(username=body['username'], moviename=body['moviename'], eventname=body['eventname'], timing=body['timing'],cost=body['cost'],seat=body['seat'],seatclass=body['seatclass'])
        
            return JsonResponse({'statusCode': 201, 'data': body})
        except Exception as e:
            return JsonResponse({'statusCode': 400, 'message': str(e)})
    else:
        
        user_filter = {
        "username" : requests.GET.getlist('username') if requests.GET.__contains__('username') else False,
        }     

        q_objects = Q() 
        if user_filter["username"]:
            q_objects &= Q(username=user_filter["username"][0])    
        
        try:
            bookings = models.Booking.objects.filter(q_objects).only('id')
            data =  list(bookings.values("id","username","moviename","eventname","timing","seatclass","seat","cost","timestamp"))
            print("*******",data)
            totalcost= 0
            for booking in data:
                totalcost+=booking["cost"]

            if len(data):                                
                return JsonResponse({'statusCode':200, 'data':data, 'totalcost':totalcost  })
            else:
                return JsonResponse({'statusCode':404, 'data':"No data found for your request"  })
        except Exception as e:
            return JsonResponse({'statusCode':400, 'message':str(e)  })


def bookingdetails(requests,booking_id):
    try:
        booking = models.booking.objects.filter(pk=booking_id)
        data = list(booking.values("id","username","salad","buns","slices","cutlets","cost","timestamp"))
       
        return JsonResponse({'statusCode':200, 'data':data[0]})
    
    except Exception as identifier:
            
        return JsonResponse({'statusCode':404, 'data':"No data found for your request"})