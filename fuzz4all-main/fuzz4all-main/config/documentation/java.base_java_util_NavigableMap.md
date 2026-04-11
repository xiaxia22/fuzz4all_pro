# Interface NavigableMap<K,​V>

**Source:** `java.base\java\util\NavigableMap.html`

### Class Description

```java
public interface
NavigableMap<K,​V>

extends
SortedMap
<K,​V>
```

A

SortedMap

extended with navigation methods returning the
closest matches for given search targets. Methods

lowerEntry(K)

,

floorEntry(K)

,

ceilingEntry(K)

,
and

higherEntry(K)

return

Map.Entry

objects
associated with keys respectively less than, less than or equal,
greater than or equal, and greater than a given key, returning

null

if there is no such key. Similarly, methods

lowerKey(K)

,

floorKey(K)

,

ceilingKey(K)

, and

higherKey(K)

return only the associated keys. All of these
methods are designed for locating, not traversing entries.

A

NavigableMap

may be accessed and traversed in either
ascending or descending key order. The

descendingMap()

method returns a view of the map with the senses of all relational
and directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. Methods

subMap(K, boolean, K, boolean)

,

headMap(K, boolean)

, and

tailMap(K, boolean)

differ from the like-named

SortedMap

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Submaps of any

NavigableMap

must implement the

NavigableMap

interface.

This interface additionally defines methods

firstEntry()

,

pollFirstEntry()

,

lastEntry()

, and

pollLastEntry()

that return and/or remove the least and
greatest mappings, if any exist, else returning

null

.

Implementations of entry-returning methods are expected to
return

Map.Entry

pairs representing snapshots of mappings
at the time they were produced, and thus generally do

not

support the optional

Entry.setValue

method. Note however
that it is possible to change mappings in the associated map using
method

put

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

**Type Parameters:** K

- the type of keys maintained by this map
**Type Parameters:** V

- the type of mapped values

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Map.Entry
<
K
,​
V
> lowerEntry​(
K
key)

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

**Parameters:**
- key

- the key

**Returns:**
- an entry with the greatest key less than

key

,
or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### K
lowerKey​(
K
key)

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Parameters:**
- key

- the key

**Returns:**
- the greatest key less than

key

,
or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### Map.Entry
<
K
,​
V
> floorEntry​(
K
key)

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

**Parameters:**
- key

- the key

**Returns:**
- an entry with the greatest key less than or equal to

key

, or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### K
floorKey​(
K
key)

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Parameters:**
- key

- the key

**Returns:**
- the greatest key less than or equal to

key

,
or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### Map.Entry
<
K
,​
V
> ceilingEntry​(
K
key)

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

**Parameters:**
- key

- the key

**Returns:**
- an entry with the least key greater than or equal to

key

, or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### K
ceilingKey​(
K
key)

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Parameters:**
- key

- the key

**Returns:**
- the least key greater than or equal to

key

,
or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### Map.Entry
<
K
,​
V
> higherEntry​(
K
key)

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

**Parameters:**
- key

- the key

**Returns:**
- an entry with the least key greater than

key

,
or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### K
higherKey​(
K
key)

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Parameters:**
- key

- the key

**Returns:**
- the least key greater than

key

,
or

null

if there is no such key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### Map.Entry
<
K
,​
V
> firstEntry()

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

**Returns:**
- an entry with the least key,
or

null

if this map is empty

---

#### Map.Entry
<
K
,​
V
> lastEntry()

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

**Returns:**
- an entry with the greatest key,
or

null

if this map is empty

---

#### Map.Entry
<
K
,​
V
> pollFirstEntry()

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

**Returns:**
- the removed first entry of this map,
or

null

if this map is empty

---

#### Map.Entry
<
K
,​
V
> pollLastEntry()

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

**Returns:**
- the removed last entry of this map,
or

null

if this map is empty

---

#### NavigableMap
<
K
,​
V
> descendingMap()

Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa. If either map is
modified while an iteration over a collection view of either map
is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined.

The returned map has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

m.descendingMap().descendingMap()

returns a
view of

m

essentially equivalent to

m

.

**Returns:**
- a reverse order view of this map

---

#### NavigableSet
<
K
> navigableKeySet()

Returns a

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:**
- a navigable set view of the keys in this map

---

#### NavigableSet
<
K
> descendingKeySet()

Returns a reverse order

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:**
- a reverse order navigable set view of the keys in this map

---

#### NavigableMap
<
K
,​
V
> subMap​(
K
fromKey,
boolean fromInclusive,

K
toKey,
boolean toInclusive)

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

. If

fromKey

and

toKey

are equal, the returned map is empty unless

fromInclusive

and

toInclusive

are both true. The
returned map is backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.

**Parameters:**
- fromKey

- low endpoint of the keys in the returned map
- fromInclusive

-

true

if the low endpoint
is to be included in the returned view
- toKey

