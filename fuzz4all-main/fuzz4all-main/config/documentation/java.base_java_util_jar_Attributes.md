# Class Attributes

**Source:** `java.base\java\util\jar\Attributes.html`

### Class Description

```java
public class
Attributes

extends
Object

implements
Map
<
Object
,​
Object
>,
Cloneable
```

The Attributes class maps Manifest attribute names to associated string
values. Valid attribute names are case-insensitive, are restricted to
the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed 70
characters in length. There must be a colon and a SPACE after the name;
the combined length will not exceed 72 characters.
Attribute values can contain any characters and
will be UTF8-encoded when written to the output stream. See the

JAR File Specification

for more information about valid attribute names and values.

This map and its views have a predictable iteration order, namely the
order that keys were inserted into the map, as with

LinkedHashMap

.

**All Implemented Interfaces:** Cloneable

,

Map

<

Object

,​

Object

>

---

### Field Details

#### protected
Map
<
Object
,​
Object
> map

The attribute name-value mappings.

---

### Constructor Details

#### public Attributes()

Constructs a new, empty Attributes object with default size.

---

#### public Attributes​(int size)

Constructs a new, empty Attributes object with the specified
initial size.

**Parameters:**
- size

- the initial number of attributes

---

#### public Attributes​(
Attributes
attr)

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

**Parameters:**
- attr

- the specified Attributes

---

### Method Details

#### public
Object
get​(
Object
name)

Returns the value of the specified attribute name, or null if the
attribute name was not found.

**Specified by:**
- get

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- name

- the attribute name

**Returns:**
- the value of the specified attribute name, or null if
not found.

---

#### public
String
getValue​(
String
name)

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found. The attribute
name is case-insensitive.

This method is defined as:

```java
return (String)get(new Attributes.Name((String)name));
```

**Parameters:**
- name

- the attribute name as a string

**Returns:**
- the String value of the specified attribute name, or null if
not found.

**Throws:**
- IllegalArgumentException

- if the attribute name is invalid

---

#### public
String
getValue​(
Attributes.Name
name)

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

This method is defined as:

```java
return (String)get(name);
```

**Parameters:**
- name

- the Attributes.Name object

**Returns:**
- the String value of the specified Attribute.Name, or null if
not found.

---

#### public
Object
put​(
Object
name,

Object
value)

Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.

**Specified by:**
- put

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- name

- the attribute name
- value

- the attribute value

**Returns:**
- the previous value of the attribute, or null if none

**Throws:**
- ClassCastException

- if the name is not a Attributes.Name
or the value is not a String

---

#### public
String
putValue​(
String
name,

String
value)

Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.

This method is defined as:

```java
return (String)put(new Attributes.Name(name), value);
```

**Parameters:**
- name

- the attribute name as a string
- value

- the attribute value

**Returns:**
- the previous value of the attribute, or null if none

**Throws:**
- IllegalArgumentException

- if the attribute name is invalid

---

#### public
Object
remove​(
Object
name)

Removes the attribute with the specified name (key) from this Map.
Returns the previous attribute value, or null if none.

**Specified by:**
- remove

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- name

- attribute name

**Returns:**
- the previous value of the attribute, or null if none

---

#### public boolean containsValue​(
Object
value)

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

**Specified by:**
- containsValue

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- value

- the attribute value

**Returns:**
- true if this Map maps one or more attribute names to
the specified value

---

#### public boolean containsKey​(
Object
name)

Returns true if this Map contains the specified attribute name (key).

**Specified by:**
- containsKey

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- name

- the attribute name

**Returns:**
- true if this Map contains the specified attribute name

---

#### public void putAll​(
Map
<?,​?> attr)

Copies all of the attribute name-value mappings from the specified
Attributes to this Map. Duplicate mappings will be replaced.

**Specified by:**
- putAll

in interface

Map

<

Object

,​

Object

>

**Parameters:**
- attr

- the Attributes to be stored in this map

**Throws:**
- ClassCastException

- if attr is not an Attributes

---

#### public void clear()

Removes all attributes from this Map.

**Specified by:**
- clear

in interface

Map

<

Object

,​

Object

>

---

#### public int size()

Returns the number of attributes in this Map.

**Specified by:**
- size

in interface

Map

<

