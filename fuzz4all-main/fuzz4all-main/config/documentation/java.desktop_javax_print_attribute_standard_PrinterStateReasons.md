# Class PrinterStateReasons

**Source:** `java.desktop\javax\print\attribute\standard\PrinterStateReasons.html`

### Class Description

```java
public final class
PrinterStateReasons

extends
HashMap
<
PrinterStateReason
,​
Severity
>
implements
PrintServiceAttribute
```

Class

PrinterStateReasons

is a printing attribute class, a set of
enumeration values, that provides additional information about the printer's
current state, i.e., information that augments the value of the printer's

PrinterState

attribute.

Instances of

PrinterStateReason

do not appear in a
Print Service's attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one, or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each

PrinterStateReason

object is associated with a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the corresponding condition
becomes true of the printer, and the printer removes the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

Class PrinterStateReasons inherits its implementation from class

java.util.HashMap

. Each entry in the map consists of a

PrinterStateReason

object (key) mapping to a

Severity

object (value):

Unlike most printing attributes which are immutable once constructed, class

PrinterStateReasons

is designed to be mutable; you can add

PrinterStateReason

objects to an existing

PrinterStateReasons

object and remove them again. However, like class

java.util.HashMap

, class

PrinterStateReasons

is not
multiple thread safe. If a

PrinterStateReasons

object will be used by
multiple threads, be sure to synchronize its operations (e.g., using a
synchronized map view obtained from class

java.util.Collections

).

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

PrinterStateReason

,​

Severity

>

,

Attribute

,

PrintServiceAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrinterStateReasons()

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

---

#### public PrinterStateReasons​(int initialCapacity)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

**Parameters:**
- initialCapacity

- initial capacity

**Throws:**
- IllegalArgumentException

- if the initial capacity is negative

---

#### public PrinterStateReasons​(int initialCapacity,
float loadFactor)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

**Parameters:**
- initialCapacity

- initial capacity
- loadFactor

- load factor

**Throws:**
- IllegalArgumentException

- if the initial capacity is negative

---

#### public PrinterStateReasons​(
Map
<
PrinterStateReason
,​
Severity
> map)

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map. The underlying hash map's initial
capacity and load factor are as specified in the superclass constructor

HashMap(Map)

.

**Parameters:**
- map

- map to copy

**Throws:**
- NullPointerException

- if

map

is

null

or if any key
or value in

map

is

null
- ClassCastException

- if any key in

map

is not an instance
of class

PrinterStateReason

or if any
value in

map

is not an instance of class

Severity

---

### Method Details

#### public
Severity
put​(
PrinterStateReason
reason,

Severity
severity)

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level. If this printer
state reasons attribute previously contained a mapping for the given
printer state reason, the old value is replaced.

**Specified by:**
- put

in interface

Map

<

PrinterStateReason

,​

Severity

>

**Overrides:**
- put

in class

HashMap

<

PrinterStateReason

,​

Severity

>

**Parameters:**
- reason

- printer state reason. This must be an instance of class

PrinterStateReason
- severity

- severity of the printer state reason. This must be an
instance of class

Severity

**Returns:**
- previous severity associated with the given printer state reason,
or

null

if the given printer state reason was not
present

**Throws:**
- NullPointerException

- if

reason

is

null

or

severity

is

null
- ClassCastException

- if

reason

is not an instance of class

PrinterStateReason

or if

severity

is not an instance of class

Severity

**Since:**
- 1.5

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PrinterStateReasons

, the category is class

PrinterStateReasons

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

PrinterStateReasons

, the category name is

"printer-state-reasons"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

#### public
Set
<
PrinterStateReason
> printerStateReasonSet​(
Severity
severity)

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute. Each element in the set view is a

PrinterStateReason

object. The only elements
in the set view are the

PrinterStateReason

objects that map to the given severity value. The set view is backed by
this

PrinterStateReasons

attribute, so changes to this

PrinterStateReasons

attribute are reflected in the set view. The
set view does not support element insertion or removal. The set view's
iterator does not support element removal.

**Parameters:**
- severity

- severity level

**Returns:**
- set view of the individual

PrinterStateReason

attributes at the
given

Severity

level

**Throws:**
- NullPointerException

- if

severity

is

null

---

### Additional Sections

#### Class PrinterStateReasons

java.lang.Object

- java.util.AbstractMap

<K,​V>
- - java.util.HashMap

<

PrinterStateReason

