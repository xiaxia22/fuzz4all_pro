# Class SettingDescriptor

**Source:** `jdk.jfr\jdk\jfr\SettingDescriptor.html`

### Class Description

```java
public final class
SettingDescriptor

extends
Object
```

Describes an event setting.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getName()

Returns the name of the setting (for example,

"threshold"

).

**Returns:**
- the name, not

null

---

#### public
String
getLabel()

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

If the setting lacks a label, the label for the type that is associated with this
setting is returned, or

null

if doesn't exist

**Returns:**
- a human-readable name, or

null

if doesn't exist

---

#### public
String
getDescription()

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

If the setting lacks a description, the description for the type that is
associated with this setting is returned, or

null

if doesn't exist.

**Returns:**
- the description, or

null

if doesn't exist

---

#### public
String
getContentType()

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

For example, if the setting descriptor represents a percentage, then

"jdk.jfr.Percentage"

hints to a client that a value of "0.5"
is formatted as "50%".

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

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

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

**Returns:**
- the type name, not

null

**See Also:**
- getTypeId()

---

#### public long getTypeId()

Returns a unique ID for the type in the Java Virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:**
- the type ID, not negative

---

#### public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)

Returns the first annotation for the specified type if an annotation
element with the same name is available,

null

otherwise.

**Parameters:**
- annotationType

- the Class object that corresponds to the annotation
type, not

null

**Returns:**
- this element's annotation for the specified annotation type if
available,

null

otherwise

**Type Parameters:**
- A

- the type of the annotation to query for and return if available

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
String
getDefaultValue()

Returns the default value for this setting descriptor.

**Returns:**
- the default value, not

null

---

### Additional Sections

#### Class SettingDescriptor

java.lang.Object

- jdk.jfr.SettingDescriptor

jdk.jfr.SettingDescriptor

```java
public final class
SettingDescriptor

extends
Object
```

Describes an event setting.

**Since:** 9

public final class

SettingDescriptor

extends

Object

Describes an event setting.

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
element with the same name is available,

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

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

String

getDefaultValue

()

Returns the default value for this setting descriptor.

String

getDescription

()

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

String

getLabel

()

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

String

getName

()

Returns the name of the setting (for example,

"threshold"

).

long

getTypeId

()

Returns a unique ID for the type in the Java Virtual Machine (JVM).

String

getTypeName

()

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

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
element with the same name is available,

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

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

String

getDefaultValue

()

Returns the default value for this setting descriptor.

String

getDescription

()

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

String

getLabel

()

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

String

getName

()

Returns the name of the setting (for example,

"threshold"

).

long

getTypeId

()

Returns a unique ID for the type in the Java Virtual Machine (JVM).

String

getTypeName

()

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

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
element with the same name is available,

null

otherwise.

Returns an immutable list of annotation elements for this value
descriptor.

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

Returns the default value for this setting descriptor.

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

Returns the name of the setting (for example,

"threshold"

).

Returns a unique ID for the type in the Java Virtual Machine (JVM).

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

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

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the setting (for example,

"threshold"

).

**Returns:** the name, not

null

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

If the setting lacks a label, the label for the type that is associated with this
setting is returned, or

null

if doesn't exist

**Returns:** a human-readable name, or

null

if doesn't exist

- getDescription

```java
public
String
getDescription()
```

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

If the setting lacks a description, the description for the type that is
associated with this setting is returned, or

null

if doesn't exist.

**Returns:** the description, or

null

if doesn't exist

- getContentType

```java
public
String
getContentType()
```

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

For example, if the setting descriptor represents a percentage, then

"jdk.jfr.Percentage"

hints to a client that a value of "0.5"
is formatted as "50%".

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

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

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

**Returns:** the type name, not

null
**See Also:** getTypeId()

- getTypeId

```java
public long getTypeId()
```

Returns a unique ID for the type in the Java Virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:** the type ID, not negative

- getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns the first annotation for the specified type if an annotation
element with the same name is available,

null

otherwise.

**Type Parameters:** A

- the type of the annotation to query for and return if available
**Parameters:** annotationType

- the Class object that corresponds to the annotation
type, not

null
**Returns:** this element's annotation for the specified annotation type if
available,

null

otherwise

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

- getDefaultValue

```java
public
String
getDefaultValue()
```

Returns the default value for this setting descriptor.

**Returns:** the default value, not

null

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the setting (for example,

"threshold"

).

**Returns:** the name, not

null

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

If the setting lacks a label, the label for the type that is associated with this
setting is returned, or

null

if doesn't exist

**Returns:** a human-readable name, or

null

if doesn't exist

- getDescription

```java
public
String
getDescription()
```

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

If the setting lacks a description, the description for the type that is
associated with this setting is returned, or

null

if doesn't exist.

**Returns:** the description, or

null

if doesn't exist

- getContentType

```java
public
String
getContentType()
```

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

For example, if the setting descriptor represents a percentage, then

"jdk.jfr.Percentage"

