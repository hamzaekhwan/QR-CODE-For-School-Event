from rest_framework.response import Response
from qrcode_app.models import *
from rest_framework.views import *
from rest_framework.decorators import *
from rest_framework.response import *
from qrcode_app.serializers import  *
from .models import *
import shortuuid
import qrcode
from PIL import Image, ImageFont, ImageDraw
from django.http import JsonResponse,HttpResponse
import textwrap
import arabic_reshaper
from bidi.algorithm import get_display
from django.shortcuts import render
import csv
from tablib import Dataset
from .resources import StudentResource

@api_view(['GET'])
def query_about_0(request):
    objs = Invite.objects.filter(student_id__startswith='0')
    response_data=""
    for i in objs:
        response_data += i.name + "\n"

    return HttpResponse(response_data, content_type="text/plain; charset=utf-8")    

def upload(request):
     if request.method == 'POST':  
        person_resource = StudentResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
      
        for data in imported_data:
         print(data[1])
         value = Student(
        		student_name=data[0],
        		student_id=data[1],
        		)
         value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

     return render(request, 'input.html')

@api_view(['GET'])
def festival_detail(request):
    num_of_student = Invite.objects.filter(position="student").count()

    num_of_others = Invite.objects.exclude(position__exact='student').count()
    print(list(Invite.objects.filter(position="student")))
    print(list(Invite.objects.all()))
    my_list=list(Invite.objects.all())
    count=0
    
    for i in my_list:
        
        if (i.first_companion) is not None  :
            count=count+1

        if ( i.second_companion )  is not None:   
            count=count+1
    
   

    
         
    
    num_of_guests=count
    all_invite=num_of_student + num_of_others + num_of_guests

    response_data = "festival info:\n"
    response_data += "عدد الطلاب المسجلين للحفل: {}\n".format(num_of_student)
    response_data += "عدد المرافقين للطلاب : {}\n".format(num_of_guests)
    response_data += "عدد الضيوف الخاصة : {}\n".format(num_of_others)
    response_data += "العدد الكلي : {}\n".format(all_invite)

    
    
            
    
    return HttpResponse(response_data, content_type="text/plain; charset=utf-8")

@api_view(['GET'])
def student_detail(request, id):
    student = Invite.objects.filter(student_id=id).last()
    response_data = "Invite Info:\n"
    response_data += "Student name : {}\n".format(student.name)
    response_data += "Student ID : {}\n".format(student.student_id)
    response_data += "Position : {}\n".format(student.position)
    response_data += "First Companion : {}\n".format(student.first_companion)
    response_data += "Second Companion : {}\n".format(student.second_companion)
    my_dict={}
    my_list=list(Invite.objects.all())
    count=0
    for i in my_list:
        count=count+1
        my_dict[i.name]=count
        
        if (i.first_companion) is not None :
            count=count+1
            my_dict[i.first_companion]=count
        if ( i.second_companion ) is not None:   
            count=count+1
            my_dict[i.second_companion]=count
    num=   my_dict[student.name] 

        
    response_data += "num : {}\n".format(num)
    
    
    
            
    
    return HttpResponse(response_data, content_type="text/plain; charset=utf-8")
   
@api_view(['GET'])
def guest1_detail(request, id):
    student = Invite.objects.filter(student_id=id).last()
    response_data = "Invite Info:\n"
    response_data += "Name : {}\n".format(student.first_companion)
    response_data += "Phone : {}\n".format(student.first_companion_number)
    response_data += "Student Name who invite me : {}\n".format(student.name)
    response_data += "Position : guest\n"

    my_dict={}
    my_list=list(Invite.objects.all())
    count=0
    for i in my_list:
        count=count+1
        my_dict[i.name]=count
       
        if (i.first_companion) is not None :
            count=count+1
            my_dict[i.first_companion]=count
        if ( i.second_companion ) is not None:   
            count=count+1
            my_dict[i.second_companion]=count
    num=   my_dict[student.first_companion] 

        
    response_data += "num : {}\n".format(num)
   
    return HttpResponse(response_data, content_type="text/plain; charset=utf-8")
    
