# Class Stack<E>

**Source:** `java.base\java\util\Stack.html`

### Class Description

```java
public class
Stack<E>

extends
Vector
<E>
```

The

Stack

class represents a last-in-first-out
(LIFO) stack of objects. It extends class

Vector

with five
operations that allow a vector to be treated as a stack. The usual

push

and

pop

operations are provided, as well as a
method to

peek

at the top item on the stack, a method to test
for whether the stack is

empty

, and a method to

search

the stack for an item and discover how far it is from the top.

When a stack is first created, it contains no items.

A more complete and consistent set of LIFO stack operations is
provided by the

Deque

interface and its implementations, which
should be used in preference to this class. For example:

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
```

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Iterable

<E>

,

Collection

<E>

,

List

<E>

,

RandomAccess

---

### Field Details

*No entries found.*

### Constructor Details

#### public Stack()

Creates an empty Stack.

---

### Method Details

#### public
E
push​(
E
item)

Pushes an item onto the top of this stack. This has exactly
the same effect as:

```java
addElement(item)
```

**Parameters:**
- item

- the item to be pushed onto this stack.

**Returns:**
- the

item

argument.

**See Also:**
- Vector.addElement(E)

---

#### public
E
pop()

Removes the object at the top of this stack and returns that
object as the value of this function.

**Returns:**
- The object at the top of this stack (the last item
of the

Vector

object).

**Throws:**
- EmptyStackException

- if this stack is empty.

---

#### public
E
peek()

Looks at the object at the top of this stack without removing it
from the stack.

**Returns:**
- the object at the top of this stack (the last item
of the

Vector

object).

**Throws:**
- EmptyStackException

- if this stack is empty.

---

#### public boolean empty()

Tests if this stack is empty.

**Returns:**
- true

if and only if this stack contains
no items;

false

otherwise.

---

#### public int search​(
Object
o)

Returns the 1-based position where an object is on this stack.
If the object

o

occurs as an item in this stack, this
method returns the distance from the top of the stack of the
occurrence nearest the top of the stack; the topmost item on the
stack is considered to be at distance

1

. The

equals

method is used to compare

o

to the
items in this stack.

**Parameters:**
- o

- the desired object.

**Returns:**
- the 1-based position from the top of the stack where
the object is located; the return value

-1

indicates that the object is not on the stack.

---

### Additional Sections

#### Class Stack<E>

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractList

<E>
- - java.util.Vector

<E>
- - java.util.Stack<E>

java.util.AbstractCollection

<E>

- java.util.AbstractList

<E>
- - java.util.Vector

<E>
- - java.util.Stack<E>

java.util.AbstractList

<E>

- java.util.Vector

<E>
- - java.util.Stack<E>

java.util.Vector

<E>

- java.util.Stack<E>

java.util.Stack<E>

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Iterable

<E>

,

Collection

<E>

,

List

<E>

,

RandomAccess

```java
public class
Stack<E>

extends
Vector
<E>
```

The

Stack

class represents a last-in-first-out
(LIFO) stack of objects. It extends class

Vector

with five
operations that allow a vector to be treated as a stack. The usual

push

and

pop

operations are provided, as well as a
method to

peek

at the top item on the stack, a method to test
for whether the stack is

empty

, and a method to

search

the stack for an item and discover how far it is from the top.

When a stack is first created, it contains no items.

A more complete and consistent set of LIFO stack operations is
provided by the

Deque

interface and its implementations, which
should be used in preference to this class. For example:

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
```

**Since:** 1.0
**See Also:** Serialized Form

public class

Stack<E>

extends

Vector

<E>

The

Stack

class represents a last-in-first-out
(LIFO) stack of objects. It extends class

Vector

with five
operations that allow a vector to be treated as a stack. The usual

push

and

pop

operations are provided, as well as a
method to

peek

at the top item on the stack, a method to test
for whether the stack is

empty

, and a method to

search

the stack for an item and discover how far it is from the top.

When a stack is first created, it contains no items.

A more complete and consistent set of LIFO stack operations is
provided by the

Deque

interface and its implementations, which
should be used in preference to this class. For example:

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
```

When a stack is first created, it contains no items.

A more complete and consistent set of LIFO stack operations is
provided by the

Deque

interface and its implementations, which
should be used in preference to this class. For example:

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
```

A more complete and consistent set of LIFO stack operations is
provided by the

Deque

