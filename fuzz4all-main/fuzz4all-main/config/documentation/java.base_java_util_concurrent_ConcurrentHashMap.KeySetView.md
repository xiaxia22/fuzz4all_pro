# Class ConcurrentHashMap.KeySetView<K,​V>

**Source:** `java.base\java\util\concurrent\ConcurrentHashMap.KeySetView.html`

### Class Description

```java
public static class
ConcurrentHashMap.KeySetView<K,​V>

extends
Object

implements
Set
<K>,
Serializable
```

A view of a ConcurrentHashMap as a

Set

of keys, in
which additions may optionally be enabled by mapping to a
common value. This class cannot be directly instantiated.
See

keySet()

,

keySet(V)

,

newKeySet()

,

newKeySet(int)

.

**All Implemented Interfaces:** Serializable

,

Iterable

<K>

,

Collection

<K>

,

Set

<K>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
V
getMappedValue()

Returns the default mapped value for additions,
or

null

if additions are not supported.

**Returns:**
- the default mapped value for additions, or

null

if not supported

---

#### public boolean contains​(
Object
o)

Returns

true

if this collection contains the specified element.
More formally, returns

true

if and only if this collection
contains at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:**
- contains

in interface

Collection

<

K

>
- contains

in interface

Set

<

K

>

**Parameters:**
- o

- element whose presence in this collection is to be tested

**Returns:**
- true

if this collection contains the specified
element

**Throws:**
- NullPointerException

- if the specified key is null

---

#### public boolean remove​(
Object
o)

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map. This method does
nothing if the key is not in the map.

**Specified by:**
- remove

in interface

Collection

<

K

>
- remove

in interface

Set

<

K

>

**Parameters:**
- o

- the key to be removed from the backing map

**Returns:**
- true

if the backing map contained the specified key

**Throws:**
- NullPointerException

- if the specified key is null

---

#### public
Iterator
<
K
> iterator()

Returns an iterator over the elements in this collection.

The returned iterator is

weakly consistent

.

**Specified by:**
- iterator

in interface

Collection

<

K

>
- iterator

in interface

Iterable

<

K

>
- iterator

in interface

Set

<

K

>

**Returns:**
- an iterator over the keys of the backing map

---

#### public boolean add​(
K
e)

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

**Specified by:**
- add

in interface

Collection

<

K

>
- add

in interface

Set

<

K

>

**Parameters:**
- e

- key to be added

**Returns:**
- true

if this set changed as a result of the call

**Throws:**
- NullPointerException

- if the specified key is null
- UnsupportedOperationException

- if no default mapped value
for additions was provided

---

#### public boolean addAll​(
Collection
<? extends
K
> c)

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

**Specified by:**
- addAll

in interface

Collection

<

K

>
- addAll

in interface

Set

<

K

>

**Parameters:**
- c

- the elements to be inserted into this set

**Returns:**
- true

if this set changed as a result of the call

**Throws:**
- NullPointerException

- if the collection or any of its
elements are

null
- UnsupportedOperationException

- if no default mapped value
for additions was provided

**See Also:**
- Set.add(Object)

---

#### public
ConcurrentHashMap
<K,​V> getMap()

Returns the map backing this view.

**Returns:**
- the map backing this view

---

#### public final void clear()

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

**Specified by:**
- clear

in interface

Collection

<K>

---

#### public final int size()

Description copied from interface:

Collection

**Specified by:**
- size

in interface

Collection

<K>

**Returns:**
- the number of elements in this collection

---

#### public final boolean isEmpty()

Description copied from interface:

Collection

**Specified by:**
- isEmpty

in interface

Collection

<K>

**Returns:**
- true

if this collection contains no elements

---

#### public final
Object
[] toArray()

Description copied from interface:

Collection

**Specified by:**
- toArray

in interface

Collection

<K>

**Returns:**
- an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

---

#### public final <T> T[] toArray​(T[] a)

