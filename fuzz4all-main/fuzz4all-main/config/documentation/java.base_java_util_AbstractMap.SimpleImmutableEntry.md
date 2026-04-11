# Class AbstractMap.SimpleImmutableEntry<K,​V>

**Source:** `java.base\java\util\AbstractMap.SimpleImmutableEntry.html`

### Class Description

```java
public static class
AbstractMap.SimpleImmutableEntry<K,​V>

extends
Object

implements
Map.Entry
<K,​V>,
Serializable
```

An Entry maintaining an immutable key and value. This class
does not support method

setValue

. This class may be
convenient in methods that return thread-safe snapshots of
key-value mappings.

**All Implemented Interfaces:** Serializable

,

Map.Entry

<K,​V>

---

### Field Details

*No entries found.*

### Constructor Details

#### public SimpleImmutableEntry​(
K
key,

V
value)

Creates an entry representing a mapping from the specified
key to the specified value.

**Parameters:**
- key

- the key represented by this entry
- value

- the value represented by this entry

---

#### public SimpleImmutableEntry​(
Map.Entry
<? extends
K
,​? extends
V
> entry)

Creates an entry representing the same mapping as the
specified entry.

**Parameters:**
- entry

- the entry to copy

---

### Method Details

#### public
K
getKey()

Returns the key corresponding to this entry.

**Specified by:**
- getKey

in interface

Map.Entry

<

K

,​

V

>

**Returns:**
- the key corresponding to this entry

---

#### public
V
getValue()

Returns the value corresponding to this entry.

**Specified by:**
- getValue

in interface

Map.Entry

<

K

,​

V

>

**Returns:**
- the value corresponding to this entry

---

#### public
V
setValue​(
V
value)

Replaces the value corresponding to this entry with the specified
value (optional operation). This implementation simply throws

UnsupportedOperationException

, as this class implements
an

immutable

map entry.

**Specified by:**
- setValue

in interface

Map.Entry

<

K

,​

V

>

**Parameters:**
- value

- new value to be stored in this entry

**Returns:**
- (Does not return)

**Throws:**
- UnsupportedOperationException

- always

---