- high endpoint of the keys in the returned map
- toInclusive

-

true

if the high endpoint
is to be included in the returned view

**Returns:**
- a view of the portion of this map whose keys range from

fromKey

to

toKey

**Throws:**
- ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
- NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
- IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

---

#### NavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:**
- toKey

- high endpoint of the keys in the returned map
- inclusive

-

true

if the high endpoint
is to be included in the returned view

**Returns:**
- a view of the portion of this map whose keys are less than
(or equal to, if

inclusive

is true)

toKey

**Throws:**
- ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
- NullPointerException

- if

toKey

is null
and this map does not permit null keys
- IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### NavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:**
- fromKey

- low endpoint of the keys in the returned map
- inclusive

-

true

if the low endpoint
is to be included in the returned view

**Returns:**
- a view of the portion of this map whose keys are greater than
(or equal to, if

inclusive

is true)

fromKey

**Throws:**
- ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
- NullPointerException

- if

fromKey

is null
and this map does not permit null keys
- IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### SortedMap
<
K
,​
V
> subMap​(
K
fromKey,

K
toKey)

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive. (If

fromKey

and

toKey

are equal, the returned map
is empty.) The returned map is backed by this map, so changes
in the returned map are reflected in this map, and vice-versa.
The returned map supports all optional map operations that this
map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

subMap(fromKey, true, toKey, false)

.

**Specified by:**
- subMap

in interface

SortedMap

<

K

,​

V

>

**Parameters:**
- fromKey

- low endpoint (inclusive) of the keys in the returned map
- toKey

- high endpoint (exclusive) of the keys in the returned map

**Returns:**
- a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive

**Throws:**
- ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
- NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
- IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

---

#### SortedMap
<
K
,​
V
> headMap​(
K
toKey)

Returns a view of the portion of this map whose keys are
strictly less than

toKey

. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

headMap(toKey, false)

.

**Specified by:**
- headMap

in interface

SortedMap

<

K

,​

V

>

**Parameters:**
- toKey

- high endpoint (exclusive) of the keys in the returned map

**Returns:**
- a view of the portion of this map whose keys are strictly
less than

toKey

**Throws:**
- ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
- NullPointerException

- if

toKey

is null and
this map does not permit null keys
- IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### SortedMap
<
K
,​
V
> tailMap​(
K
fromKey)

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

tailMap(fromKey, true)

.

**Specified by:**
- tailMap

in interface

SortedMap

<

K

,​

V

>

**Parameters:**
- fromKey

- low endpoint (inclusive) of the keys in the returned map

**Returns:**
- a view of the portion of this map whose keys are greater
than or equal to

fromKey

**Throws:**
- ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
- NullPointerException

- if

fromKey

is null and
this map does not permit null keys
- IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

### Additional Sections

#### Interface NavigableMap<K,​V>

**Type Parameters:** K

- the type of keys maintained by this map
**Type Parameters:** V

- the type of mapped values

**All Superinterfaces:** Map

<K,​V>

,

SortedMap

<K,​V>

**All Known Subinterfaces:** ConcurrentNavigableMap

<K,​V>

**All Known Implementing Classes:** ConcurrentSkipListMap

,

TreeMap

```java
public interface
NavigableMap<K,​V>

extends
SortedMap
<K,​V>
```

A

SortedMap

extended with navigation methods returning the
closest matches for given search targets. Methods

lowerEntry(K)

,

floorEntry(K)

,

ceilingEntry(K)

,
and

higherEntry(K)

return

Map.Entry

objects
associated with keys respectively less than, less than or equal,
greater than or equal, and greater than a given key, returning

null

if there is no such key. Similarly, methods

lowerKey(K)

,

floorKey(K)

,

ceilingKey(K)

, and

higherKey(K)

return only the associated keys. All of these
methods are designed for locating, not traversing entries.

A

NavigableMap

may be accessed and traversed in either
ascending or descending key order. The

descendingMap()

method returns a view of the map with the senses of all relational
and directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. Methods

subMap(K, boolean, K, boolean)

,

headMap(K, boolean)

, and

tailMap(K, boolean)

differ from the like-named

SortedMap

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Submaps of any

NavigableMap

must implement the

NavigableMap

interface.

This interface additionally defines methods

firstEntry()

,

pollFirstEntry()

,

lastEntry()

, and

pollLastEntry()

that return and/or remove the least and
greatest mappings, if any exist, else returning

null

.

Implementations of entry-returning methods are expected to
return

Map.Entry

pairs representing snapshots of mappings
at the time they were produced, and thus generally do

not

support the optional

Entry.setValue

method. Note however
that it is possible to change mappings in the associated map using
method

put

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

**Since:** 1.6

public interface

NavigableMap<K,​V>

extends

SortedMap

<K,​V>

A

SortedMap

extended with navigation methods returning the
closest matches for given search targets. Methods