Description copied from interface:

Collection

**Specified by:**
- toArray

in interface

Collection

<K>

**Parameters:**
- a

- the array into which the elements of this collection are to be
stored, if it is big enough; otherwise, a new array of the same
runtime type is allocated for this purpose.

**Returns:**
- an array containing all of the elements in this collection

**Type Parameters:**
- T

- the component type of the array to contain the collection

---

#### public final
String
toString()

Returns a string representation of this collection.
The string representation consists of the string representations
of the collection's elements in the order they are returned by
its iterator, enclosed in square brackets (

"[]"

).
Adjacent elements are separated by the characters

", "

(comma and space). Elements are converted to strings as by

String.valueOf(Object)

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this collection

---

#### public final boolean containsAll​(
Collection
<?> c)

Description copied from interface:

Collection

**Specified by:**
- containsAll

in interface

Collection

<K>

**Parameters:**
- c

- collection to be checked for containment in this collection

**Returns:**
- true

if this collection contains all of the elements
in the specified collection

**See Also:**
- Collection.contains(Object)

---

#### public boolean removeAll​(
Collection
<?> c)

Description copied from interface:

Collection

**Specified by:**
- removeAll

in interface

Collection

<K>

**Parameters:**
- c

- collection containing elements to be removed from this collection

**Returns:**
- true

if this collection changed as a result of the
call

**See Also:**
- Collection.remove(Object)

,

Collection.contains(Object)

---

#### public final boolean retainAll​(
Collection
<?> c)

Description copied from interface:

Collection

**Specified by:**
- retainAll

in interface

Collection

<K>

**Parameters:**
- c

- collection containing elements to be retained in this collection

**Returns:**
- true

if this collection changed as a result of the call

**See Also:**
- Collection.remove(Object)

,

Collection.contains(Object)

---

### Additional Sections

#### Class ConcurrentHashMap.KeySetView<K,​V>

java.lang.Object

- java.util.concurrent.ConcurrentHashMap.KeySetView<K,​V>

java.util.concurrent.ConcurrentHashMap.KeySetView<K,​V>

**All Implemented Interfaces:** Serializable

,

Iterable

<K>

,

Collection

<K>

,

Set

<K>

**Enclosing class:** ConcurrentHashMap

<

K

,​

V

>

```java
public static class
ConcurrentHashMap.KeySetView<K,​V>

extends
Object

implements
Set
<K>,
Serializable
```

A view of a ConcurrentHashMap as a

Set

of keys, in
which additions may optionally be enabled by mapping to a
common value. This class cannot be directly instantiated.
See

keySet()

,

keySet(V)

,

newKeySet()

,

newKeySet(int)

.

**Since:** 1.8
**See Also:** Serialized Form

public static class

ConcurrentHashMap.KeySetView<K,​V>

extends

Object

implements

Set

<K>,

Serializable

A view of a ConcurrentHashMap as a

Set

of keys, in
which additions may optionally be enabled by mapping to a
common value. This class cannot be directly instantiated.
See

keySet()

,

keySet(V)

,

newKeySet()

,

newKeySet(int)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

K

e)

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

boolean

addAll

​(

Collection

<? extends

K

> c)

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

void

clear

()

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

boolean

contains

​(

Object

o)

Returns

true

if this collection contains the specified element.

boolean

containsAll

​(

Collection

<?> c)

Returns

true

if this collection contains all of the elements
in the specified collection.

ConcurrentHashMap

<K,​V>

getMap

()

Returns the map backing this view.

V

getMappedValue

()

Returns the default mapped value for additions,
or

null

if additions are not supported.

boolean

isEmpty

()

Returns

true

if this collection contains no elements.

Iterator

<

K

>

iterator

()

Returns an iterator over the elements in this collection.

boolean

remove

​(

Object

o)

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map.

boolean

removeAll

​(

Collection

<?> c)

Removes all of this collection's elements that are also contained in the
specified collection (optional operation).

