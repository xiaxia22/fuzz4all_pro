# Interface Map.Entry<K,​V>

**Source:** `java.base\java\util\Map.Entry.html`

### Class Description

```java
public static interface
Map.Entry<K,​V>
```

A map entry (key-value pair). The

Map.entrySet

method returns
a collection-view of the map, whose elements are of this class. The

only

way to obtain a reference to a map entry is from the
iterator of this collection-view. These

Map.Entry

objects are
valid

only

for the duration of the iteration; more formally,
the behavior of a map entry is undefined if the backing map has been
modified after the entry was returned by the iterator, except through
the

setValue

operation on the map entry.

**All Known Implementing Classes:** AbstractMap.SimpleEntry

,

AbstractMap.SimpleImmutableEntry

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### K
getKey()

Returns the key corresponding to this entry.

**Returns:**
- the key corresponding to this entry

**Throws:**
- IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

---

#### V
getValue()

Returns the value corresponding to this entry. If the mapping
has been removed from the backing map (by the iterator's

remove

operation), the results of this call are undefined.

**Returns:**
- the value corresponding to this entry

**Throws:**
- IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

---

#### V
setValue​(
V
value)

Replaces the value corresponding to this entry with the specified
value (optional operation). (Writes through to the map.) The
behavior of this call is undefined if the mapping has already been
removed from the map (by the iterator's

remove

operation).

**Parameters:**
- value

- new value to be stored in this entry

**Returns:**
- old value corresponding to the entry

**Throws:**
- UnsupportedOperationException

- if the

put

operation
is not supported by the backing map
- ClassCastException

- if the class of the specified value
prevents it from being stored in the backing map
- NullPointerException

- if the backing map does not permit
null values, and the specified value is null
- IllegalArgumentException

- if some property of this value
prevents it from being stored in the backing map
- IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

---

#### boolean equals​(
Object
o)

Compares the specified object with this entry for equality.
Returns

true

if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries

e1

and

e2

represent the same mapping
if

