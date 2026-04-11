# Class AbstractSet<E>

**Source:** `java.base\java\util\AbstractSet.html`

### Class Description

```java
public abstract class
AbstractSet<E>

extends
AbstractCollection
<E>
implements
Set
<E>
```

This class provides a skeletal implementation of the

Set

interface to minimize the effort required to implement this
interface.

The process of implementing a set by extending this class is identical
to that of implementing a Collection by extending AbstractCollection,
except that all of the methods and constructors in subclasses of this
class must obey the additional constraints imposed by the

Set

interface (for instance, the add method must not permit addition of
multiple instances of an object to a set).

Note that this class does not override any of the implementations from
the

AbstractCollection

class. It merely adds implementations
for

equals

and

hashCode

.

This class is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements maintained by this set

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractSet()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public boolean equals​(
Object
o)

Compares the specified object with this set for equality. Returns

true

if the given object is also a set, the two sets have
the same size, and every member of the given set is contained in
this set. This ensures that the

equals

method works
properly across different implementations of the

Set

interface.

This implementation first checks if the specified object is this
set; if so it returns

true

. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns

containsAll((Collection) o)

.

**Specified by:**
- equals

in interface

Collection

<

E

>
- equals

in interface

Set

<

E

>

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- object to be compared for equality with this set

**Returns:**
- true

if the specified object is equal to this set

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this set. The hash code of a set is
defined to be the sum of the hash codes of the elements in the set,
where the hash code of a

null

element is defined to be zero.
This ensures that

s1.equals(s2)

implies that

s1.hashCode()==s2.hashCode()

for any two sets

s1

and

s2

, as required by the general contract of

Object.hashCode()

.

This implementation iterates over the set, calling the

hashCode

method on each element in the set, and adding up
the results.

**Specified by:**
- hashCode

in interface

Collection

<

E

>
- hashCode

in interface

Set

<

E

>

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this set

**See Also:**
- Object.equals(Object)

,

Set.equals(Object)

---

#### public boolean removeAll​(
Collection
<?> c)

Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the

asymmetric set difference

of
the two sets.

This implementation determines which is the smaller of this set
and the specified collection, by invoking the

size

method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's

remove

method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

**Specified by:**
- removeAll

in interface

Collection

<

E

>
- removeAll

in interface

Set

<

E

>

**Overrides:**
- removeAll

in class

AbstractCollection

<

E

>

**Parameters:**
- c

- collection containing elements to be removed from this set

**Returns:**
- true

if this set changed as a result of the call

**Throws:**
- UnsupportedOperationException

- if the

removeAll

operation
is not supported by this set
- ClassCastException

- if the class of an element of this set
is incompatible with the specified collection
(

optional

)
- NullPointerException

- if this set contains a null element and the
specified collection does not permit null elements
(

optional

),
or if the specified collection is null

**See Also:**
- AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

### Additional Sections

#### Class AbstractSet<E>

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractSet<E>

java.util.AbstractCollection

<E>

- java.util.AbstractSet<E>

java.util.AbstractSet<E>

**Type Parameters:** E

- the type of elements maintained by this set

**All Implemented Interfaces:** Iterable

<E>

,

Collection

<E>

,

Set

<E>

**Direct Known Subclasses:** ConcurrentSkipListSet

,

CopyOnWriteArraySet

,

EnumSet

,

HashSet

,

TreeSet

```java
public abstract class
AbstractSet<E>

extends
AbstractCollection
<E>
implements
Set
<E>
```

This class provides a skeletal implementation of the

Set

interface to minimize the effort required to implement this
interface.

The process of implementing a set by extending this class is identical
to that of implementing a Collection by extending AbstractCollection,
except that all of the methods and constructors in subclasses of this
class must obey the additional constraints imposed by the

Set

interface (for instance, the add method must not permit addition of
multiple instances of an object to a set).

Note that this class does not override any of the implementations from
the

AbstractCollection

class. It merely adds implementations
for

equals

and

hashCode

.

This class is a member of the

Java Collections Framework

.

**Since:** 1.2
**See Also:** Collection

,

AbstractCollection

,

Set

public abstract class

AbstractSet<E>

extends

AbstractCollection

<E>
implements

Set

<E>

This class provides a skeletal implementation of the

Set

interface to minimize the effort required to implement this
interface.

The process of implementing a set by extending this class is identical
to that of implementing a Collection by extending AbstractCollection,
except that all of the methods and constructors in subclasses of this
class must obey the additional constraints imposed by the

Set

interface (for instance, the add method must not permit addition of
multiple instances of an object to a set).

Note that this class does not override any of the implementations from
the

AbstractCollection

class. It merely adds implementations
for

equals

and

hashCode

.

This class is a member of the

Java Collections Framework

.

The process of implementing a set by extending this class is identical
to that of implementing a Collection by extending AbstractCollection,
except that all of the methods and constructors in subclasses of this
class must obey the additional constraints imposed by the

Set

interface (for instance, the add method must not permit addition of
multiple instances of an object to a set).

Note that this class does not override any of the implementations from
the

AbstractCollection

class. It merely adds implementations
for

equals

and

hashCode

.

