# Class SimpleBindings

**Source:** `java.scripting\javax\script\SimpleBindings.html`

### Class Description

```java
public class
SimpleBindings

extends
Object

implements
Bindings
```

A simple implementation of Bindings backed by
a

HashMap

or some other specified

Map

.

**All Implemented Interfaces:** Map

<

String

,​

Object

>

,

Bindings

---

### Field Details

*No entries found.*

### Constructor Details

#### public SimpleBindings​(
Map
<
String
,​
Object
> m)

Constructor uses an existing

Map

to store the values.

**Parameters:**
- m

- The

Map

backing this

SimpleBindings

.

**Throws:**
- NullPointerException

- if m is null

---

#### public SimpleBindings()

Default constructor uses a

HashMap

.

---

### Method Details

#### public
Object
put​(
String
name,

Object
value)

Sets the specified key/value in the underlying

map

field.

**Specified by:**
- put

in interface

Bindings
- put

in interface

Map

<

String

,​

Object

>

**Parameters:**
- name

- Name of value
- value

- Value to set.

**Returns:**
- Previous value for the specified key. Returns null if key was previously
unset.

**Throws:**
- NullPointerException

- if the name is null.
- IllegalArgumentException

- if the name is empty.

---

#### public void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)

putAll

is implemented using

Map.putAll

.

**Specified by:**
- putAll

in interface

Bindings
- putAll

in interface

Map

<

String

,​

Object

>

**Parameters:**
- toMerge

- The

Map

of values to add.

**Throws:**
- NullPointerException

- if toMerge map is null or if some key in the map is null.
- IllegalArgumentException

- if some key in the map is an empty String.

---

#### public boolean containsKey​(
Object
key)

Returns

true

if this map contains a mapping for the specified
key. More formally, returns

true

if and only if
this map contains a mapping for a key

k

such that

(key==null ? k==null : key.equals(k))

. (There can be
at most one such mapping.)

**Specified by:**
- containsKey

in interface

Bindings
- containsKey

in interface

Map

<

String

,​

Object

>

**Parameters:**
- key

- key whose presence in this map is to be tested.

**Returns:**
- true

if this map contains a mapping for the specified
key.

**Throws:**
- NullPointerException

- if key is null
- ClassCastException

- if key is not String
- IllegalArgumentException

- if key is empty String

---

#### public
Object
get​(
Object
key)

Returns the value to which this map maps the specified key. Returns

null

if the map contains no mapping for this key. A return
value of

null

does not

necessarily

indicate that the
map contains no mapping for the key; it's also possible that the map
explicitly maps the key to

null

. The

containsKey

operation may be used to distinguish these two cases.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

(key==null ? k==null : key.equals(k))

,
then this method returns

v

; otherwise
it returns

null

. (There can be at most one such mapping.)

**Specified by:**
- get

in interface

Bindings
- get

in interface

Map

<

String

,​

Object

>

**Parameters:**
- key

- key whose associated value is to be returned.

**Returns:**
- the value to which this map maps the specified key, or

null

if the map contains no mapping for this key.

**Throws:**
- NullPointerException

- if key is null
- ClassCastException

- if key is not String
- IllegalArgumentException

- if key is empty String

---

#### public
Object
remove​(
Object
key)

Removes the mapping for this key from this map if it is present
(optional operation). More formally, if this map contains a mapping
from key

k

to value

v

such that

(key==null ? k==null : key.equals(k))

, that mapping
is removed. (The map can contain at most one such mapping.)

Returns the value to which the map previously associated the key, or

null

if the map contained no mapping for this key. (A

null

return can also indicate that the map previously
associated

null

with the specified key if the implementation
supports

null

values.) The map will not contain a mapping for
the specified key once the call returns.

**Specified by:**
- remove

in interface

Bindings
- remove

in interface

Map

<

String

,​

Object

>

**Parameters:**
- key

- key whose mapping is to be removed from the map.

**Returns:**
- previous value associated with specified key, or

null

if there was no mapping for key.

**Throws:**
- NullPointerException

- if key is null
- ClassCastException

- if key is not String
- IllegalArgumentException

- if key is empty String

---

### Additional Sections

#### Class SimpleBindings

java.lang.Object

- javax.script.SimpleBindings

javax.script.SimpleBindings

**All Implemented Interfaces:** Map

<

String

,​

Object

>

,

Bindings

```java
public class
SimpleBindings

extends
Object

implements
Bindings
```

A simple implementation of Bindings backed by
a

HashMap

or some other specified

Map

.

**Since:** 1.6

public class

SimpleBindings

extends

Object

implements

Bindings

A simple implementation of Bindings backed by
a