lowerEntry(K)

,

floorEntry(K)

,

ceilingEntry(K)

,
and

higherEntry(K)

return

Map.Entry

objects
associated with keys respectively less than, less than or equal,
greater than or equal, and greater than a given key, returning

null

if there is no such key. Similarly, methods

lowerKey(K)

,

floorKey(K)

,

ceilingKey(K)

, and

higherKey(K)

return only the associated keys. All of these
methods are designed for locating, not traversing entries.

A

NavigableMap

may be accessed and traversed in either
ascending or descending key order. The

descendingMap()

method returns a view of the map with the senses of all relational
and directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. Methods

subMap(K, boolean, K, boolean)

,

headMap(K, boolean)

, and

tailMap(K, boolean)

differ from the like-named

SortedMap

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Submaps of any

NavigableMap

must implement the

NavigableMap

interface.

This interface additionally defines methods

firstEntry()

,

pollFirstEntry()

,

lastEntry()

, and

pollLastEntry()

that return and/or remove the least and
greatest mappings, if any exist, else returning

null

.

Implementations of entry-returning methods are expected to
return

Map.Entry

pairs representing snapshots of mappings
at the time they were produced, and thus generally do

not

support the optional

Entry.setValue

method. Note however
that it is possible to change mappings in the associated map using
method

put

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

A

NavigableMap

may be accessed and traversed in either
ascending or descending key order. The

descendingMap()

method returns a view of the map with the senses of all relational
and directional methods inverted. The performance of ascending
operations and views is likely to be faster than that of descending
ones. Methods

subMap(K, boolean, K, boolean)

,

headMap(K, boolean)

, and

tailMap(K, boolean)

differ from the like-named

SortedMap

methods in accepting
additional arguments describing whether lower and upper bounds are
inclusive versus exclusive. Submaps of any

NavigableMap

must implement the

NavigableMap

interface.

This interface additionally defines methods

firstEntry()

,

pollFirstEntry()

,

lastEntry()

, and

pollLastEntry()

that return and/or remove the least and
greatest mappings, if any exist, else returning

null

.

Implementations of entry-returning methods are expected to
return

Map.Entry

pairs representing snapshots of mappings
at the time they were produced, and thus generally do

not

support the optional

Entry.setValue

method. Note however
that it is possible to change mappings in the associated map using
method

put

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

This interface additionally defines methods

firstEntry()

,

pollFirstEntry()

,

lastEntry()

, and

pollLastEntry()

that return and/or remove the least and
greatest mappings, if any exist, else returning

null

.

Implementations of entry-returning methods are expected to
return

Map.Entry

pairs representing snapshots of mappings
at the time they were produced, and thus generally do

not

support the optional

Entry.setValue

method. Note however
that it is possible to change mappings in the associated map using
method

put

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

Implementations of entry-returning methods are expected to
return

Map.Entry

pairs representing snapshots of mappings
at the time they were produced, and thus generally do

not

support the optional

Entry.setValue

method. Note however
that it is possible to change mappings in the associated map using
method

put

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

Methods

subMap(K, K)

,

headMap(K)

, and

tailMap(K)

are specified to return

SortedMap

to allow existing
implementations of

SortedMap

to be compatibly retrofitted to
implement

NavigableMap

, but extensions and implementations
of this interface are encouraged to override these methods to return

NavigableMap

. Similarly,

SortedMap.keySet()

can be overridden to return

NavigableSet

.

This interface is a member of the

Java Collections Framework

.

This interface is a member of the

Java Collections Framework

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Map.Entry

<

K

,​

V

>

ceilingEntry

​(

K

key)

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

K

ceilingKey

​(

K

key)

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

NavigableSet

<

K

>

descendingKeySet

()

Returns a reverse order

NavigableSet

view of the keys contained in this map.

NavigableMap

<

K

,​

V

>

descendingMap

()

Returns a reverse order view of the mappings contained in this map.

Map.Entry

<

K

,​

V

>

firstEntry

()

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

Map.Entry

<

K

,​

V

>

floorEntry

​(

K

key)

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

K

floorKey

​(

K

key)

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

SortedMap

<

K

,​

V

>

headMap

​(

K

toKey)

Returns a view of the portion of this map whose keys are
strictly less than

toKey

.

NavigableMap

<

K

,​

V

>

headMap

