# Class ValueDescriptor

**Source:** `jdk.jfr\jdk\jfr\ValueDescriptor.html`

### Class Description

```java
public final class
ValueDescriptor

extends
Object
```

Describes the event fields and annotation elements.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

#### public ValueDescriptor​(
Class
<?> type,

String
name)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:**
- type

- the type, not

null
- name

- the name, not

null

**Throws:**
- SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

---

#### public ValueDescriptor​(
Class
<?> type,

String
name,

List
<
AnnotationElement
> annotations)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:**
- type

- the type, not

null
- name

- the name, not

null
- annotations

- the annotations on the value descriptors, not

null

**Throws:**
- SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

---

### Method Details

#### public
String
getLabel()

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

**Returns:**
- a human-readable name, or

null

if doesn't exist

---

#### public
String
getName()

Returns the name of the value (for example,

"maxThroughput"

).

**Returns:**
- the name, not

null

---

#### public
String
getDescription()

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

**Returns:**
- the description, or

null

if doesn't exist

---

#### public
String
getContentType()

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

For example, if the value descriptor's type is

float

and the
event value is

0.5f

, a content type of

"jdk.jfr.Percentage"

hints to a client that the value is a
percentage and that it should be rendered as

"50%"

.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

**Returns:**
- the content type, or

null

if doesn't exist

**See Also:**
- ContentType

---

#### public
String
getTypeName()

Returns the fully qualified class name of the type that is associated with
this value descriptor.

**Returns:**
- the type name, not

null

**See Also:**
- getTypeId()

---

#### public long getTypeId()

Returns a unique ID for the type in the Java virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:**
- the type ID, not negative

---

#### public boolean isArray()

Returns if this value descriptor is an array type.

**Returns:**
- true

if it is an array type,

false

otherwise

---

#### public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

**Parameters:**
- annotationType

- the Class object that corresponds to the annotation
type, not

null

**Returns:**
- this element's annotation for the specified annotation type if
directly present, else

null

**Type Parameters:**
- A

- the type of the annotation to query for and return if present

---

#### public
List
<
AnnotationElement
> getAnnotationElements()

Returns an immutable list of annotation elements for this value
descriptor.

**Returns:**
- a list of annotations, not

null

---

#### public
List
<
ValueDescriptor
> getFields()

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

**Returns:**
- a list of value descriptors, not

null

---

### Additional Sections

#### Class ValueDescriptor

java.lang.Object

- jdk.jfr.ValueDescriptor

jdk.jfr.ValueDescriptor

```java
public final class
ValueDescriptor

extends
Object
```

Describes the event fields and annotation elements.

**Since:** 9

public final class

ValueDescriptor

extends

Object

Describes the event fields and annotation elements.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ValueDescriptor

​(

Class

<?> type,

String

name)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

ValueDescriptor

​(

Class

<?> type,

String

name,

List

<

AnnotationElement

> annotations)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

<A extends

Annotation

>

A

getAnnotation

​(

Class

<A> annotationType)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

List

<

AnnotationElement

>

getAnnotationElements

()

Returns an immutable list of annotation elements for this value
descriptor.

String

getContentType

()

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

String

getDescription

()

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

List

<

ValueDescriptor

>

getFields

()

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

String

getLabel

()

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

String

getName

()

Returns the name of the value (for example,

"maxThroughput"

).

long

getTypeId

()

Returns a unique ID for the type in the Java virtual Machine (JVM).

String

getTypeName

()

Returns the fully qualified class name of the type that is associated with
this value descriptor.

boolean

isArray

()

Returns if this value descriptor is an array type.

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

ValueDescriptor

​(

Class

<?> type,

String

name)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

ValueDescriptor

​(

Class

<?> type,

String

name,

List

<

AnnotationElement

> annotations)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

---

#### Constructor Summary

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

<A extends

Annotation

>

A

getAnnotation

​(

Class

<A> annotationType)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

List

<

AnnotationElement

>

getAnnotationElements

()

Returns an immutable list of annotation elements for this value
descriptor.

String

getContentType

()

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

String

getDescription

()

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

List

<

ValueDescriptor

>

getFields

()

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

String

getLabel

()

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

String

getName

()

Returns the name of the value (for example,

"maxThroughput"

).

long

getTypeId

()

Returns a unique ID for the type in the Java virtual Machine (JVM).

String

getTypeName

()

Returns the fully qualified class name of the type that is associated with
this value descriptor.

boolean

isArray

()

Returns if this value descriptor is an array type.

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

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

Returns an immutable list of annotation elements for this value
descriptor.

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

