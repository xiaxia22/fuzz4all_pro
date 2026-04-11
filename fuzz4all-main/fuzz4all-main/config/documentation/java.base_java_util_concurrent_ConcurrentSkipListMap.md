# Class ConcurrentSkipListMap<K,​V>

**Source:** `java.base\java\util\concurrent\ConcurrentSkipListMap.html`

### Class Description

```java
public class
ConcurrentSkipListMap<K,​V>

extends
AbstractMap
<K,​V>
implements
ConcurrentNavigableMap
<K,​V>,
Cloneable
,
Serializable
```

A scalable concurrent

ConcurrentNavigableMap

implementation.
The map is sorted according to the

natural
ordering

of its keys, or by a

Comparator

provided at map
creation time, depending on which constructor is used.

This class implements a concurrent variant of

SkipLists

providing expected average

log(n)

time cost for the

containsKey

,

get

,

put

and

remove

operations and their variants. Insertion, removal,
update, and access operations safely execute concurrently by
multiple threads.

Iterators and spliterators are

weakly consistent

.

Ascending key ordered views and their iterators are faster than
descending ones.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

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

#### public ConcurrentSkipListMap()

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

---

#### public ConcurrentSkipListMap​(
Comparator
<? super
K
> comparator)

Constructs a new, empty map, sorted according to the specified
comparator.

**Parameters:**
- comparator

- the comparator that will be used to order this map.
If

null

, the

natural
ordering

of the keys will be used.

---

#### public ConcurrentSkipListMap​(
Map
<? extends
K
,​? extends
V
> m)

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

**Parameters:**
- m

- the map whose mappings are to be placed in this map

**Throws:**
- ClassCastException

- if the keys in

m

are not

Comparable

, or are not mutually comparable
- NullPointerException

- if the specified map or any of its keys
or values are null

---

#### public ConcurrentSkipListMap​(
SortedMap
<
K
,​? extends
V
> m)

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

**Parameters:**
- m

- the sorted map whose mappings are to be placed in this
map, and whose comparator is to be used to sort this map

**Throws:**
- NullPointerException

- if the specified sorted map or any of
its keys or values are null

---

### Method Details

#### public
ConcurrentSkipListMap
<
K
,​
V
> clone()

Returns a shallow copy of this

ConcurrentSkipListMap

instance. (The keys and values themselves are not cloned.)

**Overrides:**
- clone

in class

AbstractMap

<

K

,​

V

>

**Returns:**
- a shallow copy of this map

**See Also:**
- Cloneable

---

#### public boolean containsKey​(
Object
key)

Returns

true

if this map contains a mapping for the specified
key.

**Specified by:**
- containsKey

in interface

Map

<

K

,​

V

>

**Overrides:**
- containsKey

in class

AbstractMap

<

K

,​

V

>

**Parameters:**
- key

- key whose presence in this map is to be tested

**Returns:**
- true

if this map contains a mapping for the specified key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null

---

#### public
V
get​(
Object
key)

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

key

compares
equal to

k

according to the map's ordering, then this
method returns

v

; otherwise it returns

null

.
(There can be at most one such mapping.)

**Specified by:**
- get

in interface

Map

<

K

,​

V

>

**Overrides:**
- get

in class

AbstractMap

<

K

,​

V

>

**Parameters:**
- key

- the key whose associated value is to be returned

**Returns:**
- the value to which the specified key is mapped, or

null

if this map contains no mapping for the key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null

---

#### public
V
getOrDefault​(
Object
key,

V
defaultValue)

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

**Specified by:**
- getOrDefault

in interface

ConcurrentMap

<

K

,​

V

>
- getOrDefault

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- the key
- defaultValue

- the value to return if this map contains
no mapping for the given key

**Returns:**
- the mapping for the key, if present; else the defaultValue

**Throws:**
- NullPointerException

- if the specified key is null

**Since:**
- 1.8

---

#### public
V
put​(
K
key,

V
value)

Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.

**Specified by:**
- put

in interface

Map

<

K

,​

V

>

**Overrides:**
- put

in class

AbstractMap

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is to be associated
- value

- value to be associated with the specified key

**Returns:**
- the previous value associated with the specified key, or

null

if there was no mapping for the key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key or value is null

---

#### public
V
remove​(
Object
key)

Removes the mapping for the specified key from this map if present.

**Specified by:**
- remove

in interface

Map

<

K

,​

V

>

**Overrides:**
- remove

in class

AbstractMap

<

K

,​

V

>

**Parameters:**
- key

- key for which mapping should be removed

**Returns:**
- the previous value associated with the specified key, or

null

if there was no mapping for the key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null

---

#### public boolean containsValue​(
Object
value)

Returns

true

if this map maps one or more keys to the
specified value. This operation requires time linear in the
map size. Additionally, it is possible for the map to change
during execution of this method, in which case the returned
result may be inaccurate.

**Specified by:**
- containsValue

in interface

Map

<

K

,​

V

>

**Overrides:**
- containsValue

in class

AbstractMap

<

K

,​

V

>

**Parameters:**
- value

- value whose presence in this map is to be tested

**Returns:**
- true

if a mapping to

value

exists;

false

otherwise

**Throws:**
- NullPointerException

- if the specified value is null

---

#### public void clear()

Removes all of the mappings from this map.

**Specified by:**
- clear

in interface

Map

<

K

,​

V

>

**Overrides:**
- clear

in class

AbstractMap

<

K

,​

V

>

---

#### public
V
computeIfAbsent​(
K
key,

Function
<? super
K
,​? extends
V
> mappingFunction)

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

. The function
is

NOT

guaranteed to be applied once atomically only
if the value is not present.

**Specified by:**
- computeIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
- computeIfAbsent

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is to be associated
- mappingFunction

- the function to compute a value

**Returns:**
- the current (existing or computed) value associated with
the specified key, or null if the computed value is null

**Throws:**
- NullPointerException

- if the specified key is null
or the mappingFunction is null

**Since:**
- 1.8

---

#### public
V
computeIfPresent​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:**
- computeIfPresent

in interface

ConcurrentMap

<

K

,​

V

>
- computeIfPresent

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which a value may be associated
- remappingFunction

- the function to compute a value

**Returns:**
- the new value associated with the specified key, or null if none

**Throws:**
- NullPointerException

- if the specified key is null
or the remappingFunction is null

**Since:**
- 1.8

---

#### public
V
compute​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping). The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:**
- compute

in interface

ConcurrentMap

<

K

,​

V

>
- compute

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is to be associated
- remappingFunction

- the function to compute a value

**Returns:**
- the new value associated with the specified key, or null if none

**Throws:**
- NullPointerException

- if the specified key is null
or the remappingFunction is null

**Since:**
- 1.8

---

#### public
V
merge​(
K
key,

V
value,

BiFunction
<? super
V
,​? super
V
,​? extends
V
> remappingFunction)

If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if

null

. The function is

NOT

guaranteed to be applied once atomically.

**Specified by:**
- merge

in interface

ConcurrentMap

<

K

,​

V

>
- merge

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is to be associated
- value

- the value to use if absent
- remappingFunction

- the function to recompute a value if present

**Returns:**
- the new value associated with the specified key, or null if none

**Throws:**
- NullPointerException

- if the specified key or value is null
or the remappingFunction is null

**Since:**
- 1.8

---

#### public
NavigableSet
<
K
> keySet()

Returns a

NavigableSet

view of the keys contained in this map.

The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

**Specified by:**
- keySet

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- keySet

in interface

Map

<

K

,​

V

>
- keySet

in interface

SortedMap

<

K

,​

V

>

**Overrides:**
- keySet

in class

AbstractMap

<

K

,​

V

>

**Returns:**
- a navigable set view of the keys in this map

---

#### public
Collection
<
V
> values()

Returns a

Collection

view of the values contained in this map.

The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

and

Spliterator.ORDERED

, with an encounter order that is ascending
order of the corresponding keys.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

**Specified by:**
- values

in interface

Map

<

K

,​

V

>
- values

in interface

SortedMap

<

K

,​

V

>

**Overrides:**
- values

in class

AbstractMap

<

K

,​

V

>

**Returns:**
- a collection view of the values contained in this map

---

#### public
Set
<
Map.Entry
<
K
,​
V
>> entrySet()

Returns a

Set

view of the mappings contained in this map.

The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

**Specified by:**
- entrySet

in interface

Map

<

K

,​

V

>
- entrySet

in interface

SortedMap

<

K

,​

V

>

**Returns:**
- a set view of the mappings contained in this map,
sorted in ascending key order

---

#### public boolean equals​(
Object
o)

Compares the specified object with this map for equality.
Returns

