# Class RecordedObject

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedObject.html`

### Class Description

```java
public class
RecordedObject

extends
Object
```

A complex data type that consists of one or more fields.

This class provides methods to select and query nested objects by passing a
dot

"."

delimited

String

object (for instance,

"aaa.bbb"

). A method evaluates a nested object from left to right,
and if a part is

null

, it throws

NullPointerException

.

**Direct Known Subclasses:** RecordedClass

,

RecordedClassLoader

,

RecordedEvent

,

RecordedFrame

,

RecordedMethod

,

RecordedStackTrace

,

RecordedThread

,

RecordedThreadGroup

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean hasField​(
String
name)

Returns

true

if a field with the given name exists,

false

otherwise.

**Parameters:**
- name

- name of the field to get, not

null

**Returns:**
- true

if the field exists,

false

otherwise.

**See Also:**
- getFields()

---

#### public final <T> T getValue​(
String
name)

Returns the value of the field with the given name.

The return type may be a primitive type or a subclass of

RecordedObject

.

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value, can be

null

**Throws:**
- IllegalArgumentException

- if no field called

name

exists

**See Also:**
- hasField(String)

**Type Parameters:**
- T

- the return type

---

#### public
List
<
ValueDescriptor
> getFields()

Returns an immutable list of the fields for this object.

**Returns:**
- the fields, not

null

---

#### public final boolean getBoolean​(
String
name)

Returns the value of a field of type

boolean

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- name of the field to get, not

null

**Returns:**
- the value of the field,

true

or

false

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

boolean

**See Also:**
- hasField(String)

,

getValue(String)

---

#### public final byte getByte​(
String
name)

Returns the value of a field of type

byte

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

byte

**See Also:**
- hasField(String)

,

getValue(String)

---

#### public final char getChar​(
String
name)

Returns the value of a field of type

char

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field as a

char

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

char

**See Also:**
- hasField(String)

,

getValue(String)

---

#### public final short getShort​(
String
name)

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

This method can be used on the following types:

short

and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field converted to type

short

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

short

by a widening
conversion

**See Also:**
- hasField(String)

---

#### public final int getInt​(
String
name)

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

This method can be used on fields of the following types:

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field converted to type

int

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

int

by a widening
conversion

**See Also:**
- hasField(String)

---

#### public final float getFloat​(
String
name)

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

This method can be used on fields of the following types:

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field converted to type

float

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

float

by a widening
conversion

**See Also:**
- hasField(String)

---

#### public final long getLong​(
String
name)

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

This method can be used on fields of the following types:

long

,

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field converted to type

long

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

long

via a widening
conversion

**See Also:**
- hasField(String)

---

#### public final double getDouble​(
String
name)

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

This method can be used on fields of the following types:

double

,

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field converted to type

double

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

double

by a widening
conversion

**See Also:**
- hasField(String)

---

#### public final
String
getString​(
String
name)

Returns the value of a field of type

String

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field as a

String

, can be

null

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

String

**See Also:**
- hasField(String)

---

#### public final
Duration
getDuration​(
String
name)

Returns the value of a timespan field.

This method can be used on fields annotated with

@Timespan

, and of
the following types:

long

,

int

,

short

,

char

,
and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- a time span represented as a

Duration

, not

null

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to a

Duration

object

**See Also:**
- hasField(String)

---

#### public final
Instant
getInstant​(
String
name)

Returns the value of a timestamp field.

This method can be used on fields annotated with

@Timestamp

, and of
the following types:

long

,

int

,

short

,

char

and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- a timstamp represented as an

Instant

, not

null

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to an

Instant

object

**See Also:**
- hasField(String)

---

#### public final
RecordedClass
getClass​(
String
name)

Returns the value of a field of type

Class

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field as a

RecordedClass

, can be

null

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Class

**See Also:**
- hasField(String)

---

#### public final
RecordedThread
getThread​(
String
name)

Returns the value of a field of type

Thread

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:**
- name

- of the field to get, not

null

**Returns:**
- the value of the field as a

RecordedThread

object, can be

null

**Throws:**
- IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Thread

**See Also:**
- hasField(String)

---

#### public final
String
toString()

Returns a textual representation of this object.

**Overrides:**
- toString

in class

Object

**Returns:**
- textual description of this object

---

### Additional Sections

#### Class RecordedObject

java.lang.Object

- jdk.jfr.consumer.RecordedObject

jdk.jfr.consumer.RecordedObject

**Direct Known Subclasses:** RecordedClass

,

RecordedClassLoader

,

RecordedEvent

,

RecordedFrame

,

RecordedMethod

,

RecordedStackTrace

,

RecordedThread

,

RecordedThreadGroup

```java
public class
RecordedObject

