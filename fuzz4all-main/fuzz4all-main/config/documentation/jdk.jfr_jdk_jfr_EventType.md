# Class EventType

**Source:** `jdk.jfr\jdk\jfr\EventType.html`

### Class Description

```java
public final class
EventType

extends
Object
```

Describes an event, its fields, settings and annotations.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
List
<
ValueDescriptor
> getFields()

Returns an immutable list of descriptors that describe the event fields of
this event type.

**Returns:**
- the list of field descriptors, not

null

---

#### public
ValueDescriptor
getField​(
String
name)

Returns the field with the specified name, or

null

if it doesn't
exist.

**Returns:**
- a value descriptor that describes the field, or

null

if
the field with the specified name doesn't exist

---

#### public
String
getName()

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

The identifier is the fully qualified name of the event class, if not set using
the

Name

annotation.

**Returns:**
- the name, not

null

**See Also:**
- Name

---

#### public
String
getLabel()

Returns a human-readable name (for example,

"CPU Load"

).

The label of an event class can be set with

Label

.

**Returns:**
- the label, or

null

if a label is not set

**See Also:**
- Label

---

#### public long getId()

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

**Returns:**
- the ID that is used in the JVM

---

#### public
List
<
AnnotationElement
> getAnnotationElements()

Returns an immutable list of annotation elements for this event type.

**Returns:**
- an immutable list of annotations or an empty list if no
annotations exists, not

null

---

#### public boolean isEnabled()

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

By default, the event is enabled. The event can be enabled or disabled by
setting the enabled setting to

true

or

false

, programmatically or by using a
configuration file. The event can also be disabled by annotating event with
the

@Enabled(false)

annotation.

**Returns:**
- true if event is enabled, false otherwise

**See Also:**
- Enabled

,

Recording.enable(Class)

---

#### public
String
getDescription()

Returns a short sentence that describes the event class.

The description of an event class can be set with

Description

.

**Returns:**
- the description, or

null

if no description exists

**See Also:**
- Description

---

#### public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationClass)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

**Parameters:**
- annotationClass

- the

Class

object that corresponds to the
annotation type, not

null

**Returns:**
- this element's annotation for the specified annotation type if
directly present, else

null

**Type Parameters:**
- A

- the type of the annotation to query for and return if present

---

#### public static
EventType
getEventType​(
Class
<? extends
Event
> eventClass)

Returns the event type for an event class, or

null

if it doesn't
exist.

**Parameters:**
- eventClass

- the event class, not

null

**Returns:**
- the event class, or null if class doesn't exist

**Throws:**
- IllegalArgumentException

- if

eventClass

is an abstract class
- IllegalStateException

- if the class is annotated with

Registered(false)

, but not manually registered

---

#### public
List
<
SettingDescriptor
> getSettingDescriptors()

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

**Returns:**
- the list of setting descriptors for this event type, not

null

---

#### public
List
<
String
> getCategoryNames()

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

**Returns:**
- an immutable list of category names, or a list with the name

"Uncategorized"

if no category is set

**See Also:**
- Category

---

### Additional Sections

#### Class EventType

java.lang.Object

- jdk.jfr.EventType

jdk.jfr.EventType

```java
public final class
EventType

extends
Object
```

Describes an event, its fields, settings and annotations.

**Since:** 9

public final class

EventType

extends

Object

Describes an event, its fields, settings and annotations.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

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

<A> annotationClass)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

List

<

AnnotationElement

>

getAnnotationElements

()

Returns an immutable list of annotation elements for this event type.

List

<

String

>

getCategoryNames

()

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

String

getDescription

()

Returns a short sentence that describes the event class.

static

EventType

getEventType

​(

Class

<? extends

Event

> eventClass)

Returns the event type for an event class, or

null

if it doesn't
exist.

ValueDescriptor

getField

​(

String

name)

Returns the field with the specified name, or

null

if it doesn't
exist.

List

<

ValueDescriptor

>

getFields

()

Returns an immutable list of descriptors that describe the event fields of
this event type.

long

getId

()

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

String

getLabel

()

Returns a human-readable name (for example,

"CPU Load"

).

String

getName

()

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

List

<

SettingDescriptor

>

getSettingDescriptors

()

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

boolean

isEnabled

()

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

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

Static Methods

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

<A> annotationClass)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

List

<

AnnotationElement

>

getAnnotationElements

()

Returns an immutable list of annotation elements for this event type.

List

<

String

>

getCategoryNames

()

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

String

getDescription

()

Returns a short sentence that describes the event class.

static

EventType

getEventType

​(

Class

<? extends

Event

> eventClass)

Returns the event type for an event class, or

null

if it doesn't
exist.

ValueDescriptor

getField

​(

String

name)

Returns the field with the specified name, or

null

if it doesn't
exist.

List

<

ValueDescriptor

>

getFields

()

Returns an immutable list of descriptors that describe the event fields of
this event type.

long

getId

()

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

String

getLabel

()

Returns a human-readable name (for example,

"CPU Load"

).

String

getName

()

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

List

<

SettingDescriptor

>

getSettingDescriptors

()

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

boolean