​(

K

toKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

.

Map.Entry

<

K

,​

V

>

higherEntry

​(

K

key)

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

K

higherKey

​(

K

key)

Returns the least key strictly greater than the given key, or

null

if there is no such key.

Map.Entry

<

K

,​

V

>

lastEntry

()

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

Map.Entry

<

K

,​

V

>

lowerEntry

​(

K

key)

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

K

lowerKey

​(

K

key)

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

NavigableSet

<

K

>

navigableKeySet

()

Returns a

NavigableSet

view of the keys contained in this map.

Map.Entry

<

K

,​

V

>

pollFirstEntry

()

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

Map.Entry

<

K

,​

V

>

pollLastEntry

()

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

NavigableMap

<

K

,​

V

>

subMap

​(

K

fromKey,
boolean fromInclusive,

K

toKey,
boolean toInclusive)

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

.

SortedMap

<

K

,​

V

>

subMap

​(

K

fromKey,

K

toKey)

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive.

SortedMap

<

K

,​

V

>

tailMap

​(

K

fromKey)

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

.

NavigableMap

<

K

,​

V

>

tailMap

​(

K

fromKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

.

- Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsKey

,

containsValue

,

equals

,

forEach

,

get

,

getOrDefault

,

hashCode

,

isEmpty

,

merge

,

put

,

putAll

,

putIfAbsent

,

remove

,

remove

,

replace

,

replace

,

replaceAll

,

size

- Methods declared in interface java.util.

SortedMap

comparator

,

entrySet

,

firstKey

,

keySet

,

lastKey

,

values

Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

---

#### Nested classes/interfaces declared in interface java.util. Map

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Map.Entry

<

K

,​

V

>

ceilingEntry

​(

K

key)

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

K

ceilingKey

​(

K

key)

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

NavigableSet

<

K

>

descendingKeySet

()

Returns a reverse order

NavigableSet

view of the keys contained in this map.

NavigableMap

<

K

,​

V

>

descendingMap

()

Returns a reverse order view of the mappings contained in this map.

Map.Entry

<

K

,​

V

>

firstEntry

()

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

Map.Entry

<

K

,​

V

>

floorEntry

​(

K

key)

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

K

floorKey

​(

K

key)

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

SortedMap

<

K

,​

V

>

headMap

​(

K

toKey)

Returns a view of the portion of this map whose keys are
strictly less than

toKey

.

NavigableMap

<

K

,​

V

>

headMap

​(

K

toKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

.

Map.Entry

<

K

,​

V

>

higherEntry

​(

K

key)

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

K

higherKey

​(

K

key)

Returns the least key strictly greater than the given key, or

null

if there is no such key.

Map.Entry

<

K

,​

V

>

lastEntry

()

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

Map.Entry

<

K

,​

V

>

lowerEntry

​(

K

key)

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

K

lowerKey

​(

K

key)

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

NavigableSet

<

K

>

navigableKeySet

()

Returns a

NavigableSet

view of the keys contained in this map.

Map.Entry

<

K

,​

V

>

pollFirstEntry

()

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

Map.Entry

<

K

,​

V

>

pollLastEntry

()

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

NavigableMap

<

K

,​

V

>

subMap

​(

K

fromKey,
boolean fromInclusive,

K

toKey,
boolean toInclusive)

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

.

SortedMap

<

K

,​

V

>

subMap

​(

K

fromKey,

K

toKey)

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive.

SortedMap

<

K

,​

V

>

tailMap

​(

K

fromKey)

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

.

NavigableMap

<

K

,​

V

>

tailMap

​(

K

fromKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

.

- Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsKey

,

containsValue

,

equals

,

forEach

,

get

,

getOrDefault

,

hashCode

,

isEmpty

,

merge

,

put

,

putAll

,

putIfAbsent

,

remove

,

remove

,

replace

,

replace

,

replaceAll

,

size

- Methods declared in interface java.util.

SortedMap

comparator

,

entrySet

,

firstKey

,

keySet

,

lastKey

,

values

---

#### Method Summary

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

Returns a reverse order

NavigableSet

view of the keys contained in this map.

Returns a reverse order view of the mappings contained in this map.

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

Returns a view of the portion of this map whose keys are
strictly less than

toKey

.

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

.

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

Returns the least key strictly greater than the given key, or

null

if there is no such key.

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

Returns a

NavigableSet

view of the keys contained in this map.

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

.

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive.

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

.

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

.

Methods declared in interface java.util.

Map

clear

,

compute

,

computeIfAbsent

,

computeIfPresent

,

containsKey

,

containsValue

,

equals

,

forEach

,

get

,

getOrDefault

,

hashCode

,

isEmpty

,

merge

,

put

,

putAll

,

putIfAbsent

,

remove

,

remove

,

replace

,

replace

,

replaceAll

,

size

---

#### Methods declared in interface java.util. Map

Methods declared in interface java.util.

SortedMap

comparator

,

entrySet

,

firstKey

,

keySet

,

lastKey

,

values

---

#### Methods declared in interface java.util. SortedMap

============ METHOD DETAIL ==========

- Method Detail

- lowerEntry

```java
Map.Entry
<
K
,​
V
> lowerEntry​(
K
key)
```

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

**Parameters:** key

- the key
**Returns:** an entry with the greatest key less than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- lowerKey

```java
K
lowerKey​(
K
key)
```

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the greatest key less than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- floorEntry

```java
Map.Entry
<
K
,​
V
> floorEntry​(
K
key)
```

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the greatest key less than or equal to

key

, or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- floorKey

```java
K
floorKey​(
K
key)
```

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the greatest key less than or equal to

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- ceilingEntry

```java
Map.Entry
<
K
,​
V
> ceilingEntry​(
K
key)
```

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the least key greater than or equal to

key

, or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- ceilingKey

```java
K
ceilingKey​(
K
key)
```

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the least key greater than or equal to

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- higherEntry

```java
Map.Entry
<
K
,​
V
> higherEntry​(
K
key)
```

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the least key greater than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- higherKey

```java
K
higherKey​(
K
key)
```

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the least key greater than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- firstEntry

```java
Map.Entry
<
K
,​
V
> firstEntry()
```

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

**Returns:** an entry with the least key,
or

null

if this map is empty

- lastEntry

```java
Map.Entry
<
K
,​
V
> lastEntry()
```

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

**Returns:** an entry with the greatest key,
or

null

if this map is empty

- pollFirstEntry

```java
Map.Entry
<
K
,​
V
> pollFirstEntry()
```

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

**Returns:** the removed first entry of this map,
or

null

if this map is empty

- pollLastEntry

```java
Map.Entry
<
K
,​
V
> pollLastEntry()
```

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

**Returns:** the removed last entry of this map,
or

null

if this map is empty

- descendingMap

```java
NavigableMap
<
K
,​
V
> descendingMap()
```

Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa. If either map is
modified while an iteration over a collection view of either map
is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined.

The returned map has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

m.descendingMap().descendingMap()

returns a
view of

m

essentially equivalent to

m

.

**Returns:** a reverse order view of this map

- navigableKeySet

```java
NavigableSet
<
K
> navigableKeySet()
```

Returns a

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:** a navigable set view of the keys in this map

- descendingKeySet

```java
NavigableSet
<
K
> descendingKeySet()
```

Returns a reverse order

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:** a reverse order navigable set view of the keys in this map

- subMap

```java
NavigableMap
<
K
,​
V
> subMap​(
K
fromKey,
boolean fromInclusive,

K
toKey,
boolean toInclusive)
```

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

. If

fromKey

and

toKey

are equal, the returned map is empty unless

fromInclusive

and

toInclusive

are both true. The
returned map is backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.

**Parameters:** fromKey

- low endpoint of the keys in the returned map
**Parameters:** fromInclusive

-

true

if the low endpoint
is to be included in the returned view
**Parameters:** toKey

- high endpoint of the keys in the returned map
**Parameters:** toInclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys range from

fromKey

to

toKey
**Throws:** ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
**Throws:** NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
**Throws:** IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

- headMap

```java
NavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)
```

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:** toKey

- high endpoint of the keys in the returned map
**Parameters:** inclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys are less than
(or equal to, if

inclusive

is true)

toKey
**Throws:** ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

toKey

is null
and this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
NavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)
```

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:** fromKey

- low endpoint of the keys in the returned map
**Parameters:** inclusive

-

true

if the low endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys are greater than
(or equal to, if

inclusive

is true)

fromKey
**Throws:** ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

fromKey

is null
and this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

- subMap

```java
SortedMap
<
K
,​
V
> subMap​(
K
fromKey,

K
toKey)
```

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive. (If

fromKey

and

toKey

are equal, the returned map
is empty.) The returned map is backed by this map, so changes
in the returned map are reflected in this map, and vice-versa.
The returned map supports all optional map operations that this
map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

subMap(fromKey, true, toKey, false)

.

**Specified by:** subMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** fromKey

- low endpoint (inclusive) of the keys in the returned map
**Parameters:** toKey

- high endpoint (exclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive
**Throws:** ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
**Throws:** NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
**Throws:** IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

- headMap

```java
SortedMap
<
K
,​
V
> headMap​(
K
toKey)
```

Returns a view of the portion of this map whose keys are
strictly less than

toKey

. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

headMap(toKey, false)

.

**Specified by:** headMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** toKey

- high endpoint (exclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys are strictly
less than

toKey
**Throws:** ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

toKey

is null and
this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
SortedMap
<
K
,​
V
> tailMap​(
K
fromKey)
```

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

tailMap(fromKey, true)

.

**Specified by:** tailMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** fromKey

- low endpoint (inclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys are greater
than or equal to

fromKey
**Throws:** ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

fromKey

is null and
this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

Method Detail

- lowerEntry

```java
Map.Entry
<
K
,​
V
> lowerEntry​(
K
key)
```

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

**Parameters:** key

- the key
**Returns:** an entry with the greatest key less than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- lowerKey

```java
K
lowerKey​(
K
key)
```

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the greatest key less than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- floorEntry

```java
Map.Entry
<
K
,​
V
> floorEntry​(
K
key)
```

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the greatest key less than or equal to

key

, or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- floorKey

```java
K
floorKey​(
K
key)
```

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the greatest key less than or equal to

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- ceilingEntry

```java
Map.Entry
<
K
,​
V
> ceilingEntry​(
K
key)
```

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the least key greater than or equal to

key

, or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- ceilingKey

```java
K
ceilingKey​(
K
key)
```

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the least key greater than or equal to

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- higherEntry

```java
Map.Entry
<
K
,​
V
> higherEntry​(
K
key)
```

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the least key greater than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- higherKey

```java
K
higherKey​(
K
key)
```

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the least key greater than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

- firstEntry

```java
Map.Entry
<
K
,​
V
> firstEntry()
```

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

**Returns:** an entry with the least key,
or

null

if this map is empty

- lastEntry

```java
Map.Entry
<
K
,​
V
> lastEntry()
```

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

**Returns:** an entry with the greatest key,
or

null

if this map is empty

- pollFirstEntry

```java
Map.Entry
<
K
,​
V
> pollFirstEntry()
```

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

**Returns:** the removed first entry of this map,
or

null

if this map is empty

- pollLastEntry

```java
Map.Entry
<
K
,​
V
> pollLastEntry()
```

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

**Returns:** the removed last entry of this map,
or

null

if this map is empty

- descendingMap

```java
NavigableMap
<
K
,​
V
> descendingMap()
```

Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa. If either map is
modified while an iteration over a collection view of either map
is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined.

The returned map has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

m.descendingMap().descendingMap()

returns a
view of

m

essentially equivalent to

m

.

**Returns:** a reverse order view of this map

- navigableKeySet

```java
NavigableSet
<
K
> navigableKeySet()
```

Returns a

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:** a navigable set view of the keys in this map

- descendingKeySet

```java
NavigableSet
<
K
> descendingKeySet()
```

Returns a reverse order

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:** a reverse order navigable set view of the keys in this map

- subMap

```java
NavigableMap
<
K
,​
V
> subMap​(
K
fromKey,
boolean fromInclusive,

K
toKey,
boolean toInclusive)
```

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

. If

fromKey

and

toKey

are equal, the returned map is empty unless

fromInclusive

and

toInclusive

are both true. The
returned map is backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.

**Parameters:** fromKey

- low endpoint of the keys in the returned map
**Parameters:** fromInclusive

-

true

if the low endpoint
is to be included in the returned view
**Parameters:** toKey

- high endpoint of the keys in the returned map
**Parameters:** toInclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys range from

fromKey

to

toKey
**Throws:** ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
**Throws:** NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
**Throws:** IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

- headMap

```java
NavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)
```

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:** toKey

- high endpoint of the keys in the returned map
**Parameters:** inclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys are less than
(or equal to, if

inclusive

is true)

toKey
**Throws:** ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

toKey

is null
and this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
NavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)
```

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:** fromKey

- low endpoint of the keys in the returned map
**Parameters:** inclusive

-

true

if the low endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys are greater than
(or equal to, if

inclusive

is true)

fromKey
**Throws:** ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

fromKey

is null
and this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

- subMap

```java
SortedMap
<
K
,​
V
> subMap​(
K
fromKey,

K
toKey)
```

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive. (If

fromKey

and

toKey

are equal, the returned map
is empty.) The returned map is backed by this map, so changes
in the returned map are reflected in this map, and vice-versa.
The returned map supports all optional map operations that this
map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

subMap(fromKey, true, toKey, false)

.

**Specified by:** subMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** fromKey

- low endpoint (inclusive) of the keys in the returned map
**Parameters:** toKey

- high endpoint (exclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive
**Throws:** ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
**Throws:** NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
**Throws:** IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

- headMap

```java
SortedMap
<
K
,​
V
> headMap​(
K
toKey)
```

Returns a view of the portion of this map whose keys are
strictly less than

toKey

. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

headMap(toKey, false)

.

**Specified by:** headMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** toKey

- high endpoint (exclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys are strictly
less than

toKey
**Throws:** ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

toKey

is null and
this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
SortedMap
<
K
,​
V
> tailMap​(
K
fromKey)
```

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

tailMap(fromKey, true)

.

**Specified by:** tailMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** fromKey

- low endpoint (inclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys are greater
than or equal to

fromKey
**Throws:** ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

fromKey

is null and
this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### Method Detail

lowerEntry

```java
Map.Entry
<
K
,​
V
> lowerEntry​(
K
key)
```

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

**Parameters:** key

- the key
**Returns:** an entry with the greatest key less than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### lowerEntry

Map.Entry

<

K

,​

V

> lowerEntry​(

K

key)

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

lowerKey

```java
K
lowerKey​(
K
key)
```

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the greatest key less than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### lowerKey

K

lowerKey​(

K

key)

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

floorEntry

```java
Map.Entry
<
K
,​
V
> floorEntry​(
K
key)
```

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the greatest key less than or equal to

key

, or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### floorEntry

Map.Entry

<

K

,​

V

> floorEntry​(

K

key)

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

floorKey

```java
K
floorKey​(
K
key)
```

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the greatest key less than or equal to

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### floorKey

K

floorKey​(

K

key)

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

ceilingEntry

```java
Map.Entry
<
K
,​
V
> ceilingEntry​(
K
key)
```

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the least key greater than or equal to

key

, or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### ceilingEntry

Map.Entry

<

K

,​

V

> ceilingEntry​(

K

key)

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such key.

ceilingKey

```java
K
ceilingKey​(
K
key)
```

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the least key greater than or equal to

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### ceilingKey

K

ceilingKey​(

K

key)

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

higherEntry

```java
Map.Entry
<
K
,​
V
> higherEntry​(
K
key)
```

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

**Parameters:** key

- the key
**Returns:** an entry with the least key greater than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### higherEntry

Map.Entry

<

K

,​

V

> higherEntry​(

K

key)

Returns a key-value mapping associated with the least key
strictly greater than the given key, or

null

if there
is no such key.

higherKey

```java
K
higherKey​(
K
key)
```

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Parameters:** key

- the key
**Returns:** the least key greater than

key

,
or

null

if there is no such key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null
and this map does not permit null keys

---

#### higherKey

K

higherKey​(

K

key)

Returns the least key strictly greater than the given key, or

null

if there is no such key.

firstEntry

```java
Map.Entry
<
K
,​
V
> firstEntry()
```

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

**Returns:** an entry with the least key,
or

null

if this map is empty

---

#### firstEntry

Map.Entry

<

K

,​

V

> firstEntry()

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

lastEntry

```java
Map.Entry
<
K
,​
V
> lastEntry()
```

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

**Returns:** an entry with the greatest key,
or

null

if this map is empty

---

#### lastEntry

Map.Entry

<

K

,​

V

> lastEntry()

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

pollFirstEntry

```java
Map.Entry
<
K
,​
V
> pollFirstEntry()
```

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

**Returns:** the removed first entry of this map,
or

null

if this map is empty

---

#### pollFirstEntry

Map.Entry

<

K

,​

V

> pollFirstEntry()

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

pollLastEntry

```java
Map.Entry
<
K
,​
V
> pollLastEntry()
```

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

**Returns:** the removed last entry of this map,
or

null

if this map is empty

---

#### pollLastEntry

Map.Entry

<

K

,​

V

> pollLastEntry()

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

descendingMap

```java
NavigableMap
<
K
,​
V
> descendingMap()
```

Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa. If either map is
modified while an iteration over a collection view of either map
is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined.

The returned map has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

m.descendingMap().descendingMap()

returns a
view of

m

essentially equivalent to

m

.

**Returns:** a reverse order view of this map

---

#### descendingMap

NavigableMap

<

K

,​

V

> descendingMap()

Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa. If either map is
modified while an iteration over a collection view of either map
is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined.

The returned map has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

m.descendingMap().descendingMap()

returns a
view of

m

essentially equivalent to

m

.

The returned map has an ordering equivalent to

Collections.reverseOrder

(comparator())

.
The expression

m.descendingMap().descendingMap()

returns a
view of

m

essentially equivalent to

m

.

navigableKeySet

```java
NavigableSet
<
K
> navigableKeySet()
```

Returns a

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:** a navigable set view of the keys in this map

---

#### navigableKeySet

NavigableSet

<

K

> navigableKeySet()

Returns a

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

descendingKeySet

```java
NavigableSet
<
K
> descendingKeySet()
```

Returns a reverse order

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

**Returns:** a reverse order navigable set view of the keys in this map

---

#### descendingKeySet

NavigableSet

<

K

> descendingKeySet()

Returns a reverse order

NavigableSet

view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own

remove

operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations.
It does not support the

add

or

addAll

operations.

subMap

```java
NavigableMap
<
K
,​
V
> subMap​(
K
fromKey,
boolean fromInclusive,

K
toKey,
boolean toInclusive)
```

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

. If

fromKey

and

toKey

are equal, the returned map is empty unless

fromInclusive

and

toInclusive

are both true. The
returned map is backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.

**Parameters:** fromKey

- low endpoint of the keys in the returned map
**Parameters:** fromInclusive

-

true

if the low endpoint
is to be included in the returned view
**Parameters:** toKey

- high endpoint of the keys in the returned map
**Parameters:** toInclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys range from

fromKey

to

toKey
**Throws:** ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
**Throws:** NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
**Throws:** IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

---

#### subMap

NavigableMap

<

K

,​

V

> subMap​(

K

fromKey,
boolean fromInclusive,

K

toKey,
boolean toInclusive)

Returns a view of the portion of this map whose keys range from

fromKey

to

toKey

. If

fromKey

and

toKey

are equal, the returned map is empty unless

fromInclusive

and

toInclusive

are both true. The
returned map is backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside of its range, or to construct a
submap either of whose endpoints lie outside its range.

headMap

```java
NavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)
```

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:** toKey

- high endpoint of the keys in the returned map
**Parameters:** inclusive

-

true

if the high endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys are less than
(or equal to, if

inclusive

is true)

toKey
**Throws:** ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

toKey

is null
and this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### headMap

NavigableMap

<

K

,​

V

> headMap​(

K

toKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are less than (or
equal to, if

inclusive

is true)

toKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

tailMap

```java
NavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)
```

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

**Parameters:** fromKey

- low endpoint of the keys in the returned map
**Parameters:** inclusive

-

true

if the low endpoint
is to be included in the returned view
**Returns:** a view of the portion of this map whose keys are greater than
(or equal to, if

inclusive

is true)

fromKey
**Throws:** ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

fromKey

is null
and this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### tailMap

NavigableMap

<

K

,​

V

> tailMap​(

K

fromKey,
boolean inclusive)

Returns a view of the portion of this map whose keys are greater than (or
equal to, if

inclusive

is true)

fromKey

. The returned
map is backed by this map, so changes in the returned map are reflected
in this map, and vice-versa. The returned map supports all optional
map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

subMap

```java
SortedMap
<
K
,​
V
> subMap​(
K
fromKey,

K
toKey)
```

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive. (If

fromKey

and

toKey

are equal, the returned map
is empty.) The returned map is backed by this map, so changes
in the returned map are reflected in this map, and vice-versa.
The returned map supports all optional map operations that this
map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

subMap(fromKey, true, toKey, false)

.

**Specified by:** subMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** fromKey

- low endpoint (inclusive) of the keys in the returned map
**Parameters:** toKey

- high endpoint (exclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive
**Throws:** ClassCastException

- if

fromKey

and

toKey

cannot be compared to one another using this map's comparator
(or, if the map has no comparator, using natural ordering).
Implementations may, but are not required to, throw this
exception if

fromKey

or

toKey

cannot be compared to keys currently in the map.
**Throws:** NullPointerException

- if

fromKey

or

toKey

is null and this map does not permit null keys
**Throws:** IllegalArgumentException

- if

fromKey

is greater than

toKey

; or if this map itself has a restricted
range, and

fromKey

or

toKey

lies
outside the bounds of the range

---

#### subMap

SortedMap

<

K

,​

V

> subMap​(

K

fromKey,

K

toKey)

Returns a view of the portion of this map whose keys range from

fromKey

, inclusive, to

toKey

, exclusive. (If

fromKey

and

toKey

are equal, the returned map
is empty.) The returned map is backed by this map, so changes
in the returned map are reflected in this map, and vice-versa.
The returned map supports all optional map operations that this
map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

subMap(fromKey, true, toKey, false)

.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

subMap(fromKey, true, toKey, false)

.

Equivalent to

subMap(fromKey, true, toKey, false)

.

headMap

```java
SortedMap
<
K
,​
V
> headMap​(
K
toKey)
```

Returns a view of the portion of this map whose keys are
strictly less than

toKey

. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

headMap(toKey, false)

.

**Specified by:** headMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** toKey

- high endpoint (exclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys are strictly
less than

toKey
**Throws:** ClassCastException

- if

toKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

toKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

toKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

toKey

is null and
this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### headMap

SortedMap

<

K

,​

V

> headMap​(

K

toKey)

Returns a view of the portion of this map whose keys are
strictly less than

toKey

. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

headMap(toKey, false)

.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

headMap(toKey, false)

.

Equivalent to

headMap(toKey, false)

.

tailMap

```java
SortedMap
<
K
,​
V
> tailMap​(
K
fromKey)
```

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

tailMap(fromKey, true)

.

**Specified by:** tailMap

in interface

SortedMap

<

K

,​

V

>
**Parameters:** fromKey

- low endpoint (inclusive) of the keys in the returned map
**Returns:** a view of the portion of this map whose keys are greater
than or equal to

fromKey
**Throws:** ClassCastException

- if

fromKey

is not compatible
with this map's comparator (or, if the map has no comparator,
if

fromKey

does not implement

Comparable

).
Implementations may, but are not required to, throw this
exception if

fromKey

cannot be compared to keys
currently in the map.
**Throws:** NullPointerException

- if

fromKey

is null and
this map does not permit null keys
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### tailMap

SortedMap

<

K

,​

V

> tailMap​(

K

fromKey)

Returns a view of the portion of this map whose keys are
greater than or equal to

fromKey

. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

tailMap(fromKey, true)

.

The returned map will throw an

IllegalArgumentException

on an attempt to insert a key outside its range.

Equivalent to

tailMap(fromKey, true)

.

Equivalent to

tailMap(fromKey, true)

.

---