Returns the name of the value (for example,

"maxThroughput"

).

Returns a unique ID for the type in the Java virtual Machine (JVM).

Returns the fully qualified class name of the type that is associated with
this value descriptor.

Returns if this value descriptor is an array type.

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

- ValueDescriptor

```java
public ValueDescriptor​(
Class
<?> type,

String
name)
```

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:** type

- the type, not

null
**Parameters:** name

- the name, not

null
**Throws:** SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

- ValueDescriptor

```java
public ValueDescriptor​(
Class
<?> type,

String
name,

List
<
AnnotationElement
> annotations)
```

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:** type

- the type, not

null
**Parameters:** name

- the name, not

null
**Parameters:** annotations

- the annotations on the value descriptors, not

null
**Throws:** SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

============ METHOD DETAIL ==========

- Method Detail

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

**Returns:** a human-readable name, or

null

if doesn't exist

- getName

```java
public
String
getName()
```

Returns the name of the value (for example,

"maxThroughput"

).

**Returns:** the name, not

null

- getDescription

```java
public
String
getDescription()
```

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

**Returns:** the description, or

null

if doesn't exist

- getContentType

```java
public
String
getContentType()
```

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

For example, if the value descriptor's type is

float

and the
event value is

0.5f

, a content type of

"jdk.jfr.Percentage"

hints to a client that the value is a
percentage and that it should be rendered as

"50%"

.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

**Returns:** the content type, or

null

if doesn't exist
**See Also:** ContentType

- getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified class name of the type that is associated with
this value descriptor.

**Returns:** the type name, not

null
**See Also:** getTypeId()

- getTypeId

```java
public long getTypeId()
```

Returns a unique ID for the type in the Java virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:** the type ID, not negative

- isArray

```java
public boolean isArray()
```

Returns if this value descriptor is an array type.

**Returns:** true

if it is an array type,

false

otherwise

- getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

**Type Parameters:** A

- the type of the annotation to query for and return if present
**Parameters:** annotationType

- the Class object that corresponds to the annotation
type, not

null
**Returns:** this element's annotation for the specified annotation type if
directly present, else

null

- getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this value
descriptor.

**Returns:** a list of annotations, not

null

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

**Returns:** a list of value descriptors, not

null

Constructor Detail

- ValueDescriptor

```java
public ValueDescriptor​(
Class
<?> type,

String
name)
```

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:** type

- the type, not

null
**Parameters:** name

- the name, not

null
**Throws:** SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

- ValueDescriptor

```java
public ValueDescriptor​(
Class
<?> type,

String
name,

List
<
AnnotationElement
> annotations)
```

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:** type

- the type, not

null
**Parameters:** name

- the name, not

null
**Parameters:** annotations

- the annotations on the value descriptors, not

null
**Throws:** SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

---

#### Constructor Detail

ValueDescriptor

```java
public ValueDescriptor​(
Class
<?> type,

String
name)
```

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:** type

- the type, not

null
**Parameters:** name

- the name, not

null
**Throws:** SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

---

#### ValueDescriptor

public ValueDescriptor​(

Class

<?> type,

String

name)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

ValueDescriptor

```java
public ValueDescriptor​(
Class
<?> type,

String
name,

List
<
AnnotationElement
> annotations)
```

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

**Parameters:** type

- the type, not

null
**Parameters:** name

- the name, not

null
**Parameters:** annotations

- the annotations on the value descriptors, not

null
**Throws:** SecurityException

- if a security manager is present and the caller
doesn't have

FlightRecorderPermission("registerEvent")

---

#### ValueDescriptor

public ValueDescriptor​(

Class

<?> type,

String

name,

List

<

AnnotationElement

> annotations)

Constructs a value descriptor, useful for dynamically creating event types and
annotations.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

The following types are supported:

- byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

byte.class

short.class

int.class

long.class

char.class

float.class

double.class

boolean.class

String.class

Class.class

Thread.class

The name must be a valid Java identifier (for example,

"maxThroughput"

). See 3.8
Java Language Specification for more information.

Method Detail

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

**Returns:** a human-readable name, or

null

if doesn't exist

- getName

```java
public
String
getName()
```

Returns the name of the value (for example,

"maxThroughput"

).

**Returns:** the name, not

null

- getDescription

```java
public
String
getDescription()
```

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

**Returns:** the description, or

null

if doesn't exist

- getContentType

```java
public
String
getContentType()
```

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

For example, if the value descriptor's type is

float

and the
event value is

0.5f

, a content type of

