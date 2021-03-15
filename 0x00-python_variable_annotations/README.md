notes:
Defining generic classes
************************

The built-in collection classes are generic classes. Generic types
have one or more type parameters, which can be arbitrary types. For
example, ``Dict[int, str]`` has the type parameters ``int`` and
``str``, and ``List[int]`` has a type parameter ``int``.

Programs can also define new generic classes. Here is a very simple
generic class that represents a stack:

.. code-block:: python

   from typing import TypeVar, Generic

   T = TypeVar('T')

   class Stack(Generic[T]):
       def __init__(self) -> None:
           # Create an empty list with items of type T
           self.items: List[T] = []

       def push(self, item: T) -> None:
           self.items.append(item)

       def pop(self) -> T:
           return self.items.pop()

       def empty(self) -> bool:
           return not self.items

The ``Stack`` class can be used to represent a stack of any type:
``Stack[int]``, ``Stack[Tuple[int, str]]``, etc.

Using ``Stack`` is similar to built-in container types:

.. code-block:: python

   # Construct an empty Stack[int] instance
   stack = Stack[int]()
   stack.push(2)
   stack.pop()
   stack.push('x')        # Type error

Type inference works for user-defined generic types as well:

.. code-block:: python

   def process(stack: Stack[int]) -> None: ...

   process(Stack())   # Argument has inferred type Stack[int]

Construction of instances of generic types is also type checked:

.. code-block:: python

   class Box(Generic[T]):
       def __init__(self, content: T) -> None:
           self.content = content

   Box(1)  # OK, inferred type is Box[int]
   Box[int](1)  # Also OK
   s = 'some string'
   Box[int](s)  # Type error

Generic class internals
***********************

You may wonder what happens at runtime when you index
``Stack``. Actually, indexing ``Stack`` returns essentially a copy
of ``Stack`` that returns instances of the original class on
instantiation:

.. code-block:: python

   >>> print(Stack)
   __main__.Stack
   >>> print(Stack[int])
   __main__.Stack[int]
   >>> print(Stack[int]().__class__)
   __main__.Stack

Note that built-in types :py:class:`list`, :py:class:`dict` and so on do not support
indexing in Python. This is why we have the aliases :py:class:`~typing.List`, :py:class:`~typing.Dict`
and so on in the :py:mod:`typing` module. Indexing these aliases gives
you a class that directly inherits from the target class in Python:

.. code-block:: python

   >>> from typing import List
   >>> List[int]
   typing.List[int]
   >>> List[int].__bases__
   (<class 'list'>, typing.MutableSequence)

Generic types could be instantiated or subclassed as usual classes,
but the above examples illustrate that type variables are erased at
runtime. Generic ``Stack`` instances are just ordinary
Python objects, and they have no extra runtime overhead or magic due
to being generic, other than a metaclass that overloads the indexing
operator.
