# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from user.models import User_Info
from .models import Create_Topic
from .forms import PubTopic, Comment_Forms, Postmodify_Forms
from operation.models import Topic_Comment
import markdown
from itertools import chain

# Create your views here.


class Index_View(View):
    """
    查看所有主题标题
    """

    def get(self, request, page_id):
        topic_list1 = Create_Topic.objects.filter(top="置顶").order_by("-pub_time")
        topic_list2 = Create_Topic.objects.filter(top="不置顶").order_by("-pub_time")
        for i in topic_list1:
            print(i, "=" * 100)
        for i in topic_list2:
            print(i, "=" * 100)
        topic_list = list(topic_list1) + list(topic_list2)
        # topic_list = topic_list1 | topic_list2
        # topic_list = Create_Topic.objects.all().order_by("-pub_time")
        paginator = Paginator(topic_list, 8)
        page_range = paginator.page_range
        page = request.GET.get(page_id)
        pre_id = page_id - 1
        next_id = page_id + 1
        if page_id == 1:
            pre_id = 1
        if page_id == len(page_range):
            next_id = page_id
            pre_id = page_id - 1
        try:
            topics = paginator.page(page_id)
        except PageNotAnInteger:
            topics = paginator.page(1)
        except EmptyPage:
            topics = []
        return render(
            request,
            "topic/base.html",
            {
                "topics": topics,
                "page_id": page_id,
                "next_id": next_id,
                "pre_id": pre_id,
            },
        )


class PubTopic_View(View):
    """
    发布主题
    """

    def get(self, request, username):
        forms = PubTopic()
        return render(request, "topic/create_topic.html", {"forms": forms})

    def post(self, request, username):
        forms = PubTopic(request.POST)
        if forms.is_valid():
            node = forms.cleaned_data["node"]
            title = forms.cleaned_data["title"]
            ifAnony = forms.cleaned_data["ifAnony"]
            # ifAnony = forms.cleaned_data["ifAnony"]
            if Create_Topic.objects.filter(title=title).exists():
                return render(
                    request,
                    "topic/create_topic.html",
                    {"forms": forms, "message": "该标题已经存在,请换一个标题"},
                )
            content = forms.cleaned_data["content_raw"]
            content = content.replace("<", " &lt;")
            content = content.replace(">", "&gt;")
            topic = Create_Topic()
            topic.user = User_Info.objects.get(username=username)
            topic.title = title
            topic.node = node
            topic.content = content
            topic.ifAnony = ifAnony
            topic.save()
            return redirect(to="topic:index")
        else:
            return render(
                request,
                "topic/create_topic.html",
                {"forms": forms, "message": "输入的数据无法通过检查，请重新输入"},
            )


class Topic_Content_View(View):
    """
    文章详细内容展示
    """

    def get(self, request, content_id):
        forms = Comment_Forms()
        topic_content = Create_Topic.objects.get(id=content_id)
        time = topic_content.pub_time
        title = topic_content.title
        name = topic_content.user.username
        node = topic_content.node
        nickname = topic_content.user.nickname
        get_id = {
            "那个谁，我想对你说": "1",
            "动手动脚找东西": "2",
            "CQU公告": "3",
            "CQU身边事": "4",
            "技术栏目": "5",
            "文学交流": "6",
            "论坛公告": "7",
        }
        theme_id = get_id[node]
        ifAnony = topic_content.ifAnony
        content = markdown.markdown(
            topic_content.content,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
                "markdown.extensions.toc",
            ],
        )

        comment = topic_content.topic_comment_set.all().order_by("-add_time")
        len_comment = len(comment)
        for each_comment in comment:
            markdown_comment = markdown.markdown(
                each_comment.content,
                extensions=[
                    "markdown.extensions.extra",
                    "markdown.extensions.codehilite",
                    "markdown.extensions.toc",
                ],
            )
            each_comment.content = markdown_comment

        return render(
            request,
            "topic/topic_content.html",
            {
                "content_topic": topic_content,
                "time": time,
                "title": title,
                "name": name,
                "content": content,
                "node": node,
                "ifAnony": ifAnony,
                "forms": forms,
                "comment": comment,
                "len_comment": len_comment,
                "theme_id": theme_id,
                "nickname": nickname,
            },
        )


