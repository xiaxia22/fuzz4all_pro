# Class EventTypeInfo

**Source:** `jdk.management.jfr\jdk\management\jfr\EventTypeInfo.html`

### Class Description

```java
public final class
EventTypeInfo

extends
Object
```

Management representation of an

EventType

.

**Since:** 9
**See Also:** EventType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getLabel()

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

**Returns:**
- the label, or

null

if a label is not set

**See Also:**
- EventType.getLabel()

---

#### public
List
<
String
> getCategoryNames()

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

**Returns:**
- an immutable list of category names, or a list with the name

"Uncategorized"

if no category has been set

**See Also:**
- EventType.getCategoryNames()

,

Category

---

#### public long getId()

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

**Returns:**
- the ID

**See Also:**
- EventType.getId()

---

#### public
String
getName()

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

**Returns:**
- the name, not

null

**See Also:**
- EventType.getName()

---

#### public
String
getDescription()

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

**Returns:**
- the description, or

null

if no description exists

**See Also:**
- EventType.getDescription()

---

#### public
List
<
SettingDescriptorInfo
> getSettingDescriptors()

Returns settings for the event type associated with this

EventTypeInfo

.

**Returns:**
- the settings, not

null

**See Also:**
- EventType.getSettingDescriptors()

---

#### public
String
toString()

Returns a description of this

EventTypeInfo

.

**Overrides:**
- toString

in class

Object

**Returns:**
- description, not

null

---

#### public static
EventTypeInfo
from​(
CompositeData
cd)

Returns an

EventType

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

id

Long

name

String

label

String

description

String

category

ArrayType(1, SimpleType.STRING)

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:**
- cd

-

CompositeData

representing the

EventTypeInfo

to
return

**Returns:**
- an

EventTypeInfo

, or

null

if

cd

is

null

**Throws:**
- IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

---

### Additional Sections

#### Class EventTypeInfo

java.lang.Object

- jdk.management.jfr.EventTypeInfo

jdk.management.jfr.EventTypeInfo

```java
public final class
EventTypeInfo

extends
Object
```

Management representation of an

EventType

.

**Since:** 9
**See Also:** EventType

public final class

EventTypeInfo

extends

Object

Management representation of an

EventType

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

EventTypeInfo

from

​(

CompositeData

cd)

Returns an

EventType

represented by the specified

CompositeData

List

<

String

>

getCategoryNames

()

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

String

getDescription

()

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

long

getId

()

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

String

getLabel

()

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

String

getName

()

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

List

<

SettingDescriptorInfo

>

getSettingDescriptors

()

Returns settings for the event type associated with this

EventTypeInfo

.

String

toString

()

Returns a description of this

EventTypeInfo

.

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

EventTypeInfo

from

​(

CompositeData

cd)

Returns an

EventType

represented by the specified

CompositeData

List

<

String

>

getCategoryNames

()

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

String

getDescription

()

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

long

getId

()

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

String

getLabel

()

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

String

getName

()

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

List

<

SettingDescriptorInfo

>

getSettingDescriptors

()

Returns settings for the event type associated with this

EventTypeInfo

.

String

toString

()

Returns a description of this

EventTypeInfo

.

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

---

#### Method Summary

Returns an

EventType

represented by the specified

CompositeData

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

Returns settings for the event type associated with this

EventTypeInfo

.

Returns a description of this

EventTypeInfo

.

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

============ METHOD DETAIL ==========

- Method Detail

- getLabel

```java
public
String
getLabel()
```

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

**Returns:** the label, or

null

if a label is not set
**See Also:** EventType.getLabel()

- getCategoryNames

```java
public
List
<
String
> getCategoryNames()
```

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

**Returns:** an immutable list of category names, or a list with the name

"Uncategorized"

if no category has been set
**See Also:** EventType.getCategoryNames()

,

Category

- getId

```java
public long getId()
```

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

**Returns:** the ID
**See Also:** EventType.getId()

- getName

```java
public
String
getName()
```

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

**Returns:** the name, not

null
**See Also:** EventType.getName()

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

**Returns:** the description, or

null

if no description exists
**See Also:** EventType.getDescription()

- getSettingDescriptors

```java
public
List
<
SettingDescriptorInfo
> getSettingDescriptors()
```

Returns settings for the event type associated with this

EventTypeInfo

.

**Returns:** the settings, not

null
**See Also:** EventType.getSettingDescriptors()

- toString

```java
public
String
toString()
```

Returns a description of this

EventTypeInfo

.

**Overrides:** toString

in class

Object
**Returns:** description, not

null

- from

```java
public static
EventTypeInfo
from​(
CompositeData
cd)
```

Returns an

EventType

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

id

Long

name

String

label

String

description

String

category

ArrayType(1, SimpleType.STRING)

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:** cd

