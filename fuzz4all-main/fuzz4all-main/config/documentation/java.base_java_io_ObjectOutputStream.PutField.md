# Class ObjectOutputStream.PutField

**Source:** `java.base\java\io\ObjectOutputStream.PutField.html`

### Class Description

```java
public abstract static class
ObjectOutputStream.PutField

extends
Object
```

Provide programmatic access to the persistent fields to be written
to ObjectOutput.

**Enclosing class:** ObjectOutputStream

---

### Field Details

*No entries found.*

### Constructor Details

#### public PutField()

*No description found.*

---

### Method Details

#### public abstract void put​(
String
name,
boolean val)

Put the value of the named boolean field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

boolean

---

#### public abstract void put​(
String
name,
byte val)

Put the value of the named byte field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

byte

---

#### public abstract void put​(
String
name,
char val)

Put the value of the named char field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

char

---

#### public abstract void put​(
String
name,
short val)

Put the value of the named short field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

short

---

#### public abstract void put​(
String
name,
int val)

Put the value of the named int field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

int

---

#### public abstract void put​(
String
name,
long val)

Put the value of the named long field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

long

---

#### public abstract void put​(
String
name,
float val)

Put the value of the named float field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

float

---

#### public abstract void put​(
String
name,
double val)

Put the value of the named double field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

double

---

#### public abstract void put​(
String
name,

Object
val)

Put the value of the named Object field into the persistent field.

**Parameters:**
- name

- the name of the serializable field
- val

- the value to assign to the field
(which may be

null

)

**Throws:**
- IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not a
reference type

---

#### @Deprecated

public abstract void write​(
ObjectOutput
out)
throws
IOException

Write the data and fields to the specified ObjectOutput stream,
which must be the same stream that produced this

PutField

object.

**Parameters:**
- out

- the stream to write the data and fields to

**Throws:**
- IOException

- if I/O errors occur while writing to the
underlying stream
- IllegalArgumentException

- if the specified stream is not
the same stream that produced this

PutField

object

---

### Additional Sections

#### Class ObjectOutputStream.PutField

java.lang.Object

- java.io.ObjectOutputStream.PutField

java.io.ObjectOutputStream.PutField

**Enclosing class:** ObjectOutputStream

```java
public abstract static class
ObjectOutputStream.PutField

extends
Object
```

Provide programmatic access to the persistent fields to be written
to ObjectOutput.

**Since:** 1.2

public abstract static class

ObjectOutputStream.PutField

extends

Object

Provide programmatic access to the persistent fields to be written
to ObjectOutput.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PutField

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

put

​(

String

name,
boolean val)

Put the value of the named boolean field into the persistent field.

abstract void

put

​(

String

name,
byte val)

Put the value of the named byte field into the persistent field.

abstract void

put

​(

String

name,
char val)

Put the value of the named char field into the persistent field.

abstract void

put

​(

String

name,
double val)

Put the value of the named double field into the persistent field.

abstract void

put

​(

String

name,
float val)

Put the value of the named float field into the persistent field.

abstract void

put

​(

String

name,
int val)

Put the value of the named int field into the persistent field.

abstract void

put

​(

String

name,
long val)

Put the value of the named long field into the persistent field.

abstract void

put

​(

String

name,
short val)

Put the value of the named short field into the persistent field.

abstract void

put

​(

String

name,

Object

val)

Put the value of the named Object field into the persistent field.

abstract void

write

​(

ObjectOutput

out)

Deprecated.

This method does not write the values contained by this

PutField

object in a proper format, and may
result in corruption of the serialization stream.

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

PutField

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

put

​(

String

name,
boolean val)

Put the value of the named boolean field into the persistent field.

abstract void

put

​(

String

name,
byte val)

Put the value of the named byte field into the persistent field.

abstract void

put

​(

String

name,
char val)

Put the value of the named char field into the persistent field.

abstract void

put

