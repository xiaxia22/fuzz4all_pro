# Interface NavigableSet<E>

**Source:** `java.base\java\util\NavigableSet.html`

### Class Description

```java
public interface
NavigableSet<E>

extends
SortedSet
<E>
```

A

SortedSet

extended with navigation methods reporting
closest matches for given search targets. Methods

lower(E)

,

floor(E)

,

ceiling(E)

, and

higher(E)

return elements
respectively less than, less than or equal, greater than or equal,
and greater than a given element, returning

null

if there
is no such element.

A

NavigableSet

may be accessed and traversed in either
ascending or descending order. The

descendingSet()

method
returns a view of the set with the senses of all relational and
directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. This interface additionally defines methods

pollFirst()

and

pollLast()

that return and remove the lowest
and highest element, if one exists, else returning

null

.
Methods

subSet(E, boolean, E, boolean)

,

headSet(E, boolean)

, and

tailSet(E, boolean)

differ from the like-named

SortedSet

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Subsets of any

NavigableSet

must implement the

NavigableSet

interface.

The return values of navigation methods may be ambiguous in
implementations that permit

null

elements. However, even
in this case the result can be disambiguated by checking

contains(null)

. To avoid such issues, implementations of
this interface are encouraged to

not

permit insertion of

null

elements. (Note that sorted sets of

Comparable

elements intrinsically do not permit

null

.)

Methods

subSet(E, E)

,

headSet(E)

, and

tailSet(E)

are specified to return

SortedSet

to allow existing
implementations of

SortedSet

to be compatibly retrofitted to
implement

NavigableSet

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements maintained by this set

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### E
lower​(
E
e)

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

**Parameters:**
- e

- the value to match

**Returns:**
- the greatest element less than

e

,
or

null

if there is no such element

**Throws:**
- ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
- NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### E
floor​(
E
e)

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

**Parameters:**
- e

- the value to match

**Returns:**
- the greatest element less than or equal to

e

,
or

null

if there is no such element

**Throws:**
- ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
- NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### E
ceiling​(
E
e)

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

**Parameters:**
- e

- the value to match

**Returns:**
- the least element greater than or equal to

e

,
or

null

if there is no such element

**Throws:**
- ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
- NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### E
higher​(
E
e)

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

**Parameters:**
- e

- the value to match

**Returns:**
- the least element greater than

e

,
or

null

if there is no such element

**Throws:**
- ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
- NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### E
pollFirst()

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

**Returns:**
- the first element, or

null

if this set is empty

---

#### E
pollLast()

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

**Returns:**
- the last element, or

null

if this set is empty

---

#### Iterator
<
E
> iterator()

Returns an iterator over the elements in this set, in ascending order.

**Specified by:**
- iterator

in interface

Collection

<

E

>
- iterator

in interface

Iterable

<

E

>
- iterator

in interface

Set

<

E

>

**Returns:**
- an iterator over the elements in this set, in ascending order

---

#### NavigableSet
<
E
> descendingSet()

Returns a reverse order view of the elements contained in this set.
The descending set is backed by this set, so changes to the set are
reflected in the descending set, and vice-versa. If either set is
modified while an iteration over either set is in progress (except
through the iterator's own

remove

operation), the results of
the iteration are undefined.

The returned set has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

s.descendingSet().descendingSet()

returns a
view of

s

essentially equivalent to

s

.

**Returns:**
- a reverse order view of this set

---

#### Iterator
<
E
> descendingIterator()

Returns an iterator over the elements in this set, in descending order.
Equivalent in effect to

descendingSet().iterator()

.

**Returns:**
- an iterator over the elements in this set, in descending order

---

#### NavigableSet
<
E
> subSet​(
E
fromElement,
boolean fromInclusive,

E
toElement,
boolean toInclusive)

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

. If

fromElement

and

toElement

are equal, the returned set is empty unless

fromInclusive

and

toInclusive

are both true. The returned set
is backed by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all optional set
operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:**
- fromElement

- low endpoint of the returned set
- fromInclusive

-

true

if the low endpoint
is to be included in the returned view
- toElement

- high endpoint of the returned set
- toInclusive

-

true

if the high endpoint
is to be included in the returned view

**Returns:**
- a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive

**Throws:**
- ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
- NullPointerException

- if

fromElement

or

