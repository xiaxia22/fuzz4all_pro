# Class Dictionary<K,​V>

**Source:** `java.base\java\util\Dictionary.html`

### Class Description

```java
public abstract class
Dictionary<K,​V>

extends
Object
```

The

Dictionary

class is the abstract parent of any
class, such as

Hashtable

, which maps keys to values.
Every key and every value is an object. In any one

Dictionary

object, every key is associated with at most one value. Given a

Dictionary

and a key, the associated element can be looked up.
Any non-

null

object can be used as a key and as a value.

As a rule, the

equals

method should be used by
implementations of this class to decide if two keys are the same.

NOTE: This class is obsolete. New implementations should
implement the Map interface, rather than extending this class.

**Direct Known Subclasses:** Hashtable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Dictionary()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract int size()

Returns the number of entries (distinct keys) in this dictionary.

**Returns:**
- the number of keys in this dictionary.

---

#### public abstract boolean isEmpty()

Tests if this dictionary maps no keys to value. The general contract
for the

isEmpty

method is that the result is true if and only
if this dictionary contains no entries.

**Returns:**
- true

if this dictionary maps no keys to values;

false

otherwise.

---

#### public abstract
Enumeration
<
K
> keys()

Returns an enumeration of the keys in this dictionary. The general
contract for the keys method is that an

Enumeration

object
is returned that will generate all the keys for which this dictionary
contains entries.

**Returns:**
- an enumeration of the keys in this dictionary.

**See Also:**
- elements()

,

Enumeration

---

#### public abstract
Enumeration
<
V
> elements()

Returns an enumeration of the values in this dictionary. The general
contract for the

elements

method is that an

Enumeration

is returned that will generate all the elements
contained in entries in this dictionary.

**Returns:**
- an enumeration of the values in this dictionary.

**See Also:**
- keys()

,

Enumeration

---

#### public abstract
V
get​(
Object
key)

Returns the value to which the key is mapped in this dictionary.
The general contract for the

isEmpty

method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise,

null

is returned.

**Parameters:**
- key

- a key in this dictionary.

null

if the key is not mapped to any value in
this dictionary.

**Returns:**
- the value to which the key is mapped in this dictionary;

**Throws:**
- NullPointerException

- if the

key

is

null

.

**See Also:**
- put(java.lang.Object, java.lang.Object)

---

#### public abstract
V
put​(
K
key,

V
value)

Maps the specified

key

to the specified

value

in this dictionary. Neither the key nor the
value can be

null

.

If this dictionary already contains an entry for the specified

key

, the value already in this dictionary for that

key

is returned, after modifying the entry to contain the
new element.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

**Parameters:**
- key

- the hashtable key.
- value

- the value.

**Returns:**
- the previous value to which the

key

was mapped
in this dictionary, or

null

if the key did not
have a previous mapping.

**Throws:**
- NullPointerException

- if the

key

or

value

is

null

.

**See Also:**
- Object.equals(java.lang.Object)

,

get(java.lang.Object)

---

#### public abstract
V
remove​(
Object
key)

Removes the

key

(and its corresponding

value

) from this dictionary. This method does nothing
if the

key

is not in this dictionary.

**Parameters:**
- key

- the key that needs to be removed.

**Returns:**
- the value to which the

key

had been mapped in this
dictionary, or

null

if the key did not have a
mapping.

**Throws:**
- NullPointerException

- if

key

is

null

.

---

### Additional Sections

#### Class Dictionary<K,​V>

java.lang.Object

- java.util.Dictionary<K,​V>

java.util.Dictionary<K,​V>

**Direct Known Subclasses:** Hashtable

```java
public abstract class
Dictionary<K,​V>

extends
Object
```

The

Dictionary

class is the abstract parent of any
class, such as

Hashtable

, which maps keys to values.
Every key and every value is an object. In any one

Dictionary

object, every key is associated with at most one value. Given a

Dictionary

and a key, the associated element can be looked up.
Any non-

null

object can be used as a key and as a value.

As a rule, the

equals

method should be used by
implementations of this class to decide if two keys are the same.

NOTE: This class is obsolete. New implementations should
implement the Map interface, rather than extending this class.

**Since:** 1.0
**See Also:** Map

,

