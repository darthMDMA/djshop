from djangoshop.wsgi import * # без это строчки не запускался pytest
import pytest
from django import forms
from discussions.forms import ContactForm
import datetime

# pytest --tb=native  вывод более удобной информации
# pytest - запуск теста
# pytest -vv расширенный запуск теста
# pytest --tb=auto еще более расширенный
# errors.as_data()  метод django который показывает детально ошибки форм


# параметризованный тест
@pytest.mark.parametrize(
    ' date_created, subject, message, sender, cc_myself, validity',
    [
        # рабочий вариант
        (datetime.date.today(), 'Hello!', 'You"re cool!', 'vasily@mail.ru', 'cc-myself', True),
        # > 5000 символов контент
        # ('Пост отстой'*500, '2022-02-14', '@mail.ru', True),
        # > 100 символов автор
        # ('Пост отстой', '2022-02-14', '@mail.ru'*5, True),
    ]
)
def test_valid_discuss_form(date_created, subject, message, sender, cc_myself, validity):
    form = ContactForm(data={
        'date_created': date_created,
        'subject': subject,
        'message': message,
        'sender': sender,
        'cc_myself': cc_myself
     })

    f = form.errors.as_data()
    print(f)

    assert form.is_valid() is validity
######################################################################
@pytest.mark.parametrize(
    'date_created, valid_data',
    [
        (datetime.date.today(), True),
        (datetime.date.today() - datetime.timedelta(days=1), False),
        (datetime.date.today() + datetime.timedelta(days=1), False),
        ('', False),
        (None, False),
    ],
)

@pytest.mark.parametrize(
    'subject, valid_subject',
    [
        ('n' * 30, True),
        ('n' * 31, False),
        ('', False),
    ],
)

@pytest.mark.parametrize(
    'message, valid_message',
    [
        (''.join(map(str, range(100)))[:300], True),
        # (),
        # (),
    ],
)
@pytest.mark.parametrize(
    'sender, valid_sender',
    [
        ('vas@ya.ru', True),
        # (),
        # (),
    ],
)
@pytest.mark.parametrize(
    'cc_myself, valid_cc_myself',
    [
        ('cc_myself', True),
        # (),
        # (),
    ],
)

def test_comment_form(date_created, subject, message, sender, cc_myself,
                      valid_data, valid_subject, valid_message, valid_sender, valid_cc_myself):

    form = ContactForm(data= {
        'date_created': date_created,
        'subject': subject,
        'message': message,
        'sender': sender,
        'cc_myself': cc_myself,
    })

    f = form.errors.as_data()
    print(f)

    assert form.is_valid() is (valid_data and valid_subject and valid_message and valid_sender and valid_cc_myself)