boolean

retainAll

​(

Collection

<?> c)

Retains only the elements in this collection that are contained in the
specified collection (optional operation).

int

size

()

Returns the number of elements in this collection.

Object

[]

toArray

()

Returns an array containing all of the elements in this collection.

<T> T[]

toArray

​(T[] a)

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.

String

toString

()

Returns a string representation of this collection.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

clear

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

removeAll

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

K

e)

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

boolean

addAll

​(

Collection

<? extends

K

> c)

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

void

clear

()

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

boolean

contains

​(

Object

o)

Returns

true

if this collection contains the specified element.

boolean

containsAll

​(

Collection

<?> c)

Returns

true

if this collection contains all of the elements
in the specified collection.

ConcurrentHashMap

<K,​V>

getMap

()

Returns the map backing this view.

V

getMappedValue

()

Returns the default mapped value for additions,
or

null

if additions are not supported.

boolean

isEmpty

()

Returns

true

if this collection contains no elements.

Iterator

<

K

>

iterator

()

Returns an iterator over the elements in this collection.

boolean

remove

​(

Object

o)

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map.

boolean

removeAll

​(

Collection

<?> c)

Removes all of this collection's elements that are also contained in the
specified collection (optional operation).

boolean

retainAll

​(

Collection

<?> c)

Retains only the elements in this collection that are contained in the
specified collection (optional operation).

int

size

()

Returns the number of elements in this collection.

Object

[]

toArray

()

Returns an array containing all of the elements in this collection.

<T> T[]

toArray

​(T[] a)

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.

String

toString

()

Returns a string representation of this collection.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

clear

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

removeAll

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

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

Returns

true

if this collection contains the specified element.

Returns

true

if this collection contains all of the elements
in the specified collection.

Returns the map backing this view.

Returns the default mapped value for additions,
or

null

if additions are not supported.

Returns

true

if this collection contains no elements.

Returns an iterator over the elements in this collection.

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map.

Removes all of this collection's elements that are also contained in the
specified collection (optional operation).

Retains only the elements in this collection that are contained in the
specified collection (optional operation).

Returns the number of elements in this collection.

Returns an array containing all of the elements in this collection.

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.

Returns a string representation of this collection.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

clear

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

removeAll

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

============ METHOD DETAIL ==========

- Method Detail

- getMappedValue

```java
public
V
getMappedValue()
```

Returns the default mapped value for additions,
or

null

if additions are not supported.

**Returns:** the default mapped value for additions, or

null

if not supported

- contains

```java
public boolean contains​(
Object
o)
```

Returns

true

if this collection contains the specified element.
More formally, returns

true

if and only if this collection
contains at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:** contains

in interface

Collection

<

K

>
**Specified by:** contains

in interface

Set

<

K

>
**Parameters:** o

- element whose presence in this collection is to be tested
**Returns:** true

if this collection contains the specified
element
**Throws:** NullPointerException

- if the specified key is null

- remove

```java
public boolean remove​(
Object
o)
```

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map. This method does
nothing if the key is not in the map.

**Specified by:** remove

in interface

Collection

<

K

>
**Specified by:** remove

in interface

Set

<

K

>
**Parameters:** o

- the key to be removed from the backing map
**Returns:** true

if the backing map contained the specified key
**Throws:** NullPointerException

- if the specified key is null

- iterator

```java
public
Iterator
<
K
> iterator()
```

Returns an iterator over the elements in this collection.

The returned iterator is

weakly consistent

.

**Specified by:** iterator

in interface

Collection

<

K

>
**Specified by:** iterator

in interface

Iterable

<

K

>
**Specified by:** iterator

in interface

Set

<

K

>
**Returns:** an iterator over the keys of the backing map

- add

```java
public boolean add​(
K
e)
```

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

**Specified by:** add

in interface

Collection

<

K

>
**Specified by:** add

in interface

Set

<

K

>
**Parameters:** e

