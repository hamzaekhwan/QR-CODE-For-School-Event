from rest_framework.response import Response
from qrcode_app.models import *
from rest_framework.views import *
from rest_framework.decorators import *
from rest_framework.response import *

from qrcode_app.serializers import  *
from .models import *
import shortuuid
import os
import qrcode
from PIL import Image


@api_view(['POST'])
def make_invite(request):
    data=request.data
    student_id = data["student_id"]
    student_name=data["student_name"]
    academic_level=data["academic_level"]
    first_companion=data["first_companion"]
    second_companion=data["second_companion"]
    if Student.objects.filter(student_id=student_id).exists()==False:
        message={'error':'this id student is not found'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    elif Invite.objects.filter(student_id=student_id).exists()==True  :
        message={'error':'this id is already registerd'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    else:
       invite= Invite(student_id=student_id,
                              student_name=student_name,
                              academic_level=academic_level,
                              first_companion=first_companion,
                              second_companion=second_companion)


    # إنشاء رمز QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data('https://www.google.com')
    qr.make(fit=True)

    # إنشاء صورة QR
    img_qr = qr.make_image(fill_color='#005b72', back_color=(255, 255, 255, 0))

    img_qr = img_qr.resize((700, 700))
    # فتح الصورة الأساسية
    img_base = Image.open('blank_image.jpeg')

    # حساب موقع البداية لوضع رمز QR في الصورة الأساسية
    x = int((img_base.width - img_qr.width) / 2)
    y = int((img_base.height - img_qr.height)/2 ) -200

    # وضع رمز QR في الصورة الأساسية
    img_base.paste(img_qr, (x, y))

    # حفظ الصورة النهائية

    s = shortuuid.ShortUUID(alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
    otp = s.random(length=5)
    img_path = 'media/qr_code_image{}.jpg'.format(otp)
    img_base.save(img_path)

    # تعيين الصورة النهائية لخاصية invite_image في كائن invite
    invite.invite_image = img_path.split('/')[-1]

  
    invite.save()

    
    return Response("invite sent successfully")


@api_view(['GET'])
def get_invite(request, pk):
    try:
        inv=Invite.objects.filter(student_id=pk)[0]
        serializer = InviteSerializer(inv, many=False)
        return Response(serializer.data)
    
    except:
        message = {'error': 'not found'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