toElement

is null and this set does
not permit null elements
- IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range.

---

#### NavigableSet
<
E
> headSet​(
E
toElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

. The
returned set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:**
- toElement

- high endpoint of the returned set
- inclusive

-

true

if the high endpoint
is to be included in the returned view

**Returns:**
- a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

**Throws:**
- ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
- NullPointerException

- if

toElement

is null and
this set does not permit null elements
- IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

---

#### NavigableSet
<
E
> tailSet​(
E
fromElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.
The returned set is backed by this set, so changes in the returned set
are reflected in this set, and vice-versa. The returned set supports
all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:**
- fromElement

- low endpoint of the returned set
- inclusive

-

true

if the low endpoint
is to be included in the returned view

**Returns:**
- a view of the portion of this set whose elements are greater
than or equal to

fromElement

**Throws:**
- ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
- NullPointerException

- if

fromElement

is null
and this set does not permit null elements
- IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

---

#### SortedSet
<
E
> subSet​(
E
fromElement,

E
toElement)

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive. (If

fromElement

and

toElement

are
equal, the returned set is empty.) The returned set is backed
by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

subSet(fromElement, true, toElement, false)

.

**Specified by:**
- subSet

in interface

SortedSet

<

E

>

**Parameters:**
- fromElement

- low endpoint (inclusive) of the returned set
- toElement

- high endpoint (exclusive) of the returned set

**Returns:**
- a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive

**Throws:**
- ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
- NullPointerException

- if

fromElement

or

toElement

is null and this set does not permit null
elements
- IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range

---

#### SortedSet
<
E
> headSet​(
E
toElement)

Returns a view of the portion of this set whose elements are
strictly less than

toElement

. The returned set is
backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

headSet(toElement, false)

.

**Specified by:**
- headSet

in interface

SortedSet

<

E

>

**Parameters:**
- toElement

- high endpoint (exclusive) of the returned set

**Returns:**
- a view of the portion of this set whose elements are strictly
less than

toElement

**Throws:**
- ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
- NullPointerException

- if

toElement

is null and
this set does not permit null elements
- IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

---

#### SortedSet
<
E
> tailSet​(
E
fromElement)

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

. The returned
set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

tailSet(fromElement, true)

.

**Specified by:**
- tailSet

in interface

SortedSet

<

E

>

**Parameters:**
- fromElement

- low endpoint (inclusive) of the returned set

**Returns:**
- a view of the portion of this set whose elements are greater
than or equal to

fromElement

**Throws:**
- ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
- NullPointerException

- if

fromElement

is null
and this set does not permit null elements
- IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

---

### Additional Sections

#### Interface NavigableSet<E>

**Type Parameters:** E

- the type of elements maintained by this set

**All Superinterfaces:** Collection

<E>

,

Iterable

<E>

,

Set

<E>

,

SortedSet

<E>

**All Known Implementing Classes:** ConcurrentSkipListSet

,

TreeSet

```java
public interface
NavigableSet<E>

extends
SortedSet
<E>
```

A

SortedSet

extended with navigation methods reporting
closest matches for given search targets. Methods

lower(E)

,

floor(E)

,

ceiling(E)

, and

higher(E)

return elements
respectively less than, less than or equal, greater than or equal,
and greater than a given element, returning

null

if there
is no such element.

A

NavigableSet

may be accessed and traversed in either
ascending or descending order. The

descendingSet()

method
returns a view of the set with the senses of all relational and
directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. This interface additionally defines methods

pollFirst()

and

pollLast()

that return and remove the lowest
and highest element, if one exists, else returning

null

.
Methods

subSet(E, boolean, E, boolean)

,

headSet(E, boolean)

, and

tailSet(E, boolean)

differ from the like-named

SortedSet

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Subsets of any

NavigableSet

must implement the

NavigableSet

interface.

The return values of navigation methods may be ambiguous in
implementations that permit

null

elements. However, even
in this case the result can be disambiguated by checking

contains(null)

. To avoid such issues, implementations of
this interface are encouraged to

not

permit insertion of

null

elements. (Note that sorted sets of

Comparable

elements intrinsically do not permit

null

.)

Methods

subSet(E, E)

,

headSet(E)

, and

tailSet(E)

are specified to return

SortedSet

to allow existing
implementations of

SortedSet

to be compatibly retrofitted to
implement

NavigableSet

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

**Since:** 1.6

public interface

NavigableSet<E>

extends

SortedSet

<E>

A

SortedSet

extended with navigation methods reporting
closest matches for given search targets. Methods

lower(E)

,

floor(E)

,

ceiling(E)

, and

higher(E)

return elements
respectively less than, less than or equal, greater than or equal,
and greater than a given element, returning

null

if there
is no such element.

A

NavigableSet

may be accessed and traversed in either
ascending or descending order. The

descendingSet()

method
returns a view of the set with the senses of all relational and
directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. This interface additionally defines methods

pollFirst()

and

pollLast()

that return and remove the lowest
and highest element, if one exists, else returning

null

.
Methods

subSet(E, boolean, E, boolean)

,

headSet(E, boolean)

, and

tailSet(E, boolean)

differ from the like-named

SortedSet

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Subsets of any

NavigableSet

must implement the

NavigableSet

interface.

The return values of navigation methods may be ambiguous in
implementations that permit

null

elements. However, even
in this case the result can be disambiguated by checking

contains(null)

. To avoid such issues, implementations of
this interface are encouraged to

not

permit insertion of

null

elements. (Note that sorted sets of

Comparable

elements intrinsically do not permit

null

.)

Methods

subSet(E, E)

,

headSet(E)

, and

tailSet(E)

are specified to return

SortedSet

to allow existing
implementations of

SortedSet

to be compatibly retrofitted to
implement

NavigableSet

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

A

NavigableSet

may be accessed and traversed in either
ascending or descending order. The

descendingSet()

method
returns a view of the set with the senses of all relational and
directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. This interface additionally defines methods

pollFirst()

and

pollLast()

that return and remove the lowest
and highest element, if one exists, else returning

null

.
Methods

subSet(E, boolean, E, boolean)

,

headSet(E, boolean)

, and

tailSet(E, boolean)

differ from the like-named

SortedSet

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Subsets of any

NavigableSet

must implement the

NavigableSet

interface.

The return values of navigation methods may be ambiguous in
implementations that permit

null

elements. However, even
in this case the result can be disambiguated by checking

contains(null)

. To avoid such issues, implementations of
this interface are encouraged to

not

permit insertion of

null

elements. (Note that sorted sets of

Comparable

elements intrinsically do not permit

null

.)

Methods

subSet(E, E)

,

headSet(E)

, and

tailSet(E)

are specified to return

SortedSet

to allow existing
implementations of

SortedSet

to be compatibly retrofitted to
implement

NavigableSet

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

The return values of navigation methods may be ambiguous in
implementations that permit

null

elements. However, even
in this case the result can be disambiguated by checking

contains(null)

. To avoid such issues, implementations of
this interface are encouraged to

not

permit insertion of

null

elements. (Note that sorted sets of

Comparable

elements intrinsically do not permit

null

.)

Methods

subSet(E, E)

,

headSet(E)

, and

tailSet(E)

are specified to return

SortedSet

to allow existing
implementations of

SortedSet

to be compatibly retrofitted to
implement

NavigableSet

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

Methods

subSet(E, E)

,

headSet(E)

, and

tailSet(E)

are specified to return

SortedSet

to allow existing
implementations of

SortedSet

to be compatibly retrofitted to
implement

NavigableSet

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

This interface is a member of the

Java Collections Framework

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

E

ceiling

​(

E

e)

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

Iterator

<

E

>

descendingIterator

()

Returns an iterator over the elements in this set, in descending order.

NavigableSet

<

E

>

descendingSet

()

Returns a reverse order view of the elements contained in this set.

E

floor

​(

E

e)

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

SortedSet

<

E

>

headSet

​(

E

toElement)

Returns a view of the portion of this set whose elements are
strictly less than

toElement

.

NavigableSet

<

E

>

headSet

​(

E

toElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

.

E

higher

​(

E

e)

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

Iterator

<

E

>

iterator

()

Returns an iterator over the elements in this set, in ascending order.

E

lower

​(

E

e)

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

E

pollFirst

()

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

E

pollLast

()

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

NavigableSet

<

E

>

subSet

​(

E

fromElement,
boolean fromInclusive,

E

toElement,
boolean toInclusive)

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

.

SortedSet

<

E

>

subSet

​(

E

fromElement,

E

toElement)

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive.

SortedSet

<

E

>

tailSet

​(

E

fromElement)

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

.

NavigableSet

<

E

>

tailSet

​(

E

fromElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.

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

equals

,

hashCode

,

isEmpty

,

remove

,

removeAll

,

retainAll

,

size

,

toArray

,

toArray

- Methods declared in interface java.util.

SortedSet

comparator

,

first

,

last

,

spliterator

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

E

ceiling

​(

E

e)

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

Iterator

<

E

>

descendingIterator

()

Returns an iterator over the elements in this set, in descending order.

NavigableSet

<

E

>

descendingSet

()

Returns a reverse order view of the elements contained in this set.

E

floor

​(

E

e)

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

SortedSet

<

E

>

headSet

​(

E

toElement)

Returns a view of the portion of this set whose elements are
strictly less than

toElement

.

NavigableSet

<

E

>

headSet

​(

E

toElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

.

E

higher

​(

E

e)

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

Iterator

<

E

>

iterator

()

Returns an iterator over the elements in this set, in ascending order.

E

lower

​(

E

e)

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

E

pollFirst

()

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

E

pollLast

()

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

NavigableSet

<

E

>

subSet

​(

E

fromElement,
boolean fromInclusive,

E

toElement,
boolean toInclusive)

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

.

SortedSet

<

E

>

subSet

​(

E

fromElement,

E

toElement)

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive.

SortedSet

<

E

>

tailSet

​(

E

fromElement)

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

.

NavigableSet

<

E

>

tailSet

​(

E

fromElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.

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

equals

,

hashCode

,

isEmpty

,

remove

,

removeAll

,

retainAll

,

size

,

toArray

,

toArray

- Methods declared in interface java.util.

SortedSet

comparator

,

first

,

last

,

spliterator

---

#### Method Summary

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

Returns an iterator over the elements in this set, in descending order.

Returns a reverse order view of the elements contained in this set.

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

Returns a view of the portion of this set whose elements are
strictly less than

toElement

.

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

.

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

Returns an iterator over the elements in this set, in ascending order.

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

.

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive.

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

.

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.

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

equals

,

hashCode

,

isEmpty

,

remove

,

removeAll

,

retainAll

,

size

,

toArray

,

toArray

---

#### Methods declared in interface java.util. Set

Methods declared in interface java.util.

SortedSet

comparator

,

first

,

last

,

spliterator

---

#### Methods declared in interface java.util. SortedSet

============ METHOD DETAIL ==========

- Method Detail

- lower

```java
E
lower​(
E
e)
```

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the greatest element less than

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- floor

```java
E
floor​(
E
e)
```

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the greatest element less than or equal to

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- ceiling

```java
E
ceiling​(
E
e)
```

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the least element greater than or equal to

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- higher

```java
E
higher​(
E
e)
```

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the least element greater than

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- pollFirst

```java
E
pollFirst()
```

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

**Returns:** the first element, or

null

if this set is empty

- pollLast

```java
E
pollLast()
```

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

**Returns:** the last element, or

null

if this set is empty

- iterator

```java
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this set, in ascending order.

**Specified by:** iterator

in interface

Collection

<

E

>
**Specified by:** iterator

in interface

Iterable

<

E

>
**Specified by:** iterator

in interface

Set

<

E

>
**Returns:** an iterator over the elements in this set, in ascending order

- descendingSet

```java
NavigableSet
<
E
> descendingSet()
```

Returns a reverse order view of the elements contained in this set.
The descending set is backed by this set, so changes to the set are
reflected in the descending set, and vice-versa. If either set is
modified while an iteration over either set is in progress (except
through the iterator's own

remove

operation), the results of
the iteration are undefined.

The returned set has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

s.descendingSet().descendingSet()

returns a
view of

s

essentially equivalent to

s

.

**Returns:** a reverse order view of this set

- descendingIterator

```java
Iterator
<
E
> descendingIterator()
```

Returns an iterator over the elements in this set, in descending order.
Equivalent in effect to

descendingSet().iterator()

.

**Returns:** an iterator over the elements in this set, in descending order

- subSet

```java
NavigableSet
<
E
> subSet​(
E
fromElement,
boolean fromInclusive,

E
toElement,
boolean toInclusive)
```

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

. If

fromElement

and

toElement

are equal, the returned set is empty unless

fromInclusive

and

toInclusive

are both true. The returned set
is backed by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all optional set
operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** fromElement

- low endpoint of the returned set
**Parameters:** fromInclusive

-

true

if the low endpoint
is to be included in the returned view
**Parameters:** toElement

- high endpoint of the returned set
**Parameters:** toInclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive
**Throws:** ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
**Throws:** NullPointerException

- if

fromElement

or

toElement

is null and this set does
not permit null elements
**Throws:** IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range.

- headSet

```java
NavigableSet
<
E
> headSet​(
E
toElement,
boolean inclusive)
```

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

. The
returned set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** toElement

- high endpoint of the returned set
**Parameters:** inclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement
**Throws:** ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

toElement

is null and
this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

- tailSet

```java
NavigableSet
<
E
> tailSet​(
E
fromElement,
boolean inclusive)
```

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.
The returned set is backed by this set, so changes in the returned set
are reflected in this set, and vice-versa. The returned set supports
all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** fromElement

- low endpoint of the returned set
**Parameters:** inclusive

-

true

if the low endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements are greater
than or equal to

fromElement
**Throws:** ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

fromElement

is null
and this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

- subSet

```java
SortedSet
<
E
> subSet​(
E
fromElement,

E
toElement)
```

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive. (If

fromElement

and

toElement

are
equal, the returned set is empty.) The returned set is backed
by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

subSet(fromElement, true, toElement, false)

.

**Specified by:** subSet

in interface

SortedSet

<

E

>
**Parameters:** fromElement

- low endpoint (inclusive) of the returned set
**Parameters:** toElement

- high endpoint (exclusive) of the returned set
**Returns:** a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive
**Throws:** ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
**Throws:** NullPointerException

- if

fromElement

or

toElement

is null and this set does not permit null
elements
**Throws:** IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range

- headSet

```java
SortedSet
<
E
> headSet​(
E
toElement)
```

Returns a view of the portion of this set whose elements are
strictly less than

toElement

. The returned set is
backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

headSet(toElement, false)

.

**Specified by:** headSet

in interface

SortedSet

<

E

>
**Parameters:** toElement

- high endpoint (exclusive) of the returned set
**Returns:** a view of the portion of this set whose elements are strictly
less than

toElement
**Throws:** ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

toElement

is null and
this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

- tailSet

```java
SortedSet
<
E
> tailSet​(
E
fromElement)
```

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

. The returned
set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

tailSet(fromElement, true)

.

**Specified by:** tailSet

in interface

SortedSet

<

E

>
**Parameters:** fromElement

- low endpoint (inclusive) of the returned set
**Returns:** a view of the portion of this set whose elements are greater
than or equal to

fromElement
**Throws:** ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

fromElement

is null
and this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

Method Detail

- lower

```java
E
lower​(
E
e)
```

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the greatest element less than

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- floor

```java
E
floor​(
E
e)
```

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the greatest element less than or equal to

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- ceiling

```java
E
ceiling​(
E
e)
```

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the least element greater than or equal to

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- higher

```java
E
higher​(
E
e)
```

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the least element greater than

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

- pollFirst

```java
E
pollFirst()
```

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

**Returns:** the first element, or

null

if this set is empty

- pollLast

```java
E
pollLast()
```

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

**Returns:** the last element, or

null

if this set is empty

- iterator

```java
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this set, in ascending order.

**Specified by:** iterator

in interface

Collection

<

E

>
**Specified by:** iterator

in interface

Iterable

<

E

>
**Specified by:** iterator

in interface

Set

<

E

>
**Returns:** an iterator over the elements in this set, in ascending order

- descendingSet

```java
NavigableSet
<
E
> descendingSet()
```

Returns a reverse order view of the elements contained in this set.
The descending set is backed by this set, so changes to the set are
reflected in the descending set, and vice-versa. If either set is
modified while an iteration over either set is in progress (except
through the iterator's own

remove

operation), the results of
the iteration are undefined.

The returned set has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

s.descendingSet().descendingSet()

returns a
view of

s

essentially equivalent to

s

.

**Returns:** a reverse order view of this set

- descendingIterator

```java
Iterator
<
E
> descendingIterator()
```

Returns an iterator over the elements in this set, in descending order.
Equivalent in effect to

descendingSet().iterator()

.

**Returns:** an iterator over the elements in this set, in descending order

- subSet

```java
NavigableSet
<
E
> subSet​(
E
fromElement,
boolean fromInclusive,

E
toElement,
boolean toInclusive)
```

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

. If

fromElement

and

toElement

are equal, the returned set is empty unless

fromInclusive

and

toInclusive

are both true. The returned set
is backed by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all optional set
operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** fromElement

- low endpoint of the returned set
**Parameters:** fromInclusive

-

true

if the low endpoint
is to be included in the returned view
**Parameters:** toElement

- high endpoint of the returned set
**Parameters:** toInclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive
**Throws:** ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
**Throws:** NullPointerException

- if

fromElement

or

toElement

is null and this set does
not permit null elements
**Throws:** IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range.

- headSet

```java
NavigableSet
<
E
> headSet​(
E
toElement,
boolean inclusive)
```

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

. The
returned set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** toElement

- high endpoint of the returned set
**Parameters:** inclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement
**Throws:** ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

toElement

is null and
this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

- tailSet

```java
NavigableSet
<
E
> tailSet​(
E
fromElement,
boolean inclusive)
```

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.
The returned set is backed by this set, so changes in the returned set
are reflected in this set, and vice-versa. The returned set supports
all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** fromElement

- low endpoint of the returned set
**Parameters:** inclusive

-

true

if the low endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements are greater
than or equal to

fromElement
**Throws:** ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

fromElement

is null
and this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

- subSet

```java
SortedSet
<
E
> subSet​(
E
fromElement,

E
toElement)
```

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive. (If

fromElement

and

toElement

are
equal, the returned set is empty.) The returned set is backed
by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

subSet(fromElement, true, toElement, false)

.

**Specified by:** subSet

in interface

SortedSet

<

E

>
**Parameters:** fromElement

- low endpoint (inclusive) of the returned set
**Parameters:** toElement

- high endpoint (exclusive) of the returned set
**Returns:** a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive
**Throws:** ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
**Throws:** NullPointerException

- if

fromElement

or

toElement

is null and this set does not permit null
elements
**Throws:** IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range

- headSet

```java
SortedSet
<
E
> headSet​(
E
toElement)
```

Returns a view of the portion of this set whose elements are
strictly less than

toElement

. The returned set is
backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

headSet(toElement, false)

.

**Specified by:** headSet

in interface

SortedSet

<

E

>
**Parameters:** toElement

- high endpoint (exclusive) of the returned set
**Returns:** a view of the portion of this set whose elements are strictly
less than

toElement
**Throws:** ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

toElement

is null and
this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

- tailSet

```java
SortedSet
<
E
> tailSet​(
E
fromElement)
```

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

. The returned
set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

tailSet(fromElement, true)

.

**Specified by:** tailSet

in interface

SortedSet

<

E

>
**Parameters:** fromElement

- low endpoint (inclusive) of the returned set
**Returns:** a view of the portion of this set whose elements are greater
than or equal to

fromElement
**Throws:** ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

fromElement

is null
and this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

---

#### Method Detail

lower

```java
E
lower​(
E
e)
```

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the greatest element less than

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### lower

E

lower​(

E

e)

Returns the greatest element in this set strictly less than the
given element, or

null

if there is no such element.

floor

```java
E
floor​(
E
e)
```

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the greatest element less than or equal to

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### floor

E

floor​(

E

e)

Returns the greatest element in this set less than or equal to
the given element, or

null

if there is no such element.

ceiling

```java
E
ceiling​(
E
e)
```

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the least element greater than or equal to

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### ceiling

E

ceiling​(

E

e)

Returns the least element in this set greater than or equal to
the given element, or

null

if there is no such element.

higher

```java
E
higher​(
E
e)
```

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

**Parameters:** e

- the value to match
**Returns:** the least element greater than

e

,
or

null

if there is no such element
**Throws:** ClassCastException

- if the specified element cannot be
compared with the elements currently in the set
**Throws:** NullPointerException

- if the specified element is null
and this set does not permit null elements

---

#### higher

E

higher​(

E

e)

Returns the least element in this set strictly greater than the
given element, or

null

if there is no such element.

pollFirst

```java
E
pollFirst()
```

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

**Returns:** the first element, or

null

if this set is empty

---

#### pollFirst

E

pollFirst()

Retrieves and removes the first (lowest) element,
or returns

null

if this set is empty.

pollLast

```java
E
pollLast()
```

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

**Returns:** the last element, or

null

if this set is empty

---

#### pollLast

E

pollLast()

Retrieves and removes the last (highest) element,
or returns

null

if this set is empty.

iterator

```java
Iterator
<
E
> iterator()
```

Returns an iterator over the elements in this set, in ascending order.

**Specified by:** iterator

in interface

Collection

<

E

>
**Specified by:** iterator

in interface

Iterable

<

E

>
**Specified by:** iterator

in interface

Set

<

E

>
**Returns:** an iterator over the elements in this set, in ascending order

---

#### iterator

Iterator

<

E

> iterator()

Returns an iterator over the elements in this set, in ascending order.

descendingSet

```java
NavigableSet
<
E
> descendingSet()
```

Returns a reverse order view of the elements contained in this set.
The descending set is backed by this set, so changes to the set are
reflected in the descending set, and vice-versa. If either set is
modified while an iteration over either set is in progress (except
through the iterator's own

remove

operation), the results of
the iteration are undefined.

The returned set has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

s.descendingSet().descendingSet()

returns a
view of

s

essentially equivalent to

s

.

**Returns:** a reverse order view of this set

---

#### descendingSet

NavigableSet

<

E

> descendingSet()

Returns a reverse order view of the elements contained in this set.
The descending set is backed by this set, so changes to the set are
reflected in the descending set, and vice-versa. If either set is
modified while an iteration over either set is in progress (except
through the iterator's own

remove

operation), the results of
the iteration are undefined.

The returned set has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

s.descendingSet().descendingSet()

returns a
view of

s

essentially equivalent to

s

.

The returned set has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

s.descendingSet().descendingSet()

returns a
view of

s

essentially equivalent to

s

.

descendingIterator

```java
Iterator
<
E
> descendingIterator()
```

Returns an iterator over the elements in this set, in descending order.
Equivalent in effect to

descendingSet().iterator()

.

**Returns:** an iterator over the elements in this set, in descending order

---

#### descendingIterator

Iterator

<

E

> descendingIterator()

Returns an iterator over the elements in this set, in descending order.
Equivalent in effect to

descendingSet().iterator()

.

subSet

```java
NavigableSet
<
E
> subSet​(
E
fromElement,
boolean fromInclusive,

E
toElement,
boolean toInclusive)
```

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

. If

fromElement

and

toElement

are equal, the returned set is empty unless

fromInclusive

and

toInclusive

are both true. The returned set
is backed by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all optional set
operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** fromElement

- low endpoint of the returned set
**Parameters:** fromInclusive

-

true

if the low endpoint
is to be included in the returned view
**Parameters:** toElement

- high endpoint of the returned set
**Parameters:** toInclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive
**Throws:** ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
**Throws:** NullPointerException

- if

fromElement

or

toElement

is null and this set does
not permit null elements
**Throws:** IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range.

---

#### subSet

NavigableSet

<

E

> subSet​(

E

fromElement,
boolean fromInclusive,

E

toElement,
boolean toInclusive)

Returns a view of the portion of this set whose elements range from

fromElement

to

toElement

. If

fromElement

and

toElement

are equal, the returned set is empty unless

fromInclusive

and

toInclusive

are both true. The returned set
is backed by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all optional set
operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

headSet

```java
NavigableSet
<
E
> headSet​(
E
toElement,
boolean inclusive)
```

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

. The
returned set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** toElement

- high endpoint of the returned set
**Parameters:** inclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement
**Throws:** ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

toElement

is null and
this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

---

#### headSet

NavigableSet

<

E

> headSet​(

E

toElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are less than
(or equal to, if

inclusive

is true)

toElement

. The
returned set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

tailSet

```java
NavigableSet
<
E
> tailSet​(
E
fromElement,
boolean inclusive)
```

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.
The returned set is backed by this set, so changes in the returned set
are reflected in this set, and vice-versa. The returned set supports
all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

**Parameters:** fromElement

- low endpoint of the returned set
**Parameters:** inclusive

-

true

if the low endpoint
is to be included in the returned view
**Returns:** a view of the portion of this set whose elements are greater
than or equal to

fromElement
**Throws:** ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

fromElement

is null
and this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

---

#### tailSet

NavigableSet

<

E

> tailSet​(

E

fromElement,
boolean inclusive)

Returns a view of the portion of this set whose elements are greater
than (or equal to, if

inclusive

is true)

fromElement

.
The returned set is backed by this set, so changes in the returned set
are reflected in this set, and vice-versa. The returned set supports
all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

subSet

```java
SortedSet
<
E
> subSet​(
E
fromElement,

E
toElement)
```

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive. (If

fromElement

and

toElement

are
equal, the returned set is empty.) The returned set is backed
by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

subSet(fromElement, true, toElement, false)

.

**Specified by:** subSet

in interface

SortedSet

<

E

>
**Parameters:** fromElement

- low endpoint (inclusive) of the returned set
**Parameters:** toElement

- high endpoint (exclusive) of the returned set
**Returns:** a view of the portion of this set whose elements range from

fromElement

, inclusive, to

toElement

, exclusive
**Throws:** ClassCastException

- if

fromElement

and

toElement

cannot be compared to one another using this
set's comparator (or, if the set has no comparator, using
natural ordering). Implementations may, but are not required
to, throw this exception if

fromElement

or

toElement

cannot be compared to elements currently in
the set.
**Throws:** NullPointerException

- if

fromElement

or

toElement

is null and this set does not permit null
elements
**Throws:** IllegalArgumentException

- if

fromElement

is
greater than

toElement

; or if this set itself
has a restricted range, and

fromElement

or

toElement

lies outside the bounds of the range

---

#### subSet

SortedSet

<

E

> subSet​(

E

fromElement,

E

toElement)

Returns a view of the portion of this set whose elements range
from

fromElement

, inclusive, to

toElement

,
exclusive. (If

fromElement

and

toElement

are
equal, the returned set is empty.) The returned set is backed
by this set, so changes in the returned set are reflected in
this set, and vice-versa. The returned set supports all
optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

subSet(fromElement, true, toElement, false)

.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

subSet(fromElement, true, toElement, false)

.

Equivalent to

subSet(fromElement, true, toElement, false)

.

headSet

```java
SortedSet
<
E
> headSet​(
E
toElement)
```

Returns a view of the portion of this set whose elements are
strictly less than

toElement

. The returned set is
backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

headSet(toElement, false)

.

**Specified by:** headSet

in interface

SortedSet

<

E

>
**Parameters:** toElement

- high endpoint (exclusive) of the returned set
**Returns:** a view of the portion of this set whose elements are strictly
less than

toElement
**Throws:** ClassCastException

- if

toElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

toElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

toElement

is null and
this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

toElement

lies outside the
bounds of the range

---

#### headSet

SortedSet

<

E

> headSet​(

E

toElement)

Returns a view of the portion of this set whose elements are
strictly less than

toElement

. The returned set is
backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

headSet(toElement, false)

.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

headSet(toElement, false)

.

Equivalent to

headSet(toElement, false)

.

tailSet

```java
SortedSet
<
E
> tailSet​(
E
fromElement)
```

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

. The returned
set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

tailSet(fromElement, true)

.

**Specified by:** tailSet

in interface

SortedSet

<

E

>
**Parameters:** fromElement

- low endpoint (inclusive) of the returned set
**Returns:** a view of the portion of this set whose elements are greater
than or equal to

fromElement
**Throws:** ClassCastException

- if

fromElement

is not compatible
with this set's comparator (or, if the set has no comparator,
if

fromElement

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromElement

cannot be compared to elements
currently in the set.
**Throws:** NullPointerException

- if

fromElement

is null
and this set does not permit null elements
**Throws:** IllegalArgumentException

- if this set itself has a
restricted range, and

fromElement

lies outside the
bounds of the range

---

#### tailSet

SortedSet

<

E

> tailSet​(

E

fromElement)

Returns a view of the portion of this set whose elements are
greater than or equal to

fromElement

. The returned
set is backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

tailSet(fromElement, true)

.

The returned set will throw an

IllegalArgumentException

on an attempt to insert an element outside its range.

Equivalent to

tailSet(fromElement, true)

.

Equivalent to

tailSet(fromElement, true)

.

---