class Topic_Content_View1(View):
    """
    文章详细内容展示
    """

    def get(self, request, content_id, page_id):
        forms = Comment_Forms()
        topic_content = Create_Topic.objects.get(id=content_id)
        time = topic_content.pub_time
        title = topic_content.title
        name = topic_content.user.username
        node = topic_content.node
        get_id = {
            "那个谁，我想对你说": "1",
            "动手动脚找东西": "2",
            "CQU公告": "3",
            "CQU身边事": "4",
            "技术栏目": "5",
            "文学交流": "6",
            "论坛公告": "7",
        }
        theme_id = get_id[node]
        ifAnony = topic_content.ifAnony
        content = markdown.markdown(
            topic_content.content,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
                "markdown.extensions.toc",
            ],
        )

        comment_list = topic_content.topic_comment_set.all().order_by("-add_time")
        paginator = Paginator(comment_list, 8)
        page_range = paginator.page_range
        page = request.GET.get(page_id)
        pre_id = page_id - 1
        next_id = page_id + 1
        if page_id == 1:
            pre_id = 1
        if page_id == len(page_range):
            next_id = page_id
            pre_id = page_id - 1
        try:
            comment = paginator.page(page_id)
        except PageNotAnInteger:
            comment = paginator.page(1)
        except EmptyPage:
            comment = []
        len_comment = len(comment_list)
        for each_comment in comment:
            markdown_comment = markdown.markdown(
                each_comment.content,
                extensions=[
                    "markdown.extensions.extra",
                    "markdown.extensions.codehilite",
                    "markdown.extensions.toc",
                ],
            )
            each_comment.content = markdown_comment

        return render(
            request,
            "topic/topic_content.html",
            {
                "content_topic": topic_content,
                "time": time,
                "title": title,
                "name": name,
                "content": content,
                "node": node,
                "ifAnony": ifAnony,
                "forms": forms,
                "comment": comment,
                "len_comment": len_comment,
                "theme_id": theme_id,
                "content_id": content_id,
                "page_id": page_id,
                "next_id": next_id,
                "pre_id": pre_id,
            },
        )


"""
    def  post(self,request,content_id):

        topic=Create_Topic.objects.get(id=content_id)
        login_user=User_Info.objects.get(username=request.user.username)
        forms=Comment_Forms(request.POST)
        if  forms.is_valid():
            comment_content=forms.cleaned_data["content_raw"]
            comment=Topic_Comment()
            comment.user=login_user
            comment.topic=topic
            comment.content=comment_content
            comment.save()

            return  render(request,'topic/topic_content.html',{'comment':comment,'forms':forms,'content_id':content_id})

"""


def default_index(request):
    return redirect(to="page/1")


"""
redirect
可传递的参数：
一个模型对象：这个模型的get_absolute_url() 会被调用。
一个视图名称，可带参数，该视图会被反向生成。
一个绝对路径或相对路径，用作反向定位。
"""


class Theme1_View(View):
    def get(self, request, theme_id):
        reservedict = {
            "1": "那个谁，我想对你说",
            "2": "动手动脚找东西",
            "3": "CQU公告",
            "4": "CQU身边事",
            "5": "技术栏目",
            "6": "文学交流",
            "7": "论坛公告",
        }

        node_id = reservedict[str(theme_id)]
        themes = Create_Topic.objects.filter(node=node_id)
        return render(
            request,
            "topic_base.html",
            {"theme": themes, "theme_id": theme_id, "node_id": node_id},
        )


class Theme2_View(View):
    def get(self, request, theme_id, page_id):
        reservedict = {
            "1": "那个谁，我想对你说",
            "2": "动手动脚找东西",
            "3": "CQU公告",
            "4": "CQU身边事",
            "5": "技术栏目",
            "6": "文学交流",
            "7": "论坛公告",
        }
        node_id = reservedict[str(theme_id)]
        theme2 = Create_Topic.objects.filter(node=node_id)

        pre_id = page_id - 1
        next_id = page_id + 1
        paginator = Paginator(theme2, 8)
        page_range = paginator.page_range
        if page_id == 1:
            pre_id = 1
        if page_id == len(page_range):
            next_id = page_id
            pre_id = page_id - 1
        try:
            themes = paginator.page(page_id)
        except PageNotAnInteger:
            themes = paginator.page(1)
        except EmptyPage:
            themes = []
        return render(
            request,
            "topic_base.html",
            {
                "node_id": node_id,
                "theme": themes,
                "theme_id": (theme_id),
                "page_id": page_id,
                "next_id": next_id,
                "pre_id": pre_id,
            },
        )