- key to be added
**Returns:** true

if this set changed as a result of the call
**Throws:** NullPointerException

- if the specified key is null
**Throws:** UnsupportedOperationException

- if no default mapped value
for additions was provided

- addAll

```java
public boolean addAll​(
Collection
<? extends
K
> c)
```

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

**Specified by:** addAll

in interface

Collection

<

K

>
**Specified by:** addAll

in interface

Set

<

K

>
**Parameters:** c

- the elements to be inserted into this set
**Returns:** true

if this set changed as a result of the call
**Throws:** NullPointerException

- if the collection or any of its
elements are

null
**Throws:** UnsupportedOperationException

- if no default mapped value
for additions was provided
**See Also:** Set.add(Object)

- getMap

```java
public
ConcurrentHashMap
<K,​V> getMap()
```

Returns the map backing this view.

**Returns:** the map backing this view

- clear

```java
public final void clear()
```

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

**Specified by:** clear

in interface

Collection

<K>

- size

```java
public final int size()
```

Description copied from interface:

Collection

Returns the number of elements in this collection. If this collection
contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:** size

in interface

Collection

<K>
**Returns:** the number of elements in this collection

- isEmpty

```java
public final boolean isEmpty()
```

Description copied from interface:

Collection

Returns

true

if this collection contains no elements.

**Specified by:** isEmpty

in interface

Collection

<K>
**Returns:** true

if this collection contains no elements

- toArray

```java
public final
Object
[] toArray()
```

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection.
If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order. The returned array's

runtime component type

is

Object

.

The returned array will be "safe" in that no references to it are
maintained by this collection. (In other words, this method must
allocate a new array even if this collection is backed by an array).
The caller is thus free to modify the returned array.

**Specified by:** toArray

in interface

Collection

<K>
**Returns:** an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

- toArray

```java
public final <T> T[] toArray​(T[] a)
```

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.
If the collection fits in the specified array, it is returned therein.
Otherwise, a new array is allocated with the runtime type of the
specified array and the size of this collection.

If this collection fits in the specified array with room to spare
(i.e., the array has more elements than this collection), the element
in the array immediately following the end of the collection is set to

null

. (This is useful in determining the length of this
collection

only

if the caller knows that this collection does
not contain any

null

elements.)

If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order.

**Specified by:** toArray

in interface

Collection

<K>
**Type Parameters:** T

- the component type of the array to contain the collection
**Parameters:** a

- the array into which the elements of this collection are to be
stored, if it is big enough; otherwise, a new array of the same
runtime type is allocated for this purpose.
**Returns:** an array containing all of the elements in this collection

- toString

```java
public final
String
toString()
```

Returns a string representation of this collection.
The string representation consists of the string representations
of the collection's elements in the order they are returned by
its iterator, enclosed in square brackets (

"[]"

).
Adjacent elements are separated by the characters

", "

(comma and space). Elements are converted to strings as by

String.valueOf(Object)

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this collection

- containsAll

```java
public final boolean containsAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Returns

true

if this collection contains all of the elements
in the specified collection.

**Specified by:** containsAll

in interface

Collection

<K>
**Parameters:** c

- collection to be checked for containment in this collection
**Returns:** true

if this collection contains all of the elements
in the specified collection
**See Also:** Collection.contains(Object)

- removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Removes all of this collection's elements that are also contained in the
specified collection (optional operation). After this call returns,
this collection will contain no elements in common with the specified
collection.

**Specified by:** removeAll

in interface

Collection

<K>
**Parameters:** c

- collection containing elements to be removed from this collection
**Returns:** true

if this collection changed as a result of the
call
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

- retainAll

```java
public final boolean retainAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Retains only the elements in this collection that are contained in the
specified collection (optional operation). In other words, removes from
this collection all of its elements that are not contained in the
specified collection.

**Specified by:** retainAll

in interface

Collection

<K>
**Parameters:** c

