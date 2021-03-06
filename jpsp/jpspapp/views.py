# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from .models import Club, Post, Activity, Classroom, LostAndFound, UserProfile, CDUser, ActivityParticipantShip, \
    ClubMemberShip
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
import time


# Create your views here.

def student_check(username):
    try:
        if UserProfile.objects.get(UserObject__username=username):
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False


def admin_check(username):
    try:
        if CDUser.objects.get(UserObject__username=username):
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False


@require_http_methods(['GET'])
def index(request):
    template = loader.get_template('index/index.html')
    context = {'user': request.user}
    return HttpResponse(template.render(context, request))


@require_http_methods(['GET'])
def student_login_page(request):
    template = loader.get_template('index/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


@require_http_methods(['POST'])
def student_check_login(request):
    user_id = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=user_id, password=password)
    if user is not None:
        if(student_check(user_id)):
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("登陆失败啦")
    else:
        # todo: make a login error page
        return HttpResponse("登陆失败啦")


def admin_login_page(request):
    template = loader.get_template('manage/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def admin_check_login(request):
    # user_id is str
    user_id = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=user_id, password=password)
    # todo: finish the admin check login
    if user is not None:
        try:
            if CDUser.objects.get(UserName=user_id):
                login(request, user)
                return HttpResponseRedirect('/cd/')
        except:
            return HttpResponse("登陆失败啦")
    else:
        # todo: make a login error page
        return HttpResponse("登陆失败啦")


def admin_dashboard(request):
    # todo: finish the dashboard
    template = loader.get_template('manage/dashboard.html')
    content = {}
    return HttpResponse(template.render(content, request))


def student_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


@require_http_methods(['POST'])
def student_check_club_establish(request):
    try:
        clubname = request.POST['Clubname']
        shezhang_name = request.POST['Shezhang_Name']
        shezhang_qq = request.POST['Shezhang_QQ']
        shezhang_grade = request.POST['Shezhang_Grade']
        shezhang_classroom = request.POST['Shezhang_Classroom']
        introduction = request.POST['Introduction']
        if_recruit = request.POST['IfRecruit']
        qq_group = request.POST['QQGroup']
        email = request.POST['Email']
        Club.objects.create(
            Clubname=clubname,
            # TODO: ClubId
            ShezhangName=shezhang_name,
            SheZhangQq=shezhang_qq,
            ShezhangGrade=shezhang_grade,
            ShezhangClassroom=shezhang_classroom,
            IfRecruit=if_recruit,
            Introduction=introduction,
            Email=email,
            # TODO: label!
            State=False,
            Achievements="",
            Stars=0,
            EnrollGroupQq=qq_group,
        )
        return HttpResponse("Success")
    except:
        return HttpResponse("Error")