hints to a client that a value of "0.5"
is formatted as "50%".

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

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

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

**Returns:** the type name, not

null
**See Also:** getTypeId()

- getTypeId

```java
public long getTypeId()
```

Returns a unique ID for the type in the Java Virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:** the type ID, not negative

- getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns the first annotation for the specified type if an annotation
element with the same name is available,

null

otherwise.

**Type Parameters:** A

- the type of the annotation to query for and return if available
**Parameters:** annotationType

- the Class object that corresponds to the annotation
type, not

null
**Returns:** this element's annotation for the specified annotation type if
available,

null

otherwise

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

- getDefaultValue

```java
public
String
getDefaultValue()
```

Returns the default value for this setting descriptor.

**Returns:** the default value, not

null

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of the setting (for example,

"threshold"

).

**Returns:** the name, not

null

---

#### getName

public

String

getName()

Returns the name of the setting (for example,

"threshold"

).

getLabel

```java
public
String
getLabel()
```

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

If the setting lacks a label, the label for the type that is associated with this
setting is returned, or

null

if doesn't exist

**Returns:** a human-readable name, or

null

if doesn't exist

---

#### getLabel

public

String

getLabel()

Returns a human-readable name that describes the setting (for example,

"Threshold"

).

If the setting lacks a label, the label for the type that is associated with this
setting is returned, or

null

if doesn't exist

If the setting lacks a label, the label for the type that is associated with this
setting is returned, or

null

if doesn't exist

getDescription

```java
public
String
getDescription()
```

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

If the setting lacks a description, the description for the type that is
associated with this setting is returned, or

null

if doesn't exist.

**Returns:** the description, or

null

if doesn't exist

---

#### getDescription

public

String

getDescription()

Returns a sentence that describes the setting (for example

"Record event with duration
above or equal to threshold"

).

If the setting lacks a description, the description for the type that is
associated with this setting is returned, or

null

if doesn't exist.

If the setting lacks a description, the description for the type that is
associated with this setting is returned, or

null

if doesn't exist.

getContentType

```java
public
String
getContentType()
```

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

For example, if the setting descriptor represents a percentage, then

"jdk.jfr.Percentage"

hints to a client that a value of "0.5"
is formatted as "50%".

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

**Returns:** the content type, or

null

if doesn't exist
**See Also:** ContentType

---

#### getContentType

public

String

getContentType()

Returns a textual identifier that specifies how a value that is represented by
this

SettingDescriptor

object is interpreted or formatted.

For example, if the setting descriptor represents a percentage, then

"jdk.jfr.Percentage"

hints to a client that a value of "0.5"
is formatted as "50%".

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

For example, if the setting descriptor represents a percentage, then

"jdk.jfr.Percentage"

hints to a client that a value of "0.5"
is formatted as "50%".

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

The JDK provides the following predefined content types:

- jdk.jfr.Percentage
- jdk.jfr.Timespan
- jdk.jfr.Timestamp
- jdk.jfr.Frequency
- jdk.jfr.Flag
- jdk.jfr.MemoryAddress
- jdk.jfr.DataAmount
- jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

jdk.jfr.Percentage

jdk.jfr.Timespan

jdk.jfr.Timestamp

jdk.jfr.Frequency

jdk.jfr.Flag

jdk.jfr.MemoryAddress

jdk.jfr.DataAmount

jdk.jfr.NetworkAddress

User-defined content types can be created by using

ContentType

.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

If the setting lacks a content type, the content type for the type
that is associated with this setting is returned, or

null

if not
available.

getTypeName

```java
public
String
getTypeName()
```

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

**Returns:** the type name, not

null
**See Also:** getTypeId()

---

#### getTypeName

public

String

getTypeName()

Returns the fully qualified class name of the type that is associated with this
setting descriptor.

getTypeId

```java
public long getTypeId()
```

Returns a unique ID for the type in the Java Virtual Machine (JVM).

The ID might not be the same between JVM instances.

**Returns:** the type ID, not negative

---

#### getTypeId

public long getTypeId()

Returns a unique ID for the type in the Java Virtual Machine (JVM).

The ID might not be the same between JVM instances.

The ID might not be the same between JVM instances.

getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns the first annotation for the specified type if an annotation
element with the same name is available,

null

otherwise.

**Type Parameters:** A

- the type of the annotation to query for and return if available
**Parameters:** annotationType

- the Class object that corresponds to the annotation
type, not

null
**Returns:** this element's annotation for the specified annotation type if
available,

null

otherwise

---

#### getAnnotation

public <A extends

Annotation

> A getAnnotation​(

Class

<A> annotationType)

Returns the first annotation for the specified type if an annotation
element with the same name is available,

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

getDefaultValue

```java
public
String
getDefaultValue()
```

Returns the default value for this setting descriptor.

**Returns:** the default value, not

null

---

#### getDefaultValue

public

String

getDefaultValue()

Returns the default value for this setting descriptor.

---