```java
(e1.getKey()==null ?
e2.getKey()==null : e1.getKey().equals(e2.getKey())) &&
(e1.getValue()==null ?
e2.getValue()==null : e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- object to be compared for equality with this map entry

**Returns:**
- true

if the specified object is equal to this map
entry

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code value for this map entry. The hash code
of a map entry

e

is defined to be:

```java
(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())
```

This ensures that

e1.equals(e2)

implies that

e1.hashCode()==e2.hashCode()

for any two Entries

e1

and

e2

, as required by the general
contract of

Object.hashCode

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this map entry

**See Also:**
- Object.hashCode()

,

Object.equals(Object)

,

equals(Object)

---

#### static <K extends
Comparable
<? super K>,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey()

Returns a comparator that compares

Map.Entry

in natural order on key.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with a null key.

**Returns:**
- a comparator that compares

Map.Entry

in natural order on key.

**See Also:**
- Comparable

**Since:**
- 1.8

**Type Parameters:**
- K

- the

Comparable

type of then map keys
- V

- the type of the map values

---

#### static <K,​V extends
Comparable
<? super V>>
Comparator
<
Map.Entry
<K,​V>> comparingByValue()

Returns a comparator that compares

Map.Entry

in natural order on value.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with null values.

**Returns:**
- a comparator that compares

Map.Entry

in natural order on value.

**See Also:**
- Comparable

**Since:**
- 1.8

**Type Parameters:**
- K

- the type of the map keys
- V

- the

Comparable

type of the map values

---

#### static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey​(
Comparator
<? super K> cmp)

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Parameters:**
- cmp

- the key

Comparator

**Returns:**
- a comparator that compares

Map.Entry

by the key.

**Since:**
- 1.8

**Type Parameters:**
- K

- the type of the map keys
- V

- the type of the map values

---

#### static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByValue​(
Comparator
<? super V> cmp)

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Parameters:**
- cmp

- the value

Comparator

**Returns:**
- a comparator that compares

Map.Entry

by the value.

**Since:**
- 1.8

**Type Parameters:**
- K

- the type of the map keys
- V

- the type of the map values

---

### Additional Sections

#### Interface Map.Entry<K,​V>

**All Known Implementing Classes:** AbstractMap.SimpleEntry

,

AbstractMap.SimpleImmutableEntry

**Enclosing interface:** Map

<

K

,​

V

>

```java
public static interface
Map.Entry<K,​V>
```

A map entry (key-value pair). The

Map.entrySet

method returns
a collection-view of the map, whose elements are of this class. The

only

way to obtain a reference to a map entry is from the
iterator of this collection-view. These

Map.Entry

objects are
valid

only

for the duration of the iteration; more formally,
the behavior of a map entry is undefined if the backing map has been
modified after the entry was returned by the iterator, except through
the

setValue

operation on the map entry.

**Since:** 1.2
**See Also:** Map.entrySet()

public static interface

Map.Entry<K,​V>

A map entry (key-value pair). The

Map.entrySet

method returns
a collection-view of the map, whose elements are of this class. The

only

way to obtain a reference to a map entry is from the
iterator of this collection-view. These

Map.Entry

objects are
valid

only

for the duration of the iteration; more formally,
the behavior of a map entry is undefined if the backing map has been
modified after the entry was returned by the iterator, except through
the

setValue

operation on the map entry.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

static <K extends

Comparable

<? super K>,​V>

Comparator

<

Map.Entry

<K,​V>>

comparingByKey

()

Returns a comparator that compares

Map.Entry

in natural order on key.

static <K,​V>

Comparator

<

Map.Entry

<K,​V>>

comparingByKey

​(

Comparator

<? super K> cmp)

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

static <K,​V extends

Comparable

<? super V>>

Comparator

<

Map.Entry

<K,​V>>

comparingByValue

()

Returns a comparator that compares

Map.Entry

in natural order on value.

static <K,​V>

Comparator

<

Map.Entry

<K,​V>>

comparingByValue

​(

Comparator

<? super V> cmp)

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

boolean

equals

​(

Object

o)

Compares the specified object with this entry for equality.

K

getKey

()

Returns the key corresponding to this entry.

V

getValue

()

Returns the value corresponding to this entry.

int

hashCode

()

Returns the hash code value for this map entry.

V

setValue

​(

V

value)

Replaces the value corresponding to this entry with the specified
value (optional operation).

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

static <K extends

Comparable

<? super K>,​V>

Comparator

<

Map.Entry

<K,​V>>

comparingByKey

()

Returns a comparator that compares

Map.Entry

in natural order on key.

static <K,​V>

Comparator

<

Map.Entry

<K,​V>>

comparingByKey

​(

Comparator

<? super K> cmp)

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

static <K,​V extends

Comparable

<? super V>>

Comparator

<

Map.Entry

<K,​V>>

comparingByValue

()

Returns a comparator that compares

Map.Entry

in natural order on value.

static <K,​V>

Comparator

<

Map.Entry

<K,​V>>

comparingByValue

​(

Comparator

<? super V> cmp)

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

boolean

equals

​(

Object

o)

Compares the specified object with this entry for equality.

K

getKey

()

Returns the key corresponding to this entry.

V

getValue

()

Returns the value corresponding to this entry.

int

hashCode

()

Returns the hash code value for this map entry.

V

setValue

​(

V

value)

Replaces the value corresponding to this entry with the specified
value (optional operation).

---

#### Method Summary

Returns a comparator that compares

Map.Entry

in natural order on key.

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

Returns a comparator that compares

Map.Entry

in natural order on value.

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

Compares the specified object with this entry for equality.

Returns the key corresponding to this entry.

Returns the value corresponding to this entry.

Returns the hash code value for this map entry.

Replaces the value corresponding to this entry with the specified
value (optional operation).

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
K
getKey()
```

Returns the key corresponding to this entry.

**Returns:** the key corresponding to this entry
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

- getValue

```java
V
getValue()
```

Returns the value corresponding to this entry. If the mapping
has been removed from the backing map (by the iterator's

remove

operation), the results of this call are undefined.

