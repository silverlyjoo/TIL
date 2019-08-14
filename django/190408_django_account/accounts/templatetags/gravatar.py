import hashlib
from django import template

# 템플릿 라이브러리에
register = template.Library()

# 아래의 함수를 필터로 추가한다
@register.filter

def makemd5(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()

