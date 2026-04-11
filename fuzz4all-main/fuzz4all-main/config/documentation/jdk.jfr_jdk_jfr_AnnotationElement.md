# Class AnnotationElement

**Source:** `jdk.jfr\jdk\jfr\AnnotationElement.html`

### Class Description

```java
public final class
AnnotationElement

extends
Object
```

Describes event metadata, such as labels, descriptions and units.

The following example shows how

AnnotationElement

can be used to dynamically define events.

```java
List<AnnotationElement> typeAnnotations = new ArrayList<>();
typeannotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld");
typeAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
typeAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));

List<AnnotationElement> fieldAnnotations = new ArrayList<>();
fieldAnnotations.add(new AnnotationElement(Label.class, "Message"));

List<ValueDescriptor> fields = new ArrayList<>();
fields.add(new ValueDescriptor(String.class, "message", fieldAnnotations));

EventFactory f = EventFactory.create(typeAnnotations, fields);
Event event = f.newEvent();
event.commit();
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

#### public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Map
<
String
,​
Object
> values)

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays and classes, are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:**
- annotationType

- interface extending

java.lang.annotation.Annotation

, not

null
- values

- a

Map

with keys that match method names of the specified
annotation interface

**Throws:**
- IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

---

#### public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Object
value)

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:**
- annotationType

- interface extending

java.lang.annotation.Annotation,

not

null
- value

- the value that matches the

value

method of the specified

annotationType

**Throws:**
- IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

---

#### public AnnotationElement​(
Class
<? extends
Annotation
> annotationType)

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

short

,

int

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:**
- annotationType

- interface extending java.lang.annotation.Annotation,
not

null

---

### Method Details

#### public
List
<
Object
> getValues()

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

**Returns:**
- list of values, not

null

---

#### public
List
<
ValueDescriptor
> getValueDescriptors()

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

**Returns:**
- the list of value descriptors for this

Annotation

, not

null

---

#### public
List
<
AnnotationElement
> getAnnotationElements()

Returns an immutable list of annotation elements for this

AnnotationElement

.

**Returns:**
- a list of meta annotation, not

null

---

#### public
String
getTypeName()

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

**Returns:**
- type name, not

null

---

#### public
Object
getValue​(
String
name)

Returns a value for this

AnnotationElement

.

**Parameters:**
- name

- the name of the method in the annotation interface, not

null

.

**Returns:**
- the annotation value, not

null

.

**Throws:**
- IllegalArgumentException

- if a method with the specified name does
not exist in the annotation

---

#### public boolean hasValue​(
String
name)

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

.

**Parameters:**
- name

- name of the method in the annotation interface to find, not

null

**Returns:**
- true

if method exists,

false

otherwise

---

#### public final <A> A getAnnotation​(
Class
<? extends
Annotation
> annotationType)

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

**Parameters:**
- annotationType

- the

Class object

corresponding to the annotation type,
not

null

**Returns:**
- this element's annotation for the specified annotation type if
it it exists, else

null

**Type Parameters:**
- A

- the type of the annotation to query for and return if it exists

---

#### public long getTypeId()

Returns the type ID for this

AnnotationElement

.

The ID is a unique identifier for the type in the Java Virtual Machine (JVM). The ID might not
be the same between JVM instances.

**Returns:**
- the type ID, not negative

---

### Additional Sections

#### Class AnnotationElement

java.lang.Object

- jdk.jfr.AnnotationElement

jdk.jfr.AnnotationElement

```java
public final class
AnnotationElement

extends
Object
```

Describes event metadata, such as labels, descriptions and units.

The following example shows how

AnnotationElement

can be used to dynamically define events.

```java
List<AnnotationElement> typeAnnotations = new ArrayList<>();
typeannotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld");
typeAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
typeAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));

List<AnnotationElement> fieldAnnotations = new ArrayList<>();
fieldAnnotations.add(new AnnotationElement(Label.class, "Message"));

List<ValueDescriptor> fields = new ArrayList<>();
fields.add(new ValueDescriptor(String.class, "message", fieldAnnotations));

EventFactory f = EventFactory.create(typeAnnotations, fields);
Event event = f.newEvent();
event.commit();
```

**Since:** 9

public final class

AnnotationElement

extends

Object

Describes event metadata, such as labels, descriptions and units.

The following example shows how

AnnotationElement

can be used to dynamically define events.

```java
List<AnnotationElement> typeAnnotations = new ArrayList<>();
typeannotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld");
typeAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
typeAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));