This class is a member of the

Java Collections Framework

.

Note that this class does not override any of the implementations from
the

AbstractCollection

class. It merely adds implementations
for

equals

and

hashCode

.

This class is a member of the

Java Collections Framework

.

This class is a member of the

Java Collections Framework

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractSet

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Compares the specified object with this set for equality.

int

hashCode

()

Returns the hash code value for this set.

boolean

removeAll

​(

Collection

<?> c)

Removes from this set all of its elements that are contained in the
specified collection (optional operation).

- Methods declared in class java.util.

AbstractCollection

add

,

addAll

,

clear

,

contains

,

containsAll

,

isEmpty

,

iterator

,

remove

,

retainAll

,

toArray

,

toArray

,

toString

- Methods declared in class java.lang.

Object

clone

,

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

removeIf

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface java.util.

Set

add

,

addAll

,

clear

,

contains

,

containsAll

,

isEmpty

,

iterator

,

remove

,

retainAll

,

size

,

spliterator

,

toArray

,

toArray

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractSet

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Compares the specified object with this set for equality.

int

hashCode

()

Returns the hash code value for this set.

boolean

removeAll

​(

Collection

<?> c)

Removes from this set all of its elements that are contained in the
specified collection (optional operation).

- Methods declared in class java.util.

AbstractCollection

add

,

addAll

,

clear

,

contains

,

containsAll

,

isEmpty

,

iterator

,

remove

,

retainAll

,

toArray

,

toArray

,

toString

- Methods declared in class java.lang.

Object

clone

,

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

removeIf

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface java.util.

Set

add

,

addAll

,

clear

,

contains

,

containsAll

,

isEmpty

,

iterator

,

remove

,

retainAll

,

size

,

spliterator

,

toArray

,

toArray

---

#### Method Summary

Compares the specified object with this set for equality.

Returns the hash code value for this set.

Removes from this set all of its elements that are contained in the
specified collection (optional operation).

Methods declared in class java.util.

AbstractCollection

add

,

addAll

,

clear

,

contains

,

containsAll

,

isEmpty

,

iterator

,

remove

,

retainAll

,

toArray

,

toArray

,

toString

---

#### Methods declared in class java.util. AbstractCollection

Methods declared in class java.lang.

Object

clone

,

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

removeIf

,

stream

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.lang.

Iterable

forEach

---

#### Methods declared in interface java.lang. Iterable

Methods declared in interface java.util.

Set

add

,

addAll

,

clear

,

contains

,

containsAll

,

isEmpty

,

iterator

,

remove

,

retainAll

,

size

,

spliterator

,

toArray

,

toArray

---

#### Methods declared in interface java.util. Set

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractSet

```java
protected AbstractSet()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this set for equality. Returns

true

if the given object is also a set, the two sets have
the same size, and every member of the given set is contained in
this set. This ensures that the

equals

method works
properly across different implementations of the

Set

interface.

This implementation first checks if the specified object is this
set; if so it returns

true

. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns

containsAll((Collection) o)

.

**Specified by:** equals

in interface

Collection

<

E

>
**Specified by:** equals

in interface

Set

<

E

>
**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this set
**Returns:** true

if the specified object is equal to this set
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this set. The hash code of a set is
defined to be the sum of the hash codes of the elements in the set,
where the hash code of a

null

element is defined to be zero.
This ensures that

s1.equals(s2)

implies that

s1.hashCode()==s2.hashCode()

for any two sets

s1

and

s2

, as required by the general contract of

Object.hashCode()

.

This implementation iterates over the set, calling the

hashCode

method on each element in the set, and adding up
the results.

**Specified by:** hashCode

in interface

Collection

<

E

>
**Specified by:** hashCode

in interface

Set

<

E

>
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this set
**See Also:** Object.equals(Object)

,

Set.equals(Object)

- removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the

asymmetric set difference

of
the two sets.

This implementation determines which is the smaller of this set
and the specified collection, by invoking the

size

method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's

remove

method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

**Specified by:** removeAll

in interface

Collection

<

E

>
**Specified by:** removeAll

in interface

Set

<

E

>
**Overrides:** removeAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- collection containing elements to be removed from this set
**Returns:** true

if this set changed as a result of the call
**Throws:** UnsupportedOperationException

- if the

removeAll

operation
is not supported by this set
**Throws:** ClassCastException

- if the class of an element of this set
is incompatible with the specified collection
(

optional

)
**Throws:** NullPointerException

- if this set contains a null element and the
specified collection does not permit null elements
(

optional

),
or if the specified collection is null
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

Constructor Detail

- AbstractSet

```java
protected AbstractSet()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

AbstractSet