​(

String

name,
double val)

Put the value of the named double field into the persistent field.

abstract void

put

​(

String

name,
float val)

Put the value of the named float field into the persistent field.

abstract void

put

​(

String

name,
int val)

Put the value of the named int field into the persistent field.

abstract void

put

​(

String

name,
long val)

Put the value of the named long field into the persistent field.

abstract void

put

​(

String

name,
short val)

Put the value of the named short field into the persistent field.

abstract void

put

​(

String

name,

Object

val)

Put the value of the named Object field into the persistent field.

abstract void

write

​(

ObjectOutput

out)

Deprecated.

This method does not write the values contained by this

PutField

object in a proper format, and may
result in corruption of the serialization stream.

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

Put the value of the named boolean field into the persistent field.

Put the value of the named byte field into the persistent field.

Put the value of the named char field into the persistent field.

Put the value of the named double field into the persistent field.

Put the value of the named float field into the persistent field.

Put the value of the named int field into the persistent field.

Put the value of the named long field into the persistent field.

Put the value of the named short field into the persistent field.

Put the value of the named Object field into the persistent field.

Deprecated.

This method does not write the values contained by this

PutField

object in a proper format, and may
result in corruption of the serialization stream.

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

- PutField

```java
public PutField()
```

============ METHOD DETAIL ==========

- Method Detail

- put

```java
public abstract void put​(
String
name,
boolean val)
```

Put the value of the named boolean field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

boolean

- put

```java
public abstract void put​(
String
name,
byte val)
```

Put the value of the named byte field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

byte

- put

```java
public abstract void put​(
String
name,
char val)
```

Put the value of the named char field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

char

- put

```java
public abstract void put​(
String
name,
short val)
```

Put the value of the named short field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

short

- put

```java
public abstract void put​(
String
name,
int val)
```

Put the value of the named int field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

int

- put

```java
public abstract void put​(
String
name,
long val)
```

Put the value of the named long field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

long

- put

```java
public abstract void put​(
String
name,
float val)
```

Put the value of the named float field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

float

- put

```java
public abstract void put​(
String
name,
double val)
```

Put the value of the named double field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

double

- put

```java
public abstract void put​(
String
name,

Object
val)
```

Put the value of the named Object field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
(which may be

null

)
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not a
reference type

- write

```java
@Deprecated

public abstract void write​(
ObjectOutput
out)
throws
IOException
```

Deprecated.

This method does not write the values contained by this

PutField

object in a proper format, and may
result in corruption of the serialization stream. The
correct way to write

PutField

data is by
calling the

ObjectOutputStream.writeFields()

method.

Write the data and fields to the specified ObjectOutput stream,
which must be the same stream that produced this

PutField

object.

**Parameters:** out

- the stream to write the data and fields to
**Throws:** IOException

- if I/O errors occur while writing to the
underlying stream
**Throws:** IllegalArgumentException

- if the specified stream is not
the same stream that produced this

PutField

object

Constructor Detail

- PutField

```java
public PutField()
```

---

#### Constructor Detail

PutField

```java
public PutField()
```

---

#### PutField

public PutField()

Method Detail

- put

```java
public abstract void put​(
String
name,
boolean val)
```

Put the value of the named boolean field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

boolean

- put

```java
public abstract void put​(
String
name,
byte val)
```

Put the value of the named byte field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

byte

- put

```java
public abstract void put​(
String
name,
char val)
```

Put the value of the named char field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

char

- put

```java
public abstract void put​(
String
name,
short val)
```

Put the value of the named short field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

short

- put

```java
public abstract void put​(
String
name,
int val)
```

Put the value of the named int field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

int

- put

```java
public abstract void put​(
String
name,
long val)
```

Put the value of the named long field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

long

- put

```java
public abstract void put​(
String
name,
float val)
```

Put the value of the named float field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

float

- put

```java
public abstract void put​(
String
name,
double val)
```