,​

Severity

>
- - javax.print.attribute.standard.PrinterStateReasons

java.util.AbstractMap

<K,​V>

- java.util.HashMap

<

PrinterStateReason

,​

Severity

>
- - javax.print.attribute.standard.PrinterStateReasons

java.util.HashMap

<

PrinterStateReason

,​

Severity

>

- javax.print.attribute.standard.PrinterStateReasons

javax.print.attribute.standard.PrinterStateReasons

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

PrinterStateReason

,​

Severity

>

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterStateReasons

extends
HashMap
<
PrinterStateReason
,​
Severity
>
implements
PrintServiceAttribute
```

Class

PrinterStateReasons

is a printing attribute class, a set of
enumeration values, that provides additional information about the printer's
current state, i.e., information that augments the value of the printer's

PrinterState

attribute.

Instances of

PrinterStateReason

do not appear in a
Print Service's attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one, or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each

PrinterStateReason

object is associated with a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the corresponding condition
becomes true of the printer, and the printer removes the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

Class PrinterStateReasons inherits its implementation from class

java.util.HashMap

. Each entry in the map consists of a

PrinterStateReason

object (key) mapping to a

Severity

object (value):

Unlike most printing attributes which are immutable once constructed, class

PrinterStateReasons

is designed to be mutable; you can add

PrinterStateReason

objects to an existing

PrinterStateReasons

object and remove them again. However, like class

java.util.HashMap

, class

PrinterStateReasons

is not
multiple thread safe. If a

PrinterStateReasons

object will be used by
multiple threads, be sure to synchronize its operations (e.g., using a
synchronized map view obtained from class

java.util.Collections

).

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterStateReasons

extends

HashMap

<

PrinterStateReason

,​

Severity

>
implements

PrintServiceAttribute

Class

PrinterStateReasons

is a printing attribute class, a set of
enumeration values, that provides additional information about the printer's
current state, i.e., information that augments the value of the printer's

PrinterState

attribute.

Instances of

PrinterStateReason

do not appear in a
Print Service's attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one, or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each

PrinterStateReason

object is associated with a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the corresponding condition
becomes true of the printer, and the printer removes the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

Class PrinterStateReasons inherits its implementation from class

java.util.HashMap

. Each entry in the map consists of a

PrinterStateReason

object (key) mapping to a

Severity

object (value):

Unlike most printing attributes which are immutable once constructed, class

PrinterStateReasons

is designed to be mutable; you can add

PrinterStateReason

objects to an existing

PrinterStateReasons

object and remove them again. However, like class

java.util.HashMap

, class

PrinterStateReasons

is not
multiple thread safe. If a

PrinterStateReasons

object will be used by
multiple threads, be sure to synchronize its operations (e.g., using a
synchronized map view obtained from class

java.util.Collections

).

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

Instances of

PrinterStateReason

do not appear in a
Print Service's attribute set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set. The

PrinterStateReasons

attribute contains zero, one, or more than one

PrinterStateReason

objects which pertain to the
Print Service's status, and each

PrinterStateReason

object is associated with a

Severity

level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the corresponding condition
becomes true of the printer, and the printer removes the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

Class PrinterStateReasons inherits its implementation from class

java.util.HashMap

. Each entry in the map consists of a

PrinterStateReason

object (key) mapping to a

Severity

object (value):

Unlike most printing attributes which are immutable once constructed, class

PrinterStateReasons

is designed to be mutable; you can add

PrinterStateReason

objects to an existing

PrinterStateReasons

object and remove them again. However, like class

java.util.HashMap

, class

PrinterStateReasons

is not
multiple thread safe. If a

PrinterStateReasons

object will be used by
multiple threads, be sure to synchronize its operations (e.g., using a
synchronized map view obtained from class

java.util.Collections

).

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

Class PrinterStateReasons inherits its implementation from class

java.util.HashMap

. Each entry in the map consists of a

PrinterStateReason

object (key) mapping to a

Severity

object (value):

Unlike most printing attributes which are immutable once constructed, class

PrinterStateReasons

is designed to be mutable; you can add

PrinterStateReason

objects to an existing

PrinterStateReasons

object and remove them again. However, like class

java.util.HashMap

, class

PrinterStateReasons

is not
multiple thread safe. If a

PrinterStateReasons

object will be used by
multiple threads, be sure to synchronize its operations (e.g., using a
synchronized map view obtained from class

java.util.Collections

).

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

Unlike most printing attributes which are immutable once constructed, class

PrinterStateReasons

is designed to be mutable; you can add

PrinterStateReason

objects to an existing

PrinterStateReasons

object and remove them again. However, like class

java.util.HashMap

, class

PrinterStateReasons

is not
multiple thread safe. If a

PrinterStateReasons

object will be used by
multiple threads, be sure to synchronize its operations (e.g., using a
synchronized map view obtained from class

java.util.Collections

).

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The string values returned by each individual

PrinterStateReason

object's and the associated

Severity

object's

toString()

methods, concatenated
together with a hyphen (

"-"

) in between, gives the IPP keyword value.
The category name returned by

getName()

gives the IPP attribute name.

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

PrinterStateReasons

()

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

PrinterStateReasons

​(int initialCapacity)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

PrinterStateReasons

​(int initialCapacity,
float loadFactor)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

PrinterStateReasons

​(

Map

<

PrinterStateReason

,​

Severity

> map)

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

Set

<

PrinterStateReason

>

printerStateReasonSet

​(

Severity

severity)

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute.

Severity

put

​(

PrinterStateReason

reason,

Severity

severity)

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level.

- Methods declared in class java.util.

HashMap

clear

,

clone

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

entrySet

,

get

,

isEmpty

,

keySet

,

merge

,

putAll

,

remove

,

size

,

values

- Methods declared in class java.util.

AbstractMap

equals

,

hashCode

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

- Methods declared in interface java.util.

Map

equals

,

forEach

,

getOrDefault

,

hashCode

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

PrinterStateReasons

()

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

PrinterStateReasons

​(int initialCapacity)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

PrinterStateReasons

​(int initialCapacity,
float loadFactor)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

PrinterStateReasons

​(

Map

<

PrinterStateReason

,​

Severity

> map)

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map.

---

#### Constructor Summary

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

Set

<

PrinterStateReason

>

printerStateReasonSet

​(

Severity

severity)

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute.

Severity

put

​(

PrinterStateReason

reason,

Severity

severity)

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level.

- Methods declared in class java.util.

HashMap

clear

,

clone

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

entrySet

,

get

,

isEmpty

,

keySet

,

merge

,

putAll

,

remove

,

size

,

values

- Methods declared in class java.util.

AbstractMap

equals

,

hashCode

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

- Methods declared in interface java.util.

Map

equals

,

forEach

,

getOrDefault

,

hashCode

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

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute.

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level.

Methods declared in class java.util.

HashMap

clear

,

clone

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

entrySet

,

get

,

isEmpty

,

keySet

,

merge

,

putAll

,

remove

,

size

,

values

---

#### Methods declared in class java.util. HashMap

Methods declared in class java.util.

AbstractMap

equals

,

hashCode

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

Methods declared in interface java.util.

Map

equals

,

forEach

,

getOrDefault

,

hashCode

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrinterStateReasons

```java
public PrinterStateReasons()
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

