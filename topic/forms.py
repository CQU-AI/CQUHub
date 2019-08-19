from django import forms


class PubTopic(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "textinput textInput form-control"}),
    )

    theme = (
        ("那个谁，我想对你说", "那个谁，我想对你说"),
        ("动手动脚找东西", "动手动脚找东西"),
        ("CQU公告", "CQU公告"),
        ("CQU身边事", "CQU身边事"),
        ("技术栏目", "技术栏目"),
        ("文学交流", "文学交流"),
        # ('comments', '论坛公告'),
    )

    node = forms.ChoiceField(
        choices=theme, widget=forms.Select(attrs={"class": "select form-control"})
    )
    choices = (("不匿名", "不匿名"), ("匿名", "匿名"))

    ifAnony = forms.ChoiceField(
        choices=choices, widget=forms.Select(attrs={"class": "select form-control"})
    )

    content_raw = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "pagedownwidget form-control wmd-input",
                "cols": "40",
                "rows": "10",
            }
        )
    )


class Comment_Forms(forms.Form):
    content_raw = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "pagedownwidget form-control wmd-input",
                "cols": "40",
                "rows": "10",
            }
        )
    )


class Postmodify_Forms(forms.Form):
    content_raw = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "pagedownwidget form-control wmd-input",
                "cols": "40",
                "rows": "10",
            }
        )
    )
