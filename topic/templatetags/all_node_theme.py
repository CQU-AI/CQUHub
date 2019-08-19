from django import template

register = template.Library()


@register.simple_tag
def all_node_theme(value):
    reservedict1 = {
        "那个谁，我想对你说": "1",
        "动手动脚找东西": "2",
        "CQU公告": "3",
        "CQU身边事": "4",
        "技术栏目": "5",
        "文学交流": "6",
        "论坛公告": "7",
    }

    node_id = reservedict1[value]
    return node_id