- PrinterStateReasons

```java
public PrinterStateReasons​(int initialCapacity)
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

**Parameters:** initialCapacity

- initial capacity
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- PrinterStateReasons

```java
public PrinterStateReasons​(int initialCapacity,
float loadFactor)
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

**Parameters:** initialCapacity

- initial capacity
**Parameters:** loadFactor

- load factor
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- PrinterStateReasons

```java
public PrinterStateReasons​(
Map
<
PrinterStateReason
,​
Severity
> map)
```

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map. The underlying hash map's initial
capacity and load factor are as specified in the superclass constructor

HashMap(Map)

.

**Parameters:** map

- map to copy
**Throws:** NullPointerException

- if

map

is

null

or if any key
or value in

map

is

null
**Throws:** ClassCastException

- if any key in

map

is not an instance
of class

PrinterStateReason

or if any
value in

map

is not an instance of class

Severity

============ METHOD DETAIL ==========

- Method Detail

- put

```java
public
Severity
put​(
PrinterStateReason
reason,

Severity
severity)
```

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level. If this printer
state reasons attribute previously contained a mapping for the given
printer state reason, the old value is replaced.

**Specified by:** put

in interface

Map

<

PrinterStateReason

,​

Severity

>
**Overrides:** put

in class

HashMap

<

PrinterStateReason

,​

Severity

>
**Parameters:** reason

- printer state reason. This must be an instance of class

PrinterStateReason
**Parameters:** severity