Object

,​

Object

>

**Returns:**
- the number of key-value mappings in this map

---

#### public boolean isEmpty()

Returns true if this Map contains no attributes.

**Specified by:**
- isEmpty

in interface

Map

<

Object

,​

Object

>

**Returns:**
- true

if this map contains no key-value mappings

---

#### public
Set
<
Object
> keySet()

Returns a Set view of the attribute names (keys) contained in this Map.

**Specified by:**
- keySet

in interface

Map

<

Object

,​

Object

>

**Returns:**
- a set view of the keys contained in this map

---

#### public
Collection
<
Object
> values()

Returns a Collection view of the attribute values contained in this Map.

**Specified by:**
- values

in interface

Map

<

Object

,​

Object

>

**Returns:**
- a collection view of the values contained in this map

---

#### public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()

Returns a Collection view of the attribute name-value mappings
contained in this Map.

**Specified by:**
- entrySet

in interface

Map

<

Object

,​

Object

>

**Returns:**
- a set view of the mappings contained in this map

---

#### public boolean equals​(
Object
o)

Compares the specified Attributes object with this Map for equality.
Returns true if the given object is also an instance of Attributes
and the two Attributes objects represent the same mappings.

**Specified by:**
- equals

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the Object to be compared

**Returns:**
- true if the specified Object is equal to this Map

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this Map.

**Specified by:**
- hashCode

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Returns a copy of the Attributes, implemented as follows:

```java
public Object clone() { return new Attributes(this); }
```

Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Attributes

java.lang.Object

- java.util.jar.Attributes

java.util.jar.Attributes

**All Implemented Interfaces:** Cloneable

,

Map

<

Object

,​

Object

>

```java
public class
Attributes

extends
Object

implements
Map
<
Object
,​
Object
>,
Cloneable
```

The Attributes class maps Manifest attribute names to associated string
values. Valid attribute names are case-insensitive, are restricted to
the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed 70
characters in length. There must be a colon and a SPACE after the name;
the combined length will not exceed 72 characters.
Attribute values can contain any characters and
will be UTF8-encoded when written to the output stream. See the

JAR File Specification

for more information about valid attribute names and values.

This map and its views have a predictable iteration order, namely the
order that keys were inserted into the map, as with

LinkedHashMap

.

**Since:** 1.2
**See Also:** Manifest

public class

Attributes

extends

Object

implements

Map

<

Object

,​

Object

>,

Cloneable

The Attributes class maps Manifest attribute names to associated string
values. Valid attribute names are case-insensitive, are restricted to
the ASCII characters in the set [0-9a-zA-Z_-], and cannot exceed 70
characters in length. There must be a colon and a SPACE after the name;
the combined length will not exceed 72 characters.
Attribute values can contain any characters and
will be UTF8-encoded when written to the output stream. See the

JAR File Specification

for more information about valid attribute names and values.

This map and its views have a predictable iteration order, namely the
order that keys were inserted into the map, as with

LinkedHashMap

.

This map and its views have a predictable iteration order, namely the
order that keys were inserted into the map, as with

LinkedHashMap

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Attributes.Name

The Attributes.Name class represents an attribute name stored in
this Map.

- Nested classes/interfaces declared in interface java.util.

Map

Map.Entry

<

K

,​

V

>

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Map

<

Object

,​

Object

>

map

The attribute name-value mappings.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Attributes

()

Constructs a new, empty Attributes object with default size.

Attributes

​(int size)

Constructs a new, empty Attributes object with the specified
initial size.

Attributes

​(

Attributes

attr)

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Removes all attributes from this Map.

Object

clone

()

Returns a copy of the Attributes, implemented as follows:

boolean

containsKey

​(

Object

name)

Returns true if this Map contains the specified attribute name (key).

boolean

containsValue

​(

Object

value)

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

Set

<

Map.Entry

<

Object

,​

Object

>>

entrySet

()

Returns a Collection view of the attribute name-value mappings
contained in this Map.

boolean

equals

​(

Object

o)

Compares the specified Attributes object with this Map for equality.

Object

get

​(

Object

name)

Returns the value of the specified attribute name, or null if the
attribute name was not found.

String

getValue

​(

String

name)

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found.

String

getValue

​(

Attributes.Name

name)

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

