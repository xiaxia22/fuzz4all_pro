# Class JobStateReasons

**Source:** `java.desktop\javax\print\attribute\standard\JobStateReasons.html`

### Class Description

```java
public final class
JobStateReasons

extends
HashSet
<
JobStateReason
>
implements
PrintJobAttribute
```

Class

JobStateReasons

is a printing attribute class, a set of
enumeration values, that provides additional information about the job's
current state, i.e., information that augments the value of the job's

JobState

attribute.

Instances of

JobStateReason

do not appear in a Print
Job's attribute set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more than one

JobStateReason

objects which pertain to the Print
Job's status. The printer adds a

JobStateReason

object
to the Print Job's JobStateReasons attribute when the corresponding condition
becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding
condition becomes false, regardless of whether the Print Job's overall

JobState

also changed.

Class

JobStateReasons

inherits its implementation from class

java.util.HashSet

. Unlike most printing attributes
which are immutable once constructed, class

JobStateReasons

is
designed to be mutable; you can add

JobStateReason

objects to an existing

JobStateReasons

object and remove them again.
However, like class

java.util.HashSet

, class

JobStateReasons

is not multiple thread safe. If a

JobStateReasons

object will be used by multiple threads, be sure to
synchronize its operations (e.g., using a synchronized set view obtained
from class

java.util.Collections

).

IPP Compatibility:

The string value returned by each individual

JobStateReason

object's

toString()

method
gives the IPP keyword value. The category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Iterable

<

JobStateReason

>

,

Collection

<

JobStateReason

>

,

Set

<

JobStateReason

>

,

Attribute

,

PrintJobAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobStateReasons()

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

---

#### public JobStateReasons​(int initialCapacity)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

**Parameters:**
- initialCapacity

- initial capacity

**Throws:**
- IllegalArgumentException

- if the initial capacity is negative

---

#### public JobStateReasons​(int initialCapacity,
float loadFactor)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

**Parameters:**
- initialCapacity

- initial capacity
- loadFactor

- load factor

**Throws:**
- IllegalArgumentException

- if the initial capacity is negative

---

#### public JobStateReasons​(
Collection
<
JobStateReason
> collection)

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.
The underlying hash set's initial capacity and load factor are as
specified in the superclass constructor

HashSet(Collection)

.

**Parameters:**
- collection

- collection to copy

**Throws:**
- NullPointerException

- if

collection

is

null

or if
any element in

collection

is

null
- ClassCastException

- if any element in

collection

is not an
instance of class

JobStateReason

---

### Method Details

#### public boolean add​(
JobStateReason
o)

Adds the specified element to this job state reasons attribute if it is
not already present. The element to be added must be an instance of class

JobStateReason

. If this job state reasons
attribute already contains the specified element, the call leaves this
job state reasons attribute unchanged and returns

false

.

**Specified by:**
- add

in interface

Collection

<

JobStateReason

>
- add

in interface

Set

<

JobStateReason

>

**Overrides:**
- add

in class

HashSet

<

JobStateReason

>

**Parameters:**
- o

- element to be added to this job state reasons attribute

**Returns:**
- true

if this job state reasons attribute did not already
contain the specified element

**Throws:**
- NullPointerException

- if the specified element is

null
- ClassCastException

- if the specified element is not an instance of
class

JobStateReason

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

JobStateReasons

, the category is class
JobStateReasons itself.

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

For class JobStateReasons, the category name is

"job-state-reasons"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobStateReasons

java.lang.Object

- java.util.AbstractCollection

<E>
- - java.util.AbstractSet

<E>
- - java.util.HashSet

<

JobStateReason

>
- - javax.print.attribute.standard.JobStateReasons

java.util.AbstractCollection

<E>

- java.util.AbstractSet

<E>
- - java.util.HashSet

<

JobStateReason

>
- - javax.print.attribute.standard.JobStateReasons

java.util.AbstractSet

<E>

- java.util.HashSet

<

JobStateReason

>
- - javax.print.attribute.standard.JobStateReasons

java.util.HashSet

<

JobStateReason

>

- javax.print.attribute.standard.JobStateReasons

javax.print.attribute.standard.JobStateReasons

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Iterable

<

JobStateReason

>

,

Collection

<

JobStateReason

>

,

Set

<

JobStateReason

>

,

Attribute

,

PrintJobAttribute

```java
public final class
JobStateReasons

extends
HashSet
<
JobStateReason
>
implements
PrintJobAttribute
```

Class

JobStateReasons

is a printing attribute class, a set of
enumeration values, that provides additional information about the job's
current state, i.e., information that augments the value of the job's