#### public boolean equals​(
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
e2.getKey()==null :
e1.getKey().equals(e2.getKey()))
&&
(e1.getValue()==null ?
e2.getValue()==null :
e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Specified by:**
- equals

in interface

Map.Entry

<

K

,​

V

>

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
- hashCode()

---

#### public int hashCode()

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

Object.hashCode()

.

**Specified by:**
- hashCode

in interface

Map.Entry

<

K

,​

V

>

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this map entry

**See Also:**
- equals(java.lang.Object)

---

#### public
String
toString()

Returns a String representation of this map entry. This
implementation returns the string representation of this
entry's key followed by the equals character ("

=

")
followed by the string representation of this entry's value.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this map entry

---

### Additional Sections

#### Class AbstractMap.SimpleImmutableEntry<K,​V>

java.lang.Object

- java.util.AbstractMap.SimpleImmutableEntry<K,​V>

java.util.AbstractMap.SimpleImmutableEntry<K,​V>

**All Implemented Interfaces:** Serializable

,

Map.Entry

<K,​V>

**Enclosing class:** AbstractMap

<

K

,​

V

>

```java
public static class
AbstractMap.SimpleImmutableEntry<K,​V>

extends
Object

implements
Map.Entry
<K,​V>,
Serializable
```

An Entry maintaining an immutable key and value. This class
does not support method

setValue

. This class may be
convenient in methods that return thread-safe snapshots of
key-value mappings.

**Since:** 1.6
**See Also:** Serialized Form

public static class

AbstractMap.SimpleImmutableEntry<K,​V>

extends

Object

implements

Map.Entry

<K,​V>,

Serializable

An Entry maintaining an immutable key and value. This class
does not support method

setValue

. This class may be
convenient in methods that return thread-safe snapshots of
key-value mappings.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleImmutableEntry

​(

Map.Entry

<? extends

K

,​? extends

V

> entry)

Creates an entry representing the same mapping as the
specified entry.

SimpleImmutableEntry

​(

K

key,

V

value)

Creates an entry representing a mapping from the specified
key to the specified value.

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

String

toString

()

Returns a String representation of this map entry.

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

Constructor Summary

Constructors

Constructor

Description

SimpleImmutableEntry

​(

Map.Entry

<? extends

K

,​? extends

V

> entry)

Creates an entry representing the same mapping as the
specified entry.

SimpleImmutableEntry

​(

K

key,

V

value)

Creates an entry representing a mapping from the specified
key to the specified value.

---

#### Constructor Summary

Creates an entry representing the same mapping as the
specified entry.

Creates an entry representing a mapping from the specified
key to the specified value.

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

String

toString

()

Returns a String representation of this map entry.

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

---

#### Method Summary

Compares the specified object with this entry for equality.

Returns the key corresponding to this entry.

Returns the value corresponding to this entry.

Returns the hash code value for this map entry.

Replaces the value corresponding to this entry with the specified
value (optional operation).

Returns a String representation of this map entry.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleImmutableEntry

```java
public SimpleImmutableEntry​(
K
key,

V
value)
```

Creates an entry representing a mapping from the specified
key to the specified value.

**Parameters:** key

- the key represented by this entry
**Parameters:** value

- the value represented by this entry

- SimpleImmutableEntry

```java
public SimpleImmutableEntry​(
Map.Entry
<? extends
K
,​? extends
V
> entry)
```

Creates an entry representing the same mapping as the
specified entry.

**Parameters:** entry

- the entry to copy

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
public
K
getKey()
```

Returns the key corresponding to this entry.

**Specified by:** getKey

in interface

Map.Entry

<

K

,​

V

>
**Returns:** the key corresponding to this entry

- getValue

```java
public
V
getValue()
```

Returns the value corresponding to this entry.

**Specified by:** getValue

in interface

Map.Entry

<

K

,​

V

>
**Returns:** the value corresponding to this entry

- setValue

```java
public
V
setValue​(
V
value)
```

Replaces the value corresponding to this entry with the specified
value (optional operation). This implementation simply throws

UnsupportedOperationException

, as this class implements
an

immutable

map entry.

**Specified by:** setValue

in interface

Map.Entry

<

K

,​

V

>
**Parameters:** value

- new value to be stored in this entry
**Returns:** (Does not return)
**Throws:** UnsupportedOperationException

- always

- equals

```java
public boolean equals​(
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
e2.getKey()==null :
e1.getKey().equals(e2.getKey()))
&&
(e1.getValue()==null ?
e2.getValue()==null :
e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Specified by:** equals

in interface

Map.Entry

<

K

,​

V

>
**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this map entry
**Returns:** true

if the specified object is equal to this map
entry
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
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

Object.hashCode()

.

**Specified by:** hashCode

in interface

Map.Entry

<

K

,​

V

>
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this map entry
**See Also:** equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a String representation of this map entry. This
implementation returns the string representation of this
entry's key followed by the equals character ("

=

")
followed by the string representation of this entry's value.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this map entry

Constructor Detail

- SimpleImmutableEntry

```java
public SimpleImmutableEntry​(
K
key,

V
value)
```

Creates an entry representing a mapping from the specified
key to the specified value.

**Parameters:** key

- the key represented by this entry
**Parameters:** value

- the value represented by this entry

- SimpleImmutableEntry

```java
public SimpleImmutableEntry​(
Map.Entry
<? extends
K
,​? extends
V
> entry)
```

Creates an entry representing the same mapping as the
specified entry.

**Parameters:** entry

- the entry to copy

---

#### Constructor Detail

SimpleImmutableEntry

```java
public SimpleImmutableEntry​(
K
key,

V
value)
```

Creates an entry representing a mapping from the specified
key to the specified value.

**Parameters:** key

- the key represented by this entry
**Parameters:** value

- the value represented by this entry

---

#### SimpleImmutableEntry

public SimpleImmutableEntry​(

K

key,

V

value)

Creates an entry representing a mapping from the specified
key to the specified value.

SimpleImmutableEntry

```java
public SimpleImmutableEntry​(
Map.Entry
<? extends
K
,​? extends
V
> entry)
```

Creates an entry representing the same mapping as the
specified entry.

**Parameters:** entry

- the entry to copy

---

#### SimpleImmutableEntry

public SimpleImmutableEntry​(

Map.Entry

<? extends

K

,​? extends

V

> entry)

Creates an entry representing the same mapping as the
specified entry.

Method Detail

- getKey

```java
public
K
getKey()
```

Returns the key corresponding to this entry.

**Specified by:** getKey

in interface

Map.Entry

<

K

,​

V

>
**Returns:** the key corresponding to this entry

- getValue

```java
public
V
getValue()
```

Returns the value corresponding to this entry.

**Specified by:** getValue

in interface

Map.Entry

<

K

,​

V

>
**Returns:** the value corresponding to this entry

- setValue

```java
public
V
setValue​(
V
value)
```

Replaces the value corresponding to this entry with the specified
value (optional operation). This implementation simply throws

UnsupportedOperationException

, as this class implements
an

immutable

map entry.

**Specified by:** setValue

in interface

Map.Entry

<

K

,​

V

>
**Parameters:** value

- new value to be stored in this entry
**Returns:** (Does not return)
**Throws:** UnsupportedOperationException

- always

- equals

```java
public boolean equals​(
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
e2.getKey()==null :
e1.getKey().equals(e2.getKey()))
&&
(e1.getValue()==null ?
e2.getValue()==null :
e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Specified by:** equals

in interface

Map.Entry

<

K

,​

V

>
**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this map entry
**Returns:** true

if the specified object is equal to this map
entry
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
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

Object.hashCode()

.

**Specified by:** hashCode

in interface

Map.Entry

<

K

,​

V

>
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this map entry
**See Also:** equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a String representation of this map entry. This
implementation returns the string representation of this
entry's key followed by the equals character ("

=

")
followed by the string representation of this entry's value.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this map entry

---

#### Method Detail

getKey

```java
public
K
getKey()
```

Returns the key corresponding to this entry.

**Specified by:** getKey

in interface

Map.Entry

<

K

,​

V

>
**Returns:** the key corresponding to this entry

---

#### getKey

public

K

getKey()

Returns the key corresponding to this entry.

getValue

```java
public
V
getValue()
```

Returns the value corresponding to this entry.

**Specified by:** getValue

in interface

Map.Entry

<

K

,​

V

>
**Returns:** the value corresponding to this entry

---

#### getValue

public

V

getValue()

Returns the value corresponding to this entry.

setValue

```java
public
V
setValue​(
V
value)
```

Replaces the value corresponding to this entry with the specified
value (optional operation). This implementation simply throws

UnsupportedOperationException

, as this class implements
an

immutable

map entry.

**Specified by:** setValue

in interface

Map.Entry

<

K

,​

V

>
**Parameters:** value

- new value to be stored in this entry
**Returns:** (Does not return)
**Throws:** UnsupportedOperationException

- always

---

#### setValue

public

V

setValue​(

V

value)

Replaces the value corresponding to this entry with the specified
value (optional operation). This implementation simply throws

UnsupportedOperationException

, as this class implements
an

immutable

map entry.

equals

```java
public boolean equals​(
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
e2.getKey()==null :
e1.getKey().equals(e2.getKey()))
&&
(e1.getValue()==null ?
e2.getValue()==null :
e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

**Specified by:** equals

in interface

Map.Entry

<

K

,​

V

>
**Overrides:** equals

in class

Object
**Parameters:** o

- object to be compared for equality with this map entry
**Returns:** true

if the specified object is equal to this map
entry
**See Also:** hashCode()

---

#### equals

public boolean equals​(

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
e2.getKey()==null :
e1.getKey().equals(e2.getKey()))
&&
(e1.getValue()==null ?
e2.getValue()==null :
e1.getValue().equals(e2.getValue()))
```

This ensures that the

equals

method works properly across
different implementations of the

Map.Entry

interface.

(e1.getKey()==null ?
e2.getKey()==null :
e1.getKey().equals(e2.getKey()))
&&
(e1.getValue()==null ?
e2.getValue()==null :
e1.getValue().equals(e2.getValue()))

hashCode

```java
public int hashCode()
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

Object.hashCode()

.

**Specified by:** hashCode

in interface

Map.Entry

<

K

,​

V

>
**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this map entry
**See Also:** equals(java.lang.Object)

---

#### hashCode

public int hashCode()

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

Object.hashCode()

.

(e.getKey()==null ? 0 : e.getKey().hashCode()) ^
(e.getValue()==null ? 0 : e.getValue().hashCode())

toString

```java
public
String
toString()
```

Returns a String representation of this map entry. This
implementation returns the string representation of this
entry's key followed by the equals character ("

=

")
followed by the string representation of this entry's value.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this map entry

---

#### toString

public

String

toString()

Returns a String representation of this map entry. This
implementation returns the string representation of this
entry's key followed by the equals character ("

=

")
followed by the string representation of this entry's value.

---