int

hashCode

()

Returns the hash code value for this Map.

boolean

isEmpty

()

Returns true if this Map contains no attributes.

Set

<

Object

>

keySet

()

Returns a Set view of the attribute names (keys) contained in this Map.

Object

put

​(

Object

name,

Object

value)

Associates the specified value with the specified attribute name
(key) in this Map.

void

putAll

​(

Map

<?,​?> attr)

Copies all of the attribute name-value mappings from the specified
Attributes to this Map.

String

putValue

​(

String

name,

String

value)

Associates the specified value with the specified attribute name,
specified as a String.

Object

remove

​(

Object

name)

Removes the attribute with the specified name (key) from this Map.

int

size

()

Returns the number of attributes in this Map.

Collection

<

Object

>

values

()

Returns a Collection view of the attribute values contained in this Map.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Map

compute

,

computeIfAbsent

,

computeIfPresent

,

forEach

,

getOrDefault

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Attributes.Name

The Attributes.Name class represents an attribute name stored in
this Map.

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

The Attributes.Name class represents an attribute name stored in
this Map.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Map

<

Object

,​

Object

>

map

The attribute name-value mappings.

---

#### Field Summary

The attribute name-value mappings.

Constructor Summary

Constructors

Constructor

Description

Attributes

()

Constructs a new, empty Attributes object with default size.

Attributes

​(int size)

Constructs a new, empty Attributes object with the specified
initial size.

Attributes

​(

Attributes

attr)

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

---

#### Constructor Summary

Constructs a new, empty Attributes object with default size.

Constructs a new, empty Attributes object with the specified
initial size.

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Removes all attributes from this Map.

Object

clone

()

Returns a copy of the Attributes, implemented as follows:

boolean

containsKey

​(

Object

name)

Returns true if this Map contains the specified attribute name (key).

boolean

containsValue

​(

Object

value)

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

Set

<

Map.Entry

<

Object

,​

Object

>>

entrySet

()

Returns a Collection view of the attribute name-value mappings
contained in this Map.

boolean

equals

​(

Object

o)

Compares the specified Attributes object with this Map for equality.

Object

get

​(

Object

name)

Returns the value of the specified attribute name, or null if the
attribute name was not found.

String

getValue

​(

String

name)

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found.

String

getValue

​(

Attributes.Name

name)

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

int

hashCode

()

Returns the hash code value for this Map.

boolean

isEmpty

()

Returns true if this Map contains no attributes.

Set

<

Object

>

keySet

()

Returns a Set view of the attribute names (keys) contained in this Map.

Object

put

​(

Object

name,

Object

value)

Associates the specified value with the specified attribute name
(key) in this Map.

void

putAll

​(

Map

<?,​?> attr)

Copies all of the attribute name-value mappings from the specified
Attributes to this Map.

String

putValue

​(

String

name,

String

value)

Associates the specified value with the specified attribute name,
specified as a String.

Object

remove

​(

Object

name)

Removes the attribute with the specified name (key) from this Map.

int

size

()

Returns the number of attributes in this Map.

Collection

<

Object

>

values

()

Returns a Collection view of the attribute values contained in this Map.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.

Map

compute

,

computeIfAbsent

,

computeIfPresent

,

forEach

,

getOrDefault

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

---

#### Method Summary

Removes all attributes from this Map.

Returns a copy of the Attributes, implemented as follows:

Returns true if this Map contains the specified attribute name (key).

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

Returns a Collection view of the attribute name-value mappings
contained in this Map.

Compares the specified Attributes object with this Map for equality.

Returns the value of the specified attribute name, or null if the
attribute name was not found.

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found.

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

Returns the hash code value for this Map.

Returns true if this Map contains no attributes.

Returns a Set view of the attribute names (keys) contained in this Map.

Associates the specified value with the specified attribute name
(key) in this Map.

Copies all of the attribute name-value mappings from the specified
Attributes to this Map.

Associates the specified value with the specified attribute name,
specified as a String.

Removes the attribute with the specified name (key) from this Map.

Returns the number of attributes in this Map.

Returns a Collection view of the attribute values contained in this Map.

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

compute

,

computeIfAbsent

,

computeIfPresent

,

forEach

,

getOrDefault

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

---

