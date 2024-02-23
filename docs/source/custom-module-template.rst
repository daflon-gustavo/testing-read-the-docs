{{ fullname | escape | underline }}
.. automodule:: {{ module }}
{% for item in methods %}
.. autofunction:: {{ item }}
{% endfor %}