List<AnnotationElement> fieldAnnotations = new ArrayList<>();
fieldAnnotations.add(new AnnotationElement(Label.class, "Message"));

List<ValueDescriptor> fields = new ArrayList<>();
fields.add(new ValueDescriptor(String.class, "message", fieldAnnotations));

EventFactory f = EventFactory.create(typeAnnotations, fields);
Event event = f.newEvent();
event.commit();
```

The following example shows how

AnnotationElement

can be used to dynamically define events.

```java
List<AnnotationElement> typeAnnotations = new ArrayList<>();
typeannotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld");
typeAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
typeAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));

List<AnnotationElement> fieldAnnotations = new ArrayList<>();
fieldAnnotations.add(new AnnotationElement(Label.class, "Message"));

List<ValueDescriptor> fields = new ArrayList<>();
fields.add(new ValueDescriptor(String.class, "message", fieldAnnotations));

EventFactory f = EventFactory.create(typeAnnotations, fields);
Event event = f.newEvent();
event.commit();
```

List<AnnotationElement> typeAnnotations = new ArrayList<>();
typeannotations.add(new AnnotationElement(Name.class, "com.example.HelloWorld");
typeAnnotations.add(new AnnotationElement(Label.class, "Hello World"));
typeAnnotations.add(new AnnotationElement(Description.class, "Helps programmer getting started"));

List<AnnotationElement> fieldAnnotations = new ArrayList<>();
fieldAnnotations.add(new AnnotationElement(Label.class, "Message"));

List<ValueDescriptor> fields = new ArrayList<>();
fields.add(new ValueDescriptor(String.class, "message", fieldAnnotations));

EventFactory f = EventFactory.create(typeAnnotations, fields);
Event event = f.newEvent();
event.commit();

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AnnotationElement

​(

Class

<? extends

Annotation

> annotationType)

Creates an annotation element to use for dynamically defined events.

AnnotationElement

​(

Class

<? extends

Annotation

> annotationType,

Object

value)

Creates an annotation element to use for dynamically defined events.

AnnotationElement

​(

Class

<? extends

Annotation

> annotationType,

Map

<

String

,​

Object

> values)

Creates an annotation element to use for dynamically defined events.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

<A> A

getAnnotation

​(

Class

<? extends

Annotation

> annotationType)

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

List

<

AnnotationElement

>

getAnnotationElements

()

Returns an immutable list of annotation elements for this

AnnotationElement

.

long

getTypeId

()

Returns the type ID for this

AnnotationElement

.

String

getTypeName

()

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

Object

getValue

​(

String

name)

Returns a value for this

AnnotationElement

.

List

<

ValueDescriptor

>

getValueDescriptors

()

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

List

<

Object

>

getValues

()

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

boolean

hasValue

​(

String

name)

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

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

AnnotationElement

​(

Class

<? extends

Annotation

> annotationType)

Creates an annotation element to use for dynamically defined events.

AnnotationElement

​(

Class

<? extends

Annotation

> annotationType,

Object

value)

Creates an annotation element to use for dynamically defined events.

AnnotationElement

​(

Class

<? extends

Annotation

> annotationType,

Map

<

String

,​

Object

> values)

Creates an annotation element to use for dynamically defined events.

---

#### Constructor Summary

Creates an annotation element to use for dynamically defined events.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

<A> A

getAnnotation

​(

Class

<? extends

Annotation

> annotationType)

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

List

<

AnnotationElement

>

getAnnotationElements

()

Returns an immutable list of annotation elements for this

AnnotationElement

.

long

getTypeId

()

Returns the type ID for this

AnnotationElement

.

String

getTypeName

()

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

Object

getValue

​(

String

name)

Returns a value for this

AnnotationElement

.

List

<

ValueDescriptor

>

getValueDescriptors

()

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

List

<

Object

>

getValues

()

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

boolean

hasValue

​(

String

name)

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

Returns an immutable list of annotation elements for this

AnnotationElement

.

Returns the type ID for this

AnnotationElement

.

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

Returns a value for this

AnnotationElement

.

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

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

- AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Map
<
String
,​
Object
> values)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays and classes, are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending

java.lang.annotation.Annotation

, not

null
**Parameters:** values

- a

Map

with keys that match method names of the specified
annotation interface
**Throws:** IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

- AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Object
value)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending

java.lang.annotation.Annotation,

not

null
**Parameters:** value

- the value that matches the

value

method of the specified

annotationType
**Throws:** IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

- AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

short

,

int

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending java.lang.annotation.Annotation,
not

null

============ METHOD DETAIL ==========

- Method Detail

- getValues

```java
public
List
<
Object
> getValues()
```

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

**Returns:** list of values, not

null

- getValueDescriptors

```java
public
List
<
ValueDescriptor
> getValueDescriptors()
```

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

**Returns:** the list of value descriptors for this

Annotation

, not

null

- getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this

AnnotationElement

.

**Returns:** a list of meta annotation, not

null

- getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

**Returns:** type name, not

null

- getValue

```java
public
Object
getValue​(
String
name)
```

Returns a value for this

AnnotationElement

.

**Parameters:** name

- the name of the method in the annotation interface, not

null

.
**Returns:** the annotation value, not

null

.
**Throws:** IllegalArgumentException

- if a method with the specified name does
not exist in the annotation

- hasValue

```java
public boolean hasValue​(
String
name)
```

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

.

**Parameters:** name

- name of the method in the annotation interface to find, not

null
**Returns:** true

if method exists,

false

otherwise

- getAnnotation

```java
public final <A> A getAnnotation​(
Class
<? extends
Annotation
> annotationType)
```

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

**Type Parameters:** A

- the type of the annotation to query for and return if it exists
**Parameters:** annotationType

- the

Class object

corresponding to the annotation type,
not

null
**Returns:** this element's annotation for the specified annotation type if
it it exists, else

null

- getTypeId

```java
public long getTypeId()
```

Returns the type ID for this

AnnotationElement

.

The ID is a unique identifier for the type in the Java Virtual Machine (JVM). The ID might not
be the same between JVM instances.

**Returns:** the type ID, not negative

Constructor Detail

- AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Map
<
String
,​
Object
> values)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays and classes, are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending

java.lang.annotation.Annotation

, not

null
**Parameters:** values

- a

Map

with keys that match method names of the specified
annotation interface
**Throws:** IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

- AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Object
value)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending

java.lang.annotation.Annotation,

not

null
**Parameters:** value

- the value that matches the

value

method of the specified

annotationType
**Throws:** IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

- AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

short

,

int

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending java.lang.annotation.Annotation,
not

null

---

#### Constructor Detail

AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Map
<
String
,​
Object
> values)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays and classes, are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending

java.lang.annotation.Annotation

, not

null
**Parameters:** values

- a

Map

with keys that match method names of the specified
annotation interface
**Throws:** IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

---

#### AnnotationElement

public AnnotationElement​(

Class

<? extends

Annotation

> annotationType,

Map

<

String

,​

Object

> values)

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays and classes, are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays and classes, are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotation are recursively included.
However, both the

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

To statically define events, see

Event

class.

AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType,

Object
value)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending

java.lang.annotation.Annotation,

not

null
**Parameters:** value

- the value that matches the

value

method of the specified

annotationType
**Throws:** IllegalArgumentException

- if value/key is

null

, an unsupported
value type is used, or a value/key is used that doesn't match the
signatures in the

annotationType

---

#### AnnotationElement

public AnnotationElement​(

Class

<? extends

Annotation

> annotationType,

Object

value)

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

Supported value types are

byte

,

int

,

short

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

If

annotationType

has annotations (directly present, indirectly
present, or associated), then those annotations are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

To statically define events, see

Event

class.

AnnotationElement

```java
public AnnotationElement​(
Class
<? extends
Annotation
> annotationType)
```

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

short

,

int

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

**Parameters:** annotationType

- interface extending java.lang.annotation.Annotation,
not

null

---

#### AnnotationElement

public AnnotationElement​(

Class

<? extends

Annotation

> annotationType)

Creates an annotation element to use for dynamically defined events.

Supported value types are

byte

,

short

,

int

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

Supported value types are

byte

,

short

,

int

,

long

,

double

,

float

,

boolean

,

char

,
and

String

. Enums, arrays, and classes are not supported.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

If

annotationType

has annotations (directly present, indirectly
present or associated), then those annotation are recursively included.
However, both

annotationType

and any annotation found recursively
must have the

MetadataDefinition

annotation.

To statically define events, see

Event

class.

To statically define events, see

Event

class.

Method Detail

- getValues

```java
public
List
<
Object
> getValues()
```

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

**Returns:** list of values, not

null

- getValueDescriptors

```java
public
List
<
ValueDescriptor
> getValueDescriptors()
```

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

**Returns:** the list of value descriptors for this

Annotation

, not

null

- getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this

AnnotationElement

.

**Returns:** a list of meta annotation, not

null

- getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

**Returns:** type name, not

null

- getValue

```java
public
Object
getValue​(
String
name)
```

Returns a value for this

AnnotationElement

.

**Parameters:** name

- the name of the method in the annotation interface, not

null

.
**Returns:** the annotation value, not

null

.
**Throws:** IllegalArgumentException

- if a method with the specified name does
not exist in the annotation

- hasValue

```java
public boolean hasValue​(
String
name)
```

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

.

**Parameters:** name

- name of the method in the annotation interface to find, not

null
**Returns:** true

if method exists,

false

otherwise

- getAnnotation

```java
public final <A> A getAnnotation​(
Class
<? extends
Annotation
> annotationType)
```

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

**Type Parameters:** A

- the type of the annotation to query for and return if it exists
**Parameters:** annotationType

- the

Class object

corresponding to the annotation type,
not

null
**Returns:** this element's annotation for the specified annotation type if
it it exists, else

null

- getTypeId

```java
public long getTypeId()
```

Returns the type ID for this

AnnotationElement

.

The ID is a unique identifier for the type in the Java Virtual Machine (JVM). The ID might not
be the same between JVM instances.

**Returns:** the type ID, not negative

---

#### Method Detail

getValues

```java
public
List
<
Object
> getValues()
```

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

**Returns:** list of values, not

null

---

#### getValues

public

List

<

Object

> getValues()

Returns an immutable list of annotation values in an order that matches the
value descriptors for this

AnnotationElement

.

getValueDescriptors

```java
public
List
<
ValueDescriptor
> getValueDescriptors()
```

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

**Returns:** the list of value descriptors for this

Annotation

, not

null

---

#### getValueDescriptors

public

List

<

ValueDescriptor

> getValueDescriptors()

Returns an immutable list of descriptors that describes the annotation values
for this

AnnotationElement

.

getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this

AnnotationElement

.

**Returns:** a list of meta annotation, not

null

---

#### getAnnotationElements

public

List

<

AnnotationElement

> getAnnotationElements()

Returns an immutable list of annotation elements for this

AnnotationElement

.

getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

**Returns:** type name, not

null

---

#### getTypeName

public

String

getTypeName()

Returns the fully qualified name of the annotation type that corresponds to
this

AnnotationElement

(for example,

"jdk.jfr.Label"

).

getValue

```java
public
Object
getValue​(
String
name)
```

Returns a value for this

AnnotationElement

.

**Parameters:** name

- the name of the method in the annotation interface, not

null

.
**Returns:** the annotation value, not

null

.
**Throws:** IllegalArgumentException

- if a method with the specified name does
not exist in the annotation

---

#### getValue

public

Object

getValue​(

String

name)

Returns a value for this

AnnotationElement

.

hasValue

```java
public boolean hasValue​(
String
name)
```

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

.

**Parameters:** name

- name of the method in the annotation interface to find, not

null
**Returns:** true

if method exists,

false

otherwise

---

#### hasValue

public boolean hasValue​(

String

name)

Returns

true

if an annotation value with the specified name exists in
this

AnnotationElement

.

getAnnotation

```java
public final <A> A getAnnotation​(
Class
<? extends
Annotation
> annotationType)
```

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

**Type Parameters:** A

- the type of the annotation to query for and return if it exists
**Parameters:** annotationType

- the

Class object

corresponding to the annotation type,
not

null
**Returns:** this element's annotation for the specified annotation type if
it it exists, else

null

---

#### getAnnotation

public final <A> A getAnnotation​(

Class

<? extends

Annotation

> annotationType)

Returns the first annotation for the specified type if an

AnnotationElement

with the same name exists, else

null

.

getTypeId

```java
public long getTypeId()
```

Returns the type ID for this

AnnotationElement

.

The ID is a unique identifier for the type in the Java Virtual Machine (JVM). The ID might not
be the same between JVM instances.

**Returns:** the type ID, not negative

---

#### getTypeId

public long getTypeId()

Returns the type ID for this

AnnotationElement

.

The ID is a unique identifier for the type in the Java Virtual Machine (JVM). The ID might not
be the same between JVM instances.

The ID is a unique identifier for the type in the Java Virtual Machine (JVM). The ID might not
be the same between JVM instances.

---

