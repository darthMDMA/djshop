'''Специальный файл для создания вспомогательных классов'''
from django.db.models import Count
from string import ascii_lowercase, ascii_uppercase
from blog.models import *


cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
letters = cyrillic_letters + ascii_uppercase + ascii_lowercase +'-_ '


# Slugify (Cyrillic)
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ь': '', 'ы': 'i',
            'э': 'e', 'ю': 'yu','я': 'ya'}


def django_slugify(s):
    return ''.join(alphabet.get(w, w) for w in s.lower() if w in letters).strip().replace(' ', '-')



# class DataMixin:
#     paginate_by = 3 # разбивка по 3 поста на страницу
#
#     def get_user_context(self, **kwargs):
#         context = kwargs
#
#         # формируем меню для неавторизованного пользователя
#         user_menu = menu.copy() # копируем основное меню
#         # if not self.request.user.is_authenticated: # проверяем авторизован или нет
#         #     user_menu.pop(1) # удаляем тот элемент меню, который хотим скрыть для пользователя
#
#         context['side_bar'] = user_menu
#
#         return context

class DataPostMixin:
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'post'
    paginate_by = 4