@api_view(['GET'])
def guest2_detail(request, id):
    student = Invite.objects.filter(student_id=id).last()
    response_data = "Invite Info:\n"
    response_data += "Name : {}\n".format(student.second_companion)
    response_data += "Phone : {}\n".format(student.second_companion_number)
    response_data += "Student Name who invite me : {}\n".format(student.name)
    response_data += "Position : guest\n"

    my_dict={}
    my_list=list(Invite.objects.all())
    count=0
    for i in my_list:
        count=count+1
        my_dict[i.name]=count
        
        if (i.first_companion) is not None :
            count=count+1
            my_dict[i.first_companion]=count
        if ( i.second_companion ) is not None:   
            count=count+1
            my_dict[i.second_companion]=count
    num=   my_dict[student.second_companion]

    response_data += "num : {}\n".format(num)
   
    return HttpResponse(response_data, content_type="text/plain; charset=utf-8")
    
@api_view(['GET'])
def guests(request, id):
    student = Invite.objects.filter(student_id=id).last()
    response_data = "invite info:\n"
    response_data += "name: {}\n".format(student.name)
    response_data += "position: {}\n".format(student.position)
    my_dict={}
    my_list=list(Invite.objects.all())
    count=0
    for i in my_list:
        count=count+1
        my_dict[i.name]=count
        
        if (i.first_companion) is not None :
            count=count+1
            my_dict[i.first_companion]=count
        if ( i.second_companion ) is not None:   
            count=count+1
            my_dict[i.second_companion]=count
    num=   my_dict[student.name]
    response_data += "num : {}\n".format(num)
    return HttpResponse(response_data, content_type="text/plain; charset=utf-8")

