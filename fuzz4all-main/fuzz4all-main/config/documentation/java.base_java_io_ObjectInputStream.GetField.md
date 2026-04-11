# Class ObjectInputStream.GetField

**Source:** `java.base\java\io\ObjectInputStream.GetField.html`

### Class Description

```java
public abstract static class
ObjectInputStream.GetField

extends
Object
```

Provide access to the persistent fields read from the input stream.

**Enclosing class:** ObjectInputStream

---

### Field Details

*No entries found.*

### Constructor Details

#### public GetField()

*No description found.*

---

### Method Details

#### public abstract
ObjectStreamClass
getObjectStreamClass()

Get the ObjectStreamClass that describes the fields in the stream.

**Returns:**
- the descriptor class that describes the serializable fields

---

#### public abstract boolean defaulted​(
String
name)
throws
IOException

Return true if the named field is defaulted and has no value in this
stream.

**Parameters:**
- name

- the name of the field

**Returns:**
- true, if and only if the named field is defaulted

**Throws:**
- IOException

- if there are I/O errors while reading from
the underlying

InputStream
- IllegalArgumentException

- if

name

does not
correspond to a serializable field

---

#### public abstract boolean get​(
String
name,
boolean val)
throws
IOException

Get the value of the named boolean field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

boolean

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract byte get​(
String
name,
byte val)
throws
IOException

Get the value of the named byte field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

byte

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract char get​(
String
name,
char val)
throws
IOException

Get the value of the named char field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

char

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract short get​(
String
name,
short val)
throws
IOException

Get the value of the named short field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

short

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract int get​(
String
name,
int val)
throws
IOException

Get the value of the named int field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

int

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract long get​(
String
name,
long val)
throws
IOException

Get the value of the named long field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

long

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract float get​(
String
name,
float val)
throws
IOException

Get the value of the named float field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

float

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract double get​(
String
name,
double val)
throws
IOException

Get the value of the named double field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

double

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### public abstract
Object
get​(
String
name,

Object
val)
throws
IOException

Get the value of the named Object field from the persistent field.

**Parameters:**
- name

- the name of the field
- val

- the default value to use if

name

does not
have a value

**Returns:**
- the value of the named

Object

field

**Throws:**
- IOException

- if there are I/O errors while reading from the
underlying

InputStream
- IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

### Additional Sections

#### Class ObjectInputStream.GetField

java.lang.Object

- java.io.ObjectInputStream.GetField

java.io.ObjectInputStream.GetField

**Enclosing class:** ObjectInputStream

```java
public abstract static class
ObjectInputStream.GetField

extends
Object
```

Provide access to the persistent fields read from the input stream.

public abstract static class

ObjectInputStream.GetField

extends

Object

Provide access to the persistent fields read from the input stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GetField

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

defaulted

​(

String

name)

Return true if the named field is defaulted and has no value in this
stream.

abstract boolean

get

​(

String

name,
boolean val)

Get the value of the named boolean field from the persistent field.

abstract byte

get

​(

String

name,
byte val)

Get the value of the named byte field from the persistent field.

abstract char

get

​(

String

name,
char val)

Get the value of the named char field from the persistent field.

abstract double

get

​(

String

name,
double val)

Get the value of the named double field from the persistent field.

abstract float

get

​(

String

name,
float val)

Get the value of the named float field from the persistent field.

abstract int

get

​(

String

name,
int val)

Get the value of the named int field from the persistent field.

abstract long

get

​(

String

name,
long val)

Get the value of the named long field from the persistent field.

abstract short

get

​(

String

name,
short val)

Get the value of the named short field from the persistent field.

abstract

Object

get

​(

String

name,

Object

val)

Get the value of the named Object field from the persistent field.

abstract

ObjectStreamClass

getObjectStreamClass

()

Get the ObjectStreamClass that describes the fields in the stream.

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

GetField

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

defaulted

​(

String

name)

Return true if the named field is defaulted and has no value in this
stream.

abstract boolean

get

​(

String

name,
boolean val)

Get the value of the named boolean field from the persistent field.

abstract byte

get