HashMap

or some other specified

Map

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleBindings

()

Default constructor uses a

HashMap

.

SimpleBindings

​(

Map

<

String

,​

Object

> m)

Constructor uses an existing

Map

to store the values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

containsKey

​(

Object

key)

Returns

true

if this map contains a mapping for the specified
key.

Object

get

​(

Object

key)

Returns the value to which this map maps the specified key.

Object

put

​(

String

name,

Object

value)

Sets the specified key/value in the underlying

map

field.

void

putAll

​(

Map

<? extends

String

,​? extends

Object

> toMerge)

putAll

is implemented using

Map.putAll

.

Object

remove

​(

Object

key)

Removes the mapping for this key from this map if it is present
(optional operation).

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

containsValue

,

entrySet

,

equals

,

forEach

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

putIfAbsent

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

Constructor Summary

Constructors

Constructor

Description

SimpleBindings

()

Default constructor uses a

HashMap

.

SimpleBindings

​(

Map

<

String

,​

Object

> m)

Constructor uses an existing

Map

to store the values.

---

#### Constructor Summary

Default constructor uses a

HashMap

.

Constructor uses an existing

Map

to store the values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

containsKey

​(

Object

key)

Returns

true

if this map contains a mapping for the specified
key.

Object

get

​(

Object

key)

Returns the value to which this map maps the specified key.

Object

put

​(

String

name,

Object

value)

Sets the specified key/value in the underlying

map

field.

void

putAll

​(

Map

<? extends

String

,​? extends

Object

> toMerge)

putAll

is implemented using

Map.putAll

.

Object

remove

​(

Object

key)

Removes the mapping for this key from this map if it is present
(optional operation).

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

containsValue

,

entrySet

,

equals

,

forEach

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

putIfAbsent

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

,

values

---

#### Method Summary

Returns

true

if this map contains a mapping for the specified
key.

Returns the value to which this map maps the specified key.

Sets the specified key/value in the underlying

map

field.

putAll

is implemented using

Map.putAll

.

Removes the mapping for this key from this map if it is present
(optional operation).

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

containsValue

,

entrySet

,

equals

,

forEach

,

getOrDefault

,

hashCode

,

isEmpty

,

keySet

,

merge

,

putIfAbsent

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

,

values

---

#### Methods declared in interface java.util. Map

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleBindings

```java
public SimpleBindings​(
Map
<
String
,​
Object
> m)
```

Constructor uses an existing

Map

to store the values.

**Parameters:** m

- The

Map

backing this

SimpleBindings

.
**Throws:** NullPointerException

- if m is null

- SimpleBindings

```java
public SimpleBindings()
```

Default constructor uses a

HashMap

.

============ METHOD DETAIL ==========

- Method Detail

- put

```java
public
Object
put​(
String
name,

Object
value)
```

Sets the specified key/value in the underlying

map

field.

**Specified by:** put

in interface

Bindings
**Specified by:** put

in interface

Map

<

String

,​

Object

>
**Parameters:** name

- Name of value
**Parameters:** value

- Value to set.
**Returns:** Previous value for the specified key. Returns null if key was previously
unset.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

- putAll

```java
public void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)
```

putAll

is implemented using

Map.putAll

.

**Specified by:** putAll

in interface

Bindings
**Specified by:** putAll

in interface

Map

<

String

,​

Object

>
**Parameters:** toMerge

- The

Map

of values to add.
**Throws:** NullPointerException

- if toMerge map is null or if some key in the map is null.
**Throws:** IllegalArgumentException

- if some key in the map is an empty String.

- containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if this map contains a mapping for the specified
key. More formally, returns

true

if and only if
this map contains a mapping for a key

k

such that

(key==null ? k==null : key.equals(k))

. (There can be
at most one such mapping.)

**Specified by:** containsKey

in interface

Bindings
**Specified by:** containsKey

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose presence in this map is to be tested.
**Returns:** true

if this map contains a mapping for the specified
key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

- get

```java
public
Object
get​(
Object
key)
```

Returns the value to which this map maps the specified key. Returns

null

if the map contains no mapping for this key. A return
value of

null

does not

necessarily

indicate that the
map contains no mapping for the key; it's also possible that the map
explicitly maps the key to

null

. The

containsKey

operation may be used to distinguish these two cases.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

(key==null ? k==null : key.equals(k))

,
then this method returns

v

; otherwise
it returns

null

. (There can be at most one such mapping.)

**Specified by:** get

in interface

Bindings
**Specified by:** get

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose associated value is to be returned.
**Returns:** the value to which this map maps the specified key, or

null

if the map contains no mapping for this key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

- remove

