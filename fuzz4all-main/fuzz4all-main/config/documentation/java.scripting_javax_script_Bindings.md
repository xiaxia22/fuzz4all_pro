# Interface Bindings

**Source:** `java.scripting\javax\script\Bindings.html`

### Class Description

```java
public interface
Bindings

extends
Map
<
String
,​
Object
>
```

A mapping of key/value pairs, all of whose keys are

Strings

.

**All Superinterfaces:** Map

<

String

,​

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
put​(
String
name,

Object
value)

Set a named value.

**Specified by:**
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

- The name associated with the value.
- value

- The value associated with the name.

**Returns:**
- The value previously associated with the given name.
Returns null if no value was previously associated with the name.

**Throws:**
- NullPointerException

- if the name is null.
- IllegalArgumentException

- if the name is empty String.

---

#### void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)

Adds all the mappings in a given

Map

to this

Bindings

.

**Specified by:**
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

to merge with this one.

**Throws:**
- NullPointerException

- if toMerge map is null or if some key in the map is null.
- IllegalArgumentException

- if some key in the map is an empty String.

---

#### boolean containsKey​(
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

#### Object
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

#### Object
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

#### Interface Bindings

**All Superinterfaces:** Map

<

String

,​

Object

>

**All Known Implementing Classes:** ScriptObjectMirror

,

SimpleBindings

```java
public interface
Bindings

extends
Map
<
String
,​
Object
>
```

A mapping of key/value pairs, all of whose keys are

Strings

.

**Since:** 1.6

public interface

Bindings

extends

Map

<

String

,​

Object

>

A mapping of key/value pairs, all of whose keys are

Strings

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

Set a named value.

void

putAll

​(

Map

<? extends

String

,​? extends

Object

> toMerge)

Adds all the mappings in a given

Map

to this

Bindings

.

Object

remove

​(

Object

key)

Removes the mapping for this key from this map if it is present
(optional operation).

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

Method Summary

All Methods

Instance Methods

Abstract Methods

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

Set a named value.

void

putAll

​(

Map

<? extends

String

,​? extends

Object

> toMerge)

Adds all the mappings in a given

Map

to this

Bindings

.

Object

remove

​(

Object

key)

Removes the mapping for this key from this map if it is present
(optional operation).

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

Set a named value.

Adds all the mappings in a given

Map

to this

Bindings

.

Removes the mapping for this key from this map if it is present
(optional operation).

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

============ METHOD DETAIL ==========

- Method Detail

- put

```java
Object
put​(
String
name,

Object
value)
```

Set a named value.

**Specified by:** put

in interface

Map

<

String

,​

Object

>
**Parameters:** name

- The name associated with the value.
**Parameters:** value

- The value associated with the name.
**Returns:** The value previously associated with the given name.
Returns null if no value was previously associated with the name.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty String.

- putAll

```java
void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)
```

Adds all the mappings in a given

Map

to this

Bindings

.

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

to merge with this one.
**Throws:** NullPointerException

- if toMerge map is null or if some key in the map is null.
**Throws:** IllegalArgumentException

- if some key in the map is an empty String.

- containsKey

```java
boolean containsKey​(
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

Method Detail

- put

```java
Object
put​(
String
name,

Object
value)
```

Set a named value.

**Specified by:** put

in interface

Map

<

String

,​

Object

>
**Parameters:** name

- The name associated with the value.
**Parameters:** value

- The value associated with the name.
**Returns:** The value previously associated with the given name.
Returns null if no value was previously associated with the name.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty String.

- putAll

```java
void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)
```

Adds all the mappings in a given

Map

to this

Bindings

.

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

to merge with this one.
**Throws:** NullPointerException

- if toMerge map is null or if some key in the map is null.
**Throws:** IllegalArgumentException

- if some key in the map is an empty String.

- containsKey

```java
boolean containsKey​(
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
Object
put​(
String
name,

Object
value)
```

Set a named value.

**Specified by:** put

in interface

Map

<

String

,​

Object

>
**Parameters:** name

- The name associated with the value.
**Parameters:** value

- The value associated with the name.
**Returns:** The value previously associated with the given name.
Returns null if no value was previously associated with the name.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty String.

---

#### put

Object

put​(

String

name,

Object

value)

Set a named value.

putAll

```java
void putAll​(
Map
<? extends
String
,​? extends
Object
> toMerge)
```

Adds all the mappings in a given

Map

to this

Bindings

.

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

to merge with this one.
**Throws:** NullPointerException

- if toMerge map is null or if some key in the map is null.
**Throws:** IllegalArgumentException

- if some key in the map is an empty String.

---

#### putAll

void putAll​(

Map

<? extends

String

,​? extends

Object

> toMerge)

Adds all the mappings in a given

Map

to this

Bindings

.

containsKey

```java
boolean containsKey​(
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

boolean containsKey​(

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