true

if the given object is also a map and the
two maps represent the same mappings. More formally, two maps

m1

and

m2

represent the same mappings if

m1.entrySet().equals(m2.entrySet())

. This
operation may return misleading results if either map is
concurrently modified during execution of this method.

**Specified by:**
- equals

in interface

Map

<

K

,​

V

>

**Overrides:**
- equals

in class

AbstractMap

<

K

,​

V

>

**Parameters:**
- o

- object to be compared for equality with this map

**Returns:**
- true

if the specified object is equal to this map

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
V
putIfAbsent​(
K
key,

V
value)

If the specified key is not already associated
with a value, associates it with the given value.
This is equivalent to, for this

map

:

```java
if (!map.containsKey(key))
return map.put(key, value);
else
return map.get(key);
```

except that the action is performed atomically.

**Specified by:**
- putIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
- putIfAbsent

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is to be associated
- value

- value to be associated with the specified key

**Returns:**
- the previous value associated with the specified key,
or

null

if there was no mapping for the key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key or value is null

---

#### public boolean remove​(
Object
key,

Object
value)

Removes the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), value)) {
map.remove(key);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:**
- remove

in interface

ConcurrentMap

<

K

,​

V

>
- remove

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is associated
- value

- value expected to be associated with the specified key

**Returns:**
- true

if the value was removed

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key is null

---

#### public boolean replace​(
K
key,

V
oldValue,

V
newValue)

Replaces the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), oldValue)) {
map.put(key, newValue);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:**
- replace

in interface

ConcurrentMap

<

K

,​

V

>
- replace

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is associated
- oldValue

- value expected to be associated with the specified key
- newValue

- value to be associated with the specified key

**Returns:**
- true

if the value was replaced

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if any of the arguments are null

---

#### public
V
replace​(
K
key,

V
value)

Replaces the entry for a key only if currently mapped to some value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key))
return map.put(key, value);
else
return null;
```

except that the action is performed atomically.

**Specified by:**
- replace

in interface

ConcurrentMap

<

K

,​

V

>
- replace

in interface

Map

<

K

,​

V

>

**Parameters:**
- key

- key with which the specified value is associated
- value

- value to be associated with the specified key

**Returns:**
- the previous value associated with the specified key,
or

null

if there was no mapping for the key

**Throws:**
- ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
- NullPointerException

- if the specified key or value is null

---

#### public
K
firstKey()

Description copied from interface:

SortedMap

**Specified by:**
- firstKey

in interface

SortedMap

<

K

,​

V

>

**Returns:**
- the first (lowest) key currently in this map

**Throws:**
- NoSuchElementException

- if this map is empty

---

#### public
K
lastKey()

Description copied from interface:

SortedMap

**Specified by:**
- lastKey

in interface

SortedMap

<

K

,​

V

>

**Returns:**
- the last (highest) key currently in this map

**Throws:**
- NoSuchElementException

- if this map is empty

---

#### public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

**Specified by:**
- subMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- subMap

in interface

NavigableMap

<

K

,​

V

>

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

is null
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

#### public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)

Description copied from interface:

NavigableMap

**Specified by:**
- headMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- headMap

in interface

NavigableMap

<

K

,​

V

>

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
- IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)

Description copied from interface:

NavigableMap

**Specified by:**
- tailMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- tailMap

in interface

NavigableMap

<

K

,​

V

>

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
- IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### public
ConcurrentNavigableMap
<
K
,​
V
> subMap​(
K
fromKey,

K
toKey)

Description copied from interface:

NavigableMap

**Specified by:**
- subMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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

#### public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey)

Description copied from interface:

NavigableMap

**Specified by:**
- headMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- headMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
- IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey)

Description copied from interface:

NavigableMap

**Specified by:**
- tailMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
- tailMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
- IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### public
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
no such key. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:**
- lowerEntry

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
K
lowerKey​(
K
key)

Description copied from interface:

NavigableMap

**Specified by:**
- lowerKey

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:**
- floorEntry

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
K
floorKey​(
K
key)

Description copied from interface:

NavigableMap

**Specified by:**
- floorKey

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
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
there is no such entry. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:**
- ceilingEntry

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
K
ceilingKey​(
K
key)

Description copied from interface:

NavigableMap

**Specified by:**
- ceilingKey

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:**
- higherEntry

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
K
higherKey​(
K
key)

Description copied from interface:

NavigableMap

**Specified by:**
- higherKey

in interface

NavigableMap

<

K

,​

V

>

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

---

#### public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:**
- firstEntry

in interface

NavigableMap

<

K

,​

V

>

**Returns:**
- an entry with the least key,
or

null

if this map is empty

---

#### public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:**
- lastEntry

in interface

NavigableMap

<

K

,​

V

>

**Returns:**
- an entry with the greatest key,
or

null

if this map is empty

---

#### public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:**
- pollFirstEntry

in interface

NavigableMap

<

K

,​

V

>

**Returns:**
- the removed first entry of this map,
or

null

if this map is empty

---

#### public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:**
- pollLastEntry

in interface

NavigableMap

<

K

,​

V

>

**Returns:**
- the removed last entry of this map,
or

null

if this map is empty

---

### Additional Sections

#### Class ConcurrentSkipListMap<K,​V>

java.lang.Object

- java.util.AbstractMap

<K,​V>
- - java.util.concurrent.ConcurrentSkipListMap<K,​V>

java.util.AbstractMap

<K,​V>

- java.util.concurrent.ConcurrentSkipListMap<K,​V>

java.util.concurrent.ConcurrentSkipListMap<K,​V>

**Type Parameters:** K

- the type of keys maintained by this map
**Type Parameters:** V

- the type of mapped values

**All Implemented Interfaces:** Serializable

,

Cloneable

,

ConcurrentMap

<K,​V>

,

ConcurrentNavigableMap

<K,​V>

,

Map

<K,​V>

,

NavigableMap

<K,​V>

,

SortedMap

<K,​V>

```java
public class
ConcurrentSkipListMap<K,​V>