```java
public
Object
remove​(
Object
key)
```

Removes the mapping for this key from this map if it is present
(optional operation). More formally, if this map contains a mapping
from key

k

to value

v

such that

(key==null ? k==null : key.equals(k))

, that mapping
is removed. (The map can contain at most one such mapping.)

Returns the value to which the map previously associated the key, or

null

if the map contained no mapping for this key. (A

null

return can also indicate that the map previously
associated

null

with the specified key if the implementation
supports

null

values.) The map will not contain a mapping for
the specified key once the call returns.

**Specified by:** remove

in interface

Bindings
**Specified by:** remove

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose mapping is to be removed from the map.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

Constructor Detail

- SimpleBindings

```java
public SimpleBindings​(
Map
<
String
,​
Object
> m)
```

Constructor uses an existing

Map

to store the values.

**Parameters:** m

- The

Map

backing this

SimpleBindings

.
**Throws:** NullPointerException

- if m is null

- SimpleBindings

```java
public SimpleBindings()
```

Default constructor uses a

HashMap

.

---

#### Constructor Detail

SimpleBindings

```java
public SimpleBindings​(
Map
<
String
,​
Object
> m)
```

Constructor uses an existing

Map

to store the values.

**Parameters:** m

- The

Map

backing this

SimpleBindings

.
**Throws:** NullPointerException

- if m is null

---

#### SimpleBindings

public SimpleBindings​(

Map

<

String

,​

Object

> m)

Constructor uses an existing

Map

to store the values.

SimpleBindings

```java
public SimpleBindings()
```

Default constructor uses a

HashMap

.

---

#### SimpleBindings

public SimpleBindings()

Default constructor uses a

HashMap

.

Method Detail

- put

```java
public
Object
put​(
String
name,

Object
value)
```

Sets the specified key/value in the underlying

map

field.

**Specified by:** put

in interface

Bindings
**Specified by:** put

in interface

Map

<

String

,​

Object

>
**Parameters:** name

- Name of value
**Parameters:** value

- Value to set.
**Returns:** Previous value for the specified key. Returns null if key was previously
unset.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

- putAll

```java
public void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)
```

putAll

is implemented using

Map.putAll

.

**Specified by:** putAll

in interface

Bindings
**Specified by:** putAll

in interface

Map

<

String

,​

Object

>
**Parameters:** toMerge

- The

Map

of values to add.
**Throws:** NullPointerException

- if toMerge map is null or if some key in the map is null.
**Throws:** IllegalArgumentException

- if some key in the map is an empty String.

- containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if this map contains a mapping for the specified
key. More formally, returns

true

if and only if
this map contains a mapping for a key

k

such that

(key==null ? k==null : key.equals(k))

. (There can be
at most one such mapping.)

**Specified by:** containsKey

in interface

Bindings
**Specified by:** containsKey

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose presence in this map is to be tested.
**Returns:** true

if this map contains a mapping for the specified
key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

- get

```java
public
Object
get​(
Object
key)
```

Returns the value to which this map maps the specified key. Returns

null

if the map contains no mapping for this key. A return
value of

null

does not

necessarily

indicate that the
map contains no mapping for the key; it's also possible that the map
explicitly maps the key to

null

. The

containsKey

operation may be used to distinguish these two cases.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

(key==null ? k==null : key.equals(k))

,
then this method returns

v

; otherwise
it returns

null

. (There can be at most one such mapping.)

**Specified by:** get

in interface

Bindings
**Specified by:** get

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose associated value is to be returned.
**Returns:** the value to which this map maps the specified key, or

null

if the map contains no mapping for this key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

- remove

```java
public
Object
remove​(
Object
key)
```

Removes the mapping for this key from this map if it is present
(optional operation). More formally, if this map contains a mapping
from key

k

to value

v

such that

(key==null ? k==null : key.equals(k))

, that mapping
is removed. (The map can contain at most one such mapping.)

Returns the value to which the map previously associated the key, or

null

if the map contained no mapping for this key. (A

null

return can also indicate that the map previously
associated

null

with the specified key if the implementation
supports

null

values.) The map will not contain a mapping for
the specified key once the call returns.

**Specified by:** remove

in interface

Bindings
**Specified by:** remove

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose mapping is to be removed from the map.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

---

#### Method Detail

put

```java
public
Object
put​(
String
name,

Object
value)
```

Sets the specified key/value in the underlying

map

field.

**Specified by:** put

in interface

Bindings
**Specified by:** put

in interface

Map

<

String

,​

Object

>
**Parameters:** name

- Name of value
**Parameters:** value

- Value to set.
**Returns:** Previous value for the specified key. Returns null if key was previously
unset.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