​(

String

name,
byte val)

Get the value of the named byte field from the persistent field.

abstract char

get

​(

String

name,
char val)

Get the value of the named char field from the persistent field.

abstract double

get

​(

String

name,
double val)

Get the value of the named double field from the persistent field.

abstract float

get

​(

String

name,
float val)

Get the value of the named float field from the persistent field.

abstract int

get

​(

String

name,
int val)

Get the value of the named int field from the persistent field.

abstract long

get

​(

String

name,
long val)

Get the value of the named long field from the persistent field.

abstract short

get

​(

String

name,
short val)

Get the value of the named short field from the persistent field.

abstract

Object

get

​(

String

name,

Object

val)

Get the value of the named Object field from the persistent field.

abstract

ObjectStreamClass

getObjectStreamClass

()

Get the ObjectStreamClass that describes the fields in the stream.

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

Return true if the named field is defaulted and has no value in this
stream.

Get the value of the named boolean field from the persistent field.

Get the value of the named byte field from the persistent field.

Get the value of the named char field from the persistent field.

Get the value of the named double field from the persistent field.

Get the value of the named float field from the persistent field.

Get the value of the named int field from the persistent field.

Get the value of the named long field from the persistent field.

Get the value of the named short field from the persistent field.

Get the value of the named Object field from the persistent field.

Get the ObjectStreamClass that describes the fields in the stream.

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

- GetField

```java
public GetField()
```

============ METHOD DETAIL ==========

- Method Detail

- getObjectStreamClass

```java
public abstract
ObjectStreamClass
getObjectStreamClass()
```

Get the ObjectStreamClass that describes the fields in the stream.

**Returns:** the descriptor class that describes the serializable fields

- defaulted

```java
public abstract boolean defaulted​(
String
name)
throws
IOException
```

Return true if the named field is defaulted and has no value in this
stream.

**Parameters:** name

- the name of the field
**Returns:** true, if and only if the named field is defaulted
**Throws:** IOException

- if there are I/O errors while reading from
the underlying

InputStream
**Throws:** IllegalArgumentException

- if

name

does not
correspond to a serializable field

- get

```java
public abstract boolean get​(
String
name,
boolean val)
throws
IOException
```

Get the value of the named boolean field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

boolean

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract byte get​(
String
name,
byte val)
throws
IOException
```

Get the value of the named byte field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

byte

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract char get​(
String
name,
char val)
throws
IOException
```

Get the value of the named char field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

char

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract short get​(
String
name,
short val)
throws
IOException
```

Get the value of the named short field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

short

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract int get​(
String
name,
int val)
throws
IOException
```

Get the value of the named int field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

int

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract long get​(
String
name,
long val)
throws
IOException
```

Get the value of the named long field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

long

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract float get​(
String
name,
float val)
throws
IOException
```

Get the value of the named float field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

float

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract double get​(
String
name,
double val)
throws
IOException
```

Get the value of the named double field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

double

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract
Object
get​(
String
name,

Object
val)
throws
IOException
```

Get the value of the named Object field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

Object

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

Constructor Detail

- GetField

```java
public GetField()
```

---

#### Constructor Detail

GetField

```java
public GetField()
```

---

#### GetField

public GetField()

Method Detail

- getObjectStreamClass

```java
public abstract
ObjectStreamClass
getObjectStreamClass()
```

Get the ObjectStreamClass that describes the fields in the stream.

**Returns:** the descriptor class that describes the serializable fields

- defaulted

```java
public abstract boolean defaulted​(
String
name)
throws
IOException
```

Return true if the named field is defaulted and has no value in this
stream.

**Parameters:** name

- the name of the field
**Returns:** true, if and only if the named field is defaulted
**Throws:** IOException

- if there are I/O errors while reading from
the underlying

InputStream
**Throws:** IllegalArgumentException

- if

name

does not
correspond to a serializable field

- get

```java
public abstract boolean get​(
String
name,
boolean val)
throws
IOException
```

Get the value of the named boolean field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

boolean

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract byte get​(
String
name,
byte val)
throws
IOException
```

Get the value of the named byte field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

byte

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract char get​(
String
name,
char val)
throws
IOException
```