# 学生 社团列表
# Fix the unordered problem
# Fixed by add class Meta to the model Club 2018-02-08 2:26PM by Harvey Qiu
def student_club_list(request, page):
    club_object = Club.objects.filter(State=True)
    paginator = Paginator(club_object, 12)
    # paginator is a new Paginator
    template = loader.get_template('index/club/list.html')
    context = {
        'club_list': paginator.get_page(page), 'is_authenticated': False
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['user_id'] = request.user.username
    return HttpResponse(template.render(context, request))


@login_required(login_url='/s/login')
def student_club_establish(request):
    context = {}
    template = loader.get_template('index/club/establish.html')
    return HttpResponse(template.render(context, request))


@require_http_methods(['POST'])
@login_required(login_url='/s/login')
def student_club_attend(request):
    club_id = request.POST['ClubId']
    user_id = request.user.username
    userprofile = UserProfile.objects.get(UserObject__username=user_id)
    ClubMemberShip.objects.create(Club=Club.objects.get(ClubId=club_id), Member=userprofile)
    return HttpResponse("Success")


@login_required(login_url='/s/login')
@require_http_methods(['POST'])
def student_club_quit(request):
    try:
        user_id = request.POST['UserId']
        club_id = request.POST['ClubId']
    except:
        return HttpResponse("Error")


@login_required(login_url='/c/login')
def club_member_list(request):
    template = loader.get_template('club/member/list.html')
    club_member_ship_list = ClubMemberShip.objects.filter(Club__ClubObject__username=request.user.username)
    content = {
        'club_member_ship_list': club_member_ship_list
    }
    return HttpResponse(template.render(content, request))


# @require_http_methods(['POST'])
# def recruit_classroom_apply(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         club_id = body['ClubId']
#         club_name = body['ClubName']
#         date1 = body['Date1']
#         date2 = body['Date2']
#         # TODO: deal with date
#         Classroom.objects.create(
#             ClassroomId=0,
#             ClubId=Club.objects.get(User.objects.get(username=club_id)),
#             ClubName=club_name,
#             Date1=date1,
#             Date2=date2
#         )
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def recruit_classroom_operate(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         classroom = body['Classroom']
#         clubid = body['ClubId']
#         # date
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def recruit_classroom_list(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         type = body['Type']
#         response = []
#         if type == 'Confirmed':
#             pass
#         elif type == 'Denied':
#             pass
#         elif type == 'Unconfirmed':
#             pass
#         elif type == 'All':
#             classroom_objects_set = Classroom.objects.all()
#             # TODO: !!!!!!!
#             for classroom in classroom_objects_set:
#                 response.append({})
#         response_json = json.dumps(response)
#     except:
#         return 0

# @require_http_methods(['POST'])
# def club_member_remove(request):
#     try:
#         body = json.loads(request.body)
#         token = body['token']
#         # club_id -> example: '303'
#         club_id = body['ClubId']
#         # username -> example: 'S320150181'
#         user_id = body['UserId']
#         if (token_authenticate(user_id=club_id, token=token)):
#             ClubMemberShip.objects.get(Club=Club.objects.get(ClubId=club_id), Member=UserProfile.objects.get(
#                 UserObject=User.objects.get(username=user_id))).delete()
#             return JsonResponse({
#                 'message': 'success',
#                 'Access-Control-Allow-Origin': '*'
#             })
#         else:
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_apply(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         club_id = body['ClubId']
#         activity_name = body['Name']
#         region = body['Region']
#         date1 = body['Date1']
#         date2 = body['Date2']
#         content = body['Content']
#         type = body['Type']
#         Activity.objects.create(
#             ActivityName=activity_name,
#             Region=region,
#             Clubid=Club.objects.get(clubid=User.objects.get(username=club_id)),
#             ClubName=Club.objects.get(clubid=User.objects.get(username=club_id)).ClubName,
#             Content=content,
#             Date1=date1,
#             Date2=date2,
#             State='0',
#             Type=type
#         )
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_attend(requset):
#     try:
#         body = json.loads(requset.body)
#
#         # token = body['Token']
#         # activity_id -> int
#         activity_id = body['ActivityId']
#         # user_id -> str
#         user_id = body['UserId']
#         ActivityParticipantShip.objects.create(Activity=Activity.objects.get(pk=activity_id),
#                                                Participant=UserProfile.objects.get(
#                                                    UserObject=User.objects.get(username=user_id)))
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_detail(request):
#     try:
#         body = json.loads(request.body)
#         # activity_id -> int
#         activity_id = body['ActivityId']
#         activity = Activity.objects.get(pk=1)
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*',
#             'data': {
#                 'Name': activity.Name,
#                 'Region': activity.Region,
#                 'ClubName': activity.ClubObject.ClubName,
#                 'Content': activity.Content,
#                 'Date1': str(activity.Date1),
#                 'Date2': str(activity.Date2),
#             }
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_operate(request):
#     try:
#         body = json.loads(request.body)
#         token = body['token']
#         activity_id = body['ActivityId']
#         operation = body['Operation']
#         if operation == 'Confirm':
#             try:
#                 activity_object = Activity.objects.get(pk=activity_id)
#                 activity_object.State = 'Confirmed'
#                 activity_object.save()
#                 return JsonResponse({
#                     'message': 'success',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#             except:
#                 return JsonResponse({
#                     'message': 'error',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#         elif operation == 'UndoDeny':
#             try:
#                 activity_object = Activity.objects.get(pk=activity_id)
#                 activity_object.State = 'Unconfirmed'
#                 activity_object.save()
#             except:
#                 return JsonResponse({
#                     'message': 'error',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#         elif operation == 'Deny':
#             try:
#                 activity_object = Activity.objects.get(pk=activity_id)
#                 activity_object.State = 'Denied'
#                 activity_object.save()
#             except:
#                 return JsonResponse({
#                     'message': 'error',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_list(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         type = body['Type']
#         response = []
#         activityList = None
#         if type == 'All':
#             activityList = Activity.objects.all()
#         elif type == 'Past':
#             activityList = Activity.objects.filter(Date2__lt=datetime.datetime.now())
#         elif type == 'Happening':
#             activityList = Activity.objects.filter(Date1__lte=datetime.datetime.now()).filter(
#                 Date2__gte=datetime.datetime.now())
#         elif type == 'Future':
#             activityList = Activity.objects.filter(Date1__gt=datetime.datetime.now())
#         elif type == 'Unconfirmed':
#             activityList = Activity.objects.filter(State='0')
#         elif type == 'Confirmed':
#             activityList = Activity.objects.filter(State='1')
#         elif type == 'Denied':
#             activityList = Activity.objects.filter(State='2')
#         # TODO : token authenticate
#         for data in activityList:
#             response.append({
#                 'ActivityId': data.pk,
#                 'Name': data.Name,
#                 'Region': data.Region,
#                 # 'ClubId': data.ClubId,
#                 'ClubName': data.ClubName,
#                 'Content': data.Content,
#                 'Date1': str(data.Date1),
#                 'Date2': str(data.Date2),
#                 'State': data.State,
#                 'Type': data.Type
#             })
#         response_json = json.dumps(response)
#         return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
#                             safe=False)
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(["POST"])
# def laf_submit(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         lostOrFound = body['LostOrFound']
#         objectName = body['ObjectName']
#         linkmanName = body['LinkmanName']
#         linkmanGrade = body['LinkmanGrade']
#         linkmanPhoneNumber = body['LinkmanPhoneNumber']
#         linkmanClass = body['LinkmanClass']
#         linkmanQq = body['LinkmanQq']
#         region = body['Region']
#         date1 = body['Date1']
#         importance = body['Importance']
#         desc = body['Desc']
#         try:
#             LostAndFound.objects.create(
#                 LostOrFound=lostOrFound,
#                 LinkmanName=linkmanName,
#                 LinkmanGrade=linkmanGrade,
#                 LinkmanClassroom=linkmanClass,
#                 LinkmanPhoneNumber=linkmanPhoneNumber,
#                 LinkmanQq=linkmanQq,
#                 LostObjectName=objectName,
#                 LostPlace=region,
#                 Importance=importance,
#                 Desc=desc,
#                 LostDateTime=date1
#             )
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#         except:
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(["POST"])
# def laf_list(request):
#     try:
#         body = json.loads(request.body)
#         type = body['Type']
#         response = []
#         LostAndFoundList = None
#         if type == 'Lost':
#             LostAndFoundList = LostAndFound.objects.filter()
#             # TODO: filter
#         elif type == 'Found':
#             LostAndFoundList = LostAndFound.objects.all()
#             # TODO: filter
#         elif type == 'Past':
#             LostAndFoundList = LostAndFound.objects.all()
#             # TODO: filter
#         elif type == 'All':
#             LostAndFoundList = LostAndFound.objects.all()
#         for data in LostAndFoundList:
#             response.append({
#                 'LostorFound': data.LostOrFound,
#                 'ObjectName': data.LostObjectName,
#                 'LinkmanGrade': data.LinkmanGrade,
#                 'LinkmanClass': data.LinkmanClass,
#                 'LinkmanPhoneNumber': data.LinkmanPhoneNumber,
#                 'LinkmanQq': data.LinkmanQq,
#                 'LinkmanName': data.LinkmanName,
#                 'Region': data.LostPlace,
#                 'Date1': data.LostDateTime,
#                 'Importance': data.Importacne,
#                 'Desc': data.Desc
#             })
#         response_json = json.dumps(response)
#         return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
#                             safe=False)
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


def student_club_detail(request, club_id):
    club = Club.objects.get(ClubId=club_id)
    template = loader.get_template('index/club/detail.html')
    content = {'Club': club}
    return HttpResponse(template.render(content, request))


def student_club_news(request, club_id):
    # todo: finish the function
    profile = Club.objects.get(ClubId=club_id)
    template = loader.get_template('index/club/detail.html')
    content = {}
    return HttpResponse(template.render(content, request))


def club_login_page(request):
    template = loader.get_template('club/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


@require_http_methods(['POST'])
def club_check_login(request):
    user_id = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=user_id, password=password)
    if user is not None:
        try:
            if Club.objects.get(ClubId=user_id, State=True):
                login(request, user)
                return HttpResponseRedirect('/c/dashboard')
        except ObjectDoesNotExist:
            return HttpResponse("登陆失败啦")
    else:
        # todo: make a login error page
        return HttpResponse("登陆失败啦")


@login_required(login_url='c/login')
def club_dashboard_index(request):
    template = loader.get_template('club/dashboard/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='c/login')
def club_post_add(request):
    template = loader.get_template('club/post/add.html')
    context = {'ClubId': request.user.username}
    return HttpResponse(template.render(context, request))


def club_logout(request):
    logout(request)
    return HttpResponseRedirect("/c/login")

@require_http_methods(['POST'])
@login_required(login_url='c/login')
def club_post_add_check(r):
    Post.objects.create(LinkmanGrade=r.POST['LinkmanGrade'], LinkmanClass=r.POST['LinkmanClass'],
                        LinkmanName=r.POST['LinkmanName'], LinkmanPhoneNumber=r.POST['LinkmanPhone'],
                        LinkmanQq=r.POST['LinkmanQQ'], Region=r.POST['Region'], Process=r.POST['Process'],
                        Content=r.POST['Content'], Assessment=r.POST['Assessment'], Feeling=r.POST['Feeling'],
                        ClubObject=Club.objects.get(ClubId=r.user.username),
                        Date=r.POST['Date'], Time=r.POST['Time'])
    return HttpResponse("成功提交社团记录")


@require_http_methods(["POST"])
def club_profile_update(request):
    body = request.POST
    shezhang_name = body['shezhang_name']
    shezhang_qq = body['shezhang_qq']
    shezhang_grade = body['shezhang_grade']
    shezhang_class = body['shezhang_class']
    if_recruit = body['if_recruit']
    enroll_group_qq = body['enroll_group_qq']
    email = body['email']
    label = body['label']
    state = body['state']
    introduction = body['introduction']
    achievements = body['achievements']
    club_object = Club.objects.get(ClubId=body['clubid'])
    club_object.ClubName = body['clubname']
    club_object.ShezhangName = shezhang_name
    club_object.ShezhangGrade = shezhang_grade
    club_object.ShezhangClassroom = shezhang_class
    club_object.ShezhangQq = shezhang_qq
    club_object.IfRecruit = if_recruit
    club_object.EnrollGroupQq = enroll_group_qq
    club_object.Email = email
    club_object.Label = label
    club_object.State = state
    club_object.Introduction = introduction
    club_object.Achievements = achievements
    club_object.save()
    return HttpResponse()

@require_http_methods(["POST"])
def event_submit(request):
    pass


def admin_event_list(request, page):
    template = loader.get_template('manage/event/list.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_file_upload(request):
    template = loader.get_template('manage/file/upload.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_file_upload_list(request):
    template = loader.get_template('manage/file/upload_list.html')
    context = {}
    return HttpResponse(template.render(context, request))


#
def admin_file_download_list(request):
    template = loader.get_template('manage/file/download_list.html')
    context = {}
    return HttpResponse(template.render(context, request))


def club_file_upload(request):
    template = loader.get_template('club/file/upload.html')
    content = {}
    return HttpResponse(template.render(content, request))


def club_file_upload_list(request):
    template = loader.get_template('club/file/upload_list.html')
    content = {}
    return HttpResponse(template.render(content, request))


@require_http_methods(['POST'])
def club_file_download_list(request):
    template = loader.get_template('club/file/download_list.html')
    content = {}
    return HttpResponse(template.render(content, request))


@login_required(login_url='/s/login')
@user_passes_test(student_check)
def student_dashboard_index(request):
    template = loader.get_template('index/dashboard/index.html')
    user_profile = UserProfile.objects.get(UserObject__username=request.user.username)
    content = {
        'user_id':request.user.username,
        'realname':user_profile.UserName,
        'is_authenticated': True
    }
    return HttpResponse(template.render(content, request))


@login_required(login_url='/s/login')
@user_passes_test(student_check)
def student_dashboard_clubs(request):
    membership_list = ClubMemberShip.objects.filter(Member__UserObject__username=request.user.username)
    template = loader.get_template('index/dashboard/clubs.html')
    content = {
        'list': membership_list,
        'is_authenticated': True,
        'user_id':request.user.username
    }
    return HttpResponse(template.render(content, request))


@login_required(login_url='/s/login')
@user_passes_test(student_check)
def student_dashboard_activities(request):
    template = loader.get_template('index/dashboard/activities.html')
    content = {
        'is_authenticated': True,
        'user_id': request.user.username
    }
    return HttpResponse(template.render(content, request))


@login_required(login_url='/s/login')
@user_passes_test(student_check)
def student_dashboard_password(request):
    template = loader.get_template('index/dashboard/password.html')
    context = {
        'is_authenticated': True,
        'user_id': request.user.username
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/cd/login')
def admin_student_list(request):
    template = loader.get_template('manage/student/list.html')
    content = {
        'is_authenticated': True,
    }
    return HttpResponse(template.render(content, request))


@login_required(login_url='/cd/login')
def admin_student_detail(request):
    template = loader.get_template('manage/student/detail.html')
    content = {}
    return HttpResponse(template.render(content, request))


@login_required(login_url='/cd/login')
def admin_post_list(request, page):
    template = loader.get_template('manage/post/list.html')
    paginator = Paginator(Post.objects.all().order_by('-id'), 20)
    context = {
        'posts': paginator.get_page(page)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/cd/login')
def admin_post_detail(request, post_id):
    template = loader.get_template('manage/post/detail.html')
    context = {'post': Post.objects.get(id=post_id)}
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url='/cd/login')
def admin_post_star(request):
    post_id = request.POST['PostId']
    stars = request.POST['Stars']
    post_object = Post.objects.get(id=int(post_id))
    post_object.Stars = float(stars)
    print(type(stars))
    post_object.save()
    # todo: prettify the star success page
    return HttpResponse("打分成功")


@staff_member_required(login_url='/cd/login')
def admin_club_list(request):
    template = loader.get_template('manage/club/list.html')
    context = {}
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template('index/about.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    template = loader.get_template('index/contact.html')
    return HttpResponse(template.render({}, request))