---

#### put

public

Object

put​(

String

name,

Object

value)

Sets the specified key/value in the underlying

map

field.

putAll

```java
public void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)
```

putAll

is implemented using

Map.putAll

.

**Specified by:** putAll

in interface

Bindings
**Specified by:** putAll

in interface

Map

<

String

,​

Object

>
**Parameters:** toMerge

- The

Map

of values to add.
**Throws:** NullPointerException

- if toMerge map is null or if some key in the map is null.
**Throws:** IllegalArgumentException

- if some key in the map is an empty String.

---

#### putAll

public void putAll​(

Map

<? extends

String

,​? extends

Object

> toMerge)

putAll

is implemented using

Map.putAll

.

containsKey

```java
public boolean containsKey​(
Object
key)
```

Returns

true

if this map contains a mapping for the specified
key. More formally, returns

true

if and only if
this map contains a mapping for a key

k

such that

(key==null ? k==null : key.equals(k))

. (There can be
at most one such mapping.)

**Specified by:** containsKey

in interface

Bindings
**Specified by:** containsKey

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose presence in this map is to be tested.
**Returns:** true

if this map contains a mapping for the specified
key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

---

#### containsKey

public boolean containsKey​(

Object

key)

Returns

true

if this map contains a mapping for the specified
key. More formally, returns

true

if and only if
this map contains a mapping for a key

k

such that

(key==null ? k==null : key.equals(k))

. (There can be
at most one such mapping.)

get

```java
public
Object
get​(
Object
key)
```

Returns the value to which this map maps the specified key. Returns

null

if the map contains no mapping for this key. A return
value of

null

does not

necessarily

indicate that the
map contains no mapping for the key; it's also possible that the map
explicitly maps the key to

null

. The

containsKey

operation may be used to distinguish these two cases.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

(key==null ? k==null : key.equals(k))

,
then this method returns

v

; otherwise
it returns

null

. (There can be at most one such mapping.)

**Specified by:** get

in interface

Bindings
**Specified by:** get

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose associated value is to be returned.
**Returns:** the value to which this map maps the specified key, or

null

if the map contains no mapping for this key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

---

#### get

public

Object

get​(

Object

key)

Returns the value to which this map maps the specified key. Returns

null

if the map contains no mapping for this key. A return
value of

null

does not

necessarily

indicate that the
map contains no mapping for the key; it's also possible that the map
explicitly maps the key to

null

. The

containsKey

operation may be used to distinguish these two cases.

More formally, if this map contains a mapping from a key

k

to a value

v

such that

(key==null ? k==null : key.equals(k))

,
then this method returns

v

; otherwise
it returns

null

. (There can be at most one such mapping.)

More formally, if this map contains a mapping from a key

k

to a value

v

such that

(key==null ? k==null : key.equals(k))

,
then this method returns

v

; otherwise
it returns

null

. (There can be at most one such mapping.)

remove

```java
public
Object
remove​(
Object
key)
```

Removes the mapping for this key from this map if it is present
(optional operation). More formally, if this map contains a mapping
from key

k

to value

v

such that

(key==null ? k==null : key.equals(k))

, that mapping
is removed. (The map can contain at most one such mapping.)

Returns the value to which the map previously associated the key, or

null

if the map contained no mapping for this key. (A

null

return can also indicate that the map previously
associated

null

with the specified key if the implementation
supports

null

values.) The map will not contain a mapping for
the specified key once the call returns.

**Specified by:** remove

in interface

Bindings
**Specified by:** remove

in interface

Map

<

String

,​

Object

>
**Parameters:** key

- key whose mapping is to be removed from the map.
**Returns:** previous value associated with specified key, or

null

if there was no mapping for key.
**Throws:** NullPointerException

- if key is null
**Throws:** ClassCastException

- if key is not String
**Throws:** IllegalArgumentException

- if key is empty String

---

#### remove

public

Object

remove​(

Object

key)

Removes the mapping for this key from this map if it is present
(optional operation). More formally, if this map contains a mapping
from key

k

to value

v

such that

(key==null ? k==null : key.equals(k))

, that mapping
is removed. (The map can contain at most one such mapping.)

Returns the value to which the map previously associated the key, or

null

if the map contained no mapping for this key. (A

null

return can also indicate that the map previously
associated

null

with the specified key if the implementation
supports

null

values.) The map will not contain a mapping for
the specified key once the call returns.

Returns the value to which the map previously associated the key, or

null

if the map contained no mapping for this key. (A

null

return can also indicate that the map previously
associated

null

with the specified key if the implementation
supports

null

values.) The map will not contain a mapping for
the specified key once the call returns.

---