Object.equals(java.lang.Object)

,

Object.hashCode()

,

Hashtable

public abstract class

Dictionary<K,​V>

extends

Object

The

Dictionary

class is the abstract parent of any
class, such as

Hashtable

, which maps keys to values.
Every key and every value is an object. In any one

Dictionary

object, every key is associated with at most one value. Given a

Dictionary

and a key, the associated element can be looked up.
Any non-

null

object can be used as a key and as a value.

As a rule, the

equals

method should be used by
implementations of this class to decide if two keys are the same.

NOTE: This class is obsolete. New implementations should
implement the Map interface, rather than extending this class.

As a rule, the

equals

method should be used by
implementations of this class to decide if two keys are the same.

NOTE: This class is obsolete. New implementations should
implement the Map interface, rather than extending this class.

NOTE: This class is obsolete. New implementations should
implement the Map interface, rather than extending this class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Dictionary

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Enumeration

<

V

>

elements

()

Returns an enumeration of the values in this dictionary.

abstract

V

get

​(

Object

key)

Returns the value to which the key is mapped in this dictionary.

abstract boolean

isEmpty

()

Tests if this dictionary maps no keys to value.

abstract

Enumeration

<

K

>

keys

()

Returns an enumeration of the keys in this dictionary.

abstract

V

put

​(

K

key,

V

value)

Maps the specified

key

to the specified

value

in this dictionary.

abstract

V

remove

​(

Object

key)

Removes the

key

(and its corresponding

value

) from this dictionary.

abstract int

size

()

Returns the number of entries (distinct keys) in this dictionary.

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

toString

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

Dictionary

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Enumeration

<

V

>

elements

()

Returns an enumeration of the values in this dictionary.

abstract

V

get

​(

Object

key)

Returns the value to which the key is mapped in this dictionary.

abstract boolean

isEmpty

()

Tests if this dictionary maps no keys to value.

abstract

Enumeration

<

K

>

keys

()

Returns an enumeration of the keys in this dictionary.

abstract

V

put

​(

K

key,

V

value)

Maps the specified

key

to the specified

value

in this dictionary.

abstract

V

remove

​(

Object

key)

Removes the

key

(and its corresponding

value

) from this dictionary.

abstract int

size

()

Returns the number of entries (distinct keys) in this dictionary.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns an enumeration of the values in this dictionary.

Returns the value to which the key is mapped in this dictionary.

Tests if this dictionary maps no keys to value.

Returns an enumeration of the keys in this dictionary.

Maps the specified

key

to the specified

value

in this dictionary.

Removes the

key

(and its corresponding

value

) from this dictionary.

Returns the number of entries (distinct keys) in this dictionary.

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

toString

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

- Dictionary

```java
public Dictionary()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- size

```java
public abstract int size()
```

Returns the number of entries (distinct keys) in this dictionary.

**Returns:** the number of keys in this dictionary.

- isEmpty

```java
public abstract boolean isEmpty()
```

Tests if this dictionary maps no keys to value. The general contract
for the

isEmpty

method is that the result is true if and only
if this dictionary contains no entries.

**Returns:** true

if this dictionary maps no keys to values;

false

otherwise.

- keys

```java
public abstract
Enumeration
<
K
> keys()
```

Returns an enumeration of the keys in this dictionary. The general
contract for the keys method is that an

Enumeration

object
is returned that will generate all the keys for which this dictionary
contains entries.

**Returns:** an enumeration of the keys in this dictionary.
**See Also:** elements()

,

Enumeration

- elements

```java
public abstract
Enumeration
<
V
> elements()
```

Returns an enumeration of the values in this dictionary. The general
contract for the

elements

method is that an

Enumeration

is returned that will generate all the elements
contained in entries in this dictionary.

**Returns:** an enumeration of the values in this dictionary.
**See Also:** keys()

,

Enumeration

- get

```java
public abstract
V
get​(
Object
key)
```

Returns the value to which the key is mapped in this dictionary.
The general contract for the

isEmpty

method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise,

null

is returned.

**Parameters:** key

- a key in this dictionary.

null

if the key is not mapped to any value in
this dictionary.
**Returns:** the value to which the key is mapped in this dictionary;
**Throws:** NullPointerException

- if the

key

is

null

.
**See Also:** put(java.lang.Object, java.lang.Object)

- put

```java
public abstract
V
put​(
K
key,

V
value)
```

Maps the specified

key

to the specified

value

in this dictionary. Neither the key nor the
value can be

null

.

If this dictionary already contains an entry for the specified

key

, the value already in this dictionary for that

key

is returned, after modifying the entry to contain the
new element.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

**Parameters:** key

- the hashtable key.
**Parameters:** value

- the value.
**Returns:** the previous value to which the

key

was mapped
in this dictionary, or

null

if the key did not
have a previous mapping.
**Throws:** NullPointerException

- if the

key

or

value

is

null

.
**See Also:** Object.equals(java.lang.Object)

,

get(java.lang.Object)

- remove

```java
public abstract
V
remove​(
Object
key)
```

Removes the

key

(and its corresponding

value

) from this dictionary. This method does nothing
if the

key

is not in this dictionary.

**Parameters:** key

- the key that needs to be removed.
**Returns:** the value to which the

key

had been mapped in this
dictionary, or

null

if the key did not have a
mapping.
**Throws:** NullPointerException

- if

key

is

null

.

Constructor Detail

- Dictionary

```java
public Dictionary()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

