
Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``example.get_random_ingredients()`` function:

.. autofunction:: example.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`example.get_random_ingredients`
will raise an exception.

.. autoexception:: example.InvalidKindError

For example:

>>> import example
>>> example.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']