JobState

attribute.

Instances of

JobStateReason

do not appear in a Print
Job's attribute set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more than one

JobStateReason

objects which pertain to the Print
Job's status. The printer adds a

JobStateReason

object
to the Print Job's JobStateReasons attribute when the corresponding condition
becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding
condition becomes false, regardless of whether the Print Job's overall

JobState

also changed.

Class

JobStateReasons

inherits its implementation from class

java.util.HashSet

. Unlike most printing attributes
which are immutable once constructed, class

JobStateReasons

is
designed to be mutable; you can add

JobStateReason

objects to an existing

JobStateReasons

object and remove them again.
However, like class

java.util.HashSet

, class

JobStateReasons

is not multiple thread safe. If a

JobStateReasons

object will be used by multiple threads, be sure to
synchronize its operations (e.g., using a synchronized set view obtained
from class

java.util.Collections

).

IPP Compatibility:

The string value returned by each individual

JobStateReason

object's

toString()

method
gives the IPP keyword value. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

JobStateReasons

extends

HashSet

<

JobStateReason

>
implements

PrintJobAttribute

Class

JobStateReasons

is a printing attribute class, a set of
enumeration values, that provides additional information about the job's
current state, i.e., information that augments the value of the job's

JobState

attribute.

Instances of

JobStateReason

do not appear in a Print
Job's attribute set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more than one

JobStateReason

objects which pertain to the Print
Job's status. The printer adds a

JobStateReason

object
to the Print Job's JobStateReasons attribute when the corresponding condition
becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding
condition becomes false, regardless of whether the Print Job's overall

JobState

also changed.

Class

JobStateReasons

inherits its implementation from class

java.util.HashSet

. Unlike most printing attributes
which are immutable once constructed, class

JobStateReasons

is
designed to be mutable; you can add

JobStateReason

objects to an existing

JobStateReasons

object and remove them again.
However, like class

java.util.HashSet

, class

JobStateReasons

is not multiple thread safe. If a

JobStateReasons

object will be used by multiple threads, be sure to
synchronize its operations (e.g., using a synchronized set view obtained
from class

java.util.Collections

).

IPP Compatibility:

The string value returned by each individual

JobStateReason

object's

toString()

method
gives the IPP keyword value. The category name returned by

getName()

gives the IPP attribute name.

Instances of

JobStateReason

do not appear in a Print
Job's attribute set directly. Rather, a

JobStateReasons

attribute
appears in the Print Job's attribute set. The

JobStateReasons

attribute contains zero, one, or more than one

JobStateReason

objects which pertain to the Print
Job's status. The printer adds a

JobStateReason

object
to the Print Job's JobStateReasons attribute when the corresponding condition
becomes true of the Print Job, and the printer removes the

JobStateReason

object again when the corresponding
condition becomes false, regardless of whether the Print Job's overall

JobState

also changed.

Class

JobStateReasons

inherits its implementation from class

java.util.HashSet

. Unlike most printing attributes
which are immutable once constructed, class

JobStateReasons

is
designed to be mutable; you can add

JobStateReason

objects to an existing

JobStateReasons

object and remove them again.
However, like class

java.util.HashSet

, class

JobStateReasons

is not multiple thread safe. If a

JobStateReasons

object will be used by multiple threads, be sure to
synchronize its operations (e.g., using a synchronized set view obtained
from class

java.util.Collections

).

IPP Compatibility:

The string value returned by each individual

JobStateReason

object's

toString()

method
gives the IPP keyword value. The category name returned by

getName()

gives the IPP attribute name.

Class

JobStateReasons

inherits its implementation from class

java.util.HashSet

. Unlike most printing attributes
which are immutable once constructed, class

JobStateReasons

is
designed to be mutable; you can add

JobStateReason

objects to an existing

JobStateReasons

object and remove them again.
However, like class

java.util.HashSet

, class

JobStateReasons

is not multiple thread safe. If a

JobStateReasons

object will be used by multiple threads, be sure to
synchronize its operations (e.g., using a synchronized set view obtained
from class

java.util.Collections

).

IPP Compatibility:

The string value returned by each individual

JobStateReason

object's

toString()

method
gives the IPP keyword value. The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The string value returned by each individual

JobStateReason

object's

toString()

method
gives the IPP keyword value. The category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JobStateReasons

()

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

JobStateReasons

​(int initialCapacity)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

JobStateReasons

​(int initialCapacity,
float loadFactor)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

JobStateReasons

​(

Collection

<

JobStateReason

> collection)

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.

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

JobStateReason

o)