- collection containing elements to be retained in this collection
**Returns:** true

if this collection changed as a result of the call
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

Method Detail

- getMappedValue

```java
public
V
getMappedValue()
```

Returns the default mapped value for additions,
or

null

if additions are not supported.

**Returns:** the default mapped value for additions, or

null

if not supported

- contains

```java
public boolean contains​(
Object
o)
```

Returns

true

if this collection contains the specified element.
More formally, returns

true

if and only if this collection
contains at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:** contains

in interface

Collection

<

K

>
**Specified by:** contains

in interface

Set

<

K

>
**Parameters:** o

- element whose presence in this collection is to be tested
**Returns:** true

if this collection contains the specified
element
**Throws:** NullPointerException

- if the specified key is null

- remove

```java
public boolean remove​(
Object
o)
```

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map. This method does
nothing if the key is not in the map.

**Specified by:** remove

in interface

Collection

<

K

>
**Specified by:** remove

in interface

Set

<

K

>
**Parameters:** o

- the key to be removed from the backing map
**Returns:** true

if the backing map contained the specified key
**Throws:** NullPointerException

- if the specified key is null

- iterator

```java
public
Iterator
<
K
> iterator()
```

Returns an iterator over the elements in this collection.

The returned iterator is

weakly consistent

.

**Specified by:** iterator

in interface

Collection

<

K

>
**Specified by:** iterator

in interface

Iterable

<

K

>
**Specified by:** iterator

in interface

Set

<

K

>
**Returns:** an iterator over the keys of the backing map

- add

```java
public boolean add​(
K
e)
```

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

**Specified by:** add

in interface

Collection

<

K

>
**Specified by:** add

in interface

Set

<

K

>
**Parameters:** e

- key to be added
**Returns:** true

if this set changed as a result of the call
**Throws:** NullPointerException

- if the specified key is null
**Throws:** UnsupportedOperationException

- if no default mapped value
for additions was provided

- addAll

```java
public boolean addAll​(
Collection
<? extends
K
> c)
```

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

**Specified by:** addAll

in interface

Collection

<

K

>
**Specified by:** addAll

in interface

Set

<

K

>
**Parameters:** c

- the elements to be inserted into this set
**Returns:** true

if this set changed as a result of the call
**Throws:** NullPointerException

- if the collection or any of its
elements are

null
**Throws:** UnsupportedOperationException

- if no default mapped value
for additions was provided
**See Also:** Set.add(Object)

- getMap

```java
public
ConcurrentHashMap
<K,​V> getMap()
```

Returns the map backing this view.

**Returns:** the map backing this view

- clear

```java
public final void clear()
```

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

**Specified by:** clear

in interface

Collection

<K>

- size

```java
public final int size()
```

Description copied from interface:

Collection

Returns the number of elements in this collection. If this collection
contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:** size

in interface

Collection

<K>
**Returns:** the number of elements in this collection

- isEmpty

```java
public final boolean isEmpty()
```

Description copied from interface:

Collection

Returns

true

if this collection contains no elements.

**Specified by:** isEmpty

in interface

Collection

<K>
**Returns:** true

if this collection contains no elements

- toArray

```java
public final
Object
[] toArray()
```

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection.
If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order. The returned array's

runtime component type

is

Object

.

The returned array will be "safe" in that no references to it are
maintained by this collection. (In other words, this method must
allocate a new array even if this collection is backed by an array).
The caller is thus free to modify the returned array.

**Specified by:** toArray

in interface

Collection

<K>
**Returns:** an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

- toArray

```java
public final <T> T[] toArray​(T[] a)
```

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.
If the collection fits in the specified array, it is returned therein.
Otherwise, a new array is allocated with the runtime type of the
specified array and the size of this collection.

If this collection fits in the specified array with room to spare
(i.e., the array has more elements than this collection), the element
in the array immediately following the end of the collection is set to

null

