# coding=utf-8
"""
    @project: maxkb
    @Author：虎
    @file： field_message.py
    @date：2024/3/1 14:30
    @desc:
"""
from django.utils.translation import gettext_lazy


class ErrMessage:
    @staticmethod
    def char(field: str):
        return {
            'invalid': gettext_lazy("【%s】不是有效的字符串。" % field),
            'blank': gettext_lazy("【%s】此字段不能为空字符串。" % field),
            'max_length': gettext_lazy("【%s】请确保此字段的字符数不超过 {max_length} 个。" % field),
            'min_length': gettext_lazy("【%s】请确保此字段至少包含 {min_length} 个字符。" % field),
            'required': gettext_lazy('【%s】此字段必填。' % field),
            'null': gettext_lazy('【%s】此字段不能为null。' % field)
        }

    @staticmethod
    def uuid(field: str):
        return {'required': gettext_lazy('【%s】此字段必填。' % field),
                'null': gettext_lazy('【%s】此字段不能为null。' % field),
                'invalid': gettext_lazy("【%s】必须是有效的UUID。" % field),
                }

    @staticmethod
    def integer(field: str):
        return {'invalid': gettext_lazy('【%s】必须是有效的integer。' % field),
                'max_value': gettext_lazy('【%s】请确保此值小于或等于 {max_value} 。' % field),
                'min_value': gettext_lazy('【%s】请确保此值大于或等于 {min_value} 。' % field),
                'max_string_length': gettext_lazy('【%s】字符串值太大。') % field,
                'required': gettext_lazy('【%s】此字段必填。' % field),
                'null': gettext_lazy('【%s】此字段不能为null。' % field),
                }

    @staticmethod
    def list(field: str):
        return {'not_a_list': gettext_lazy('【%s】应为列表,但得到的类型为 "{input_type}".' % field),
                'empty': gettext_lazy('【%s】此列表不能为空。' % field),
                'min_length': gettext_lazy('【%s】请确保此字段至少包含 {min_length} 个元素。' % field),
                'max_length': gettext_lazy('【%s】请确保此字段的元素不超过 {max_length} 个。' % field),
                'required': gettext_lazy('【%s】此字段必填。' % field),
                'null': gettext_lazy('【%s】此字段不能为null。' % field),
                }

    @staticmethod
    def boolean(field: str):
        return {'invalid': gettext_lazy('【%s】必须是有效的布尔值。' % field),
                'required': gettext_lazy('【%s】此字段必填。' % field),
                'null': gettext_lazy('【%s】此字段不能为null。' % field)}

    @staticmethod
    def dict(field: str):
        return {'not_a_dict': gettext_lazy('【%s】应为字典,但得到的类型为 "{input_type}' % field),
                'empty': gettext_lazy('【%s】能是空的。' % field),
                'required': gettext_lazy('【%s】此字段必填。' % field),
                'null': gettext_lazy('【%s】此字段不能为null。' % field),
                }

    @staticmethod
    def float(field: str):
        return {'invalid': gettext_lazy('【%s】需要一个有效的数字。' % field),
                'max_value': gettext_lazy('【%s】请确保此值小于或等于 {max_value}。' % field),
                'min_value': gettext_lazy('【%s】请确保此值大于或等于 {min_value}。' % field),
                'max_string_length': gettext_lazy('【%s】字符串值太大。' % field),
                'required': gettext_lazy('【%s】此字段必填。' % field),
                'null': gettext_lazy('【%s】此字段不能为null。' % field),
                }

    @staticmethod
    def json(field: str):
        return {
            'invalid': gettext_lazy('【%s】值必须是有效的JSON。' % field),
            'required': gettext_lazy('【%s】此字段必填。' % field),
            'null': gettext_lazy('【%s】此字段不能为null。' % field),
        }

    @staticmethod
    def base(field: str):
        return {
            'required': gettext_lazy('【%s】此字段必填。' % field),
            'null': gettext_lazy('【%s】此字段不能为null。' % field),
        }