isEnabled

()

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

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
element with the same name is directly present, otherwise

null

.

Returns an immutable list of annotation elements for this event type.

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

Returns a short sentence that describes the event class.

Returns the event type for an event class, or

null

if it doesn't
exist.

Returns the field with the specified name, or

null

if it doesn't
exist.

Returns an immutable list of descriptors that describe the event fields of
this event type.

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

Returns a human-readable name (for example,

"CPU Load"

).

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

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

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of descriptors that describe the event fields of
this event type.

**Returns:** the list of field descriptors, not

null

- getField

```java
public
ValueDescriptor
getField​(
String
name)
```

Returns the field with the specified name, or

null

if it doesn't
exist.

**Returns:** a value descriptor that describes the field, or

null

if
the field with the specified name doesn't exist

- getName

```java
public
String
getName()
```

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

The identifier is the fully qualified name of the event class, if not set using
the

Name

annotation.

**Returns:** the name, not

null
**See Also:** Name

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name (for example,

"CPU Load"

).

The label of an event class can be set with

Label

.

**Returns:** the label, or

null

if a label is not set
**See Also:** Label

- getId

```java
public long getId()
```

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

**Returns:** the ID that is used in the JVM

- getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this event type.

**Returns:** an immutable list of annotations or an empty list if no
annotations exists, not

null

- isEnabled

```java
public boolean isEnabled()
```

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

By default, the event is enabled. The event can be enabled or disabled by
setting the enabled setting to

true

or

false

, programmatically or by using a
configuration file. The event can also be disabled by annotating event with
the

@Enabled(false)

annotation.

**Returns:** true if event is enabled, false otherwise
**See Also:** Enabled

,

Recording.enable(Class)

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the event class.

The description of an event class can be set with

Description

.

**Returns:** the description, or

null

if no description exists
**See Also:** Description

- getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationClass)
```

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

**Type Parameters:** A

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the

Class

object that corresponds to the
annotation type, not

null
**Returns:** this element's annotation for the specified annotation type if
directly present, else

null

- getEventType

```java
public static
EventType
getEventType​(
Class
<? extends
Event
> eventClass)
```

Returns the event type for an event class, or

null

if it doesn't
exist.

**Parameters:** eventClass

- the event class, not

null
**Returns:** the event class, or null if class doesn't exist
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract class
**Throws:** IllegalStateException

- if the class is annotated with

Registered(false)

, but not manually registered

- getSettingDescriptors

```java
public
List
<
SettingDescriptor
> getSettingDescriptors()
```

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

**Returns:** the list of setting descriptors for this event type, not

null

- getCategoryNames

```java
public
List
<
String
> getCategoryNames()
```

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

**Returns:** an immutable list of category names, or a list with the name

"Uncategorized"

if no category is set
**See Also:** Category

Method Detail

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of descriptors that describe the event fields of
this event type.

**Returns:** the list of field descriptors, not

null

- getField

```java
public
ValueDescriptor
getField​(
String
name)
```

Returns the field with the specified name, or

null

if it doesn't
exist.

**Returns:** a value descriptor that describes the field, or

null

if
the field with the specified name doesn't exist

- getName

```java
public
String
getName()
```

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

The identifier is the fully qualified name of the event class, if not set using
the

Name

annotation.

**Returns:** the name, not

null
**See Also:** Name

- getLabel

```java
public
String
getLabel()
```

Returns a human-readable name (for example,

"CPU Load"

).

The label of an event class can be set with

Label

.

**Returns:** the label, or

null

if a label is not set
**See Also:** Label

- getId

```java
public long getId()
```

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

**Returns:** the ID that is used in the JVM

- getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this event type.

**Returns:** an immutable list of annotations or an empty list if no
annotations exists, not

null

- isEnabled

```java
public boolean isEnabled()
```

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

By default, the event is enabled. The event can be enabled or disabled by
setting the enabled setting to

true

or

false

, programmatically or by using a
configuration file. The event can also be disabled by annotating event with
the

@Enabled(false)

annotation.

**Returns:** true if event is enabled, false otherwise
**See Also:** Enabled

,

Recording.enable(Class)

- getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the event class.

The description of an event class can be set with

Description

.

**Returns:** the description, or

null

if no description exists
**See Also:** Description

- getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationClass)
```

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

**Type Parameters:** A

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the

Class

object that corresponds to the
annotation type, not

null
**Returns:** this element's annotation for the specified annotation type if
directly present, else

null

- getEventType

```java
public static
EventType
getEventType​(
Class
<? extends
Event
> eventClass)
```

Returns the event type for an event class, or

null

if it doesn't
exist.

**Parameters:** eventClass

- the event class, not

null
**Returns:** the event class, or null if class doesn't exist
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract class
**Throws:** IllegalStateException

- if the class is annotated with

Registered(false)

, but not manually registered

- getSettingDescriptors

```java
public
List
<
SettingDescriptor
> getSettingDescriptors()
```

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

**Returns:** the list of setting descriptors for this event type, not

null

- getCategoryNames

```java
public
List
<
String
> getCategoryNames()
```

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