**Returns:** the value corresponding to this entry
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

- setValue

```java
V
setValue​(
V
value)
```

Replaces the value corresponding to this entry with the specified
value (optional operation). (Writes through to the map.) The
behavior of this call is undefined if the mapping has already been
removed from the map (by the iterator's

remove

operation).

**Parameters:** value

- new value to be stored in this entry
**Returns:** old value corresponding to the entry
**Throws:** UnsupportedOperationException

- if the

put

operation
is not supported by the backing map
**Throws:** ClassCastException

- if the class of the specified value
prevents it from being stored in the backing map
**Throws:** NullPointerException

- if the backing map does not permit
null values, and the specified value is null
**Throws:** IllegalArgumentException

- if some property of this value
prevents it from being stored in the backing map
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

- equals

```java
boolean equals​(
Object
o)
```

Compares the specified object with this entry for equality.
Returns

true

if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries

e1

and

e2

represent the same mapping
if

```java
(e1.getKey()==null ?
e2.getKey()==null : e1.getKey().equals(e2.getKey())) &&
(e1.getValue()==null ?
e2.getValue()==null : e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this map entry
**Returns:** true

if the specified object is equal to this map
entry
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this map entry. The hash code
of a map entry

e

is defined to be:

```java
(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())
```

This ensures that

e1.equals(e2)

implies that

e1.hashCode()==e2.hashCode()

for any two Entries

e1

and

e2

, as required by the general
contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this map entry
**See Also:** Object.hashCode()

,

Object.equals(Object)

,

equals(Object)

- comparingByKey

```java
static <K extends
Comparable
<? super K>,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey()
```

Returns a comparator that compares

Map.Entry

in natural order on key.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with a null key.

**Type Parameters:** K

- the

Comparable

type of then map keys
**Type Parameters:** V

- the type of the map values
**Returns:** a comparator that compares

Map.Entry

in natural order on key.
**Since:** 1.8
**See Also:** Comparable

- comparingByValue

```java
static <K,​V extends
Comparable
<? super V>>
Comparator
<
Map.Entry
<K,​V>> comparingByValue()
```

Returns a comparator that compares

Map.Entry

in natural order on value.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with null values.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the

Comparable

type of the map values
**Returns:** a comparator that compares

Map.Entry

in natural order on value.
**Since:** 1.8
**See Also:** Comparable

- comparingByKey

```java
static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey​(
Comparator
<? super K> cmp)
```

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the type of the map values
**Parameters:** cmp

- the key

Comparator
**Returns:** a comparator that compares

Map.Entry

by the key.
**Since:** 1.8

- comparingByValue

```java
static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByValue​(
Comparator
<? super V> cmp)
```

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the type of the map values
**Parameters:** cmp

- the value

Comparator
**Returns:** a comparator that compares

Map.Entry

by the value.
**Since:** 1.8

Method Detail

- getKey

```java
K
getKey()
```

Returns the key corresponding to this entry.

**Returns:** the key corresponding to this entry
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

- getValue

```java
V
getValue()
```

Returns the value corresponding to this entry. If the mapping
has been removed from the backing map (by the iterator's

remove

operation), the results of this call are undefined.

**Returns:** the value corresponding to this entry
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

- setValue

```java
V
setValue​(
V
value)
```

Replaces the value corresponding to this entry with the specified
value (optional operation). (Writes through to the map.) The
behavior of this call is undefined if the mapping has already been
removed from the map (by the iterator's

remove

operation).

**Parameters:** value

- new value to be stored in this entry
**Returns:** old value corresponding to the entry
**Throws:** UnsupportedOperationException

- if the

put

operation
is not supported by the backing map
**Throws:** ClassCastException

- if the class of the specified value
prevents it from being stored in the backing map
**Throws:** NullPointerException

- if the backing map does not permit
null values, and the specified value is null
**Throws:** IllegalArgumentException

- if some property of this value
prevents it from being stored in the backing map
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

- equals

```java
boolean equals​(
Object
o)
```

Compares the specified object with this entry for equality.
Returns

true

if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries

e1

and

e2

represent the same mapping
if

```java
(e1.getKey()==null ?
e2.getKey()==null : e1.getKey().equals(e2.getKey())) &&
(e1.getValue()==null ?
e2.getValue()==null : e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this map entry
**Returns:** true

if the specified object is equal to this map
entry
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code value for this map entry. The hash code
of a map entry

e

is defined to be:

```java
(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())
```

This ensures that

e1.equals(e2)

implies that

e1.hashCode()==e2.hashCode()

for any two Entries

e1

and

e2

, as required by the general
contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this map entry
**See Also:** Object.hashCode()

,

Object.equals(Object)

,

equals(Object)

- comparingByKey

```java
static <K extends
Comparable
<? super K>,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey()
```

Returns a comparator that compares

Map.Entry

in natural order on key.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with a null key.

**Type Parameters:** K

- the

Comparable

type of then map keys
**Type Parameters:** V

- the type of the map values
**Returns:** a comparator that compares

Map.Entry

in natural order on key.
**Since:** 1.8
**See Also:** Comparable

- comparingByValue

```java
static <K,​V extends
Comparable
<? super V>>
Comparator
<
Map.Entry
<K,​V>> comparingByValue()
```

Returns a comparator that compares

Map.Entry

in natural order on value.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with null values.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the

Comparable

type of the map values
**Returns:** a comparator that compares

Map.Entry

in natural order on value.
**Since:** 1.8
**See Also:** Comparable

- comparingByKey

```java
static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey​(
Comparator
<? super K> cmp)
```

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the type of the map values
**Parameters:** cmp

- the key

Comparator
**Returns:** a comparator that compares

Map.Entry

by the key.
**Since:** 1.8

- comparingByValue

```java
static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByValue​(
Comparator
<? super V> cmp)
```

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the type of the map values
**Parameters:** cmp

- the value

Comparator
**Returns:** a comparator that compares

Map.Entry

by the value.
**Since:** 1.8

---

#### Method Detail

getKey

```java
K
getKey()
```

Returns the key corresponding to this entry.

**Returns:** the key corresponding to this entry
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

---

#### getKey

K

getKey()

Returns the key corresponding to this entry.

getValue

```java
V
getValue()
```

Returns the value corresponding to this entry. If the mapping
has been removed from the backing map (by the iterator's

remove

operation), the results of this call are undefined.

**Returns:** the value corresponding to this entry
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

---

#### getValue

V

getValue()

Returns the value corresponding to this entry. If the mapping
has been removed from the backing map (by the iterator's

remove

operation), the results of this call are undefined.

setValue

```java
V
setValue​(
V
value)
```

Replaces the value corresponding to this entry with the specified
value (optional operation). (Writes through to the map.) The
behavior of this call is undefined if the mapping has already been
removed from the map (by the iterator's

remove

operation).

**Parameters:** value

- new value to be stored in this entry
**Returns:** old value corresponding to the entry
**Throws:** UnsupportedOperationException

- if the

put

operation
is not supported by the backing map
**Throws:** ClassCastException

- if the class of the specified value
prevents it from being stored in the backing map
**Throws:** NullPointerException

- if the backing map does not permit
null values, and the specified value is null
**Throws:** IllegalArgumentException

- if some property of this value
prevents it from being stored in the backing map
**Throws:** IllegalStateException

- implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

---

#### setValue

V

setValue​(

V

value)

Replaces the value corresponding to this entry with the specified
value (optional operation). (Writes through to the map.) The
behavior of this call is undefined if the mapping has already been
removed from the map (by the iterator's

remove

operation).

equals

```java
boolean equals​(
Object
o)
```

Compares the specified object with this entry for equality.
Returns

true

if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries

e1

and

e2

represent the same mapping
if

```java
(e1.getKey()==null ?
e2.getKey()==null : e1.getKey().equals(e2.getKey())) &&
(e1.getValue()==null ?
e2.getValue()==null : e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this map entry
**Returns:** true

if the specified object is equal to this map
entry
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

o)

Compares the specified object with this entry for equality.
Returns

true

if the given object is also a map entry and
the two entries represent the same mapping. More formally, two
entries

e1

and

e2

represent the same mapping
if

```java
(e1.getKey()==null ?
e2.getKey()==null : e1.getKey().equals(e2.getKey())) &&
(e1.getValue()==null ?
e2.getValue()==null : e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

(e1.getKey()==null ?
e2.getKey()==null : e1.getKey().equals(e2.getKey())) &&
(e1.getValue()==null ?
e2.getValue()==null : e1.getValue().equals(e2.getValue()))

hashCode

```java
int hashCode()
```

Returns the hash code value for this map entry. The hash code
of a map entry

e

is defined to be:

```java
(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())
```

This ensures that

e1.equals(e2)

implies that

e1.hashCode()==e2.hashCode()

for any two Entries

e1

and

e2

, as required by the general
contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this map entry
**See Also:** Object.hashCode()

,

Object.equals(Object)

,

equals(Object)

---

#### hashCode

int hashCode()

Returns the hash code value for this map entry. The hash code
of a map entry

e

is defined to be:

```java
(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())
```

This ensures that

e1.equals(e2)

implies that

e1.hashCode()==e2.hashCode()

for any two Entries

e1

and

e2

, as required by the general
contract of

Object.hashCode

.

(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())

comparingByKey

```java
static <K extends
Comparable
<? super K>,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey()
```

Returns a comparator that compares

Map.Entry

in natural order on key.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with a null key.

**Type Parameters:** K

- the

Comparable

type of then map keys
**Type Parameters:** V

- the type of the map values
**Returns:** a comparator that compares

Map.Entry

in natural order on key.
**Since:** 1.8
**See Also:** Comparable

---

#### comparingByKey

static <K extends

Comparable

<? super K>,​V>

Comparator

<

Map.Entry

<K,​V>> comparingByKey()

Returns a comparator that compares

Map.Entry

in natural order on key.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with a null key.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with a null key.

comparingByValue

```java
static <K,​V extends
Comparable
<? super V>>
Comparator
<
Map.Entry
<K,​V>> comparingByValue()
```

Returns a comparator that compares

Map.Entry

in natural order on value.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with null values.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the

Comparable

type of the map values
**Returns:** a comparator that compares

Map.Entry

in natural order on value.
**Since:** 1.8
**See Also:** Comparable

---

#### comparingByValue

static <K,​V extends

Comparable

<? super V>>

Comparator

<

Map.Entry

<K,​V>> comparingByValue()

Returns a comparator that compares

Map.Entry

in natural order on value.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with null values.

The returned comparator is serializable and throws

NullPointerException

when comparing an entry with null values.

comparingByKey

```java
static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByKey​(
Comparator
<? super K> cmp)
```

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the type of the map values
**Parameters:** cmp

- the key

Comparator
**Returns:** a comparator that compares

Map.Entry

by the key.
**Since:** 1.8

---

#### comparingByKey

static <K,​V>

Comparator

<

Map.Entry

<K,​V>> comparingByKey​(

Comparator

<? super K> cmp)

Returns a comparator that compares

Map.Entry

by key using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

The returned comparator is serializable if the specified comparator
is also serializable.

comparingByValue

```java
static <K,​V>
Comparator
<
Map.Entry
<K,​V>> comparingByValue​(
Comparator
<? super V> cmp)
```

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

**Type Parameters:** K

- the type of the map keys
**Type Parameters:** V

- the type of the map values
**Parameters:** cmp

- the value

Comparator
**Returns:** a comparator that compares

Map.Entry

by the value.
**Since:** 1.8

---

#### comparingByValue

static <K,​V>

Comparator

<

Map.Entry

<K,​V>> comparingByValue​(

Comparator

<? super V> cmp)

Returns a comparator that compares

Map.Entry

by value using the given

Comparator

.

The returned comparator is serializable if the specified comparator
is also serializable.

The returned comparator is serializable if the specified comparator
is also serializable.

---