. (This is useful in determining the length of this
collection

only

if the caller knows that this collection does
not contain any

null

elements.)

If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order.

**Specified by:** toArray

in interface

Collection

<K>
**Type Parameters:** T

- the component type of the array to contain the collection
**Parameters:** a

- the array into which the elements of this collection are to be
stored, if it is big enough; otherwise, a new array of the same
runtime type is allocated for this purpose.
**Returns:** an array containing all of the elements in this collection

- toString

```java
public final
String
toString()
```

Returns a string representation of this collection.
The string representation consists of the string representations
of the collection's elements in the order they are returned by
its iterator, enclosed in square brackets (

"[]"

).
Adjacent elements are separated by the characters

", "

(comma and space). Elements are converted to strings as by

String.valueOf(Object)

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this collection

- containsAll

```java
public final boolean containsAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Returns

true

if this collection contains all of the elements
in the specified collection.

**Specified by:** containsAll

in interface

Collection

<K>
**Parameters:** c

- collection to be checked for containment in this collection
**Returns:** true

if this collection contains all of the elements
in the specified collection
**See Also:** Collection.contains(Object)

- removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Removes all of this collection's elements that are also contained in the
specified collection (optional operation). After this call returns,
this collection will contain no elements in common with the specified
collection.

**Specified by:** removeAll

in interface

Collection

<K>
**Parameters:** c

- collection containing elements to be removed from this collection
**Returns:** true

if this collection changed as a result of the
call
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

- retainAll

```java
public final boolean retainAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Retains only the elements in this collection that are contained in the
specified collection (optional operation). In other words, removes from
this collection all of its elements that are not contained in the
specified collection.

**Specified by:** retainAll

in interface

Collection

<K>
**Parameters:** c

- collection containing elements to be retained in this collection
**Returns:** true

if this collection changed as a result of the call
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

---

#### Method Detail

getMappedValue

```java
public
V
getMappedValue()
```

Returns the default mapped value for additions,
or

null

if additions are not supported.

**Returns:** the default mapped value for additions, or

null

if not supported

---

#### getMappedValue

public

V

getMappedValue()

Returns the default mapped value for additions,
or

null

if additions are not supported.

contains

```java
public boolean contains​(
Object
o)
```

Returns

true

if this collection contains the specified element.
More formally, returns

true

if and only if this collection
contains at least one element

e

such that

Objects.equals(o, e)

.

**Specified by:** contains

in interface

Collection

<

K

>
**Specified by:** contains

in interface

Set

<

K

>
**Parameters:** o

- element whose presence in this collection is to be tested
**Returns:** true

if this collection contains the specified
element
**Throws:** NullPointerException

- if the specified key is null

---

#### contains

public boolean contains​(

Object

o)

Returns

true

if this collection contains the specified element.
More formally, returns

true

if and only if this collection
contains at least one element

e

such that

Objects.equals(o, e)

.

remove

```java
public boolean remove​(
Object
o)
```

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map. This method does
nothing if the key is not in the map.

**Specified by:** remove

in interface

Collection

<

K

>
**Specified by:** remove

in interface

Set

<

K

>
**Parameters:** o

- the key to be removed from the backing map
**Returns:** true

if the backing map contained the specified key
**Throws:** NullPointerException

- if the specified key is null

---

#### remove

public boolean remove​(

Object

o)

Removes the key from this map view, by removing the key (and its
corresponding value) from the backing map. This method does
nothing if the key is not in the map.

iterator

```java
public
Iterator
<
K
> iterator()
```

Returns an iterator over the elements in this collection.

The returned iterator is

weakly consistent

.

**Specified by:** iterator

in interface

Collection

<

K

>
**Specified by:** iterator

in interface

Iterable

<

K

>
**Specified by:** iterator

in interface

Set

<

K

>
**Returns:** an iterator over the keys of the backing map

---

#### iterator

public

Iterator

<

K

> iterator()

Returns an iterator over the elements in this collection.