def Go_Page(request):
    try:
        page_id = int(request.GET.get("go_page"))
    except:
        page_id = int(request.GET.get("cur_page"))
    topic_list = Create_Topic.objects.all().order_by("-pub_time")
    paginator = Paginator(topic_list, 8)
    page_range = paginator.page_range
    max = len(page_range)
    if page_id > max or page_id < 1:
        page_id = int(request.GET.get("cur_page"))
    pre_id = page_id - 1
    next_id = page_id + 1
    if page_id == 1:
        pre_id = 1
    if page_id == len(page_range):
        next_id = page_id
        pre_id = page_id - 1
    try:
        topics = paginator.page(page_id)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = []
    return render(
        request,
        "topic/base.html",
        {"topics": topics, "page_id": page_id, "next_id": next_id, "pre_id": pre_id},
    )


def Go_theme_Page(request, theme_id):
    reservedict = {
        "1": "那个谁，我想对你说",
        "2": "动手动脚找东西",
        "3": "CQU公告",
        "4": "CQU身边事",
        "5": "技术栏目",
        "6": "文学交流",
        "7": "论坛公告",
    }
    node_id = reservedict[str(theme_id)]
    theme2 = Create_Topic.objects.filter(node=node_id)
    try:
        page_id = int(request.GET.get("go_theme_page"))
    except:
        page_id = int(request.GET.get("cur_page"))
    paginator = Paginator(theme2, 8)
    page_range = paginator.page_range
    max = len(page_range)
    if page_id > max or page_id < 1:
        page_id = int(request.GET.get("cur_page"))
    pre_id = page_id - 1
    next_id = page_id + 1
    if page_id == 1:
        pre_id = 1
    if page_id == len(page_range):
        next_id = page_id
        pre_id = page_id - 1
    try:
        themes = paginator.page(page_id)
    except PageNotAnInteger:
        themes = paginator.page(1)
    except EmptyPage:
        themes = []
    return render(
        request,
        "topic_base.html",
        {
            "theme": themes,
            "theme_id": (theme_id),
            "page_id": page_id,
            "next_id": next_id,
            "pre_id": pre_id,
        },
    )


def search1(request, page_id):

    nvkeywords = str(request.GET.get("nvkeywords"))
    if nvkeywords != "":
        error_msg = ""
        topic_list = Create_Topic.objects.filter(title__icontains=nvkeywords)
        # topic_list = Create_Topic.objects.all().order_by("-pub_time")
        # print(len(post_list))

    else:
        error_msg = "请输入搜索内容!"
        topic_list = []

    paginator = Paginator(topic_list, 8)
    page_range = paginator.page_range

    max = len(page_range)
    if page_id > max:
        page_id = int(request.GET.get("cur_page"))
    pre_id = page_id - 1
    next_id = page_id + 1
    if page_id == 1:
        pre_id = 1
    if page_id == len(page_range):
        next_id = page_id
        pre_id = page_id - 1
    try:
        topic_list = paginator.page(page_id)
    except PageNotAnInteger:
        topic_list = paginator.page(1)
    except EmptyPage:
        topic_list = []

    return render(
        request,
        "search_base.html",
        {
            "error_msg": error_msg,
            "keywords": nvkeywords,
            "topic_list": topic_list,
            "page_id": page_id,
            "next_id": next_id,
            "pre_id": pre_id,
        },
    )


def search2(request, page_id, keywords):

    keywords = str(keywords)
    topic_list = Create_Topic.objects.filter(title__icontains=keywords)
    # topic_list = Create_Topic.objects.all().order_by("-pub_time")
    # print(len(post_list))

    paginator = Paginator(topic_list, 8)
    page_range = paginator.page_range

    max = len(page_range)
    if page_id > max:
        page_id = int(request.GET.get("cur_page"))
    pre_id = page_id - 1
    next_id = page_id + 1
    if page_id == 1:
        pre_id = 1
    if page_id == len(page_range):
        next_id = page_id
        pre_id = page_id - 1
    try:
        topic_list = paginator.page(page_id)
    except PageNotAnInteger:
        topic_list = paginator.page(1)
    except EmptyPage:
        topic_list = []
    return render(
        request,
        "search_base.html",
        {
            "keywords": keywords,
            "topic_list": topic_list,
            "page_id": page_id,
            "next_id": next_id,
            "pre_id": pre_id,
        },
    )