Get the value of the named char field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

char

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract short get​(
String
name,
short val)
throws
IOException
```

Get the value of the named short field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

short

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract int get​(
String
name,
int val)
throws
IOException
```

Get the value of the named int field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

int

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract long get​(
String
name,
long val)
throws
IOException
```

Get the value of the named long field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

long

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract float get​(
String
name,
float val)
throws
IOException
```

Get the value of the named float field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

float

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract double get​(
String
name,
double val)
throws
IOException
```

Get the value of the named double field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

double

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

- get

```java
public abstract
Object
get​(
String
name,

Object
val)
throws
IOException
```

Get the value of the named Object field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

Object

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### Method Detail

getObjectStreamClass

```java
public abstract
ObjectStreamClass
getObjectStreamClass()
```

Get the ObjectStreamClass that describes the fields in the stream.

**Returns:** the descriptor class that describes the serializable fields

---

#### getObjectStreamClass

public abstract

ObjectStreamClass

getObjectStreamClass()

Get the ObjectStreamClass that describes the fields in the stream.

defaulted

```java
public abstract boolean defaulted​(
String
name)
throws
IOException
```

Return true if the named field is defaulted and has no value in this
stream.

**Parameters:** name

- the name of the field
**Returns:** true, if and only if the named field is defaulted
**Throws:** IOException

- if there are I/O errors while reading from
the underlying

InputStream
**Throws:** IllegalArgumentException

- if

name

does not
correspond to a serializable field

---

#### defaulted

public abstract boolean defaulted​(

String

name)
throws

IOException

Return true if the named field is defaulted and has no value in this
stream.

get

```java
public abstract boolean get​(
String
name,
boolean val)
throws
IOException
```

Get the value of the named boolean field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

boolean

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract boolean get​(

String

name,
boolean val)
throws

IOException

Get the value of the named boolean field from the persistent field.

get

```java
public abstract byte get​(
String
name,
byte val)
throws
IOException
```

Get the value of the named byte field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

byte

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract byte get​(

String

name,
byte val)
throws

IOException

Get the value of the named byte field from the persistent field.

get

```java
public abstract char get​(
String
name,
char val)
throws
IOException
```

Get the value of the named char field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

char

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract char get​(

String

name,
char val)
throws

IOException

Get the value of the named char field from the persistent field.

get

```java
public abstract short get​(
String
name,
short val)
throws
IOException
```

Get the value of the named short field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

short

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract short get​(

String

name,
short val)
throws

IOException

Get the value of the named short field from the persistent field.

get

```java
public abstract int get​(
String
name,
int val)
throws
IOException
```

Get the value of the named int field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

int

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract int get​(

String

name,
int val)
throws

IOException

Get the value of the named int field from the persistent field.

get

```java
public abstract long get​(
String
name,
long val)
throws
IOException
```

Get the value of the named long field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

long

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract long get​(

String

name,
long val)
throws

IOException

Get the value of the named long field from the persistent field.

get

```java
public abstract float get​(
String
name,
float val)
throws
IOException
```

Get the value of the named float field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

float

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract float get​(

String

name,
float val)
throws

IOException

Get the value of the named float field from the persistent field.

get

```java
public abstract double get​(
String
name,
double val)
throws
IOException
```

Get the value of the named double field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

double

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract double get​(

String

name,
double val)
throws

IOException

Get the value of the named double field from the persistent field.

get

```java
public abstract
Object
get​(
String
name,

Object
val)
throws
IOException
```

Get the value of the named Object field from the persistent field.

**Parameters:** name

- the name of the field
**Parameters:** val

- the default value to use if

name

does not
have a value
**Returns:** the value of the named

Object

field
**Throws:** IOException

- if there are I/O errors while reading from the
underlying

InputStream
**Throws:** IllegalArgumentException

- if type of

name

is
not serializable or if the field type is incorrect

---

#### get

public abstract

Object

get​(

String

name,

Object

val)
throws

IOException

Get the value of the named Object field from the persistent field.

---