#### Methods declared in interface java.util. Map

============ FIELD DETAIL ===========

- Field Detail

- map

```java
protected
Map
<
Object
,​
Object
> map
```

The attribute name-value mappings.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Attributes

```java
public Attributes()
```

Constructs a new, empty Attributes object with default size.

- Attributes

```java
public Attributes​(int size)
```

Constructs a new, empty Attributes object with the specified
initial size.

**Parameters:** size

- the initial number of attributes

- Attributes

```java
public Attributes​(
Attributes
attr)
```

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

**Parameters:** attr

- the specified Attributes

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public
Object
get​(
Object
name)
```

Returns the value of the specified attribute name, or null if the
attribute name was not found.

**Specified by:** get

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Returns:** the value of the specified attribute name, or null if
not found.

- getValue

```java
public
String
getValue​(
String
name)
```

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found. The attribute
name is case-insensitive.

This method is defined as:

```java
return (String)get(new Attributes.Name((String)name));
```

**Parameters:** name

- the attribute name as a string
**Returns:** the String value of the specified attribute name, or null if
not found.
**Throws:** IllegalArgumentException

- if the attribute name is invalid

- getValue

```java
public
String
getValue​(
Attributes.Name
name)
```

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

This method is defined as:

```java
return (String)get(name);
```

**Parameters:** name

- the Attributes.Name object
**Returns:** the String value of the specified Attribute.Name, or null if
not found.

- put

```java
public
Object
put​(
Object
name,

Object
value)
```

Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Parameters:** value

- the attribute value
**Returns:** the previous value of the attribute, or null if none
**Throws:** ClassCastException

- if the name is not a Attributes.Name
or the value is not a String

- putValue

```java
public
String
putValue​(
String
name,

String
value)
```

Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.

This method is defined as:

```java
return (String)put(new Attributes.Name(name), value);
```

**Parameters:** name

- the attribute name as a string
**Parameters:** value

- the attribute value
**Returns:** the previous value of the attribute, or null if none
**Throws:** IllegalArgumentException

- if the attribute name is invalid

- remove

```java
public
Object
remove​(
Object
name)
```

Removes the attribute with the specified name (key) from this Map.
Returns the previous attribute value, or null if none.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- attribute name
**Returns:** the previous value of the attribute, or null if none

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

**Specified by:** containsValue

in interface

Map

<

Object

,​

Object

>
**Parameters:** value

- the attribute value
**Returns:** true if this Map maps one or more attribute names to
the specified value

- containsKey

```java
public boolean containsKey​(
Object
name)
```

Returns true if this Map contains the specified attribute name (key).

**Specified by:** containsKey

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Returns:** true if this Map contains the specified attribute name

- putAll

```java
public void putAll​(
Map
<?,​?> attr)
```

Copies all of the attribute name-value mappings from the specified
Attributes to this Map. Duplicate mappings will be replaced.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Parameters:** attr

- the Attributes to be stored in this map
**Throws:** ClassCastException

- if attr is not an Attributes

- clear

```java
public void clear()
```

Removes all attributes from this Map.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>

- size

```java
public int size()
```

Returns the number of attributes in this Map.

**Specified by:** size

in interface

Map

<

Object

,​

Object

>
**Returns:** the number of key-value mappings in this map

- isEmpty

```java
public boolean isEmpty()
```

Returns true if this Map contains no attributes.

**Specified by:** isEmpty

in interface

Map

<

Object

,​

Object

>
**Returns:** true

if this map contains no key-value mappings

- keySet

```java
public
Set
<
Object
> keySet()
```

Returns a Set view of the attribute names (keys) contained in this Map.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a set view of the keys contained in this map

- values

```java
public
Collection
<
Object
> values()
```

Returns a Collection view of the attribute values contained in this Map.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Returns:** a collection view of the values contained in this map

- entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns a Collection view of the attribute name-value mappings
contained in this Map.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a set view of the mappings contained in this map

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Attributes object with this Map for equality.
Returns true if the given object is also an instance of Attributes
and the two Attributes objects represent the same mappings.

**Specified by:** equals

in interface

Map

<

Object

,​

Object

>
**Overrides:** equals

in class

Object
**Parameters:** o

- the Object to be compared
**Returns:** true if the specified Object is equal to this Map
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this Map.

**Specified by:** hashCode

in interface

Map

<

Object

,​

Object

>
**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a copy of the Attributes, implemented as follows:

```java
public Object clone() { return new Attributes(this); }
```

Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

Field Detail

- map

```java
protected
Map
<
Object
,​
Object
> map
```

The attribute name-value mappings.

---

#### Field Detail

map

```java
protected
Map
<
Object
,​
Object
> map
```

The attribute name-value mappings.

---

#### map

protected

Map

<

Object

,​

Object

> map

The attribute name-value mappings.

Constructor Detail

- Attributes

```java
public Attributes()
```

Constructs a new, empty Attributes object with default size.

- Attributes

```java
public Attributes​(int size)
```

Constructs a new, empty Attributes object with the specified
initial size.

**Parameters:** size

- the initial number of attributes

- Attributes

```java
public Attributes​(
Attributes
attr)
```

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

**Parameters:** attr

- the specified Attributes

---

#### Constructor Detail

Attributes

```java
public Attributes()
```

Constructs a new, empty Attributes object with default size.

---

#### Attributes

public Attributes()

Constructs a new, empty Attributes object with default size.

Attributes

```java
public Attributes​(int size)
```

Constructs a new, empty Attributes object with the specified
initial size.

**Parameters:** size

- the initial number of attributes

---

#### Attributes

public Attributes​(int size)

Constructs a new, empty Attributes object with the specified
initial size.

Attributes

```java
public Attributes​(
Attributes
attr)
```

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

**Parameters:** attr

- the specified Attributes

---

#### Attributes

public Attributes​(

Attributes

attr)

Constructs a new Attributes object with the same attribute name-value
mappings as in the specified Attributes.

Method Detail

- get

```java
public
Object
get​(
Object
name)
```

Returns the value of the specified attribute name, or null if the
attribute name was not found.

**Specified by:** get

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Returns:** the value of the specified attribute name, or null if
not found.

- getValue

```java
public
String
getValue​(
String
name)
```

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found. The attribute
name is case-insensitive.

This method is defined as:

```java
return (String)get(new Attributes.Name((String)name));
```

**Parameters:** name

- the attribute name as a string
**Returns:** the String value of the specified attribute name, or null if
not found.
**Throws:** IllegalArgumentException

- if the attribute name is invalid

- getValue

```java
public
String
getValue​(
Attributes.Name
name)
```

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

This method is defined as:

```java
return (String)get(name);
```

**Parameters:** name

- the Attributes.Name object
**Returns:** the String value of the specified Attribute.Name, or null if
not found.

- put

```java
public
Object
put​(
Object
name,

Object
value)
```

Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Parameters:** value

- the attribute value
**Returns:** the previous value of the attribute, or null if none
**Throws:** ClassCastException

- if the name is not a Attributes.Name
or the value is not a String

- putValue

```java
public
String
putValue​(
String
name,

String
value)
```

Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.

This method is defined as:

```java
return (String)put(new Attributes.Name(name), value);
```

**Parameters:** name

- the attribute name as a string
**Parameters:** value

- the attribute value
**Returns:** the previous value of the attribute, or null if none
**Throws:** IllegalArgumentException

- if the attribute name is invalid

- remove

```java
public
Object
remove​(
Object
name)
```

Removes the attribute with the specified name (key) from this Map.
Returns the previous attribute value, or null if none.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- attribute name
**Returns:** the previous value of the attribute, or null if none

- containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

**Specified by:** containsValue

in interface

Map

<

Object

,​

Object

>
**Parameters:** value

- the attribute value
**Returns:** true if this Map maps one or more attribute names to
the specified value

- containsKey

```java
public boolean containsKey​(
Object
name)
```

Returns true if this Map contains the specified attribute name (key).

**Specified by:** containsKey

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Returns:** true if this Map contains the specified attribute name

- putAll

```java
public void putAll​(
Map
<?,​?> attr)
```

Copies all of the attribute name-value mappings from the specified
Attributes to this Map. Duplicate mappings will be replaced.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Parameters:** attr

- the Attributes to be stored in this map
**Throws:** ClassCastException

- if attr is not an Attributes

- clear

```java
public void clear()
```

Removes all attributes from this Map.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>

- size

```java
public int size()
```

Returns the number of attributes in this Map.

**Specified by:** size

in interface

Map

<

Object

,​

Object

>
**Returns:** the number of key-value mappings in this map

- isEmpty

```java
public boolean isEmpty()
```

Returns true if this Map contains no attributes.

**Specified by:** isEmpty

in interface

Map

<

Object

,​

Object

>
**Returns:** true

if this map contains no key-value mappings

- keySet

```java
public
Set
<
Object
> keySet()
```

Returns a Set view of the attribute names (keys) contained in this Map.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a set view of the keys contained in this map

- values

```java
public
Collection
<
Object
> values()
```

Returns a Collection view of the attribute values contained in this Map.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Returns:** a collection view of the values contained in this map

- entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns a Collection view of the attribute name-value mappings
contained in this Map.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a set view of the mappings contained in this map

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Attributes object with this Map for equality.
Returns true if the given object is also an instance of Attributes
and the two Attributes objects represent the same mappings.

**Specified by:** equals

in interface

Map

<

Object

,​

Object

>
**Overrides:** equals

in class

Object
**Parameters:** o

- the Object to be compared
**Returns:** true if the specified Object is equal to this Map
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this Map.

**Specified by:** hashCode

in interface

Map

<

Object

,​

Object

>
**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a copy of the Attributes, implemented as follows:

```java
public Object clone() { return new Attributes(this); }
```

Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### Method Detail

get

```java
public
Object
get​(
Object
name)
```

Returns the value of the specified attribute name, or null if the
attribute name was not found.

**Specified by:** get

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Returns:** the value of the specified attribute name, or null if
not found.

---

#### get

public

Object

get​(

Object

name)

Returns the value of the specified attribute name, or null if the
attribute name was not found.

getValue

```java
public
String
getValue​(
String
name)
```

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found. The attribute
name is case-insensitive.

This method is defined as:

```java
return (String)get(new Attributes.Name((String)name));
```

**Parameters:** name

- the attribute name as a string
**Returns:** the String value of the specified attribute name, or null if
not found.
**Throws:** IllegalArgumentException

- if the attribute name is invalid

---

#### getValue

public

String

getValue​(

String

name)

Returns the value of the specified attribute name, specified as
a string, or null if the attribute was not found. The attribute
name is case-insensitive.

This method is defined as:

```java
return (String)get(new Attributes.Name((String)name));
```

This method is defined as:

```java
return (String)get(new Attributes.Name((String)name));
```

return (String)get(new Attributes.Name((String)name));

getValue

```java
public
String
getValue​(
Attributes.Name
name)
```

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

This method is defined as:

```java
return (String)get(name);
```

**Parameters:** name

- the Attributes.Name object
**Returns:** the String value of the specified Attribute.Name, or null if
not found.

---

#### getValue

public

String

getValue​(

Attributes.Name

name)

Returns the value of the specified Attributes.Name, or null if the
attribute was not found.

This method is defined as:

```java
return (String)get(name);
```

This method is defined as:

```java
return (String)get(name);
```

return (String)get(name);

put

```java
public
Object
put​(
Object
name,

Object
value)
```

Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Parameters:** value

- the attribute value
**Returns:** the previous value of the attribute, or null if none
**Throws:** ClassCastException

- if the name is not a Attributes.Name
or the value is not a String

---

#### put

public

Object

put​(

Object

name,

Object

value)

Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.

putValue

```java
public
String
putValue​(
String
name,

String
value)
```

Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.

This method is defined as:

```java
return (String)put(new Attributes.Name(name), value);
```

**Parameters:** name

- the attribute name as a string
**Parameters:** value

- the attribute value
**Returns:** the previous value of the attribute, or null if none
**Throws:** IllegalArgumentException

- if the attribute name is invalid

---

#### putValue

public

String

putValue​(

String

name,

String

value)

Associates the specified value with the specified attribute name,
specified as a String. The attributes name is case-insensitive.
If the Map previously contained a mapping for the attribute name,
the old value is replaced.

This method is defined as:

```java
return (String)put(new Attributes.Name(name), value);
```

This method is defined as:

```java
return (String)put(new Attributes.Name(name), value);
```

return (String)put(new Attributes.Name(name), value);

remove

```java
public
Object
remove​(
Object
name)
```

Removes the attribute with the specified name (key) from this Map.
Returns the previous attribute value, or null if none.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- attribute name
**Returns:** the previous value of the attribute, or null if none

---

#### remove

public

Object

remove​(

Object

name)

Removes the attribute with the specified name (key) from this Map.
Returns the previous attribute value, or null if none.

containsValue

```java
public boolean containsValue​(
Object
value)
```

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

**Specified by:** containsValue

in interface

Map

<

Object

,​

Object

>
**Parameters:** value

- the attribute value
**Returns:** true if this Map maps one or more attribute names to
the specified value

---

#### containsValue

public boolean containsValue​(

Object

value)

Returns true if this Map maps one or more attribute names (keys)
to the specified value.

containsKey

```java
public boolean containsKey​(
Object
name)
```

Returns true if this Map contains the specified attribute name (key).

**Specified by:** containsKey

in interface

Map

<

Object

,​

Object

>
**Parameters:** name

- the attribute name
**Returns:** true if this Map contains the specified attribute name

---

#### containsKey

public boolean containsKey​(

Object

name)

Returns true if this Map contains the specified attribute name (key).

putAll

```java
public void putAll​(
Map
<?,​?> attr)
```

Copies all of the attribute name-value mappings from the specified
Attributes to this Map. Duplicate mappings will be replaced.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Parameters:** attr

- the Attributes to be stored in this map
**Throws:** ClassCastException

- if attr is not an Attributes

---

#### putAll

public void putAll​(

Map

<?,​?> attr)

Copies all of the attribute name-value mappings from the specified
Attributes to this Map. Duplicate mappings will be replaced.

clear

```java
public void clear()
```

Removes all attributes from this Map.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>

---

#### clear

public void clear()

Removes all attributes from this Map.

size

```java
public int size()
```

Returns the number of attributes in this Map.

**Specified by:** size

in interface

Map

<

Object

,​

Object

>
**Returns:** the number of key-value mappings in this map

---

#### size

public int size()

Returns the number of attributes in this Map.

isEmpty

```java
public boolean isEmpty()
```

Returns true if this Map contains no attributes.

**Specified by:** isEmpty

in interface

Map

<

Object

,​

Object

>
**Returns:** true

if this map contains no key-value mappings

---

#### isEmpty

public boolean isEmpty()

Returns true if this Map contains no attributes.

keySet

```java
public
Set
<
Object
> keySet()
```

Returns a Set view of the attribute names (keys) contained in this Map.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a set view of the keys contained in this map

---

#### keySet

public

Set

<

Object

> keySet()

Returns a Set view of the attribute names (keys) contained in this Map.

values

```java
public
Collection
<
Object
> values()
```

Returns a Collection view of the attribute values contained in this Map.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Returns:** a collection view of the values contained in this map

---

#### values

public

Collection

<

Object

> values()

Returns a Collection view of the attribute values contained in this Map.

entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns a Collection view of the attribute name-value mappings
contained in this Map.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Returns:** a set view of the mappings contained in this map

---

#### entrySet

public

Set

<

Map.Entry

<

Object

,​

Object

>> entrySet()

Returns a Collection view of the attribute name-value mappings
contained in this Map.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Attributes object with this Map for equality.
Returns true if the given object is also an instance of Attributes
and the two Attributes objects represent the same mappings.

**Specified by:** equals

in interface

Map

<

Object

,​

Object

>
**Overrides:** equals

in class

Object
**Parameters:** o

- the Object to be compared
**Returns:** true if the specified Object is equal to this Map
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified Attributes object with this Map for equality.
Returns true if the given object is also an instance of Attributes
and the two Attributes objects represent the same mappings.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this Map.

**Specified by:** hashCode

in interface

Map

<

Object

,​

Object

>
**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this Map.

clone

```java
public
Object
clone()
```

Returns a copy of the Attributes, implemented as follows:

```java
public Object clone() { return new Attributes(this); }
```

Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a copy of the Attributes, implemented as follows:

```java
public Object clone() { return new Attributes(this); }
```

Since the attribute names and values are themselves immutable,
the Attributes returned can be safely modified without affecting
the original.

public Object clone() { return new Attributes(this); }

---