interface and its implementations, which
should be used in preference to this class. For example:

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
```

Deque<Integer> stack = new ArrayDeque<Integer>();

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

Vector

capacityIncrement

,

elementCount

,

elementData

- Fields declared in class java.util.

AbstractList

modCount

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Stack

()

Creates an empty Stack.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

empty

()

Tests if this stack is empty.

E

peek

()

Looks at the object at the top of this stack without removing it
from the stack.

E

pop

()

Removes the object at the top of this stack and returns that
object as the value of this function.

E

push

​(

E

item)

Pushes an item onto the top of this stack.

int

search

​(

Object

o)

Returns the 1-based position where an object is on this stack.

- Methods declared in class java.util.

Vector

add

,

add

,

addAll

,

addAll

,

addElement

,

capacity

,

clear

,

clone

,

contains

,

containsAll

,

copyInto

,

elementAt

,

elements

,

ensureCapacity

,

equals

,

firstElement

,

forEach

,

get

,

hashCode

,

indexOf

,

indexOf

,

insertElementAt

,

isEmpty

,

iterator

,

lastElement

,

lastIndexOf

,

lastIndexOf

,

listIterator

,

listIterator

,

remove

,

remove

,

removeAll

,

removeAllElements

,

removeElement

,

removeElementAt

,

removeIf

,

removeRange

,

replaceAll

,

retainAll

,

set

,

setElementAt

,

setSize

,

size

,

spliterator

,

subList

,

toArray

,

toArray

,

toString

,

trimToSize

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Collection

parallelStream

,

stream

,

toArray

- Methods declared in interface java.util.

List

sort

Field Summary

- Fields declared in class java.util.

Vector

capacityIncrement

,

elementCount

,

elementData

- Fields declared in class java.util.

AbstractList

modCount

---

#### Field Summary

Fields declared in class java.util.

Vector

capacityIncrement

,

elementCount

,

elementData

---

#### Fields declared in class java.util. Vector

Fields declared in class java.util.

AbstractList

modCount

---

#### Fields declared in class java.util. AbstractList

Constructor Summary

Constructors

Constructor

Description

Stack

()

Creates an empty Stack.

---

#### Constructor Summary

Creates an empty Stack.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

empty

()

Tests if this stack is empty.

E

peek

()

Looks at the object at the top of this stack without removing it
from the stack.

E

pop

()

Removes the object at the top of this stack and returns that
object as the value of this function.

E

push

​(

E

item)

Pushes an item onto the top of this stack.

int

search

​(

Object

o)

Returns the 1-based position where an object is on this stack.

- Methods declared in class java.util.

Vector

add

,

add

,

addAll

,

addAll

,

addElement

,

capacity

,

clear

,

clone

,

contains

,

containsAll

,

copyInto

,

elementAt

,

elements

,

ensureCapacity

,

equals

,

firstElement

,

forEach

,

get

,

hashCode

,

indexOf

,

indexOf

,

insertElementAt

,

isEmpty

,

iterator

,

lastElement

,

lastIndexOf

,

lastIndexOf

,

listIterator

,

listIterator

,

remove

,

remove

,

removeAll

,

removeAllElements

,

removeElement

,

removeElementAt

,

removeIf

,

removeRange

,

replaceAll

,

retainAll

,

set

,

setElementAt

,

setSize

,

size

,

spliterator

,

subList

,

toArray

,

toArray

,

toString

,

trimToSize

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Collection

parallelStream

,

stream

,

toArray

- Methods declared in interface java.util.

List

sort

---

#### Method Summary

Tests if this stack is empty.

Looks at the object at the top of this stack without removing it
from the stack.

Removes the object at the top of this stack and returns that
object as the value of this function.

Pushes an item onto the top of this stack.

Returns the 1-based position where an object is on this stack.

Methods declared in class java.util.

Vector

add

,

add

,

addAll

,

addAll

,

addElement

,

capacity

,

clear

,

clone

,

contains

,

containsAll

,

copyInto

,

elementAt

,

elements

,

ensureCapacity

,

equals

,

firstElement

,

forEach

,

get

,

hashCode

,

indexOf

,

indexOf

,

insertElementAt

,

isEmpty

,

iterator

,

lastElement

,

lastIndexOf

,

lastIndexOf

,

listIterator

,

listIterator

,

remove

,

remove

,

removeAll

,

removeAllElements

,

removeElement

,

removeElementAt

,

removeIf

,

removeRange

,

replaceAll

,

retainAll

,

set

,

setElementAt

,

setSize

,

size

,

spliterator

,

subList

,

toArray

,

toArray

,

toString

,

trimToSize

---

#### Methods declared in class java.util. Vector

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.

Collection

parallelStream

,

stream

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.util.

List

sort

---

#### Methods declared in interface java.util. List

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Stack

```java
public Stack()
```

Creates an empty Stack.

============ METHOD DETAIL ==========

- Method Detail

- push

```java
public
E
push​(
E
item)
```

Pushes an item onto the top of this stack. This has exactly
the same effect as:

```java
addElement(item)
```

**Parameters:** item

- the item to be pushed onto this stack.
**Returns:** the

item

argument.
**See Also:** Vector.addElement(E)

- pop

```java
public
E
pop()
```

Removes the object at the top of this stack and returns that
object as the value of this function.

**Returns:** The object at the top of this stack (the last item
of the

Vector

object).
**Throws:** EmptyStackException

- if this stack is empty.

- peek

```java
public
E
peek()
```

Looks at the object at the top of this stack without removing it
from the stack.

**Returns:** the object at the top of this stack (the last item
of the

Vector

object).
**Throws:** EmptyStackException

- if this stack is empty.

- empty

```java
public boolean empty()
```

Tests if this stack is empty.

**Returns:** true

if and only if this stack contains
no items;

false

otherwise.

- search

```java
public int search​(
Object
o)
```

Returns the 1-based position where an object is on this stack.
If the object

o

occurs as an item in this stack, this
method returns the distance from the top of the stack of the
occurrence nearest the top of the stack; the topmost item on the
stack is considered to be at distance

1

. The

equals

method is used to compare

o

to the
items in this stack.

**Parameters:** o

- the desired object.
**Returns:** the 1-based position from the top of the stack where
the object is located; the return value

-1

indicates that the object is not on the stack.

Constructor Detail

- Stack

```java
public Stack()
```

Creates an empty Stack.

---

#### Constructor Detail

Stack

```java
public Stack()
```

Creates an empty Stack.

---

#### Stack

public Stack()

Creates an empty Stack.

Method Detail

- push

```java
public
E
push​(
E
item)
```

Pushes an item onto the top of this stack. This has exactly
the same effect as:

```java
addElement(item)
```

**Parameters:** item

- the item to be pushed onto this stack.
**Returns:** the

item

argument.
**See Also:** Vector.addElement(E)

- pop

```java
public
E
pop()
```

Removes the object at the top of this stack and returns that
object as the value of this function.

**Returns:** The object at the top of this stack (the last item
of the

Vector

object).
**Throws:** EmptyStackException

- if this stack is empty.

- peek

```java
public
E
peek()
```

Looks at the object at the top of this stack without removing it
from the stack.

**Returns:** the object at the top of this stack (the last item
of the

Vector

object).
**Throws:** EmptyStackException

- if this stack is empty.

- empty

```java
public boolean empty()
```

Tests if this stack is empty.

**Returns:** true

if and only if this stack contains
no items;

false

otherwise.

- search

```java
public int search​(
Object
o)
```

Returns the 1-based position where an object is on this stack.
If the object

o

occurs as an item in this stack, this
method returns the distance from the top of the stack of the
occurrence nearest the top of the stack; the topmost item on the
stack is considered to be at distance

1

. The

equals

method is used to compare

o

to the
items in this stack.

**Parameters:** o

- the desired object.
**Returns:** the 1-based position from the top of the stack where
the object is located; the return value

-1

indicates that the object is not on the stack.

---

#### Method Detail

push

```java
public
E
push​(
E
item)
```

Pushes an item onto the top of this stack. This has exactly
the same effect as:

```java
addElement(item)
```

**Parameters:** item

- the item to be pushed onto this stack.
**Returns:** the

item

argument.
**See Also:** Vector.addElement(E)

---

#### push

public

E

push​(

E

item)

Pushes an item onto the top of this stack. This has exactly
the same effect as:

```java
addElement(item)
```

addElement(item)

pop

```java
public
E
pop()
```

Removes the object at the top of this stack and returns that
object as the value of this function.

**Returns:** The object at the top of this stack (the last item
of the

Vector

object).
**Throws:** EmptyStackException

- if this stack is empty.

---

#### pop

public

E

pop()

Removes the object at the top of this stack and returns that
object as the value of this function.

peek

```java
public
E
peek()
```

Looks at the object at the top of this stack without removing it
from the stack.

**Returns:** the object at the top of this stack (the last item
of the

Vector

object).
**Throws:** EmptyStackException

- if this stack is empty.

---

#### peek

public

E

peek()

Looks at the object at the top of this stack without removing it
from the stack.

empty

```java
public boolean empty()
```

Tests if this stack is empty.

**Returns:** true

if and only if this stack contains
no items;

false

otherwise.

---

#### empty

public boolean empty()

Tests if this stack is empty.

search

```java
public int search​(
Object
o)
```

Returns the 1-based position where an object is on this stack.
If the object

o

occurs as an item in this stack, this
method returns the distance from the top of the stack of the
occurrence nearest the top of the stack; the topmost item on the
stack is considered to be at distance

1

. The

equals

method is used to compare

o

to the
items in this stack.

**Parameters:** o

- the desired object.
**Returns:** the 1-based position from the top of the stack where
the object is located; the return value

-1

indicates that the object is not on the stack.

---

#### search

public int search​(

Object

o)

Returns the 1-based position where an object is on this stack.
If the object

o

occurs as an item in this stack, this
method returns the distance from the top of the stack of the
occurrence nearest the top of the stack; the topmost item on the
stack is considered to be at distance

1

. The

equals

method is used to compare

o

to the
items in this stack.

---