@api_view(['GET'])
def save_dict_to_excel(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=reservations(11 month).csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer=csv.writer(response)
    writer.writerow(["name","num"]  )

    my_dict={}
    my_list=list(Invite.objects.all())
    count=0
    for i in my_list:
        count=count+1
        my_dict[i.name+"{}".format(i.id)]=count
        
        if (i.first_companion) is not None :
            count=count+1
            my_dict[i.first_companion+"{}".format(i.id)]=[count,i.first_companion_number]
        if ( i.second_companion ) is not None:   
            count=count+1
            my_dict[i.second_companion+"{}".format(i.id)]=[count,i.second_companion_number]

    for name, data in my_dict.items():
        if isinstance(data, list):
            writer.writerow([str(name), str(data[0]), str(data[1])])
        else:
            writer.writerow([str(name), str(data)])

    
    return response
    
@api_view(['POST'])
def make_invite(request):
   data=request.data
   student_id = data["student_id"]
   student_name=data["student_name"]

   first_companion=data["first_companion"]
   second_companion=data["second_companion"]
   first_companion_number=data['first_companion_number']
   second_companion_number=data['second_companion_number']
   if Student.objects.filter(student_id=student_id).exists()==False:
        message={'error':'المعلومات التي ادخلتها غير صحيحة'}
        return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST,safe=False)

   elif Invite.objects.filter(student_id=student_id).exists()==True  :
        message={'message':'لديك دعوة تم انشائها مسبقا'}
        return JsonResponse(message,safe=False)
    
   else:
    invite= Invite(student_id=student_id,
                              name=student_name,
                            #academic_level=academic_level,
                              first_companion=first_companion,
                              second_companion=second_companion,
                              first_companion_number=first_companion_number,
                              second_companion_number=second_companion_number,
                              position="student")


    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    url="http://127.0.0.1:8000/qrcode_app/students/{}/".format(student_id)
    qr.add_data(url)
    qr.make(fit=True)


    img_qr = qr.make_image(fill_color='#005b72', back_color=(255, 255, 255, 0))

    img_qr = img_qr.resize((600, 600))
  
    img_base = Image.open('blank_image.jpeg')


    x = int((img_base.width - img_qr.width) / 2)
    y = int((img_base.height - img_qr.height)/2 ) -150

    img_base.paste(img_qr, (x, y))
    draw = ImageDraw.Draw(img_base)
    font = ImageFont.truetype("alfont_com_NotoNaskhArabic-Regular.ttf", size=50)

    text ="{}".format(student_name)
    reshaped_text = arabic_reshaper.reshape(text) 
    text = get_display(reshaped_text)

    width = 500


    wrapped_text = textwrap.wrap(text, width=width)

  
    text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_text)

   
    x_center = img_base.width // 2
    y_center = img_base.height // 2

    y_start = y_center - (text_height // 2)

    for line in wrapped_text:

        line_width, line_height = draw.textsize(line, font=font)

     
        x_start = x_center - (line_width // 2)

       
        draw.text((x_start, y - text_height - 80), line,stroke_width = 2, font=font, fill='#005b72')


        y_start += line_height

    text = "طالبة"
    reshaped_text = arabic_reshaper.reshape(text) 
    text = get_display(reshaped_text)
    text_width, text_height = draw.textsize(text, font)
    draw.text((x + 250, y - text_height ), text,stroke_width = 1, font=font, fill='#005b72')


    s = shortuuid.ShortUUID(alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
    otp = s.random(length=5)
    img_path = 'media/qr_code_image{}.jpg'.format(otp)
    img_base.save(img_path)

    invite.invite_image = img_path.split('/')[-1]
    invite.link1=url

  
    invite.save()

    if first_companion != "":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        url="http://127.0.0.1:8000/qrcode_app/guest1/{}/".format(student_id)
        qr.add_data(url)
        qr.make(fit=True)

        # إنشاء صورة QR
        img_qr = qr.make_image(fill_color='#005b72', back_color=(255, 255, 255, 0))

        img_qr = img_qr.resize((600, 600))
  
        img_base = Image.open('blank_image.jpeg')

      
        x = int((img_base.width - img_qr.width) / 2)
        y = int((img_base.height - img_qr.height)/2 ) -150

     
        img_base.paste(img_qr, (x, y))
        draw = ImageDraw.Draw(img_base)
        font = ImageFont.truetype("alfont_com_NotoNaskhArabic-Regular.ttf", size=50)

        text ="{}".format(first_companion)
        reshaped_text = arabic_reshaper.reshape(text) 
        text = get_display(reshaped_text)



        width = 500


        wrapped_text = textwrap.wrap(text, width=width)


        text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_text)

       
        x_center = img_base.width // 2
        y_center = img_base.height // 2

        y_start = y_center - (text_height // 2)

        for line in wrapped_text:
  
            line_width, line_height = draw.textsize(line, font=font)

        
            x_start = x_center - (line_width // 2)

          
            draw.text((x_start, y - text_height - 80), line,stroke_width = 2, font=font, fill='#005b72')

          
            y_start += line_height

        text = "ضيف"
        reshaped_text = arabic_reshaper.reshape(text) 
        text = get_display(reshaped_text)
        text_width, text_height = draw.textsize(text, font)
        draw.text((x + 250, y - text_height ), text,stroke_width = 1, font=font, fill='#005b72')

        s = shortuuid.ShortUUID(alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
        otp = s.random(length=5)
        img_path = 'media/qr_code_image_guest{}.jpg'.format(otp)
        img_base.save(img_path)

        invite.first_companion_invite_image = img_path.split('/')[-1]
        invite.link2=url

    
        invite.save()
    if second_companion != "":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        url="http://127.0.0.1:8000/qrcode_app/guest2/{}/".format(student_id)
        qr.add_data(url)
        qr.make(fit=True)


        img_qr = qr.make_image(fill_color='#005b72', back_color=(255, 255, 255, 0))

        img_qr = img_qr.resize((600, 600))
  
        img_base = Image.open('blank_image.jpeg')

    
        x = int((img_base.width - img_qr.width) / 2)
        y = int((img_base.height - img_qr.height)/2 ) -150

    
        img_base.paste(img_qr, (x, y))
        draw = ImageDraw.Draw(img_base)
        font = ImageFont.truetype("alfont_com_NotoNaskhArabic-Regular.ttf", size=50)

        text ="{}".format(second_companion)
        reshaped_text = arabic_reshaper.reshape(text) 
        text = get_display(reshaped_text)


        width = 500


        wrapped_text = textwrap.wrap(text, width=width)


        text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_text)


        x_center = img_base.width // 2
        y_center = img_base.height // 2

        y_start = y_center - (text_height // 2)

        for line in wrapped_text:
 
            line_width, line_height = draw.textsize(line, font=font)

           
            x_start = x_center - (line_width // 2)

         
            draw.text((x_start, y - text_height - 80), line,stroke_width = 2, font=font, fill='#005b72')

       
            y_start += line_height
        

        text = "ضيف"
        reshaped_text = arabic_reshaper.reshape(text) 
        text = get_display(reshaped_text)
        text_width, text_height = draw.textsize(text, font)
        draw.text((x + 250, y - text_height ), text,stroke_width = 1, font=font, fill='#005b72')
        

        s = shortuuid.ShortUUID(alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
        otp = s.random(length=5)
        img_path = 'media/qr_code_image_guest{}.jpg'.format(otp)
        img_base.save(img_path)

        invite.second_companion_invite_image = img_path.split('/')[-1]
        invite.link3=url

    
        invite.save()


    
    message={'message':'تم انشاء الدعوة بنجاح'}
    return JsonResponse(message, safe=False)

@api_view(['POST'])
def make_special_invite(request):
    data=request.data
    token=data['token']
    name=data['name']
    position=data['position']
    invite=Invite(student_id=token,
                  name=name,
                  position=position)
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    url="http://127.0.0.1:8000/qrcode_app/guests/{}/".format(token)
    qr.add_data(url)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color='#005b72', back_color=(255, 255, 255, 0))

    img_qr = img_qr.resize((600, 600))

    img_base = Image.open('blank_image.jpeg')


    x = int((img_base.width - img_qr.width) / 2)
    y = int((img_base.height - img_qr.height)/2 ) -150


    img_base.paste(img_qr, (x, y))
    draw = ImageDraw.Draw(img_base)
    font = ImageFont.truetype("alfont_com_NotoNaskhArabic-Regular.ttf", size=50)

    text ="{}".format(name)
    reshaped_text = arabic_reshaper.reshape(text) 
    text = get_display(reshaped_text)

    width = 500


    wrapped_text = textwrap.wrap(text, width=width)

 
    text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_text)

  
    x_center = img_base.width // 2
    y_center = img_base.height // 2

    y_start = y_center - (text_height // 2)

    for line in wrapped_text:

            line_width, line_height = draw.textsize(line, font=font)


            x_start = x_center - (line_width // 2)


            draw.text((x_start, y - text_height - 80), line,stroke_width = 2, font=font, fill='#005b72')


            y_start += line_height

    
    
    text = position
    reshaped_text = arabic_reshaper.reshape(text) 
    text = get_display(reshaped_text)


    width = 500

    wrapped_text = textwrap.wrap(text, width=width)


    text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_text)


    x_center = img_base.width // 2
    y_center = img_base.height // 2

    y_start = y_center - (text_height // 2)

    for line in wrapped_text:

            line_width, line_height = draw.textsize(line, font=font)

     
            x_start = x_center - (line_width // 2)


            draw.text((x_start, y - text_height - 5), line,stroke_width = 1, font=font, fill='#005b72')


            y_start += line_height



    s = shortuuid.ShortUUID(alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
    otp = s.random(length=5)
    img_path = 'media/qr_code_image{}.jpg'.format(otp)
    img_base.save(img_path)


    invite.invite_image = img_path.split('/')[-1]
    invite.link1=url

  
    invite.save()

    message={'message':'تم انشاء الدعوة بنجاح'}
    return JsonResponse(message, safe=False)

@api_view(['POST'])
def get_invite(request):
    data=request.data
    try:
        pk=data['p_id']
        inv=Invite.objects.filter(student_id=pk).last()
        serializer = InviteSerializer(inv, many=False)
        return Response(serializer.data)
    
    except:
        message = {'error': 'not found'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