extends
Object
```

A complex data type that consists of one or more fields.

This class provides methods to select and query nested objects by passing a
dot

"."

delimited

String

object (for instance,

"aaa.bbb"

). A method evaluates a nested object from left to right,
and if a part is

null

, it throws

NullPointerException

.

**Since:** 9

public class

RecordedObject

extends

Object

A complex data type that consists of one or more fields.

This class provides methods to select and query nested objects by passing a
dot

"."

delimited

String

object (for instance,

"aaa.bbb"

). A method evaluates a nested object from left to right,
and if a part is

null

, it throws

NullPointerException

.

This class provides methods to select and query nested objects by passing a
dot

"."

delimited

String

object (for instance,

"aaa.bbb"

). A method evaluates a nested object from left to right,
and if a part is

null

, it throws

NullPointerException

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

getBoolean

​(

String

name)

Returns the value of a field of type

boolean

.

byte

getByte

​(

String

name)

Returns the value of a field of type

byte

.

char

getChar

​(

String

name)

Returns the value of a field of type

char

.

RecordedClass

getClass

​(

String

name)

Returns the value of a field of type

Class

.

double

getDouble

​(

String

name)

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

Duration

getDuration

​(

String

name)

Returns the value of a timespan field.

List

<

ValueDescriptor

>

getFields

()

Returns an immutable list of the fields for this object.

float

getFloat

​(

String

name)

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

Instant

getInstant

​(

String

name)

Returns the value of a timestamp field.

int

getInt

​(

String

name)

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

long

getLong

​(

String

name)

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

short

getShort

​(

String

name)

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

String

getString

​(

String

name)

Returns the value of a field of type

String

.

RecordedThread

getThread

​(

String

name)

Returns the value of a field of type

Thread

.

<T> T

getValue

​(

String

name)

Returns the value of the field with the given name.

boolean

hasField

​(

String

name)

Returns

true

if a field with the given name exists,

false

otherwise.

String

toString

()

Returns a textual representation of this object.

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

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

getBoolean

​(

String

name)

Returns the value of a field of type

boolean

.

byte

getByte

​(

String

name)

Returns the value of a field of type

byte

.

char

getChar

​(

String

name)

Returns the value of a field of type

char

.

RecordedClass

getClass

​(

String

name)

Returns the value of a field of type

Class

.

double

getDouble

​(

String

name)

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

Duration

getDuration

​(

String

name)

Returns the value of a timespan field.

List

<

ValueDescriptor

>

getFields

()

Returns an immutable list of the fields for this object.

float

getFloat

​(

String

name)

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

Instant

getInstant

​(

String

name)

Returns the value of a timestamp field.

int

getInt

​(

String

name)

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

long

getLong

​(

String

name)

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

short

getShort

​(

String

name)

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

String

getString

​(

String

name)

Returns the value of a field of type

String

.

RecordedThread

getThread

​(

String

name)

Returns the value of a field of type

Thread

.

<T> T

getValue

​(

String

name)

Returns the value of the field with the given name.

boolean

hasField

​(

String

name)

Returns

true

if a field with the given name exists,

false

otherwise.

String

toString

()

Returns a textual representation of this object.

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

Returns the value of a field of type

boolean

.

Returns the value of a field of type

byte

.

Returns the value of a field of type

char

.

Returns the value of a field of type

Class

.

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

Returns the value of a timespan field.

Returns an immutable list of the fields for this object.

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

Returns the value of a timestamp field.

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

Returns the value of a field of type

String

.

Returns the value of a field of type

Thread

.

Returns the value of the field with the given name.

Returns

true

if a field with the given name exists,

false

otherwise.

Returns a textual representation of this object.

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

- hasField

```java
public boolean hasField​(
String
name)
```

Returns

true

if a field with the given name exists,

false

otherwise.

**Parameters:** name

- name of the field to get, not

null
**Returns:** true

if the field exists,

false

otherwise.
**See Also:** getFields()

- getValue

```java
public final <T> T getValue​(
String
name)
```

Returns the value of the field with the given name.

The return type may be a primitive type or a subclass of

RecordedObject

.

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

**Type Parameters:** T

- the return type
**Parameters:** name

- of the field to get, not

null
**Returns:** the value, can be

null
**Throws:** IllegalArgumentException

- if no field called

name

exists
**See Also:** hasField(String)

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of the fields for this object.

**Returns:** the fields, not

null

- getBoolean

```java
public final boolean getBoolean​(
String
name)
```

Returns the value of a field of type

boolean

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- name of the field to get, not

null
**Returns:** the value of the field,

true

or

false
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

boolean
**See Also:** hasField(String)

,

getValue(String)

- getByte

```java
public final byte getByte​(
String
name)
```

Returns the value of a field of type

byte

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

byte
**See Also:** hasField(String)

,

getValue(String)

- getChar

```java
public final char getChar​(
String
name)
```

Returns the value of a field of type

char

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

char
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

char
**See Also:** hasField(String)

,

getValue(String)

- getShort

```java
public final short getShort​(
String
name)
```

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

This method can be used on the following types:

short

and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

short
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

short

by a widening
conversion
**See Also:** hasField(String)

- getInt

```java
public final int getInt​(
String
name)
```

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

This method can be used on fields of the following types:

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

int
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

int

by a widening
conversion
**See Also:** hasField(String)

- getFloat

```java
public final float getFloat​(
String
name)
```

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

This method can be used on fields of the following types:

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

float
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

float

by a widening
conversion
**See Also:** hasField(String)

- getLong

```java
public final long getLong​(
String
name)
```

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

This method can be used on fields of the following types:

long

,

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

long
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

long

via a widening
conversion
**See Also:** hasField(String)

- getDouble

```java
public final double getDouble​(
String
name)
```

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

This method can be used on fields of the following types:

double

,

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

double
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

double

by a widening
conversion
**See Also:** hasField(String)

- getString

```java
public final
String
getString​(
String
name)
```

Returns the value of a field of type

String

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

String

, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

String
**See Also:** hasField(String)

- getDuration

```java
public final
Duration
getDuration​(
String
name)
```

Returns the value of a timespan field.

This method can be used on fields annotated with

@Timespan

, and of
the following types:

long

,

int

,

short

,

char

,
and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** a time span represented as a

Duration

, not

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to a

Duration

object
**See Also:** hasField(String)

- getInstant

```java
public final
Instant
getInstant​(
String
name)
```

Returns the value of a timestamp field.

This method can be used on fields annotated with

@Timestamp

, and of
the following types:

long

,

int

,

short

,

char

and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** a timstamp represented as an

Instant

, not

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to an

Instant

object
**See Also:** hasField(String)

- getClass

```java
public final
RecordedClass
getClass​(
String
name)
```

Returns the value of a field of type

Class

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

RecordedClass

, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Class
**See Also:** hasField(String)

- getThread

```java
public final
RecordedThread
getThread​(
String
name)
```

Returns the value of a field of type

Thread

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

RecordedThread

object, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Thread
**See Also:** hasField(String)

- toString

```java
public final
String
toString()
```

Returns a textual representation of this object.

**Overrides:** toString

in class

Object
**Returns:** textual description of this object

Method Detail

- hasField

```java
public boolean hasField​(
String
name)
```

Returns

true

if a field with the given name exists,

false

otherwise.

**Parameters:** name

- name of the field to get, not

null
**Returns:** true

if the field exists,

false

otherwise.
**See Also:** getFields()

- getValue

```java
public final <T> T getValue​(
String
name)
```

Returns the value of the field with the given name.

The return type may be a primitive type or a subclass of

RecordedObject

.

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

**Type Parameters:** T

- the return type
**Parameters:** name

- of the field to get, not

null
**Returns:** the value, can be

null
**Throws:** IllegalArgumentException

- if no field called

name

exists
**See Also:** hasField(String)

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of the fields for this object.

**Returns:** the fields, not

null

- getBoolean

```java
public final boolean getBoolean​(
String
name)
```

Returns the value of a field of type

boolean

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- name of the field to get, not

null
**Returns:** the value of the field,

true

or

false
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

boolean
**See Also:** hasField(String)

,

getValue(String)

- getByte

```java
public final byte getByte​(
String
name)
```

Returns the value of a field of type

byte

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

byte
**See Also:** hasField(String)

,

getValue(String)

- getChar

```java
public final char getChar​(
String
name)
```

Returns the value of a field of type

char

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

char
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

char
**See Also:** hasField(String)

,

getValue(String)

- getShort

```java
public final short getShort​(
String
name)
```

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

This method can be used on the following types:

short

and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

short
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

short

by a widening
conversion
**See Also:** hasField(String)

- getInt

```java
public final int getInt​(
String
name)
```

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

This method can be used on fields of the following types:

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

int
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

int

by a widening
conversion
**See Also:** hasField(String)

- getFloat

```java
public final float getFloat​(
String
name)
```

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

This method can be used on fields of the following types:

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

float
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

float

by a widening
conversion
**See Also:** hasField(String)

- getLong

```java
public final long getLong​(
String
name)
```

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

This method can be used on fields of the following types:

long

,

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

long
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

long

via a widening
conversion
**See Also:** hasField(String)

- getDouble

```java
public final double getDouble​(
String
name)
```

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

This method can be used on fields of the following types:

double

,

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

double
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

double

by a widening
conversion
**See Also:** hasField(String)

- getString

```java
public final
String
getString​(
String
name)
```

Returns the value of a field of type

String

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

String

, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

String
**See Also:** hasField(String)

- getDuration

```java
public final
Duration
getDuration​(
String
name)
```

Returns the value of a timespan field.

This method can be used on fields annotated with

@Timespan

, and of
the following types:

long

,

int

,

short

,

char

,
and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** a time span represented as a

Duration

, not

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to a

Duration

object
**See Also:** hasField(String)

- getInstant

```java
public final
Instant
getInstant​(
String
name)
```

Returns the value of a timestamp field.

This method can be used on fields annotated with

@Timestamp

, and of
the following types:

long

,

int

,

short

,

char

and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** a timstamp represented as an

Instant

, not

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to an

Instant

object
**See Also:** hasField(String)

- getClass

```java
public final
RecordedClass
getClass​(
String
name)
```

Returns the value of a field of type

Class

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

RecordedClass

, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Class
**See Also:** hasField(String)

- getThread

```java
public final
RecordedThread
getThread​(
String
name)
```

Returns the value of a field of type

Thread

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

RecordedThread

object, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Thread
**See Also:** hasField(String)

- toString

```java
public final
String
toString()
```

Returns a textual representation of this object.

**Overrides:** toString

in class

Object
**Returns:** textual description of this object

---

#### Method Detail

hasField

```java
public boolean hasField​(
String
name)
```

Returns

true

if a field with the given name exists,

false

otherwise.

**Parameters:** name

- name of the field to get, not

null
**Returns:** true

if the field exists,

false

otherwise.
**See Also:** getFields()

---

#### hasField

public boolean hasField​(

String

name)

Returns

true

if a field with the given name exists,

false

otherwise.

getValue

```java
public final <T> T getValue​(
String
name)
```

Returns the value of the field with the given name.

The return type may be a primitive type or a subclass of

RecordedObject

.

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

**Type Parameters:** T

- the return type
**Parameters:** name

- of the field to get, not

null
**Returns:** the value, can be

null
**Throws:** IllegalArgumentException

- if no field called

name

exists
**See Also:** hasField(String)

---

#### getValue

public final <T> T getValue​(

String

name)

Returns the value of the field with the given name.

The return type may be a primitive type or a subclass of

RecordedObject

.

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

The return type may be a primitive type or a subclass of

RecordedObject

.

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

It's possible to index into a nested object by using

"."

(for
instance

"thread.group.parent.name

").

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

Example

```java
if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}
```

if (event.hasField("intValue")) {
int intValue = event.getValue("intValue");
System.out.println("Int value: " + intValue);
}

if (event.hasField("objectClass")) {
RecordedClass clazz = event.getValue("objectClass");
System.out.println("Class name: " + clazz.getName());
}

if (event.hasField("sampledThread")) {
RecordedThread sampledThread = event.getValue("sampledThread");
System.out.println("Sampled thread: " + sampledThread.getName());
}

getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns an immutable list of the fields for this object.

**Returns:** the fields, not

null

---

#### getFields

public

List

<

ValueDescriptor

> getFields()

Returns an immutable list of the fields for this object.

getBoolean

```java
public final boolean getBoolean​(
String
name)
```

Returns the value of a field of type

boolean

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- name of the field to get, not

null
**Returns:** the value of the field,

true

or

false
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

boolean
**See Also:** hasField(String)

,

getValue(String)

---

#### getBoolean

public final boolean getBoolean​(

String

name)

Returns the value of a field of type

boolean

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getByte

```java
public final byte getByte​(
String
name)
```

Returns the value of a field of type

byte

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

byte
**See Also:** hasField(String)

,

getValue(String)

---

#### getByte

public final byte getByte​(

String

name)

Returns the value of a field of type

byte

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getChar

```java
public final char getChar​(
String
name)
```

Returns the value of a field of type

char

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

char
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field is
not of type

char
**See Also:** hasField(String)

,

getValue(String)

---

#### getChar

public final char getChar​(

String

name)

Returns the value of a field of type

char

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getShort

```java
public final short getShort​(
String
name)
```

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

This method can be used on the following types:

short

and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

short
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

short

by a widening
conversion
**See Also:** hasField(String)

---

#### getShort

public final short getShort​(

String

name)

Returns the value of a field of type

short

or of another primitive
type convertible to type

short

by a widening conversion.

This method can be used on the following types:

short

and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on the following types:

short

and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

If the field has the

@Unsigned

annotation and is of a narrower type
than

short

, then the value is returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getInt

```java
public final int getInt​(
String
name)
```

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

This method can be used on fields of the following types:

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

int
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

int

by a widening
conversion
**See Also:** hasField(String)

---

#### getInt

public final int getInt​(

String

name)

Returns the value of a field of type

int

or of another primitive type
that is convertible to type

int

by a widening conversion.

This method can be used on fields of the following types:

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on fields of the following types:

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

If the field has the

@Unsigned

annotation and is of a narrower type
than

int

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getFloat

```java
public final float getFloat​(
String
name)
```

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

This method can be used on fields of the following types:

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

float
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

float

by a widening
conversion
**See Also:** hasField(String)

---

#### getFloat

public final float getFloat​(

String

name)

Returns the value of a field of type

float

or of another primitive
type convertible to type

float

by a widening conversion.

This method can be used on fields of the following types:

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on fields of the following types:

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getLong

```java
public final long getLong​(
String
name)
```

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

This method can be used on fields of the following types:

long

,

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

long
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

long

via a widening
conversion
**See Also:** hasField(String)

---

#### getLong

public final long getLong​(

String

name)

Returns the value of a field of type

long

or of another primitive
type that is convertible to type

long

by a widening conversion.

This method can be used on fields of the following types:

long

,

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on fields of the following types:

long

,

int

,

short

,

char

, and

byte

.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

If the field has the

@Unsigned

annotation and is of a narrower type
than

long

, then the value will be returned as an unsigned.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getDouble

```java
public final double getDouble​(
String
name)
```

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

This method can be used on fields of the following types:

double

,

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field converted to type

double
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to the type

double

by a widening
conversion
**See Also:** hasField(String)

---

#### getDouble

public final double getDouble​(

String

name)

Returns the value of a field of type

double

or of another primitive
type that is convertible to type

double

by a widening conversion.

This method can be used on fields of the following types:

double

,

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on fields of the following types:

double

,

float

,

long

,

int

,

short

,

char

, and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getString

```java
public final
String
getString​(
String
name)
```

Returns the value of a field of type

String

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

String

, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

String
**See Also:** hasField(String)

---

#### getString

public final

String

getString​(

String

name)

Returns the value of a field of type

String

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getDuration

```java
public final
Duration
getDuration​(
String
name)
```

Returns the value of a timespan field.

This method can be used on fields annotated with

@Timespan

, and of
the following types:

long

,

int

,

short

,

char

,
and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** a time span represented as a

Duration

, not

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to a

Duration

object
**See Also:** hasField(String)

---

#### getDuration

public final

Duration

getDuration​(

String

name)

Returns the value of a timespan field.

This method can be used on fields annotated with

@Timespan

, and of
the following types:

long

,

int

,

short

,

char

,
and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on fields annotated with

@Timespan

, and of
the following types:

long

,

int

,

short

,

char

,
and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getInstant

```java
public final
Instant
getInstant​(
String
name)
```

Returns the value of a timestamp field.

This method can be used on fields annotated with

@Timestamp

, and of
the following types:

long

,

int

,

short

,

char

and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** a timstamp represented as an

Instant

, not

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
value can't be converted to an

Instant

object
**See Also:** hasField(String)

---

#### getInstant

public final

Instant

getInstant​(

String

name)

Returns the value of a timestamp field.

This method can be used on fields annotated with

@Timestamp

, and of
the following types:

long

,

int

,

short

,

char

and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

This method can be used on fields annotated with

@Timestamp

, and of
the following types:

long

,

int

,

short

,

char

and

byte

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getClass

```java
public final
RecordedClass
getClass​(
String
name)
```

Returns the value of a field of type

Class

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

RecordedClass

, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Class
**See Also:** hasField(String)

---

#### getClass

public final

RecordedClass

getClass​(

String

name)

Returns the value of a field of type

Class

.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"aaa.bbb"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

getThread

```java
public final
RecordedThread
getThread​(
String
name)
```

Returns the value of a field of type

Thread

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

**Parameters:** name

- of the field to get, not

null
**Returns:** the value of the field as a

RecordedThread

object, can be

null
**Throws:** IllegalArgumentException

- if the field doesn't exist, or the field
isn't of type

Thread
**See Also:** hasField(String)

---

#### getThread

public final

RecordedThread

getThread​(

String

name)

Returns the value of a field of type

Thread

.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

It's possible to index into a nested object using

"."

(for example,

"foo.bar"

).

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

A field might change or be removed in a future JDK release. A best practice
for callers of this method is to validate the field before attempting access.

toString

```java
public final
String
toString()
```

Returns a textual representation of this object.

**Overrides:** toString

in class

Object
**Returns:** textual description of this object

---

#### toString

public final

String

toString()

Returns a textual representation of this object.

---