Adds the specified element to this job state reasons attribute if it is
not already present.

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

- Methods declared in class java.util.

HashSet

clear

,

clone

,

contains

,

isEmpty

,

iterator

,

remove

,

size

,

spliterator

- Methods declared in class java.util.

AbstractSet

equals

,

hashCode

,

removeAll

- Methods declared in class java.util.

AbstractCollection

addAll

,

containsAll

,

retainAll

,

toArray

,

toArray

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

addAll

,

containsAll

,

equals

,

hashCode

,

removeAll

,

retainAll

,

toArray

,

toArray

Constructor Summary

Constructors

Constructor

Description

JobStateReasons

()

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

JobStateReasons

​(int initialCapacity)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

JobStateReasons

​(int initialCapacity,
float loadFactor)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

JobStateReasons

​(

Collection

<

JobStateReason

> collection)

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.

---

#### Constructor Summary

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.

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

JobStateReason

o)

Adds the specified element to this job state reasons attribute if it is
not already present.

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

- Methods declared in class java.util.

HashSet

clear

,

clone

,

contains

,

isEmpty

,

iterator

,

remove

,

size

,

spliterator

- Methods declared in class java.util.

AbstractSet

equals

,

hashCode

,

removeAll

- Methods declared in class java.util.

AbstractCollection

addAll

,

containsAll

,

retainAll

,

toArray

,

toArray

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

addAll

,

containsAll

,

equals

,

hashCode

,

removeAll

,

retainAll

,

toArray

,

toArray

---

#### Method Summary

Adds the specified element to this job state reasons attribute if it is
not already present.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class java.util.

HashSet

clear

,

clone

,

contains

,

isEmpty

,

iterator

,

remove

,

size

,

spliterator

---

#### Methods declared in class java.util. HashSet

Methods declared in class java.util.

AbstractSet

equals

,

hashCode

,

removeAll

---

#### Methods declared in class java.util. AbstractSet

Methods declared in class java.util.

AbstractCollection

addAll

,

containsAll

,

retainAll

,

toArray

,

toArray

,

toString

---

#### Methods declared in class java.util. AbstractCollection

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

addAll

,

containsAll

,

equals

,

hashCode

,

removeAll

,

retainAll

,

toArray

,

toArray

---

#### Methods declared in interface java.util. Set

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JobStateReasons

```java
public JobStateReasons()
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

- JobStateReasons

```java
public JobStateReasons​(int initialCapacity)
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

**Parameters:** initialCapacity

- initial capacity
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- JobStateReasons

```java
public JobStateReasons​(int initialCapacity,
float loadFactor)
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

**Parameters:** initialCapacity

- initial capacity
**Parameters:** loadFactor

- load factor
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- JobStateReasons

```java
public JobStateReasons​(
Collection
<
JobStateReason
> collection)
```

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.
The underlying hash set's initial capacity and load factor are as
specified in the superclass constructor

HashSet(Collection)

.

**Parameters:** collection

- collection to copy
**Throws:** NullPointerException

- if

collection

is

null

or if
any element in

collection

is

null
**Throws:** ClassCastException

- if any element in

collection

is not an
instance of class

JobStateReason

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public boolean add​(
JobStateReason
o)
```

Adds the specified element to this job state reasons attribute if it is
not already present. The element to be added must be an instance of class

JobStateReason

. If this job state reasons
attribute already contains the specified element, the call leaves this
job state reasons attribute unchanged and returns

false

.

**Specified by:** add

in interface

Collection

<

JobStateReason

>
**Specified by:** add

in interface

Set

<

JobStateReason

>
**Overrides:** add

in class

HashSet

<

JobStateReason

>
**Parameters:** o

- element to be added to this job state reasons attribute
**Returns:** true

if this job state reasons attribute did not already
contain the specified element
**Throws:** NullPointerException

- if the specified element is

null
**Throws:** ClassCastException

- if the specified element is not an instance of
class

JobStateReason
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

JobStateReasons

, the category is class
JobStateReasons itself.

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

For class JobStateReasons, the category name is

"job-state-reasons"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobStateReasons

```java
public JobStateReasons()
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

- JobStateReasons

```java
public JobStateReasons​(int initialCapacity)
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

**Parameters:** initialCapacity

- initial capacity
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- JobStateReasons