Dictionary

```java
public Dictionary()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Dictionary

public Dictionary()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- size

```java
public abstract int size()
```

Returns the number of entries (distinct keys) in this dictionary.

**Returns:** the number of keys in this dictionary.

- isEmpty

```java
public abstract boolean isEmpty()
```

Tests if this dictionary maps no keys to value. The general contract
for the

isEmpty

method is that the result is true if and only
if this dictionary contains no entries.

**Returns:** true

if this dictionary maps no keys to values;

false

otherwise.

- keys

```java
public abstract
Enumeration
<
K
> keys()
```

Returns an enumeration of the keys in this dictionary. The general
contract for the keys method is that an

Enumeration

object
is returned that will generate all the keys for which this dictionary
contains entries.

**Returns:** an enumeration of the keys in this dictionary.
**See Also:** elements()

,

Enumeration

- elements

```java
public abstract
Enumeration
<
V
> elements()
```

Returns an enumeration of the values in this dictionary. The general
contract for the

elements

method is that an

Enumeration

is returned that will generate all the elements
contained in entries in this dictionary.

**Returns:** an enumeration of the values in this dictionary.
**See Also:** keys()

,

Enumeration

- get

```java
public abstract
V
get​(
Object
key)
```

Returns the value to which the key is mapped in this dictionary.
The general contract for the

isEmpty

method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise,

null

is returned.

**Parameters:** key

- a key in this dictionary.

null

if the key is not mapped to any value in
this dictionary.
**Returns:** the value to which the key is mapped in this dictionary;
**Throws:** NullPointerException

- if the

key

is

null

.
**See Also:** put(java.lang.Object, java.lang.Object)

- put

```java
public abstract
V
put​(
K
key,

V
value)
```

Maps the specified

key

to the specified

value

in this dictionary. Neither the key nor the
value can be

null

.

If this dictionary already contains an entry for the specified

key

, the value already in this dictionary for that

key

is returned, after modifying the entry to contain the
new element.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

**Parameters:** key

- the hashtable key.
**Parameters:** value

- the value.
**Returns:** the previous value to which the

key

was mapped
in this dictionary, or

null

if the key did not
have a previous mapping.
**Throws:** NullPointerException

- if the

key

or

value

is

null

.
**See Also:** Object.equals(java.lang.Object)

,

get(java.lang.Object)

- remove

```java
public abstract
V
remove​(
Object
key)
```

Removes the

key

(and its corresponding

value

) from this dictionary. This method does nothing
if the

key

is not in this dictionary.

**Parameters:** key

- the key that needs to be removed.
**Returns:** the value to which the

key

had been mapped in this
dictionary, or

null

if the key did not have a
mapping.
**Throws:** NullPointerException

- if

key

is

null

.

---

#### Method Detail

size

```java
public abstract int size()
```

Returns the number of entries (distinct keys) in this dictionary.

**Returns:** the number of keys in this dictionary.

---

#### size

public abstract int size()

Returns the number of entries (distinct keys) in this dictionary.

isEmpty

```java
public abstract boolean isEmpty()
```

Tests if this dictionary maps no keys to value. The general contract
for the

isEmpty

method is that the result is true if and only
if this dictionary contains no entries.

**Returns:** true

if this dictionary maps no keys to values;

false

otherwise.

---

#### isEmpty

public abstract boolean isEmpty()

Tests if this dictionary maps no keys to value. The general contract
for the

isEmpty

method is that the result is true if and only
if this dictionary contains no entries.

keys

```java
public abstract
Enumeration
<
K
> keys()
```

Returns an enumeration of the keys in this dictionary. The general
contract for the keys method is that an

Enumeration

object
is returned that will generate all the keys for which this dictionary
contains entries.

**Returns:** an enumeration of the keys in this dictionary.
**See Also:** elements()

,

Enumeration

---

#### keys

public abstract

Enumeration

<

K

> keys()

Returns an enumeration of the keys in this dictionary. The general
contract for the keys method is that an

Enumeration

object
is returned that will generate all the keys for which this dictionary
contains entries.

elements

```java
public abstract
Enumeration
<
V
> elements()
```

Returns an enumeration of the values in this dictionary. The general
contract for the

elements

method is that an

Enumeration

is returned that will generate all the elements
contained in entries in this dictionary.

**Returns:** an enumeration of the values in this dictionary.
**See Also:** keys()

,

Enumeration

---

#### elements

public abstract

Enumeration

<

V

> elements()

Returns an enumeration of the values in this dictionary. The general
contract for the

elements

method is that an

Enumeration

is returned that will generate all the elements
contained in entries in this dictionary.

get

```java
public abstract
V
get​(
Object
key)
```

Returns the value to which the key is mapped in this dictionary.
The general contract for the

isEmpty

method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise,

null

is returned.

**Parameters:** key

- a key in this dictionary.

null

if the key is not mapped to any value in
this dictionary.
**Returns:** the value to which the key is mapped in this dictionary;
**Throws:** NullPointerException

- if the

key

is

null

.
**See Also:** put(java.lang.Object, java.lang.Object)

---

#### get

public abstract

V

get​(

Object

key)

Returns the value to which the key is mapped in this dictionary.
The general contract for the

isEmpty

method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise,

null

is returned.

put

```java
public abstract
V
put​(
K
key,

V
value)
```

Maps the specified

key

to the specified

value

in this dictionary. Neither the key nor the
value can be

null

.

If this dictionary already contains an entry for the specified

key

, the value already in this dictionary for that

key

is returned, after modifying the entry to contain the
new element.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

**Parameters:** key

- the hashtable key.
**Parameters:** value

- the value.
**Returns:** the previous value to which the

key

was mapped
in this dictionary, or

null

if the key did not
have a previous mapping.
**Throws:** NullPointerException

- if the

key

or

value

is

null

.
**See Also:** Object.equals(java.lang.Object)

,

get(java.lang.Object)

---

#### put

public abstract

V

put​(

K

key,

V

value)

Maps the specified

key

to the specified

value

in this dictionary. Neither the key nor the
value can be

null

.

If this dictionary already contains an entry for the specified

key

, the value already in this dictionary for that

key

is returned, after modifying the entry to contain the
new element.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

If this dictionary already contains an entry for the specified

key

, the value already in this dictionary for that

key

is returned, after modifying the entry to contain the
new element.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

If this dictionary does not already have an entry
for the specified

key

, an entry is created for the
specified

key

and

value

, and

null

is
returned.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

The

value

can be retrieved by calling the

get

method with a

key

that is equal to
the original

key

.

remove

```java
public abstract
V
remove​(
Object
key)
```

Removes the

key

(and its corresponding

value

) from this dictionary. This method does nothing
if the

key

is not in this dictionary.

**Parameters:** key

- the key that needs to be removed.
**Returns:** the value to which the

key

had been mapped in this
dictionary, or

null

if the key did not have a
mapping.
**Throws:** NullPointerException

- if

key

is

null

.

---

#### remove

public abstract

V

remove​(

Object

key)

Removes the

key

(and its corresponding

value

) from this dictionary. This method does nothing
if the

key

is not in this dictionary.

---