extends
AbstractMap
<K,​V>
implements
ConcurrentNavigableMap
<K,​V>,
Cloneable
,
Serializable
```

A scalable concurrent

ConcurrentNavigableMap

implementation.
The map is sorted according to the

natural
ordering

of its keys, or by a

Comparator

provided at map
creation time, depending on which constructor is used.

This class implements a concurrent variant of

SkipLists

providing expected average

log(n)

time cost for the

containsKey

,

get

,

put

and

remove

operations and their variants. Insertion, removal,
update, and access operations safely execute concurrently by
multiple threads.

Iterators and spliterators are

weakly consistent

.

Ascending key ordered views and their iterators are faster than
descending ones.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

**Since:** 1.6
**See Also:** Serialized Form

public class

ConcurrentSkipListMap<K,​V>

extends

AbstractMap

<K,​V>
implements

ConcurrentNavigableMap

<K,​V>,

Cloneable

,

Serializable

A scalable concurrent

ConcurrentNavigableMap

implementation.
The map is sorted according to the

natural
ordering

of its keys, or by a

Comparator

provided at map
creation time, depending on which constructor is used.

This class implements a concurrent variant of

SkipLists

providing expected average

log(n)

time cost for the

containsKey

,

get

,

put

and

remove

operations and their variants. Insertion, removal,
update, and access operations safely execute concurrently by
multiple threads.

Iterators and spliterators are

weakly consistent

.

Ascending key ordered views and their iterators are faster than
descending ones.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

This class implements a concurrent variant of

SkipLists

providing expected average

log(n)

time cost for the

containsKey

,

get

,

put

and

remove

operations and their variants. Insertion, removal,
update, and access operations safely execute concurrently by
multiple threads.

Iterators and spliterators are

weakly consistent

.

Ascending key ordered views and their iterators are faster than
descending ones.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

Iterators and spliterators are

weakly consistent

.

Ascending key ordered views and their iterators are faster than
descending ones.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

Ascending key ordered views and their iterators are faster than
descending ones.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

All

Map.Entry

pairs returned by methods in this class
and its views represent snapshots of mappings at the time they were
produced. They do

not

support the

Entry.setValue

method. (Note however that it is possible to change mappings in the
associated map using

put

,

putIfAbsent

, or

replace

, depending on exactly which effect you need.)

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

Beware that bulk operations

putAll

,

equals

,

toArray

,

containsValue

, and

clear

are

not

guaranteed to be performed atomically. For example, an
iterator operating concurrently with a

putAll

operation
might view only some of the added elements.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

This class and its views and iterators implement all of the

optional

methods of the

Map

and

Iterator

interfaces. Like most other concurrent collections, this class does

not

permit the use of

null

keys or values because some
null return values cannot be reliably distinguished from the absence of
elements.

This class is a member of the

Java Collections Framework

.

This class is a member of the

Java Collections Framework

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.util.

AbstractMap

AbstractMap.SimpleEntry

<

K

,​

V

>,

AbstractMap.SimpleImmutableEntry

<

K

,​

V

>

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConcurrentSkipListMap

()

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

ConcurrentSkipListMap

​(

Comparator

<? super

K

> comparator)

Constructs a new, empty map, sorted according to the specified
comparator.

ConcurrentSkipListMap

​(

Map

<? extends

K

,​? extends

V

> m)

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

ConcurrentSkipListMap

​(

SortedMap

<

K

,​? extends

V

> m)

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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
there is no such entry.

K

ceilingKey

​(

K

key)

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

void

clear

()

Removes all of the mappings from this map.

ConcurrentSkipListMap

<

K

,​

V

>

clone

()

Returns a shallow copy of this

ConcurrentSkipListMap

instance.

V

compute

​(

K

key,

BiFunction

<? super

K

,​? super

V

,​? extends

V

> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

V

computeIfAbsent

​(

K

key,

Function

<? super

K

,​? extends

V

> mappingFunction)

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

.

V

computeIfPresent

​(

K

key,

BiFunction

<? super

K

,​? super

V

,​? extends

V

> remappingFunction)

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value.

boolean

containsKey

​(

Object

key)

Returns

true

if this map contains a mapping for the specified
key.

boolean

containsValue

​(

Object

value)

Returns

true

if this map maps one or more keys to the
specified value.

Set

<

Map.Entry

<

K

,​

V

>>

entrySet

()

Returns a

Set

view of the mappings contained in this map.

boolean

equals

​(

Object

o)

Compares the specified object with this map for equality.

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

K

firstKey

()

Returns the first (lowest) key currently in this map.

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

V

get

​(

Object

key)

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

V

getOrDefault

​(

Object

key,

V

defaultValue)

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

NavigableSet

<

K

>

keySet

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

lastEntry

()

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

K

lastKey

()

Returns the last (highest) key currently in this map.

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

V

merge

​(

K

key,

V

value,

BiFunction

<? super

V

,​? super

V

,​? extends

V

> remappingFunction)

If the specified key is not already associated with a value,
associates it with the given value.

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

V

put

​(

K

key,

V

value)

Associates the specified value with the specified key in this map.

V

putIfAbsent

​(

K

key,

V

value)

If the specified key is not already associated
with a value, associates it with the given value.

V

remove

​(

Object

key)

Removes the mapping for the specified key from this map if present.

boolean

remove

​(

Object

key,

Object

value)

Removes the entry for a key only if currently mapped to a given value.

V

replace

​(

K

key,

V

value)

Replaces the entry for a key only if currently mapped to some value.

boolean

replace

​(

K

key,

V

oldValue,

V

newValue)

Replaces the entry for a key only if currently mapped to a given value.

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

Collection

<

V

>

values

()

Returns a

Collection

view of the values contained in this map.

- Methods declared in class java.util.

AbstractMap

hashCode

,

isEmpty

,

putAll

,

size

,

toString

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

- Methods declared in interface java.util.concurrent.

ConcurrentMap

forEach

,

replaceAll

- Methods declared in interface java.util.concurrent.

ConcurrentNavigableMap

descendingKeySet

,

descendingMap

,

navigableKeySet

- Methods declared in interface java.util.

Map

hashCode

,

isEmpty

,

putAll

,

size

- Methods declared in interface java.util.

SortedMap

comparator

Nested Class Summary

- Nested classes/interfaces declared in class java.util.

AbstractMap

AbstractMap.SimpleEntry

<

K

,​

V

>,

AbstractMap.SimpleImmutableEntry

<

K

,​

V

>

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

Nested classes/interfaces declared in class java.util.

AbstractMap

AbstractMap.SimpleEntry

<

K

,​

V

>,

AbstractMap.SimpleImmutableEntry

<

K

,​

V

>

---

#### Nested classes/interfaces declared in class java.util. AbstractMap

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

Constructor Summary

Constructors

Constructor

Description

ConcurrentSkipListMap

()

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

ConcurrentSkipListMap

​(

Comparator

<? super

K

> comparator)

Constructs a new, empty map, sorted according to the specified
comparator.

ConcurrentSkipListMap

​(

Map

<? extends

K

,​? extends

V

> m)

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

ConcurrentSkipListMap

​(

SortedMap

<

K

,​? extends

V

> m)

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

---

#### Constructor Summary

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

Constructs a new, empty map, sorted according to the specified
comparator.

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

Method Summary

All Methods

Instance Methods

Concrete Methods

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
there is no such entry.

K

ceilingKey

​(

K

key)

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

void

clear

()

Removes all of the mappings from this map.

ConcurrentSkipListMap

<

K

,​

V

>

clone

()

Returns a shallow copy of this

ConcurrentSkipListMap

instance.

V

compute

​(

K

key,

BiFunction

<? super

K

,​? super

V

,​? extends

V

> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

V

computeIfAbsent

​(

K

key,

Function

<? super

K

,​? extends

V

> mappingFunction)

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

.

V

computeIfPresent

​(

K

key,

BiFunction

<? super

K

,​? super

V

,​? extends

V

> remappingFunction)

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value.

boolean

containsKey

​(

Object

key)

Returns

true

if this map contains a mapping for the specified
key.

boolean

containsValue

​(

Object

value)

Returns

true

if this map maps one or more keys to the
specified value.

Set

<

Map.Entry

<

K

,​

V

>>

entrySet

()

Returns a

Set

view of the mappings contained in this map.

boolean

equals

​(

Object

o)

Compares the specified object with this map for equality.

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

K

firstKey

()

Returns the first (lowest) key currently in this map.

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

V

get

​(

Object

key)

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

V

getOrDefault

​(

Object

key,

V

defaultValue)

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

NavigableSet

<

K

>

keySet

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

lastEntry

()

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

K

lastKey

()

Returns the last (highest) key currently in this map.

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

V

merge

​(

K

key,

V

value,

BiFunction

<? super

V

,​? super

V

,​? extends

V

> remappingFunction)

If the specified key is not already associated with a value,
associates it with the given value.

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

V

put

​(

K

key,

V

value)

Associates the specified value with the specified key in this map.

V

putIfAbsent

​(

K

key,

V

value)

If the specified key is not already associated
with a value, associates it with the given value.

V

remove

​(

Object

key)

Removes the mapping for the specified key from this map if present.

boolean

remove

​(

Object

key,

Object

value)

Removes the entry for a key only if currently mapped to a given value.

V

replace

​(

K

key,

V

value)

Replaces the entry for a key only if currently mapped to some value.

boolean

replace

​(

K

key,

V

oldValue,

V

newValue)

Replaces the entry for a key only if currently mapped to a given value.

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

ConcurrentNavigableMap

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

Collection

<

V

>

values

()

Returns a

Collection

view of the values contained in this map.

- Methods declared in class java.util.

AbstractMap

hashCode

,

isEmpty

,

putAll

,

size

,

toString

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

- Methods declared in interface java.util.concurrent.

ConcurrentMap

forEach

,

replaceAll

- Methods declared in interface java.util.concurrent.

ConcurrentNavigableMap

descendingKeySet

,

descendingMap

,

navigableKeySet

- Methods declared in interface java.util.

Map

hashCode

,

isEmpty

,

putAll

,

size

- Methods declared in interface java.util.

SortedMap

comparator

---

#### Method Summary

Returns a key-value mapping associated with the least key
greater than or equal to the given key, or

null

if
there is no such entry.

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

Removes all of the mappings from this map.

Returns a shallow copy of this

ConcurrentSkipListMap

instance.

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

.

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value.

Returns

true

if this map contains a mapping for the specified
key.

Returns

true

if this map maps one or more keys to the
specified value.

Returns a

Set

view of the mappings contained in this map.

Compares the specified object with this map for equality.

Returns a key-value mapping associated with the least
key in this map, or

null

if the map is empty.

Returns the first (lowest) key currently in this map.

Returns a key-value mapping associated with the greatest key
less than or equal to the given key, or

null

if there
is no such key.

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

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

Returns a

NavigableSet

view of the keys contained in this map.

Returns a key-value mapping associated with the greatest
key in this map, or

null

if the map is empty.

Returns the last (highest) key currently in this map.

Returns a key-value mapping associated with the greatest key
strictly less than the given key, or

null

if there is
no such key.

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

If the specified key is not already associated with a value,
associates it with the given value.

Removes and returns a key-value mapping associated with
the least key in this map, or

null

if the map is empty.

Removes and returns a key-value mapping associated with
the greatest key in this map, or

null

if the map is empty.

Associates the specified value with the specified key in this map.

If the specified key is not already associated
with a value, associates it with the given value.

Removes the mapping for the specified key from this map if present.

Removes the entry for a key only if currently mapped to a given value.

Replaces the entry for a key only if currently mapped to some value.

Replaces the entry for a key only if currently mapped to a given value.

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

Returns a

Collection

view of the values contained in this map.

Methods declared in class java.util.

AbstractMap

hashCode

,

isEmpty

,

putAll

,

size

,

toString

---

#### Methods declared in class java.util. AbstractMap

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

Methods declared in interface java.util.concurrent.

ConcurrentMap

forEach

,

replaceAll

---

#### Methods declared in interface java.util.concurrent. ConcurrentMap

Methods declared in interface java.util.concurrent.

ConcurrentNavigableMap

descendingKeySet

,

descendingMap

,

navigableKeySet

---

#### Methods declared in interface java.util.concurrent. ConcurrentNavigableMap

Methods declared in interface java.util.

Map

hashCode

,

isEmpty

,

putAll

,

size

---

#### Methods declared in interface java.util. Map

Methods declared in interface java.util.

SortedMap

comparator

---

#### Methods declared in interface java.util. SortedMap

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap()
```

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
Comparator
<? super
K
> comparator)
```

Constructs a new, empty map, sorted according to the specified
comparator.

**Parameters:** comparator

- the comparator that will be used to order this map.
If

null

, the

natural
ordering

of the keys will be used.

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
Map
<? extends
K
,​? extends
V
> m)
```

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

