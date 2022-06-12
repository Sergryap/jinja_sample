from jinja2 import Template

# фильтры
# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'Шкода', 'price': 17300},
#     {'model': 'Вольво', 'price': 44300},
#     {'model': 'Фольксваген', 'price': 21300},
# ]
#
# tpl = "Суммарная цена автомобилей {{ (cs | max(attribute='price')).model }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# persons = [
#     {'name': 'алексей', 'old': 18, 'weight': 78.5},
#     {'name': 'николай', 'old': 28, 'weight': 82.3},
#     {'name': 'иван', 'old': 33, 'weight': 94.0}
# ]
#
# tpl = """
# {% for u in users -%}
# {% filter capitalize %}{{u.name}}{% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)

# Макроопределения
# html = """
# {% macro input(name, value="None", type="text", size=20) -%}
#     <input type="{{ type }}" name="{{name}}" value="{{ value|e }}" size="{{ size }}">
# {%- endmacro %}}
#
# <p>{{ input('username', "Hello") }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# Вложенные макросы

persons = [
    {'name': 'алексей', 'old': 18, 'weight': 78.5},
    {'name': 'николай', 'old': 28, 'weight': 82.3},
    {'name': 'иван', 'old': 33, 'weight': 94.0}
]

html = """
{% macro list_users(list_of_users) -%}
<ul>
{% for u in list_of_users -%}
    <li>{% filter upper %}{{u.name}}{% endfilter %} {{caller(u)}}
{%- endfor -%}
</ul>
{%- endmacro -%}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall %}

"""

tm = Template(html)
msg = tm.render(users=persons)

print(msg)