The returned iterator is

weakly consistent

.

The returned iterator is

weakly consistent

.

add

```java
public boolean add​(
K
e)
```

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

**Specified by:** add

in interface

Collection

<

K

>
**Specified by:** add

in interface

Set

<

K

>
**Parameters:** e

- key to be added
**Returns:** true

if this set changed as a result of the call
**Throws:** NullPointerException

- if the specified key is null
**Throws:** UnsupportedOperationException

- if no default mapped value
for additions was provided

---

#### add

public boolean add​(

K

e)

Adds the specified key to this set view by mapping the key to
the default mapped value in the backing map, if defined.

addAll

```java
public boolean addAll​(
Collection
<? extends
K
> c)
```

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

**Specified by:** addAll

in interface

Collection

<

K

>
**Specified by:** addAll

in interface

Set

<

K

>
**Parameters:** c

- the elements to be inserted into this set
**Returns:** true

if this set changed as a result of the call
**Throws:** NullPointerException

- if the collection or any of its
elements are

null
**Throws:** UnsupportedOperationException

- if no default mapped value
for additions was provided
**See Also:** Set.add(Object)

---

#### addAll

public boolean addAll​(

Collection

<? extends

K

> c)

Adds all of the elements in the specified collection to this set,
as if by calling

add(K)

on each one.

getMap

```java
public
ConcurrentHashMap
<K,​V> getMap()
```

Returns the map backing this view.

**Returns:** the map backing this view

---

#### getMap

public

ConcurrentHashMap

<K,​V> getMap()

Returns the map backing this view.

clear

```java
public final void clear()
```

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

**Specified by:** clear

in interface

Collection

<K>

---

#### clear

public final void clear()

Removes all of the elements from this view, by removing all
the mappings from the map backing this view.

size

```java
public final int size()
```

Description copied from interface:

Collection

Returns the number of elements in this collection. If this collection
contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

**Specified by:** size

in interface

Collection

<K>
**Returns:** the number of elements in this collection

---

#### size

public final int size()

Description copied from interface:

Collection

Returns the number of elements in this collection. If this collection
contains more than

Integer.MAX_VALUE

elements, returns

Integer.MAX_VALUE

.

isEmpty

```java
public final boolean isEmpty()
```

Description copied from interface:

Collection

Returns

true

if this collection contains no elements.

**Specified by:** isEmpty

in interface

Collection

<K>
**Returns:** true

if this collection contains no elements

---

#### isEmpty

public final boolean isEmpty()

Description copied from interface:

Collection

Returns

true

if this collection contains no elements.

toArray

```java
public final
Object
[] toArray()
```

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection.
If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order. The returned array's

runtime component type

is

Object

.

The returned array will be "safe" in that no references to it are
maintained by this collection. (In other words, this method must
allocate a new array even if this collection is backed by an array).
The caller is thus free to modify the returned array.

**Specified by:** toArray

in interface

Collection

<K>
**Returns:** an array, whose

runtime component
type

is

Object

, containing all of the elements in this collection

---

#### toArray

public final

Object

[] toArray()

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection.
If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order. The returned array's

runtime component type

is

Object

.

The returned array will be "safe" in that no references to it are
maintained by this collection. (In other words, this method must
allocate a new array even if this collection is backed by an array).
The caller is thus free to modify the returned array.

The returned array will be "safe" in that no references to it are
maintained by this collection. (In other words, this method must
allocate a new array even if this collection is backed by an array).
The caller is thus free to modify the returned array.

toArray

```java
public final <T> T[] toArray​(T[] a)
```

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.
If the collection fits in the specified array, it is returned therein.
Otherwise, a new array is allocated with the runtime type of the
specified array and the size of this collection.

If this collection fits in the specified array with room to spare
(i.e., the array has more elements than this collection), the element
in the array immediately following the end of the collection is set to

null

. (This is useful in determining the length of this
collection

only

if the caller knows that this collection does
not contain any

null

elements.)