**Parameters:** m

- the map whose mappings are to be placed in this map
**Throws:** ClassCastException

- if the keys in

m

are not

Comparable

, or are not mutually comparable
**Throws:** NullPointerException

- if the specified map or any of its keys
or values are null

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
SortedMap
<
K
,​? extends
V
> m)
```

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

**Parameters:** m

- the sorted map whose mappings are to be placed in this
map, and whose comparator is to be used to sort this map
**Throws:** NullPointerException

- if the specified sorted map or any of
its keys or values are null

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
ConcurrentSkipListMap
<
K
,​
V
> clone()
```

Returns a shallow copy of this

ConcurrentSkipListMap

instance. (The keys and values themselves are not cloned.)

**Overrides:** clone

in class

AbstractMap

<

K

,​

V

>
**Returns:** a shallow copy of this map
**See Also:** Cloneable

- containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if this map contains a mapping for the specified
key.

**Specified by:** containsKey

in interface

Map

<

K

,​

V

>
**Overrides:** containsKey

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key whose presence in this map is to be tested
**Returns:** true

if this map contains a mapping for the specified key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- get

```java
public
V
get​(
Object
key)
```

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

key

compares
equal to

k

according to the map's ordering, then this
method returns

v

; otherwise it returns

null

.
(There can be at most one such mapping.)

**Specified by:** get

in interface

Map

<

K

,​

V

>
**Overrides:** get

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which the specified key is mapped, or

null

if this map contains no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- getOrDefault

```java
public
V
getOrDefault​(
Object
key,

V
defaultValue)
```

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

**Specified by:** getOrDefault

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** getOrDefault

in interface

Map

<

K

,​

V

>
**Parameters:** key

- the key
**Parameters:** defaultValue

- the value to return if this map contains
no mapping for the given key
**Returns:** the mapping for the key, if present; else the defaultValue
**Throws:** NullPointerException

- if the specified key is null
**Since:** 1.8

- put

```java
public
V
put​(
K
key,

V
value)
```

Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.

**Specified by:** put

in interface

Map

<

K

,​

V

>
**Overrides:** put

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

- remove

```java
public
V
remove​(
Object
key)
```

Removes the mapping for the specified key from this map if present.

**Specified by:** remove

in interface

Map

<

K

,​

V

>
**Overrides:** remove

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key for which mapping should be removed
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if this map maps one or more keys to the
specified value. This operation requires time linear in the
map size. Additionally, it is possible for the map to change
during execution of this method, in which case the returned
result may be inaccurate.

**Specified by:** containsValue

in interface

Map

<

K

,​

V

>
**Overrides:** containsValue

in class

AbstractMap

<

K

,​

V

>
**Parameters:** value

- value whose presence in this map is to be tested
**Returns:** true

if a mapping to

value

exists;

false

otherwise
**Throws:** NullPointerException

- if the specified value is null

- clear

```java
public void clear()
```

Removes all of the mappings from this map.

**Specified by:** clear

in interface

Map

<

K

,​

V

>
**Overrides:** clear

in class

AbstractMap

<

K

,​

V

>

- computeIfAbsent

```java
public
V
computeIfAbsent​(
K
key,

Function
<? super
K
,​? extends
V
> mappingFunction)
```

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

. The function
is

NOT

guaranteed to be applied once atomically only
if the value is not present.

**Specified by:** computeIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** computeIfAbsent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** mappingFunction

- the function to compute a value
**Returns:** the current (existing or computed) value associated with
the specified key, or null if the computed value is null
**Throws:** NullPointerException

- if the specified key is null
or the mappingFunction is null
**Since:** 1.8

- computeIfPresent

```java
public
V
computeIfPresent​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)
```

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:** computeIfPresent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** computeIfPresent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which a value may be associated
**Parameters:** remappingFunction

- the function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key is null
or the remappingFunction is null
**Since:** 1.8

- compute

```java
public
V
compute​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)
```

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping). The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:** compute

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** compute

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key is null
or the remappingFunction is null
**Since:** 1.8

- merge

```java
public
V
merge​(
K
key,

V
value,

BiFunction
<? super
V
,​? super
V
,​? extends
V
> remappingFunction)
```

If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if

null

. The function is

NOT

guaranteed to be applied once atomically.

**Specified by:** merge

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** merge

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- the value to use if absent
**Parameters:** remappingFunction

- the function to recompute a value if present
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key or value is null
or the remappingFunction is null
**Since:** 1.8

- keySet

```java
public
NavigableSet
<
K
> keySet()
```

Returns a

NavigableSet

view of the keys contained in this map.

The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

**Specified by:** keySet

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** keySet

in interface

Map

<

K

,​

V

>
**Specified by:** keySet

in interface

SortedMap

<

K

,​

V

>
**Overrides:** keySet

in class

AbstractMap

<

K

,​

V

>
**Returns:** a navigable set view of the keys in this map

- values

```java
public
Collection
<
V
> values()
```

Returns a

Collection

view of the values contained in this map.

The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

and

Spliterator.ORDERED

, with an encounter order that is ascending
order of the corresponding keys.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

**Specified by:** values

in interface

Map

<

K

,​

V

>
**Specified by:** values

in interface

SortedMap

<

K

,​

V

>
**Overrides:** values

in class

AbstractMap

<

K

,​

V

>
**Returns:** a collection view of the values contained in this map

- entrySet

```java
public
Set
<
Map.Entry
<
K
,​
V
>> entrySet()
```

Returns a

Set

view of the mappings contained in this map.

The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

**Specified by:** entrySet

in interface

Map

<

K

,​

V

>
**Specified by:** entrySet

in interface

SortedMap

<

K

,​

V

>
**Returns:** a set view of the mappings contained in this map,
sorted in ascending key order

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this map for equality.
Returns

true

if the given object is also a map and the
two maps represent the same mappings. More formally, two maps

m1

and

m2

represent the same mappings if

m1.entrySet().equals(m2.entrySet())

. This
operation may return misleading results if either map is
concurrently modified during execution of this method.

**Specified by:** equals

in interface

Map

<

K

,​

V

>
**Overrides:** equals

in class

AbstractMap

<

K

,​

V

>
**Parameters:** o

- object to be compared for equality with this map
**Returns:** true

if the specified object is equal to this map
**See Also:** Object.hashCode()

,

HashMap

- putIfAbsent

```java
public
V
putIfAbsent​(
K
key,

V
value)
```

If the specified key is not already associated
with a value, associates it with the given value.
This is equivalent to, for this

map

:

```java
if (!map.containsKey(key))
return map.put(key, value);
else
return map.get(key);
```

except that the action is performed atomically.

**Specified by:** putIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** putIfAbsent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key,
or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

- remove

```java
public boolean remove​(
Object
key,

Object
value)
```