"jdk.jfr.Percentage"

hints to a client that the value is a
percentage and that it should be rendered as

"50%"

.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

**Returns:** the content type, or

null

if doesn't exist
**See Also:** ContentType

- getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified class name of the type that is associated with
this value descriptor.

**Returns:** the type name, not

null
**See Also:** getTypeId()

- getTypeId

```java
public long getTypeId()
```

Returns a unique ID for the type in the Java virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:** the type ID, not negative

- isArray

```java
public boolean isArray()
```

Returns if this value descriptor is an array type.

**Returns:** true

if it is an array type,

false

otherwise

- getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

**Type Parameters:** A

- the type of the annotation to query for and return if present
**Parameters:** annotationType

- the Class object that corresponds to the annotation
type, not

null
**Returns:** this element's annotation for the specified annotation type if
directly present, else

null

- getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this value
descriptor.

**Returns:** a list of annotations, not

null

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

**Returns:** a list of value descriptors, not

null

---

#### Method Detail

getLabel

```java
public
String
getLabel()
```

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

**Returns:** a human-readable name, or

null

if doesn't exist

---

#### getLabel

public

String

getLabel()

Returns a human-readable name that describes the value (for example,

"Maximum Throughput"

).

getName

```java
public
String
getName()
```

Returns the name of the value (for example,

"maxThroughput"

).

**Returns:** the name, not

null

---

#### getName

public

String

getName()

Returns the name of the value (for example,

"maxThroughput"

).

getDescription

```java
public
String
getDescription()
```

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

**Returns:** the description, or

null

if doesn't exist

---

#### getDescription

public

String

getDescription()

Returns a sentence describing the value (for example,

"Maximum
throughput in the transaction system. Value is reset after each new
batch."

).

getContentType

```java
public
String
getContentType()
```

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

For example, if the value descriptor's type is

float

and the
event value is

0.5f

, a content type of

"jdk.jfr.Percentage"

hints to a client that the value is a
percentage and that it should be rendered as

"50%"

.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

**Returns:** the content type, or

null

if doesn't exist
**See Also:** ContentType

---

#### getContentType

public

String

getContentType()

Returns a textual identifier that specifies how a value represented by
this

ValueDescriptor

is interpreted or formatted.

For example, if the value descriptor's type is

float

and the
event value is

0.5f

, a content type of

"jdk.jfr.Percentage"

hints to a client that the value is a
percentage and that it should be rendered as

"50%"

.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

For example, if the value descriptor's type is

float

and the
event value is

0.5f

, a content type of

"jdk.jfr.Percentage"

hints to a client that the value is a
percentage and that it should be rendered as

"50%"

.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

jdk.jfr.Percentage

jdk.jfr.Timespan

jdk.jfr.Timestamp

jdk.jfr.Frequency

jdk.jfr.Flag

jdk.jfr.MemoryAddress

jdk.jfr.DataAmount

jdk.jfr.NetworkAddress

User-defined content types can be created by using the

ContentType

class.

getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified class name of the type that is associated with
this value descriptor.

**Returns:** the type name, not

null
**See Also:** getTypeId()

---

#### getTypeName

public

String

getTypeName()

Returns the fully qualified class name of the type that is associated with
this value descriptor.

getTypeId

```java
public long getTypeId()
```

Returns a unique ID for the type in the Java virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:** the type ID, not negative

---

#### getTypeId

public long getTypeId()

Returns a unique ID for the type in the Java virtual Machine (JVM).

The ID might not be the same between JVM instances.

isArray

```java
public boolean isArray()
```

Returns if this value descriptor is an array type.

**Returns:** true

if it is an array type,

false

otherwise

---

#### isArray

public boolean isArray()

Returns if this value descriptor is an array type.

getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

**Type Parameters:** A

- the type of the annotation to query for and return if present
**Parameters:** annotationType

- the Class object that corresponds to the annotation
type, not

null
**Returns:** this element's annotation for the specified annotation type if
directly present, else

null

---

#### getAnnotation

public <A extends

Annotation

> A getAnnotation​(

Class

<A> annotationType)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present for this value descriptor,

null

otherwise.

getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this value
descriptor.

**Returns:** a list of annotations, not

null

---

#### getAnnotationElements

public

List

<

AnnotationElement

> getAnnotationElements()

Returns an immutable list of annotation elements for this value
descriptor.

getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

**Returns:** a list of value descriptors, not

null

---

#### getFields

public

List

<

ValueDescriptor

> getFields()

Returns an immutable list of value descriptors if the type is complex,
else an empty list.

---