**Returns:** an immutable list of category names, or a list with the name

"Uncategorized"

if no category is set
**See Also:** Category

---

#### Method Detail

getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of descriptors that describe the event fields of
this event type.

**Returns:** the list of field descriptors, not

null

---

#### getFields

public

List

<

ValueDescriptor

> getFields()

Returns an immutable list of descriptors that describe the event fields of
this event type.

getField

```java
public
ValueDescriptor
getField​(
String
name)
```

Returns the field with the specified name, or

null

if it doesn't
exist.

**Returns:** a value descriptor that describes the field, or

null

if
the field with the specified name doesn't exist

---

#### getField

public

ValueDescriptor

getField​(

String

name)

Returns the field with the specified name, or

null

if it doesn't
exist.

getName

```java
public
String
getName()
```

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

The identifier is the fully qualified name of the event class, if not set using
the

Name

annotation.

**Returns:** the name, not

null
**See Also:** Name

---

#### getName

public

String

getName()

Returns an identifier for the event (for example,

"jdk.CPULoad"

).

The identifier is the fully qualified name of the event class, if not set using
the

Name

annotation.

The identifier is the fully qualified name of the event class, if not set using
the

Name

annotation.

getLabel

```java
public
String
getLabel()
```

Returns a human-readable name (for example,

"CPU Load"

).

The label of an event class can be set with

Label

.

**Returns:** the label, or

null

if a label is not set
**See Also:** Label

---

#### getLabel

public

String

getLabel()

Returns a human-readable name (for example,

"CPU Load"

).

The label of an event class can be set with

Label

.

The label of an event class can be set with

Label

.

getId

```java
public long getId()
```

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

**Returns:** the ID that is used in the JVM

---

#### getId

public long getId()

Returns a unique ID for this event type in the Java Virtual Machine (JVM).

getAnnotationElements

```java
public
List
<
AnnotationElement
> getAnnotationElements()
```

Returns an immutable list of annotation elements for this event type.

**Returns:** an immutable list of annotations or an empty list if no
annotations exists, not

null

---

#### getAnnotationElements

public

List

<

AnnotationElement

> getAnnotationElements()

Returns an immutable list of annotation elements for this event type.

isEnabled

```java
public boolean isEnabled()
```

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

By default, the event is enabled. The event can be enabled or disabled by
setting the enabled setting to

true

or

false

, programmatically or by using a
configuration file. The event can also be disabled by annotating event with
the

@Enabled(false)

annotation.

**Returns:** true if event is enabled, false otherwise
**See Also:** Enabled

,

Recording.enable(Class)

---

#### isEnabled

public boolean isEnabled()

Returns

true

if the event is enabled and at least one recording is
running,

false

otherwise.

By default, the event is enabled. The event can be enabled or disabled by
setting the enabled setting to

true

or

false

, programmatically or by using a
configuration file. The event can also be disabled by annotating event with
the

@Enabled(false)

annotation.

By default, the event is enabled. The event can be enabled or disabled by
setting the enabled setting to

true

or

false

, programmatically or by using a
configuration file. The event can also be disabled by annotating event with
the

@Enabled(false)

annotation.

getDescription

```java
public
String
getDescription()
```

Returns a short sentence that describes the event class.

The description of an event class can be set with

Description

.

**Returns:** the description, or

null

if no description exists
**See Also:** Description

---

#### getDescription

public

String

getDescription()

Returns a short sentence that describes the event class.

The description of an event class can be set with

Description

.

The description of an event class can be set with

Description

.

getAnnotation

```java
public <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationClass)
```

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

**Type Parameters:** A

- the type of the annotation to query for and return if present
**Parameters:** annotationClass

- the

Class

object that corresponds to the
annotation type, not

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

<A> annotationClass)

Returns the first annotation for the specified type if an annotation
element with the same name is directly present, otherwise

null

.

getEventType

```java
public static
EventType
getEventType​(
Class
<? extends
Event
> eventClass)
```

Returns the event type for an event class, or

null

if it doesn't
exist.

**Parameters:** eventClass

- the event class, not

null
**Returns:** the event class, or null if class doesn't exist
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract class
**Throws:** IllegalStateException

- if the class is annotated with

Registered(false)

, but not manually registered

---

#### getEventType

public static

EventType

getEventType​(

Class

<? extends

Event

> eventClass)

Returns the event type for an event class, or

null

if it doesn't
exist.

getSettingDescriptors

```java
public
List
<
SettingDescriptor
> getSettingDescriptors()
```

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

**Returns:** the list of setting descriptors for this event type, not

null

---

#### getSettingDescriptors

public

List

<

SettingDescriptor

> getSettingDescriptors()

Returns an immutable list of the setting descriptors that describe the available
event settings for this event type.

getCategoryNames

```java
public
List
<
String
> getCategoryNames()
```

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

**Returns:** an immutable list of category names, or a list with the name

"Uncategorized"

if no category is set
**See Also:** Category

---

#### getCategoryNames

public

List

<

String

> getCategoryNames()

Returns the list of human-readable names that makes up the categories for
this event type (for example,

"Java Application"

,

"Statistics"

).

---