Removes the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), value)) {
map.remove(key);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:** remove

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** remove

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value expected to be associated with the specified key
**Returns:** true

if the value was removed
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- replace

```java
public boolean replace​(
K
key,

V
oldValue,

V
newValue)
```

Replaces the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), oldValue)) {
map.put(key, newValue);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:** replace

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** replace

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** oldValue

- value expected to be associated with the specified key
**Parameters:** newValue

- value to be associated with the specified key
**Returns:** true

if the value was replaced
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if any of the arguments are null

- replace

```java
public
V
replace​(
K
key,

V
value)
```

Replaces the entry for a key only if currently mapped to some value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key))
return map.put(key, value);
else
return null;
```

except that the action is performed atomically.

**Specified by:** replace

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** replace

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key,
or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

- firstKey

```java
public
K
firstKey()
```

Description copied from interface:

SortedMap

Returns the first (lowest) key currently in this map.

**Specified by:** firstKey

in interface

SortedMap

<

K

,​

V

>
**Returns:** the first (lowest) key currently in this map
**Throws:** NoSuchElementException

- if this map is empty

- lastKey

```java
public
K
lastKey()
```

Description copied from interface:

SortedMap

Returns the last (highest) key currently in this map.

**Specified by:** lastKey

in interface

SortedMap

<

K

,​

V

>
**Returns:** the last (highest) key currently in this map
**Throws:** NoSuchElementException

- if this map is empty

- subMap

```java
public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

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

**Specified by:** subMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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
public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)
```

Description copied from interface:

NavigableMap

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

**Specified by:** headMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** headMap

in interface

NavigableMap

<

K

,​

V

>
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
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)
```

Description copied from interface:

NavigableMap

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

**Specified by:** tailMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** tailMap

in interface

NavigableMap

<

K

,​

V

>
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
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

- subMap

```java
public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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
public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey)
```

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** headMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey)
```

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** tailMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

- lowerEntry

```java
public
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
no such key. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:** lowerEntry

in interface

NavigableMap

<

K

,​

V

>
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

- lowerKey

```java
public
K
lowerKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Specified by:** lowerKey

in interface

NavigableMap

<

K

,​

V

>
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

- floorEntry

```java
public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** floorEntry

in interface

NavigableMap

<

K

,​

V

>
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

- floorKey

```java
public
K
floorKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Specified by:** floorKey

in interface

NavigableMap

<

K

,​

V

>
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

- ceilingEntry

```java
public
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
there is no such entry. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:** ceilingEntry

in interface

NavigableMap

<

K

,​

V

>
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

- ceilingKey

```java
public
K
ceilingKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Specified by:** ceilingKey

in interface

NavigableMap

<

K

,​

V

>
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

- higherEntry

```java
public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** higherEntry

in interface

NavigableMap

<

K

,​

V

>
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

- higherKey

```java
public
K
higherKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Specified by:** higherKey

in interface

NavigableMap

<

K

,​

V

>
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

- firstEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** firstEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** an entry with the least key,
or

null

if this map is empty

- lastEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** lastEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** an entry with the greatest key,
or

null

if this map is empty

- pollFirstEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** pollFirstEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** the removed first entry of this map,
or

null

if this map is empty

- pollLastEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** pollLastEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** the removed last entry of this map,
or

null

if this map is empty

Constructor Detail

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap()
```

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
Comparator
<? super
K
> comparator)
```

Constructs a new, empty map, sorted according to the specified
comparator.

**Parameters:** comparator

- the comparator that will be used to order this map.
If

null

, the

natural
ordering

of the keys will be used.

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
Map
<? extends
K
,​? extends
V
> m)
```

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

**Parameters:** m

- the map whose mappings are to be placed in this map
**Throws:** ClassCastException

- if the keys in

m

are not

Comparable

, or are not mutually comparable
**Throws:** NullPointerException

- if the specified map or any of its keys
or values are null

- ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
SortedMap
<
K
,​? extends
V
> m)
```

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

**Parameters:** m

- the sorted map whose mappings are to be placed in this
map, and whose comparator is to be used to sort this map
**Throws:** NullPointerException

- if the specified sorted map or any of
its keys or values are null

---

#### Constructor Detail

ConcurrentSkipListMap

```java
public ConcurrentSkipListMap()
```

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

---

#### ConcurrentSkipListMap

public ConcurrentSkipListMap()

Constructs a new, empty map, sorted according to the

natural ordering

of the keys.

ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
Comparator
<? super
K
> comparator)
```

Constructs a new, empty map, sorted according to the specified
comparator.

**Parameters:** comparator

- the comparator that will be used to order this map.
If

null

, the

natural
ordering

of the keys will be used.

---

#### ConcurrentSkipListMap

public ConcurrentSkipListMap​(

Comparator

<? super

K

> comparator)

Constructs a new, empty map, sorted according to the specified
comparator.

ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
Map
<? extends
K
,​? extends
V
> m)
```

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

**Parameters:** m

- the map whose mappings are to be placed in this map
**Throws:** ClassCastException

- if the keys in

m

are not

Comparable

, or are not mutually comparable
**Throws:** NullPointerException

- if the specified map or any of its keys
or values are null

---

#### ConcurrentSkipListMap

public ConcurrentSkipListMap​(

Map

<? extends

K

,​? extends

V

> m)

Constructs a new map containing the same mappings as the given map,
sorted according to the

natural ordering

of
the keys.

ConcurrentSkipListMap

```java
public ConcurrentSkipListMap​(
SortedMap
<
K
,​? extends
V
> m)
```

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

**Parameters:** m

- the sorted map whose mappings are to be placed in this
map, and whose comparator is to be used to sort this map
**Throws:** NullPointerException

- if the specified sorted map or any of
its keys or values are null

---

#### ConcurrentSkipListMap

public ConcurrentSkipListMap​(

SortedMap

<

K

,​? extends

V

> m)

Constructs a new map containing the same mappings and using the
same ordering as the specified sorted map.

Method Detail

- clone

```java
public
ConcurrentSkipListMap
<
K
,​
V
> clone()
```

Returns a shallow copy of this

ConcurrentSkipListMap

instance. (The keys and values themselves are not cloned.)

**Overrides:** clone

in class

AbstractMap

<

K

,​

V

>
**Returns:** a shallow copy of this map
**See Also:** Cloneable

- containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if this map contains a mapping for the specified
key.

**Specified by:** containsKey

in interface

Map

<

K

,​

V

>
**Overrides:** containsKey

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key whose presence in this map is to be tested
**Returns:** true

if this map contains a mapping for the specified key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- get

```java
public
V
get​(
Object
key)
```

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

key

compares
equal to

k

according to the map's ordering, then this
method returns

v

; otherwise it returns

null

.
(There can be at most one such mapping.)

**Specified by:** get

in interface

Map

<

K

,​

V

>
**Overrides:** get

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which the specified key is mapped, or

null

if this map contains no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- getOrDefault

```java
public
V
getOrDefault​(
Object
key,

V
defaultValue)
```

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

**Specified by:** getOrDefault

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** getOrDefault

in interface

Map

<

K

,​

V

>
**Parameters:** key

- the key
**Parameters:** defaultValue

- the value to return if this map contains
no mapping for the given key
**Returns:** the mapping for the key, if present; else the defaultValue
**Throws:** NullPointerException

- if the specified key is null
**Since:** 1.8

- put

```java
public
V
put​(
K
key,

V
value)
```

Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.

**Specified by:** put

in interface

Map

<

K

,​

V

>
**Overrides:** put

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

- remove

```java
public
V
remove​(
Object
key)
```

Removes the mapping for the specified key from this map if present.

**Specified by:** remove

in interface

Map

<

K

,​

V

>
**Overrides:** remove

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key for which mapping should be removed
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if this map maps one or more keys to the
specified value. This operation requires time linear in the
map size. Additionally, it is possible for the map to change
during execution of this method, in which case the returned
result may be inaccurate.

**Specified by:** containsValue

in interface

Map

<

K

,​

V

>
**Overrides:** containsValue

in class

AbstractMap

<

K

,​

V

>
**Parameters:** value

- value whose presence in this map is to be tested
**Returns:** true

if a mapping to

value

exists;

false

otherwise
**Throws:** NullPointerException

- if the specified value is null

- clear

```java
public void clear()
```

Removes all of the mappings from this map.

**Specified by:** clear

in interface

Map

<

K

,​

V

>
**Overrides:** clear

in class

AbstractMap

<

K

,​

V

>

- computeIfAbsent

```java
public
V
computeIfAbsent​(
K
key,

Function
<? super
K
,​? extends
V
> mappingFunction)
```

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

. The function
is

NOT

guaranteed to be applied once atomically only
if the value is not present.

**Specified by:** computeIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** computeIfAbsent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** mappingFunction

- the function to compute a value
**Returns:** the current (existing or computed) value associated with
the specified key, or null if the computed value is null
**Throws:** NullPointerException

- if the specified key is null
or the mappingFunction is null
**Since:** 1.8

- computeIfPresent

```java
public
V
computeIfPresent​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)
```

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:** computeIfPresent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** computeIfPresent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which a value may be associated
**Parameters:** remappingFunction

- the function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key is null
or the remappingFunction is null
**Since:** 1.8

- compute

```java
public
V
compute​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)
```

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping). The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:** compute

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** compute

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key is null
or the remappingFunction is null
**Since:** 1.8

- merge

```java
public
V
merge​(
K
key,

V
value,

BiFunction
<? super
V
,​? super
V
,​? extends
V
> remappingFunction)
```

If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if

null

. The function is

NOT

guaranteed to be applied once atomically.

**Specified by:** merge

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** merge

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- the value to use if absent
**Parameters:** remappingFunction

- the function to recompute a value if present
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key or value is null
or the remappingFunction is null
**Since:** 1.8

- keySet

```java
public
NavigableSet
<
K
> keySet()
```

Returns a

NavigableSet

view of the keys contained in this map.

The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

**Specified by:** keySet

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** keySet

in interface

Map

<

K

,​

V

>
**Specified by:** keySet

in interface

SortedMap

<

K

,​

V

>
**Overrides:** keySet

in class

AbstractMap

<

K

,​

V

>
**Returns:** a navigable set view of the keys in this map

- values

```java
public
Collection
<
V
> values()
```

Returns a

Collection

view of the values contained in this map.

The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

and

Spliterator.ORDERED

, with an encounter order that is ascending
order of the corresponding keys.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

**Specified by:** values

in interface

Map

<

K

,​

V

>
**Specified by:** values

in interface

SortedMap

<

K

,​

V

>
**Overrides:** values

in class

AbstractMap

<

K

,​

V

>
**Returns:** a collection view of the values contained in this map

- entrySet

```java
public
Set
<
Map.Entry
<
K
,​
V
>> entrySet()
```

Returns a

Set

view of the mappings contained in this map.

The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

**Specified by:** entrySet

in interface

Map

<

K

,​

V

>
**Specified by:** entrySet

in interface

SortedMap

<

K

,​

V

>
**Returns:** a set view of the mappings contained in this map,
sorted in ascending key order

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this map for equality.
Returns

true

if the given object is also a map and the
two maps represent the same mappings. More formally, two maps

m1

and

m2

represent the same mappings if

m1.entrySet().equals(m2.entrySet())

. This
operation may return misleading results if either map is
concurrently modified during execution of this method.

**Specified by:** equals

in interface

Map

<

K

,​

V

>
**Overrides:** equals

in class

AbstractMap

<

K

,​

V

>
**Parameters:** o

- object to be compared for equality with this map
**Returns:** true

if the specified object is equal to this map
**See Also:** Object.hashCode()

,

HashMap

- putIfAbsent

```java
public
V
putIfAbsent​(
K
key,

V
value)
```

If the specified key is not already associated
with a value, associates it with the given value.
This is equivalent to, for this

map

:

```java
if (!map.containsKey(key))
return map.put(key, value);
else
return map.get(key);
```

except that the action is performed atomically.

**Specified by:** putIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** putIfAbsent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key,
or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

- remove

```java
public boolean remove​(
Object
key,

Object
value)
```

Removes the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), value)) {
map.remove(key);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:** remove

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** remove

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value expected to be associated with the specified key
**Returns:** true

if the value was removed
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

- replace

```java
public boolean replace​(
K
key,

V
oldValue,

V
newValue)
```

Replaces the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), oldValue)) {
map.put(key, newValue);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:** replace

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** replace

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** oldValue

- value expected to be associated with the specified key
**Parameters:** newValue

- value to be associated with the specified key
**Returns:** true

if the value was replaced
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if any of the arguments are null

- replace

```java
public
V
replace​(
K
key,

V
value)
```

Replaces the entry for a key only if currently mapped to some value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key))
return map.put(key, value);
else
return null;
```