- severity of the printer state reason. This must be an
instance of class

Severity
**Returns:** previous severity associated with the given printer state reason,
or

null

if the given printer state reason was not
present
**Throws:** NullPointerException

- if

reason

is

null

or

severity

is

null
**Throws:** ClassCastException

- if

reason

is not an instance of class

PrinterStateReason

or if

severity

is not an instance of class

Severity
**Since:** 1.5

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PrinterStateReasons

, the category is class

PrinterStateReasons

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

PrinterStateReasons

, the category name is

"printer-state-reasons"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

- printerStateReasonSet

```java
public
Set
<
PrinterStateReason
> printerStateReasonSet​(
Severity
severity)
```

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute. Each element in the set view is a

PrinterStateReason

object. The only elements
in the set view are the

PrinterStateReason

objects that map to the given severity value. The set view is backed by
this

PrinterStateReasons

attribute, so changes to this

PrinterStateReasons

attribute are reflected in the set view. The
set view does not support element insertion or removal. The set view's
iterator does not support element removal.

**Parameters:** severity

- severity level
**Returns:** set view of the individual

PrinterStateReason

attributes at the
given

Severity

level
**Throws:** NullPointerException

- if

severity

is

null

Constructor Detail

- PrinterStateReasons

```java
public PrinterStateReasons()
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

- PrinterStateReasons

```java
public PrinterStateReasons​(int initialCapacity)
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

**Parameters:** initialCapacity

- initial capacity
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- PrinterStateReasons

```java
public PrinterStateReasons​(int initialCapacity,
float loadFactor)
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

**Parameters:** initialCapacity

- initial capacity
**Parameters:** loadFactor

- load factor
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- PrinterStateReasons

```java
public PrinterStateReasons​(
Map
<
PrinterStateReason
,​
Severity
> map)
```

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map. The underlying hash map's initial
capacity and load factor are as specified in the superclass constructor

HashMap(Map)

.

**Parameters:** map

- map to copy
**Throws:** NullPointerException

- if

map

is

null

or if any key
or value in

map

is

null
**Throws:** ClassCastException

- if any key in

map

is not an instance
of class

PrinterStateReason

or if any
value in

map

is not an instance of class

Severity

---

#### Constructor Detail

PrinterStateReasons

```java
public PrinterStateReasons()
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

---

#### PrinterStateReasons

public PrinterStateReasons()

Construct a new, empty printer state reasons attribute; the underlying
hash map has the default initial capacity and load factor.

PrinterStateReasons