```java
protected AbstractSet()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### AbstractSet

protected AbstractSet()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this set for equality. Returns

true

if the given object is also a set, the two sets have
the same size, and every member of the given set is contained in
this set. This ensures that the

equals

method works
properly across different implementations of the

Set

interface.

This implementation first checks if the specified object is this
set; if so it returns

true

. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns

containsAll((Collection) o)

.

**Specified by:** equals

in interface

Collection

<

E

>
**Specified by:** equals

in interface

Set

<

E

>
**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this set
**Returns:** true

if the specified object is equal to this set
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this set. The hash code of a set is
defined to be the sum of the hash codes of the elements in the set,
where the hash code of a

null

element is defined to be zero.
This ensures that

s1.equals(s2)

implies that

s1.hashCode()==s2.hashCode()

for any two sets

s1

and

s2

, as required by the general contract of

Object.hashCode()

.

This implementation iterates over the set, calling the

hashCode

method on each element in the set, and adding up
the results.

**Specified by:** hashCode

in interface

Collection

<

E

>
**Specified by:** hashCode

in interface

Set

<

E

>
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this set
**See Also:** Object.equals(Object)

,

Set.equals(Object)

- removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the

asymmetric set difference

of
the two sets.

This implementation determines which is the smaller of this set
and the specified collection, by invoking the

size

method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's

remove

method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

**Specified by:** removeAll

in interface

Collection

<

E

>
**Specified by:** removeAll

in interface

Set

<

E

>
**Overrides:** removeAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- collection containing elements to be removed from this set
**Returns:** true

if this set changed as a result of the call
**Throws:** UnsupportedOperationException

- if the

removeAll

operation
is not supported by this set
**Throws:** ClassCastException

- if the class of an element of this set
is incompatible with the specified collection
(

optional

)
**Throws:** NullPointerException

- if this set contains a null element and the
specified collection does not permit null elements
(

optional

),
or if the specified collection is null
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

#### Method Detail

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this set for equality. Returns

true

if the given object is also a set, the two sets have
the same size, and every member of the given set is contained in
this set. This ensures that the

equals

method works
properly across different implementations of the

Set

interface.

This implementation first checks if the specified object is this
set; if so it returns

true

. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns

containsAll((Collection) o)

.

**Specified by:** equals

in interface

Collection

<

E

>
**Specified by:** equals

in interface

Set

<

E

>
**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this set
**Returns:** true

if the specified object is equal to this set
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified object with this set for equality. Returns

true

if the given object is also a set, the two sets have
the same size, and every member of the given set is contained in
this set. This ensures that the

equals

method works
properly across different implementations of the

Set

interface.

This implementation first checks if the specified object is this
set; if so it returns

true

. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns

containsAll((Collection) o)

.

This implementation first checks if the specified object is this
set; if so it returns

true

. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns

containsAll((Collection) o)

.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this set. The hash code of a set is
defined to be the sum of the hash codes of the elements in the set,
where the hash code of a

null

element is defined to be zero.
This ensures that

s1.equals(s2)

implies that

s1.hashCode()==s2.hashCode()

for any two sets

s1

and

s2

, as required by the general contract of

Object.hashCode()

.

This implementation iterates over the set, calling the

hashCode

method on each element in the set, and adding up
the results.

**Specified by:** hashCode

in interface

Collection

<

E

>
**Specified by:** hashCode

in interface

Set

<

E

>
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this set
**See Also:** Object.equals(Object)

,

Set.equals(Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this set. The hash code of a set is
defined to be the sum of the hash codes of the elements in the set,
where the hash code of a

null

element is defined to be zero.
This ensures that

s1.equals(s2)

implies that

s1.hashCode()==s2.hashCode()

for any two sets

s1

and

s2

, as required by the general contract of

Object.hashCode()

.

This implementation iterates over the set, calling the

hashCode

method on each element in the set, and adding up
the results.

This implementation iterates over the set, calling the

hashCode

method on each element in the set, and adding up
the results.

removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the

asymmetric set difference

of
the two sets.

This implementation determines which is the smaller of this set
and the specified collection, by invoking the

size

method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's

remove

method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

**Specified by:** removeAll

in interface

Collection

<

E

>
**Specified by:** removeAll

in interface

Set

<

E

>
**Overrides:** removeAll

in class

AbstractCollection

<

E

>
**Parameters:** c

- collection containing elements to be removed from this set
**Returns:** true

if this set changed as a result of the call
**Throws:** UnsupportedOperationException

- if the

removeAll

operation
is not supported by this set
**Throws:** ClassCastException

- if the class of an element of this set
is incompatible with the specified collection
(

optional

)
**Throws:** NullPointerException

- if this set contains a null element and the
specified collection does not permit null elements
(

optional

),
or if the specified collection is null
**See Also:** AbstractCollection.remove(Object)

,

AbstractCollection.contains(Object)

---

#### removeAll

public boolean removeAll​(

Collection

<?> c)

Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the

asymmetric set difference

of
the two sets.

This implementation determines which is the smaller of this set
and the specified collection, by invoking the

size

method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's

remove

method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

This implementation determines which is the smaller of this set
and the specified collection, by invoking the

size

method on each. If this set has fewer elements, then the
implementation iterates over this set, checking each element
returned by the iterator in turn to see if it is contained in
the specified collection. If it is so contained, it is removed
from this set with the iterator's

remove

method. If
the specified collection has fewer elements, then the
implementation iterates over the specified collection, removing
from this set each element returned by the iterator, using this
set's

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

Note that this implementation will throw an

UnsupportedOperationException

if the iterator returned by the

iterator

method does not implement the

remove

method.

---