except that the action is performed atomically.

**Specified by:** replace

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** replace

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key,
or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

- firstKey

```java
public
K
firstKey()
```

Description copied from interface:

SortedMap

Returns the first (lowest) key currently in this map.

**Specified by:** firstKey

in interface

SortedMap

<

K

,​

V

>
**Returns:** the first (lowest) key currently in this map
**Throws:** NoSuchElementException

- if this map is empty

- lastKey

```java
public
K
lastKey()
```

Description copied from interface:

SortedMap

Returns the last (highest) key currently in this map.

**Specified by:** lastKey

in interface

SortedMap

<

K

,​

V

>
**Returns:** the last (highest) key currently in this map
**Throws:** NoSuchElementException

- if this map is empty

- subMap

```java
public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

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

**Specified by:** subMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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
public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)
```

Description copied from interface:

NavigableMap

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

**Specified by:** headMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** headMap

in interface

NavigableMap

<

K

,​

V

>
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
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)
```

Description copied from interface:

NavigableMap

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

**Specified by:** tailMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** tailMap

in interface

NavigableMap

<

K

,​

V

>
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
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

- subMap

```java
public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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
public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey)
```

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** headMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

- tailMap

```java
public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey)
```

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** tailMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

- lowerEntry

```java
public
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
no such key. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:** lowerEntry

in interface

NavigableMap

<

K

,​

V

>
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

- lowerKey

```java
public
K
lowerKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Specified by:** lowerKey

in interface

NavigableMap

<

K

,​

V

>
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

- floorEntry

```java
public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** floorEntry

in interface

NavigableMap

<

K

,​

V

>
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

- floorKey

```java
public
K
floorKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Specified by:** floorKey

in interface

NavigableMap

<

K

,​

V

>
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

- ceilingEntry

```java
public
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
there is no such entry. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:** ceilingEntry

in interface

NavigableMap

<

K

,​

V

>
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

- ceilingKey

```java
public
K
ceilingKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Specified by:** ceilingKey

in interface

NavigableMap

<

K

,​

V

>
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

- higherEntry

```java
public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** higherEntry

in interface

NavigableMap

<

K

,​

V

>
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

- higherKey