```java
public PrinterStateReasons​(int initialCapacity)
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

**Parameters:** initialCapacity

- initial capacity
**Throws:** IllegalArgumentException

- if the initial capacity is negative

---

#### PrinterStateReasons

public PrinterStateReasons​(int initialCapacity)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and the default load factor.

PrinterStateReasons

```java
public PrinterStateReasons​(int initialCapacity,
float loadFactor)
```

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

**Parameters:** initialCapacity

- initial capacity
**Parameters:** loadFactor

- load factor
**Throws:** IllegalArgumentException

- if the initial capacity is negative

---

#### PrinterStateReasons

public PrinterStateReasons​(int initialCapacity,
float loadFactor)

Construct a new, empty printer state reasons attribute; the underlying
hash map has the given initial capacity and load factor.

PrinterStateReasons

```java
public PrinterStateReasons​(
Map
<
PrinterStateReason
,​
Severity
> map)
```

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map. The underlying hash map's initial
capacity and load factor are as specified in the superclass constructor

HashMap(Map)

.

**Parameters:** map

- map to copy
**Throws:** NullPointerException

- if

map

is

null

or if any key
or value in

map

is

null
**Throws:** ClassCastException

- if any key in

map

is not an instance
of class

PrinterStateReason

or if any
value in

map

is not an instance of class

Severity

---

#### PrinterStateReasons

public PrinterStateReasons​(

Map

<

PrinterStateReason

,​

Severity

> map)

Construct a new printer state reasons attribute that contains the same

PrinterStateReason

-to-

Severity

mappings as the given map. The underlying hash map's initial
capacity and load factor are as specified in the superclass constructor

HashMap(Map)

.

Method Detail

- put

```java
public
Severity
put​(
PrinterStateReason
reason,

Severity
severity)
```

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level. If this printer
state reasons attribute previously contained a mapping for the given
printer state reason, the old value is replaced.

**Specified by:** put

in interface

Map

<

PrinterStateReason

,​

Severity

>
**Overrides:** put

in class

HashMap

<

PrinterStateReason

,​

Severity

>
**Parameters:** reason

- printer state reason. This must be an instance of class

PrinterStateReason
**Parameters:** severity

- severity of the printer state reason. This must be an
instance of class

Severity
**Returns:** previous severity associated with the given printer state reason,
or

null

if the given printer state reason was not
present
**Throws:** NullPointerException

- if

reason

is

null

or

severity

is

null
**Throws:** ClassCastException

- if

reason

is not an instance of class

PrinterStateReason

or if

severity

is not an instance of class

Severity
**Since:** 1.5

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PrinterStateReasons

, the category is class

PrinterStateReasons

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

PrinterStateReasons

, the category name is

"printer-state-reasons"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

- printerStateReasonSet

```java
public
Set
<
PrinterStateReason
> printerStateReasonSet​(
Severity
severity)
```

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute. Each element in the set view is a

PrinterStateReason

object. The only elements
in the set view are the

PrinterStateReason

objects that map to the given severity value. The set view is backed by
this

PrinterStateReasons

attribute, so changes to this

PrinterStateReasons

attribute are reflected in the set view. The
set view does not support element insertion or removal. The set view's
iterator does not support element removal.

**Parameters:** severity

- severity level
**Returns:** set view of the individual

PrinterStateReason

attributes at the
given

Severity

level
**Throws:** NullPointerException

- if

severity

is

null

---

#### Method Detail

put

```java
public
Severity
put​(
PrinterStateReason
reason,

Severity
severity)
```

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level. If this printer
state reasons attribute previously contained a mapping for the given
printer state reason, the old value is replaced.

**Specified by:** put

in interface

Map

<

PrinterStateReason

,​

Severity

>
**Overrides:** put

in class

HashMap

<

PrinterStateReason

,​

Severity

>
**Parameters:** reason

- printer state reason. This must be an instance of class

PrinterStateReason
**Parameters:** severity

- severity of the printer state reason. This must be an
instance of class

Severity
**Returns:** previous severity associated with the given printer state reason,
or

null

if the given printer state reason was not
present
**Throws:** NullPointerException

- if

reason

is

null

or

severity

is

null
**Throws:** ClassCastException

- if

reason

is not an instance of class

PrinterStateReason

or if

severity

is not an instance of class

Severity
**Since:** 1.5

---

#### put

public

Severity

put​(

PrinterStateReason

reason,

Severity

severity)

Adds the given printer state reason to this printer state reasons
attribute, associating it with the given severity level. If this printer
state reasons attribute previously contained a mapping for the given
printer state reason, the old value is replaced.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PrinterStateReasons

, the category is class

PrinterStateReasons

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

PrinterStateReasons

, the category is class

PrinterStateReasons

itself.

For class

PrinterStateReasons

, the category is class

PrinterStateReasons

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

PrinterStateReasons

, the category name is

"printer-state-reasons"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

PrinterStateReasons

, the category name is

"printer-state-reasons"

.

For class

PrinterStateReasons

, the category name is

"printer-state-reasons"

.

printerStateReasonSet

```java
public
Set
<
PrinterStateReason
> printerStateReasonSet​(
Severity
severity)
```

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute. Each element in the set view is a

PrinterStateReason

object. The only elements
in the set view are the

PrinterStateReason

objects that map to the given severity value. The set view is backed by
this

PrinterStateReasons

attribute, so changes to this

PrinterStateReasons

attribute are reflected in the set view. The
set view does not support element insertion or removal. The set view's
iterator does not support element removal.

**Parameters:** severity

- severity level
**Returns:** set view of the individual

PrinterStateReason

attributes at the
given

Severity

level
**Throws:** NullPointerException

- if

severity

is

null

---

#### printerStateReasonSet

public

Set

<

PrinterStateReason

> printerStateReasonSet​(

Severity

severity)

Obtain an unmodifiable set view of the individual printer state reason
attributes at the given severity level in this

PrinterStateReasons

attribute. Each element in the set view is a

PrinterStateReason

object. The only elements
in the set view are the

PrinterStateReason

objects that map to the given severity value. The set view is backed by
this

PrinterStateReasons

attribute, so changes to this

PrinterStateReasons

attribute are reflected in the set view. The
set view does not support element insertion or removal. The set view's
iterator does not support element removal.

---