```java
public JobStateReasons​(int initialCapacity,
float loadFactor)
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

**Parameters:** initialCapacity

- initial capacity
**Parameters:** loadFactor

- load factor
**Throws:** IllegalArgumentException

- if the initial capacity is negative

- JobStateReasons

```java
public JobStateReasons​(
Collection
<
JobStateReason
> collection)
```

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.
The underlying hash set's initial capacity and load factor are as
specified in the superclass constructor

HashSet(Collection)

.

**Parameters:** collection

- collection to copy
**Throws:** NullPointerException

- if

collection

is

null

or if
any element in

collection

is

null
**Throws:** ClassCastException

- if any element in

collection

is not an
instance of class

JobStateReason

---

#### Constructor Detail

JobStateReasons

```java
public JobStateReasons()
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

---

#### JobStateReasons

public JobStateReasons()

Construct a new, empty job state reasons attribute; the underlying hash
set has the default initial capacity and load factor.

JobStateReasons

```java
public JobStateReasons​(int initialCapacity)
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

**Parameters:** initialCapacity

- initial capacity
**Throws:** IllegalArgumentException

- if the initial capacity is negative

---

#### JobStateReasons

public JobStateReasons​(int initialCapacity)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and the default load factor.

JobStateReasons

```java
public JobStateReasons​(int initialCapacity,
float loadFactor)
```

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

**Parameters:** initialCapacity

- initial capacity
**Parameters:** loadFactor

- load factor
**Throws:** IllegalArgumentException

- if the initial capacity is negative

---

#### JobStateReasons

public JobStateReasons​(int initialCapacity,
float loadFactor)

Construct a new, empty job state reasons attribute; the underlying hash
set has the given initial capacity and load factor.

JobStateReasons

```java
public JobStateReasons​(
Collection
<
JobStateReason
> collection)
```

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.
The underlying hash set's initial capacity and load factor are as
specified in the superclass constructor

HashSet(Collection)

.

**Parameters:** collection

- collection to copy
**Throws:** NullPointerException

- if

collection

is

null

or if
any element in

collection

is

null
**Throws:** ClassCastException

- if any element in

collection

is not an
instance of class

JobStateReason

---

#### JobStateReasons

public JobStateReasons​(

Collection

<

JobStateReason

> collection)

Construct a new job state reasons attribute that contains the same

JobStateReason

objects as the given collection.
The underlying hash set's initial capacity and load factor are as
specified in the superclass constructor

HashSet(Collection)

.

Method Detail

- add

```java
public boolean add​(
JobStateReason
o)
```

Adds the specified element to this job state reasons attribute if it is
not already present. The element to be added must be an instance of class

JobStateReason

. If this job state reasons
attribute already contains the specified element, the call leaves this
job state reasons attribute unchanged and returns

false

.

**Specified by:** add

in interface

Collection

<

JobStateReason

>
**Specified by:** add

in interface

Set

<

JobStateReason

>
**Overrides:** add

in class

HashSet

<

JobStateReason

>
**Parameters:** o

- element to be added to this job state reasons attribute
**Returns:** true

if this job state reasons attribute did not already
contain the specified element
**Throws:** NullPointerException

- if the specified element is

null
**Throws:** ClassCastException

- if the specified element is not an instance of
class

JobStateReason
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

JobStateReasons

, the category is class
JobStateReasons itself.

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

For class JobStateReasons, the category name is

"job-state-reasons"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

add

```java
public boolean add​(
JobStateReason
o)
```

Adds the specified element to this job state reasons attribute if it is
not already present. The element to be added must be an instance of class

JobStateReason

. If this job state reasons
attribute already contains the specified element, the call leaves this
job state reasons attribute unchanged and returns

false

.

**Specified by:** add

in interface

Collection

<

JobStateReason

>
**Specified by:** add

in interface

Set

<

JobStateReason

>
**Overrides:** add

in class

HashSet

<

JobStateReason

>
**Parameters:** o

- element to be added to this job state reasons attribute
**Returns:** true

if this job state reasons attribute did not already
contain the specified element
**Throws:** NullPointerException

- if the specified element is

null
**Throws:** ClassCastException

- if the specified element is not an instance of
class

JobStateReason
**Since:** 1.5

---

#### add

public boolean add​(

JobStateReason

o)

Adds the specified element to this job state reasons attribute if it is
not already present. The element to be added must be an instance of class

JobStateReason

. If this job state reasons
attribute already contains the specified element, the call leaves this
job state reasons attribute unchanged and returns

false

.

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

JobStateReasons

, the category is class
JobStateReasons itself.

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

JobStateReasons

, the category is class
JobStateReasons itself.

For class

JobStateReasons

, the category is class
JobStateReasons itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class JobStateReasons, the category name is

"job-state-reasons"

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

For class JobStateReasons, the category name is

"job-state-reasons"

.

For class JobStateReasons, the category name is

"job-state-reasons"

.

---