```java
public
K
higherKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Specified by:** higherKey

in interface

NavigableMap

<

K

,​

V

>
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

- firstEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** firstEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** an entry with the least key,
or

null

if this map is empty

- lastEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** lastEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** an entry with the greatest key,
or

null

if this map is empty

- pollFirstEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** pollFirstEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** the removed first entry of this map,
or

null

if this map is empty

- pollLastEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** pollLastEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** the removed last entry of this map,
or

null

if this map is empty

---

#### Method Detail

clone

```java
public
ConcurrentSkipListMap
<
K
,​
V
> clone()
```

Returns a shallow copy of this

ConcurrentSkipListMap

instance. (The keys and values themselves are not cloned.)

**Overrides:** clone

in class

AbstractMap

<

K

,​

V

>
**Returns:** a shallow copy of this map
**See Also:** Cloneable

---

#### clone

public

ConcurrentSkipListMap

<

K

,​

V

> clone()

Returns a shallow copy of this

ConcurrentSkipListMap

instance. (The keys and values themselves are not cloned.)

containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if this map contains a mapping for the specified
key.

**Specified by:** containsKey

in interface

Map

<

K

,​

V

>
**Overrides:** containsKey

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key whose presence in this map is to be tested
**Returns:** true

if this map contains a mapping for the specified key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

---

#### containsKey

public boolean containsKey​(

Object

key)

Returns

true

if this map contains a mapping for the specified
key.

get

```java
public
V
get​(
Object
key)
```

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

key

compares
equal to

k

according to the map's ordering, then this
method returns

v

; otherwise it returns

null

.
(There can be at most one such mapping.)

**Specified by:** get

in interface

Map

<

K

,​

V

>
**Overrides:** get

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- the key whose associated value is to be returned
**Returns:** the value to which the specified key is mapped, or

null

if this map contains no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

---

#### get

public

V

get​(

Object

key)

Returns the value to which the specified key is mapped,
or

null

if this map contains no mapping for the key.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

key

compares
equal to

k

according to the map's ordering, then this
method returns

v

; otherwise it returns

null

.
(There can be at most one such mapping.)

More formally, if this map contains a mapping from a key

k

to a value

v

such that

key

compares
equal to

k

according to the map's ordering, then this
method returns

v

; otherwise it returns

null

.
(There can be at most one such mapping.)

getOrDefault

```java
public
V
getOrDefault​(
Object
key,

V
defaultValue)
```

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

**Specified by:** getOrDefault

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** getOrDefault

in interface

Map

<

K

,​

V

>
**Parameters:** key

- the key
**Parameters:** defaultValue

- the value to return if this map contains
no mapping for the given key
**Returns:** the mapping for the key, if present; else the defaultValue
**Throws:** NullPointerException

- if the specified key is null
**Since:** 1.8

---

#### getOrDefault

public

V

getOrDefault​(

Object

key,

V

defaultValue)

Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.

put

```java
public
V
put​(
K
key,

V
value)
```

Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.

**Specified by:** put

in interface

Map

<

K

,​

V

>
**Overrides:** put

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

---

#### put

public

V

put​(

K

key,

V

value)

Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.

remove

```java
public
V
remove​(
Object
key)
```

Removes the mapping for the specified key from this map if present.

**Specified by:** remove

in interface

Map

<

K

,​

V

>
**Overrides:** remove

in class

AbstractMap

<

K

,​

V

>
**Parameters:** key

- key for which mapping should be removed
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

---

#### remove

public

V

remove​(

Object

key)

Removes the mapping for the specified key from this map if present.

containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns

true

if this map maps one or more keys to the
specified value. This operation requires time linear in the
map size. Additionally, it is possible for the map to change
during execution of this method, in which case the returned
result may be inaccurate.

**Specified by:** containsValue

in interface

Map

<

K

,​

V

>
**Overrides:** containsValue

in class

AbstractMap

<

K

,​

V

>
**Parameters:** value

- value whose presence in this map is to be tested
**Returns:** true

if a mapping to

value

exists;

false

otherwise
**Throws:** NullPointerException

- if the specified value is null

---

#### containsValue

public boolean containsValue​(

Object

value)

Returns

true

if this map maps one or more keys to the
specified value. This operation requires time linear in the
map size. Additionally, it is possible for the map to change
during execution of this method, in which case the returned
result may be inaccurate.

clear

```java
public void clear()
```

Removes all of the mappings from this map.

**Specified by:** clear

in interface

Map

<

K

,​

V

>
**Overrides:** clear

in class

AbstractMap

<

K

,​

V

>

---

#### clear

public void clear()

Removes all of the mappings from this map.

computeIfAbsent

```java
public
V
computeIfAbsent​(
K
key,

Function
<? super
K
,​? extends
V
> mappingFunction)
```

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

. The function
is

NOT

guaranteed to be applied once atomically only
if the value is not present.

**Specified by:** computeIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** computeIfAbsent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** mappingFunction

- the function to compute a value
**Returns:** the current (existing or computed) value associated with
the specified key, or null if the computed value is null
**Throws:** NullPointerException

- if the specified key is null
or the mappingFunction is null
**Since:** 1.8

---

#### computeIfAbsent

public

V

computeIfAbsent​(

K

key,

Function

<? super

K

,​? extends

V

> mappingFunction)

If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless

null

. The function
is

NOT

guaranteed to be applied once atomically only
if the value is not present.

computeIfPresent

```java
public
V
computeIfPresent​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)
```

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:** computeIfPresent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** computeIfPresent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which a value may be associated
**Parameters:** remappingFunction

- the function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key is null
or the remappingFunction is null
**Since:** 1.8

---

#### computeIfPresent

public

V

computeIfPresent​(

K

key,

BiFunction

<? super

K

,​? super

V

,​? extends

V

> remappingFunction)

If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is

NOT

guaranteed to be applied
once atomically.

compute

```java
public
V
compute​(
K
key,

BiFunction
<? super
K
,​? super
V
,​? extends
V
> remappingFunction)
```

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping). The function is

NOT

guaranteed to be applied
once atomically.

**Specified by:** compute

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** compute

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key is null
or the remappingFunction is null
**Since:** 1.8

---

#### compute

public

V

compute​(

K

key,

BiFunction

<? super

K

,​? super

V

,​? extends

V

> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping). The function is

NOT

guaranteed to be applied
once atomically.

merge

```java
public
V
merge​(
K
key,

V
value,

BiFunction
<? super
V
,​? super
V
,​? extends
V
> remappingFunction)
```

If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if

null

. The function is

NOT

guaranteed to be applied once atomically.

**Specified by:** merge

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** merge

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- the value to use if absent
**Parameters:** remappingFunction

- the function to recompute a value if present
**Returns:** the new value associated with the specified key, or null if none
**Throws:** NullPointerException

- if the specified key or value is null
or the remappingFunction is null
**Since:** 1.8

---

#### merge

public

V

merge​(

K

key,

V

value,

BiFunction

<? super

V

,​? super

V

,​? extends

V

> remappingFunction)

If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if

null

. The function is

NOT

guaranteed to be applied once atomically.

keySet

```java
public
NavigableSet
<
K
> keySet()
```

Returns a

NavigableSet

view of the keys contained in this map.

The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

**Specified by:** keySet

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** keySet

in interface

Map

<

K

,​

V

>
**Specified by:** keySet

in interface

SortedMap

<

K

,​

V

>
**Overrides:** keySet

in class

AbstractMap

<

K

,​

V

>
**Returns:** a navigable set view of the keys in this map

---

#### keySet

public

NavigableSet

<

K

> keySet()

Returns a

NavigableSet

view of the keys contained in this map.

The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

The

spliterator's comparator

is

null

if the

map's comparator

is

null

.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

, and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

The view's iterators and spliterators are

weakly consistent

.

This method is equivalent to method

navigableKeySet

.

This method is equivalent to method

navigableKeySet

.

values

```java
public
Collection
<
V
> values()
```

Returns a

Collection

view of the values contained in this map.

The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

and

Spliterator.ORDERED

, with an encounter order that is ascending
order of the corresponding keys.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

**Specified by:** values

in interface

Map

<

K

,​

V

>
**Specified by:** values

in interface

SortedMap

<

K

,​

V

>
**Overrides:** values

in class

AbstractMap

<

K

,​

V

>
**Returns:** a collection view of the values contained in this map

---

#### values

public

Collection

<

V

> values()

Returns a

Collection

view of the values contained in this map.

The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

and

Spliterator.ORDERED

, with an encounter order that is ascending
order of the corresponding keys.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

and

Spliterator.ORDERED

, with an encounter order that is ascending
order of the corresponding keys.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the

Iterator.remove

,

Collection.remove

,

removeAll

,

retainAll

and

clear

operations. It does not
support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The view's iterators and spliterators are

weakly consistent

.

entrySet

```java
public
Set
<
Map.Entry
<
K
,​
V
>> entrySet()
```

Returns a

Set

view of the mappings contained in this map.

The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

**Specified by:** entrySet

in interface

Map

<

K

,​

V

>
**Specified by:** entrySet

in interface

SortedMap

<

K

,​

V

>
**Returns:** a set view of the mappings contained in this map,
sorted in ascending key order

---

#### entrySet

public

Set

<

Map.Entry

<

K

,​

V

>> entrySet()

Returns a

Set

view of the mappings contained in this map.

The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports

Spliterator.CONCURRENT

,

Spliterator.NONNULL

,

Spliterator.SORTED

and

Spliterator.ORDERED

, with an encounter order that is ascending
key order.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the

Iterator.remove

,

Set.remove

,

removeAll

,

retainAll

and

clear

operations. It does not support the

add

or

addAll

operations.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

The view's iterators and spliterators are

weakly consistent

.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

The

Map.Entry

elements traversed by the

iterator

or

spliterator

do

not

support the

setValue

operation.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified object with this map for equality.
Returns

true

if the given object is also a map and the
two maps represent the same mappings. More formally, two maps

m1

and

m2

represent the same mappings if

m1.entrySet().equals(m2.entrySet())

. This
operation may return misleading results if either map is
concurrently modified during execution of this method.

**Specified by:** equals

in interface

Map

<

K

,​

V

>
**Overrides:** equals

in class

AbstractMap

<

K

,​

V

>
**Parameters:** o

- object to be compared for equality with this map
**Returns:** true

if the specified object is equal to this map
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified object with this map for equality.
Returns

true

if the given object is also a map and the
two maps represent the same mappings. More formally, two maps

m1

and

m2

represent the same mappings if

m1.entrySet().equals(m2.entrySet())

. This
operation may return misleading results if either map is
concurrently modified during execution of this method.

putIfAbsent

```java
public
V
putIfAbsent​(
K
key,

V
value)
```

If the specified key is not already associated
with a value, associates it with the given value.
This is equivalent to, for this

map

:

```java
if (!map.containsKey(key))
return map.put(key, value);
else
return map.get(key);
```

except that the action is performed atomically.

**Specified by:** putIfAbsent

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** putIfAbsent

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key,
or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

---

#### putIfAbsent

public

V

putIfAbsent​(

K

key,

V

value)

If the specified key is not already associated
with a value, associates it with the given value.
This is equivalent to, for this

map

:

```java
if (!map.containsKey(key))
return map.put(key, value);
else
return map.get(key);
```

except that the action is performed atomically.

if (!map.containsKey(key))
return map.put(key, value);
else
return map.get(key);

remove

```java
public boolean remove​(
Object
key,

Object
value)
```

Removes the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), value)) {
map.remove(key);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:** remove

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** remove

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value expected to be associated with the specified key
**Returns:** true

if the value was removed
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key is null

---

#### remove

public boolean remove​(

Object

key,

Object

value)

Removes the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), value)) {
map.remove(key);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

if (map.containsKey(key)
&& Objects.equals(map.get(key), value)) {
map.remove(key);
return true;
} else {
return false;
}

replace

```java
public boolean replace​(
K
key,

V
oldValue,

V
newValue)
```

Replaces the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), oldValue)) {
map.put(key, newValue);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

**Specified by:** replace

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** replace

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** oldValue

- value expected to be associated with the specified key
**Parameters:** newValue

- value to be associated with the specified key
**Returns:** true

if the value was replaced
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if any of the arguments are null

---

#### replace

public boolean replace​(

K

key,

V

oldValue,

V

newValue)

Replaces the entry for a key only if currently mapped to a given value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key)
&& Objects.equals(map.get(key), oldValue)) {
map.put(key, newValue);
return true;
} else {
return false;
}
```