def Go_Search_Page(request):

    keywords = str(request.GET.get("keywords"))
    try:
        page_id = int(request.GET.get("go_search_page"))
    except:
        page_id = int(request.GET.get("cur_page"))
    topic_list = Create_Topic.objects.filter(title__icontains=keywords)
    print(page_id)
    paginator = Paginator(topic_list, 8)
    page_range = paginator.page_range
    max = len(page_range)
    if page_id > max or page_id < 1:
        page_id = int(request.GET.get("cur_page"))
    pre_id = page_id - 1
    next_id = page_id + 1
    if page_id == 1:
        pre_id = 1
    if page_id == len(page_range):
        next_id = page_id
        pre_id = page_id - 1
    try:
        topic_list = paginator.page(page_id)
    except PageNotAnInteger:
        topic_list = paginator.page(1)
    except EmptyPage:
        topic_list = []

    return render(
        request,
        "search_base.html",
        {
            "keywords": keywords,
            "topic_list": topic_list,
            "page_id": page_id,
            "next_id": next_id,
            "pre_id": pre_id,
        },
    )


class delete_topic(View):
    def post(self, request, title1, name):
        Create_Topic.objects.filter(title=title1).delete()
        return redirect(to="/user/{}/".format(name))


class modifypage(View):
    def get(self, request, content_id):
        forms = Postmodify_Forms()
        topic_content = Create_Topic.objects.get(id=content_id)
        # forms.content_raw.widget.attrs.values = topic_content.content
        return render(
            request,
            "topic/topic_modify.html",
            {"content_id_aaa": content_id, "forms": forms},
        )


class topicmodify(View):
    def post(self, request, content_id):
        forms = Postmodify_Forms(request.POST)

        if forms.is_valid():
            content = forms.cleaned_data["content_raw"]
            content = content.replace("<", " &lt;")
            content = content.replace(">", "&gt;")
            Create_Topic.objects.filter(id=content_id).update(content=content)
            return redirect(to="topic:topic_content1", content_id=content_id, page_id=1)
        else:
            return render(
                request,
                "topic/topic_modify.html",
                {"forms": forms, "message": "输入的数据无法通过检查，请重新输入"},
            )


class Go_Comment_Page(View):
    def get(self, request, content_id):
        forms = Comment_Forms()
        topic_content = Create_Topic.objects.get(id=content_id)
        time = topic_content.pub_time
        title = topic_content.title
        name = topic_content.user.username
        node = topic_content.node
        get_id = {
            "那个谁，我想对你说": "1",
            "动手动脚找东西": "2",
            "CQU公告": "3",
            "CQU身边事": "4",
            "技术栏目": "5",
            "文学交流": "6",
            "论坛公告": "7",
        }
        theme_id = get_id[node]
        ifAnony = topic_content.ifAnony
        content = markdown.markdown(
            topic_content.content,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
                "markdown.extensions.toc",
            ],
        )

        try:
            page_id = int(request.GET.get("go_comment_page"))
        except:
            page_id = int(request.GET.get("cur_comment_page"))
        comment_list = topic_content.topic_comment_set.all().order_by("-add_time")
        paginator = Paginator(comment_list, 8)
        page_range = paginator.page_range
        max = len(page_range)
        if page_id > max:
            page_id = int(request.GET.get("cur_comment_page"))
        pre_id = page_id - 1
        next_id = page_id + 1
        if page_id == 1:
            pre_id = 1
        if page_id == len(page_range):
            next_id = page_id
            pre_id = page_id - 1
        try:
            comment = paginator.page(page_id)
        except PageNotAnInteger:
            comment = paginator.page(1)
        except EmptyPage:
            comment = []
        len_comment = len(comment_list)
        for each_comment in comment:
            markdown_comment = markdown.markdown(
                each_comment.content,
                extensions=[
                    "markdown.extensions.extra",
                    "markdown.extensions.codehilite",
                    "markdown.extensions.toc",
                ],
            )
            each_comment.content = markdown_comment

        return render(
            request,
            "topic/topic_content.html",
            {
                "content_topic": topic_content,
                "time": time,
                "title": title,
                "name": name,
                "content": content,
                "node": node,
                "ifAnony": ifAnony,
                "forms": forms,
                "comment": comment,
                "len_comment": len_comment,
                "theme_id": theme_id,
                "page_id": page_id,
                "next_id": next_id,
                "pre_id": pre_id,
                "content_id": content_id,
            },
        )