-

CompositeData

representing the

EventTypeInfo

to
return
**Returns:** an

EventTypeInfo

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

Method Detail

- getLabel

```java
public
String
getLabel()
```

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

**Returns:** the label, or

null

if a label is not set
**See Also:** EventType.getLabel()

- getCategoryNames

```java
public
List
<
String
> getCategoryNames()
```

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

**Returns:** an immutable list of category names, or a list with the name

"Uncategorized"

if no category has been set
**See Also:** EventType.getCategoryNames()

,

Category

- getId

```java
public long getId()
```

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

**Returns:** the ID
**See Also:** EventType.getId()

- getName

```java
public
String
getName()
```

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

**Returns:** the name, not

null
**See Also:** EventType.getName()

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

**Returns:** the description, or

null

if no description exists
**See Also:** EventType.getDescription()

- getSettingDescriptors

```java
public
List
<
SettingDescriptorInfo
> getSettingDescriptors()
```

Returns settings for the event type associated with this

EventTypeInfo

.

**Returns:** the settings, not

null
**See Also:** EventType.getSettingDescriptors()

- toString

```java
public
String
toString()
```

Returns a description of this

EventTypeInfo

.

**Overrides:** toString

in class

Object
**Returns:** description, not

null

- from

```java
public static
EventTypeInfo
from​(
CompositeData
cd)
```

Returns an

EventType

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

id

Long

name

String

label

String

description

String

category

ArrayType(1, SimpleType.STRING)

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:** cd

-

CompositeData

representing the

EventTypeInfo

to
return
**Returns:** an

EventTypeInfo

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

---

#### Method Detail

getLabel

```java
public
String
getLabel()
```

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

**Returns:** the label, or

null

if a label is not set
**See Also:** EventType.getLabel()

---

#### getLabel

public

String

getLabel()

Returns the label, a human-readable name, associated with the event type
for this

EventTypeInfo

(for example,

"Garbage Collection"

).

getCategoryNames

```java
public
List
<
String
> getCategoryNames()
```

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

**Returns:** an immutable list of category names, or a list with the name

"Uncategorized"

if no category has been set
**See Also:** EventType.getCategoryNames()

,

Category

---

#### getCategoryNames

public

List

<

String

> getCategoryNames()

Returns the list of human-readable names that makes up the category for this

EventTypeInfo

(for example,

"Java Virtual Machine"

or

"Garbage Collector"

).

getId

```java
public long getId()
```

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

**Returns:** the ID
**See Also:** EventType.getId()

---

#### getId

public long getId()

Returns the unique ID for the event type associated with this

EventTypeInfo

, not guaranteed to be the same for different Java
Virtual Machines (JVMs) instances.

getName

```java
public
String
getName()
```

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

**Returns:** the name, not

null
**See Also:** EventType.getName()

---

#### getName

public

String

getName()

Returns the name for the event type associated with this

EventTypeInfo

(for example,

"jdk.GarbageCollection"

).

getDescription

```java
public
String
getDescription()
```

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

**Returns:** the description, or

null

if no description exists
**See Also:** EventType.getDescription()

---

#### getDescription

public

String

getDescription()

Returns a short sentence or two describing the event type associated with
this

EventTypeInfo

, for example

"Garbage collection performed by the JVM""

.

getSettingDescriptors

```java
public
List
<
SettingDescriptorInfo
> getSettingDescriptors()
```

Returns settings for the event type associated with this

EventTypeInfo

.

**Returns:** the settings, not

null
**See Also:** EventType.getSettingDescriptors()

---

#### getSettingDescriptors

public

List

<

SettingDescriptorInfo

> getSettingDescriptors()

Returns settings for the event type associated with this

EventTypeInfo

.

toString

```java
public
String
toString()
```

Returns a description of this

EventTypeInfo

.

**Overrides:** toString

in class

Object
**Returns:** description, not

null

---

#### toString

public

String

toString()

Returns a description of this

EventTypeInfo

.

from

```java
public static
EventTypeInfo
from​(
CompositeData
cd)
```

Returns an

EventType

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

id

Long

name

String

label

String

description

String

category

ArrayType(1, SimpleType.STRING)

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:** cd

-

CompositeData

representing the

EventTypeInfo

to
return
**Returns:** an

EventTypeInfo

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

EventTypeInfo

---

#### from

public static

EventTypeInfo

from​(

CompositeData

cd)

Returns an

EventType

represented by the specified

CompositeData

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

id

Long

name

String

label

String

description

String

category

ArrayType(1, SimpleType.STRING)

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

The supplied

CompositeData

must have the following item names and
item types to be valid.

The name and type the specified CompositeData must contain

Name

Type

id

Long

name

String

label

String

description

String

category

ArrayType(1, SimpleType.STRING)

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

---