except that the action is performed atomically.

if (map.containsKey(key)
&& Objects.equals(map.get(key), oldValue)) {
map.put(key, newValue);
return true;
} else {
return false;
}

replace

```java
public
V
replace​(
K
key,

V
value)
```

Replaces the entry for a key only if currently mapped to some value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key))
return map.put(key, value);
else
return null;
```

except that the action is performed atomically.

**Specified by:** replace

in interface

ConcurrentMap

<

K

,​

V

>
**Specified by:** replace

in interface

Map

<

K

,​

V

>
**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key,
or

null

if there was no mapping for the key
**Throws:** ClassCastException

- if the specified key cannot be compared
with the keys currently in the map
**Throws:** NullPointerException

- if the specified key or value is null

---

#### replace

public

V

replace​(

K

key,

V

value)

Replaces the entry for a key only if currently mapped to some value.
This is equivalent to, for this

map

:

```java
if (map.containsKey(key))
return map.put(key, value);
else
return null;
```

except that the action is performed atomically.

if (map.containsKey(key))
return map.put(key, value);
else
return null;

firstKey

```java
public
K
firstKey()
```

Description copied from interface:

SortedMap

Returns the first (lowest) key currently in this map.

**Specified by:** firstKey

in interface

SortedMap

<

K

,​

V

>
**Returns:** the first (lowest) key currently in this map
**Throws:** NoSuchElementException

- if this map is empty

---

#### firstKey

public

K

firstKey()

Description copied from interface:

SortedMap

Returns the first (lowest) key currently in this map.

lastKey

```java
public
K
lastKey()
```

Description copied from interface:

SortedMap

Returns the last (highest) key currently in this map.

**Specified by:** lastKey

in interface

SortedMap

<

K

,​

V

>
**Returns:** the last (highest) key currently in this map
**Throws:** NoSuchElementException

- if this map is empty

---

#### lastKey

public

K

lastKey()

Description copied from interface:

SortedMap

Returns the last (highest) key currently in this map.

subMap

```java
public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

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

**Specified by:** subMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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

public

ConcurrentNavigableMap

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

Description copied from interface:

NavigableMap

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
public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey,
boolean inclusive)
```

Description copied from interface:

NavigableMap

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

**Specified by:** headMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** headMap

in interface

NavigableMap

<

K

,​

V

>
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
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### headMap

public

ConcurrentNavigableMap

<

K

,​

V

> headMap​(

K

toKey,
boolean inclusive)

Description copied from interface:

NavigableMap

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
public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey,
boolean inclusive)
```

Description copied from interface:

NavigableMap

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

**Specified by:** tailMap

in interface

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** tailMap

in interface

NavigableMap

<

K

,​

V

>
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
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### tailMap

public

ConcurrentNavigableMap

<

K

,​

V

> tailMap​(

K

fromKey,
boolean inclusive)

Description copied from interface:

NavigableMap

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
public
ConcurrentNavigableMap
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

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** subMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
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

public

ConcurrentNavigableMap

<

K

,​

V

> subMap​(

K

fromKey,

K

toKey)

Description copied from interface:

NavigableMap

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
public
ConcurrentNavigableMap
<
K
,​
V
> headMap​(
K
toKey)
```

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** headMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

toKey

lies outside the
bounds of the range

---

#### headMap

public

ConcurrentNavigableMap

<

K

,​

V

> headMap​(

K

toKey)

Description copied from interface:

NavigableMap

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
public
ConcurrentNavigableMap
<
K
,​
V
> tailMap​(
K
fromKey)
```

Description copied from interface:

NavigableMap

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

ConcurrentNavigableMap

<

K

,​

V

>
**Specified by:** tailMap

in interface

NavigableMap

<

K

,​

V

>
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

is null
**Throws:** IllegalArgumentException

- if this map itself has a
restricted range, and

fromKey

lies outside the
bounds of the range

---

#### tailMap

public

ConcurrentNavigableMap

<

K

,​

V

> tailMap​(

K

fromKey)

Description copied from interface:

NavigableMap

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

lowerEntry

```java
public
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
no such key. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:** lowerEntry

in interface

NavigableMap

<

K

,​

V

>
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

---

#### lowerEntry

public

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
no such key. The returned entry does

not

support the

Entry.setValue

method.

lowerKey

```java
public
K
lowerKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

**Specified by:** lowerKey

in interface

NavigableMap

<

K

,​

V

>
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

---

#### lowerKey

public

K

lowerKey​(

K

key)

Description copied from interface:

NavigableMap

Returns the greatest key strictly less than the given key, or

null

if there is no such key.

floorEntry

```java
public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** floorEntry

in interface

NavigableMap

<

K

,​

V

>
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

---

#### floorEntry

public

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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

floorKey

```java
public
K
floorKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

**Specified by:** floorKey

in interface

NavigableMap

<

K

,​

V

>
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

---

#### floorKey

public

K

floorKey​(

K

key)

Description copied from interface:

NavigableMap

Returns the greatest key less than or equal to the given key,
or

null

if there is no such key.

ceilingEntry

```java
public
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
there is no such entry. The returned entry does

not

support the

Entry.setValue

method.

**Specified by:** ceilingEntry

in interface

NavigableMap

<

K

,​

V

>
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

---

#### ceilingEntry

public

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
there is no such entry. The returned entry does

not

support the

Entry.setValue

method.

ceilingKey

```java
public
K
ceilingKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

**Specified by:** ceilingKey

in interface

NavigableMap

<

K

,​

V

>
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

---

#### ceilingKey

public

K

ceilingKey​(

K

key)

Description copied from interface:

NavigableMap

Returns the least key greater than or equal to the given key,
or

null

if there is no such key.

higherEntry

```java
public
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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** higherEntry

in interface

NavigableMap

<

K

,​

V

>
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

---

#### higherEntry

public

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
is no such key. The returned entry does

not

support
the

Entry.setValue

method.

higherKey

```java
public
K
higherKey​(
K
key)
```

Description copied from interface:

NavigableMap

Returns the least key strictly greater than the given key, or

null

if there is no such key.

**Specified by:** higherKey

in interface

NavigableMap

<

K

,​

V

>
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

---

#### higherKey

public

K

higherKey​(

K

key)

Description copied from interface:

NavigableMap

Returns the least key strictly greater than the given key, or

null

if there is no such key.

firstEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** firstEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** an entry with the least key,
or

null

if this map is empty

---

#### firstEntry

public

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
The returned entry does

not

support
the

Entry.setValue

method.

lastEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** lastEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** an entry with the greatest key,
or

null

if this map is empty

---

#### lastEntry

public

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
The returned entry does

not

support
the

Entry.setValue

method.

pollFirstEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** pollFirstEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** the removed first entry of this map,
or

null

if this map is empty

---

#### pollFirstEntry

public

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
The returned entry does

not

support
the

Entry.setValue

method.

pollLastEntry

```java
public
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
The returned entry does

not

support
the

Entry.setValue

method.

**Specified by:** pollLastEntry

in interface

NavigableMap

<

K

,​

V

>
**Returns:** the removed last entry of this map,
or

null

if this map is empty

---

#### pollLastEntry

public

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
The returned entry does

not

support
the

Entry.setValue

method.

---