Put the value of the named double field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

double

- put

```java
public abstract void put​(
String
name,

Object
val)
```

Put the value of the named Object field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
(which may be

null

)
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not a
reference type

- write

```java
@Deprecated

public abstract void write​(
ObjectOutput
out)
throws
IOException
```

Deprecated.

This method does not write the values contained by this

PutField

object in a proper format, and may
result in corruption of the serialization stream. The
correct way to write

PutField

data is by
calling the

ObjectOutputStream.writeFields()

method.

Write the data and fields to the specified ObjectOutput stream,
which must be the same stream that produced this

PutField

object.

**Parameters:** out

- the stream to write the data and fields to
**Throws:** IOException

- if I/O errors occur while writing to the
underlying stream
**Throws:** IllegalArgumentException

- if the specified stream is not
the same stream that produced this

PutField

object

---

#### Method Detail

put

```java
public abstract void put​(
String
name,
boolean val)
```

Put the value of the named boolean field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

boolean

---

#### put

public abstract void put​(

String

name,
boolean val)

Put the value of the named boolean field into the persistent field.

put

```java
public abstract void put​(
String
name,
byte val)
```

Put the value of the named byte field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

byte

---

#### put

public abstract void put​(

String

name,
byte val)

Put the value of the named byte field into the persistent field.

put

```java
public abstract void put​(
String
name,
char val)
```

Put the value of the named char field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

char

---

#### put

public abstract void put​(

String

name,
char val)

Put the value of the named char field into the persistent field.

put

```java
public abstract void put​(
String
name,
short val)
```

Put the value of the named short field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

short

---

#### put

public abstract void put​(

String

name,
short val)

Put the value of the named short field into the persistent field.

put

```java
public abstract void put​(
String
name,
int val)
```

Put the value of the named int field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

int

---

#### put

public abstract void put​(

String

name,
int val)

Put the value of the named int field into the persistent field.

put

```java
public abstract void put​(
String
name,
long val)
```

Put the value of the named long field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

long

---

#### put

public abstract void put​(

String

name,
long val)

Put the value of the named long field into the persistent field.

put

```java
public abstract void put​(
String
name,
float val)
```

Put the value of the named float field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

float

---

#### put

public abstract void put​(

String

name,
float val)

Put the value of the named float field into the persistent field.

put

```java
public abstract void put​(
String
name,
double val)
```

Put the value of the named double field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not

double

---

#### put

public abstract void put​(

String

name,
double val)

Put the value of the named double field into the persistent field.

put

```java
public abstract void put​(
String
name,

Object
val)
```

Put the value of the named Object field into the persistent field.

**Parameters:** name

- the name of the serializable field
**Parameters:** val

- the value to assign to the field
(which may be

null

)
**Throws:** IllegalArgumentException

- if

name

does not
match the name of a serializable field for the class whose fields
are being written, or if the type of the named field is not a
reference type

---

#### put

public abstract void put​(

String

name,

Object

val)

Put the value of the named Object field into the persistent field.

write

```java
@Deprecated

public abstract void write​(
ObjectOutput
out)
throws
IOException
```

Deprecated.

This method does not write the values contained by this

PutField

object in a proper format, and may
result in corruption of the serialization stream. The
correct way to write

PutField

data is by
calling the

ObjectOutputStream.writeFields()

method.

Write the data and fields to the specified ObjectOutput stream,
which must be the same stream that produced this

PutField

object.

**Parameters:** out

- the stream to write the data and fields to
**Throws:** IOException

- if I/O errors occur while writing to the
underlying stream
**Throws:** IllegalArgumentException

- if the specified stream is not
the same stream that produced this

PutField

object

---

#### write

@Deprecated

public abstract void write​(

ObjectOutput

out)
throws

IOException

Write the data and fields to the specified ObjectOutput stream,
which must be the same stream that produced this

PutField

object.

---

