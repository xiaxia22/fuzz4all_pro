# Interface Enumeration<E>

**Source:** `java.base\java\util\Enumeration.html`

### Class Description

```java
public interface
Enumeration<E>
```

An object that implements the Enumeration interface generates a
series of elements, one at a time. Successive calls to the

nextElement

method return successive elements of the
series.

For example, to print all elements of a

Vector<E>

v

:

```java
for (Enumeration<E> e = v.elements(); e.hasMoreElements();)
System.out.println(e.nextElement());
```

Methods are provided to enumerate through the elements of a
vector, the keys of a hashtable, and the values in a hashtable.
Enumerations are also used to specify the input streams to a

SequenceInputStream

.

**All Known Subinterfaces:** NamingEnumeration

<T>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean hasMoreElements()

Tests if this enumeration contains more elements.

**Returns:**
- true

if and only if this enumeration object
contains at least one more element to provide;

false

otherwise.

---

#### E
nextElement()

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

**Returns:**
- the next element of this enumeration.

**Throws:**
- NoSuchElementException

- if no more elements exist.

---

#### default
Iterator
<
E
> asIterator()

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration. Traversal is undefined if any methods
are called on this enumeration after the call to

asIterator

.

**Returns:**
- an Iterator representing the remaining elements of this Enumeration

**Since:**
- 9

**API Note:**
- This method is intended to help adapt code that produces

Enumeration

instances to code that consumes

Iterator

instances. For example, the

JarFile.entries()

method returns an

Enumeration<JarEntry>

.
This can be turned into an

Iterator

, and then the

forEachRemaining()

method can be used:

```java
JarFile jarFile = ... ;
jarFile.entries().asIterator().forEachRemaining(entry -> { ... });
```

(Note that there is also a

JarFile.stream()

method that returns a

Stream

of entries,
which may be more convenient in some cases.)

**Implementation Requirements:**
- The default implementation returns an

Iterator

whose

hasNext

method calls this Enumeration's

hasMoreElements

method, whose

next

method calls this Enumeration's

nextElement

method, and
whose

remove

method throws

UnsupportedOperationException

.

---

### Additional Sections

#### Interface Enumeration<E>

**All Known Subinterfaces:** NamingEnumeration

<T>

**All Known Implementing Classes:** StringTokenizer

```java
public interface
Enumeration<E>
```

An object that implements the Enumeration interface generates a
series of elements, one at a time. Successive calls to the

nextElement

method return successive elements of the
series.

For example, to print all elements of a

Vector<E>

v

:

```java
for (Enumeration<E> e = v.elements(); e.hasMoreElements();)
System.out.println(e.nextElement());
```

Methods are provided to enumerate through the elements of a
vector, the keys of a hashtable, and the values in a hashtable.
Enumerations are also used to specify the input streams to a

SequenceInputStream

.

**API Note:** The functionality of this interface is duplicated by the

Iterator

interface. In addition,

Iterator

adds an optional remove operation,
and has shorter method names. New implementations should consider using

Iterator

in preference to

Enumeration

. It is possible to
adapt an

Enumeration

to an

Iterator

by using the

asIterator()

method.
**Since:** 1.0
**See Also:** Iterator

,

SequenceInputStream

,

nextElement()

,

Hashtable

,

Hashtable.elements()

,

Hashtable.keys()

,

Vector

,

Vector.elements()

public interface

Enumeration<E>

An object that implements the Enumeration interface generates a
series of elements, one at a time. Successive calls to the

nextElement

method return successive elements of the
series.

For example, to print all elements of a

Vector<E>

v

:

```java
for (Enumeration<E> e = v.elements(); e.hasMoreElements();)
System.out.println(e.nextElement());
```

Methods are provided to enumerate through the elements of a
vector, the keys of a hashtable, and the values in a hashtable.
Enumerations are also used to specify the input streams to a

SequenceInputStream

.

For example, to print all elements of a

Vector<E>

v

:

```java
for (Enumeration<E> e = v.elements(); e.hasMoreElements();)
System.out.println(e.nextElement());
```

Methods are provided to enumerate through the elements of a
vector, the keys of a hashtable, and the values in a hashtable.
Enumerations are also used to specify the input streams to a

SequenceInputStream

.

for (Enumeration<E> e = v.elements(); e.hasMoreElements();)
System.out.println(e.nextElement());

Methods are provided to enumerate through the elements of a
vector, the keys of a hashtable, and the values in a hashtable.
Enumerations are also used to specify the input streams to a

SequenceInputStream

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

Iterator

<

E

>

asIterator

()

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration.

boolean

hasMoreElements

()

Tests if this enumeration contains more elements.

E

nextElement

()

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

Iterator

<

E

>

asIterator

()

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration.

boolean

hasMoreElements

()

Tests if this enumeration contains more elements.

E

nextElement

()

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

---

#### Method Summary

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration.

