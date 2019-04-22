from django import template
register = template.Library()

@register.filter
def hashtag_link(post):
    content = post.content
    hashtags = post.hashtags.all()
    
        
        
    for hashtag in hashtags:
        # 1
        # content = content.replace(hashtag.content, f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a>')
        # 2
        content = content.replace(hashtag.content+' ', f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a> ')
        # 3
        # content = re.sub(fr'hashtag.content'{})
        # content = re.sub(r'\#'+hashtag.content+r'\b', '<a href="/posts/hashtag/'+hashtag.content+'">#'+hashtag.content+'</a>', content)
        
        
        
    return content