If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order.

**Specified by:** toArray

in interface

Collection

<K>
**Type Parameters:** T

- the component type of the array to contain the collection
**Parameters:** a

- the array into which the elements of this collection are to be
stored, if it is big enough; otherwise, a new array of the same
runtime type is allocated for this purpose.
**Returns:** an array containing all of the elements in this collection

---

#### toArray

public final <T> T[] toArray​(T[] a)

Description copied from interface:

Collection

Returns an array containing all of the elements in this collection;
the runtime type of the returned array is that of the specified array.
If the collection fits in the specified array, it is returned therein.
Otherwise, a new array is allocated with the runtime type of the
specified array and the size of this collection.

If this collection fits in the specified array with room to spare
(i.e., the array has more elements than this collection), the element
in the array immediately following the end of the collection is set to

null

. (This is useful in determining the length of this
collection

only

if the caller knows that this collection does
not contain any

null

elements.)

If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order.

If this collection fits in the specified array with room to spare
(i.e., the array has more elements than this collection), the element
in the array immediately following the end of the collection is set to

null

. (This is useful in determining the length of this
collection

only

if the caller knows that this collection does
not contain any

null

elements.)

If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order.

If this collection makes any guarantees as to what order its elements
are returned by its iterator, this method must return the elements in
the same order.

toString

```java
public final
String
toString()
```

Returns a string representation of this collection.
The string representation consists of the string representations
of the collection's elements in the order they are returned by
its iterator, enclosed in square brackets (

"[]"

).
Adjacent elements are separated by the characters

", "

(comma and space). Elements are converted to strings as by

String.valueOf(Object)

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this collection

---

#### toString

public final

String

toString()

Returns a string representation of this collection.
The string representation consists of the string representations
of the collection's elements in the order they are returned by
its iterator, enclosed in square brackets (

"[]"

).
Adjacent elements are separated by the characters

", "

(comma and space). Elements are converted to strings as by

String.valueOf(Object)

.

containsAll

```java
public final boolean containsAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Returns

true

if this collection contains all of the elements
in the specified collection.

**Specified by:** containsAll

in interface

Collection

<K>
**Parameters:** c

- collection to be checked for containment in this collection
**Returns:** true

if this collection contains all of the elements
in the specified collection
**See Also:** Collection.contains(Object)

---

#### containsAll

public final boolean containsAll​(

Collection

<?> c)

Description copied from interface:

Collection

Returns

true

if this collection contains all of the elements
in the specified collection.

removeAll

```java
public boolean removeAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Removes all of this collection's elements that are also contained in the
specified collection (optional operation). After this call returns,
this collection will contain no elements in common with the specified
collection.

**Specified by:** removeAll

in interface

Collection

<K>
**Parameters:** c

- collection containing elements to be removed from this collection
**Returns:** true

if this collection changed as a result of the
call
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

---

#### removeAll

public boolean removeAll​(

Collection

<?> c)

Description copied from interface:

Collection

Removes all of this collection's elements that are also contained in the
specified collection (optional operation). After this call returns,
this collection will contain no elements in common with the specified
collection.

retainAll

```java
public final boolean retainAll​(
Collection
<?> c)
```

Description copied from interface:

Collection

Retains only the elements in this collection that are contained in the
specified collection (optional operation). In other words, removes from
this collection all of its elements that are not contained in the
specified collection.

**Specified by:** retainAll

in interface

Collection

<K>
**Parameters:** c

- collection containing elements to be retained in this collection
**Returns:** true

if this collection changed as a result of the call
**See Also:** Collection.remove(Object)

,

Collection.contains(Object)

---

#### retainAll

public final boolean retainAll​(

Collection

<?> c)

Description copied from interface:

Collection

Retains only the elements in this collection that are contained in the
specified collection (optional operation). In other words, removes from
this collection all of its elements that are not contained in the
specified collection.

---