Tests if this enumeration contains more elements.

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

============ METHOD DETAIL ==========

- Method Detail

- hasMoreElements

```java
boolean hasMoreElements()
```

Tests if this enumeration contains more elements.

**Returns:** true

if and only if this enumeration object
contains at least one more element to provide;

false

otherwise.

- nextElement

```java
E
nextElement()
```

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

**Returns:** the next element of this enumeration.
**Throws:** NoSuchElementException

- if no more elements exist.

- asIterator

```java
default
Iterator
<
E
> asIterator()
```

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration. Traversal is undefined if any methods
are called on this enumeration after the call to

asIterator

.

**API Note:** This method is intended to help adapt code that produces

Enumeration

instances to code that consumes

Iterator

instances. For example, the

JarFile.entries()

method returns an

Enumeration<JarEntry>

.
This can be turned into an

Iterator

, and then the

forEachRemaining()

method can be used:

```java
JarFile jarFile = ... ;
jarFile.entries().asIterator().forEachRemaining(entry -> { ... });
```

(Note that there is also a

JarFile.stream()

method that returns a

Stream

of entries,
which may be more convenient in some cases.)
**Implementation Requirements:** The default implementation returns an

Iterator

whose

hasNext

method calls this Enumeration's

hasMoreElements

method, whose

next

method calls this Enumeration's

nextElement

method, and
whose

remove

method throws

UnsupportedOperationException

.
**Returns:** an Iterator representing the remaining elements of this Enumeration
**Since:** 9

Method Detail

- hasMoreElements

```java
boolean hasMoreElements()
```

Tests if this enumeration contains more elements.

**Returns:** true

if and only if this enumeration object
contains at least one more element to provide;

false

otherwise.

- nextElement

```java
E
nextElement()
```

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

**Returns:** the next element of this enumeration.
**Throws:** NoSuchElementException

- if no more elements exist.

- asIterator

```java
default
Iterator
<
E
> asIterator()
```

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration. Traversal is undefined if any methods
are called on this enumeration after the call to

asIterator

.

**API Note:** This method is intended to help adapt code that produces

Enumeration

instances to code that consumes

Iterator

instances. For example, the

JarFile.entries()

method returns an

Enumeration<JarEntry>

.
This can be turned into an

Iterator

, and then the

forEachRemaining()

method can be used:

```java
JarFile jarFile = ... ;
jarFile.entries().asIterator().forEachRemaining(entry -> { ... });
```

(Note that there is also a

JarFile.stream()

method that returns a

Stream

of entries,
which may be more convenient in some cases.)
**Implementation Requirements:** The default implementation returns an

Iterator

whose

hasNext

method calls this Enumeration's

hasMoreElements

method, whose

next

method calls this Enumeration's

nextElement

method, and
whose

remove

method throws

UnsupportedOperationException

.
**Returns:** an Iterator representing the remaining elements of this Enumeration
**Since:** 9

---

#### Method Detail

hasMoreElements

```java
boolean hasMoreElements()
```

Tests if this enumeration contains more elements.

**Returns:** true

if and only if this enumeration object
contains at least one more element to provide;

false

otherwise.

---

#### hasMoreElements

boolean hasMoreElements()

Tests if this enumeration contains more elements.

nextElement

```java
E
nextElement()
```

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

**Returns:** the next element of this enumeration.
**Throws:** NoSuchElementException

- if no more elements exist.

---

#### nextElement

E

nextElement()

Returns the next element of this enumeration if this enumeration
object has at least one more element to provide.

asIterator

```java
default
Iterator
<
E
> asIterator()
```

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration. Traversal is undefined if any methods
are called on this enumeration after the call to

asIterator

.

**API Note:** This method is intended to help adapt code that produces

Enumeration

instances to code that consumes

Iterator

instances. For example, the

JarFile.entries()

method returns an

Enumeration<JarEntry>

.
This can be turned into an

Iterator

, and then the

forEachRemaining()

method can be used:

```java
JarFile jarFile = ... ;
jarFile.entries().asIterator().forEachRemaining(entry -> { ... });
```

(Note that there is also a

JarFile.stream()

method that returns a

Stream

of entries,
which may be more convenient in some cases.)
**Implementation Requirements:** The default implementation returns an

Iterator

whose

hasNext

method calls this Enumeration's

hasMoreElements

method, whose

next

method calls this Enumeration's

nextElement

method, and
whose

remove

method throws

UnsupportedOperationException

.
**Returns:** an Iterator representing the remaining elements of this Enumeration
**Since:** 9

---

#### asIterator

default

Iterator

<

E

> asIterator()

Returns an

Iterator

that traverses the remaining elements
covered by this enumeration. Traversal is undefined if any methods
are called on this enumeration after the call to

asIterator

.

JarFile jarFile = ... ;
jarFile.entries().asIterator().forEachRemaining(entry -> { ... });

---

