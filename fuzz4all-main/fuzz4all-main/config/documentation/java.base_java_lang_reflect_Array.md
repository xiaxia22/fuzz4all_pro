# Class Array

**Source:** `java.base\java\lang\reflect\Array.html`

### Class Description

```java
public final class
Array

extends
Object
```

The

Array

class provides static methods to dynamically create and
access Java arrays.

Array

permits widening conversions to occur during a get or set
operation, but throws an

IllegalArgumentException

if a narrowing
conversion would occur.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Object
newInstance​(
Class
<?> componentType,
int length)
throws
NegativeArraySizeException

Creates a new array with the specified component type and
length.
Invoking this method is equivalent to creating an array
as follows:

```java
int[] x = {length};
Array.newInstance(componentType, x);
```

The number of dimensions of the new array must not
exceed 255.

**Parameters:**
- componentType

- the

Class

object representing the
component type of the new array
- length

- the length of the new array

**Returns:**
- the new array

**Throws:**
- NullPointerException

- if the specified

componentType

parameter is null
- IllegalArgumentException

- if componentType is

Void.TYPE

or if the number of dimensions of the requested array
instance exceed 255.
- NegativeArraySizeException

- if the specified

length

is negative

---

#### public static
Object
newInstance​(
Class
<?> componentType,
int... dimensions)
throws
IllegalArgumentException
,

NegativeArraySizeException

Creates a new array
with the specified component type and dimensions.
If

componentType

represents a non-array class or interface, the new array
has

dimensions.length

dimensions and

componentType

as its component type. If

componentType

represents an array class, the
number of dimensions of the new array is equal to the sum
of

dimensions.length

and the number of
dimensions of

componentType

. In this case, the
component type of the new array is the component type of

componentType

.

The number of dimensions of the new array must not
exceed 255.

**Parameters:**
- componentType

- the

Class

object representing the component
type of the new array
- dimensions

- an array of

int

representing the dimensions of
the new array

**Returns:**
- the new array

**Throws:**
- NullPointerException

- if the specified

componentType

argument is null
- IllegalArgumentException

- if the specified

dimensions

argument is a zero-dimensional array, if componentType is

Void.TYPE

, or if the number of dimensions of the requested array
instance exceed 255.
- NegativeArraySizeException

- if any of the components in
the specified

dimensions

argument is negative.

---

#### public static int getLength​(
Object
array)
throws
IllegalArgumentException

Returns the length of the specified array object, as an

int

.

**Parameters:**
- array

- the array

**Returns:**
- the length of the array

**Throws:**
- IllegalArgumentException

- if the object argument is not
an array

---

#### public static
Object
get​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object. The value is automatically wrapped in an object
if it has a primitive type.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the (possibly wrapped) value of the indexed component in
the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

---

#### public static boolean getBoolean​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

boolean

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static byte getByte​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

byte

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static char getChar​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

char

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static short getShort​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

short

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static int getInt​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as an

int

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static long getLong​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

long

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static float getFloat​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

float

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static double getDouble​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

double

.

**Parameters:**
- array

- the array
- index

- the index

**Returns:**
- the value of the indexed component in the specified array

**Throws:**
- NullPointerException

- If the specified object is null
- IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

**See Also:**
- get(java.lang.Object, int)

---

#### public static void set​(
Object
array,
int index,

Object
value)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified new value. The new value is first
automatically unwrapped if the array has a primitive component
type.

**Parameters:**
- array

- the array
- index

- the index into the array
- value

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the array component type is primitive and
an unwrapping conversion fails
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

---

#### public static void setBoolean​(
Object
array,
int index,
boolean z)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- z

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setByte​(
Object
array,
int index,
byte b)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- b

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setChar​(
Object
array,
int index,
char c)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

char

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- c

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setShort​(
Object
array,
int index,
short s)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

short

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- s

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setInt​(
Object
array,
int index,
int i)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

int

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- i

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setLong​(
Object
array,
int index,
long l)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

long

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- l

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setFloat​(
Object
array,
int index,
float f)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

float

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- f

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

#### public static void setDouble​(
Object
array,
int index,
double d)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

double

value.

**Parameters:**
- array

- the array
- index

- the index into the array
- d

- the new value of the indexed component

**Throws:**
- NullPointerException

- If the specified object argument
is null
- IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
- ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

**See Also:**
- set(java.lang.Object, int, java.lang.Object)

---

### Additional Sections

#### Class Array

java.lang.Object

- java.lang.reflect.Array

java.lang.reflect.Array

```java
public final class
Array

extends
Object
```

The

Array

class provides static methods to dynamically create and
access Java arrays.

Array

permits widening conversions to occur during a get or set
operation, but throws an

IllegalArgumentException

if a narrowing
conversion would occur.

**Since:** 1.1

public final class

Array

extends

Object

The

Array

class provides static methods to dynamically create and
access Java arrays.

Array

permits widening conversions to occur during a get or set
operation, but throws an

IllegalArgumentException

if a narrowing
conversion would occur.

Array

permits widening conversions to occur during a get or set
operation, but throws an

IllegalArgumentException

if a narrowing
conversion would occur.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Object

get

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object.

static boolean

getBoolean

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

boolean

.

static byte

getByte

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

byte

.

static char

getChar

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

char

.

static double

getDouble

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

double

.

static float

getFloat

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

float

.

static int

getInt

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as an

int

.

static int

getLength

​(

Object

array)

Returns the length of the specified array object, as an

int

.

static long

getLong

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

long

.

static short

getShort

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

short

.

static

Object

newInstance

​(

Class

<?> componentType,
int length)

Creates a new array with the specified component type and
length.

static

Object

newInstance

​(

Class

<?> componentType,
int... dimensions)

Creates a new array
with the specified component type and dimensions.

static void

set

​(

Object

array,
int index,

Object

value)

Sets the value of the indexed component of the specified array
object to the specified new value.

static void

setBoolean

​(

Object

array,
int index,
boolean z)

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

static void

setByte

​(

Object

array,
int index,
byte b)

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

static void

setChar

​(

Object

array,
int index,
char c)

Sets the value of the indexed component of the specified array
object to the specified

char

value.

static void

setDouble

​(

Object

array,
int index,
double d)

Sets the value of the indexed component of the specified array
object to the specified

double

value.

static void

setFloat

​(

Object

array,
int index,
float f)

Sets the value of the indexed component of the specified array
object to the specified

float

value.

static void

setInt

​(

Object

array,
int index,
int i)

Sets the value of the indexed component of the specified array
object to the specified

int

value.

static void

setLong

​(

Object

array,
int index,
long l)

Sets the value of the indexed component of the specified array
object to the specified

long

value.

static void

setShort

​(

Object

array,
int index,
short s)

Sets the value of the indexed component of the specified array
object to the specified

short

value.

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

Concrete Methods

Modifier and Type

Method

Description

static

Object

get

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object.

static boolean

getBoolean

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

boolean

.

static byte

getByte

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

byte

.

static char

getChar

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

char

.

static double

getDouble

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

double

.

static float

getFloat

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

float

.

static int

getInt

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as an

int

.

static int

getLength

​(

Object

array)

Returns the length of the specified array object, as an

int

.

static long

getLong

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

long

.

static short

getShort

​(

Object

array,
int index)

Returns the value of the indexed component in the specified
array object, as a

short

.

static

Object

newInstance

​(

Class

<?> componentType,
int length)

Creates a new array with the specified component type and
length.

static

Object

newInstance

​(

Class

<?> componentType,
int... dimensions)

Creates a new array
with the specified component type and dimensions.

static void

set

​(

Object

array,
int index,

Object

value)

Sets the value of the indexed component of the specified array
object to the specified new value.

static void

setBoolean

​(

Object

array,
int index,
boolean z)

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

static void

setByte

​(

Object

array,
int index,
byte b)

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

static void

setChar

​(

Object

array,
int index,
char c)

Sets the value of the indexed component of the specified array
object to the specified

char

value.

static void

setDouble

​(

Object

array,
int index,
double d)

Sets the value of the indexed component of the specified array
object to the specified

double

value.

static void

setFloat

​(

Object

array,
int index,
float f)

Sets the value of the indexed component of the specified array
object to the specified

float

value.

static void

setInt

​(

Object

array,
int index,
int i)

Sets the value of the indexed component of the specified array
object to the specified

int

value.

static void

setLong

​(

Object

array,
int index,
long l)

Sets the value of the indexed component of the specified array
object to the specified

long

value.

static void

setShort

​(

Object

array,
int index,
short s)

Sets the value of the indexed component of the specified array
object to the specified

short

value.

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

Returns the value of the indexed component in the specified
array object.

Returns the value of the indexed component in the specified
array object, as a

boolean

.

Returns the value of the indexed component in the specified
array object, as a

byte

.

Returns the value of the indexed component in the specified
array object, as a

char

.

Returns the value of the indexed component in the specified
array object, as a

double

.

Returns the value of the indexed component in the specified
array object, as a

float

.

Returns the value of the indexed component in the specified
array object, as an

int

.

Returns the length of the specified array object, as an

int

.

Returns the value of the indexed component in the specified
array object, as a

long

.

Returns the value of the indexed component in the specified
array object, as a

short

.

Creates a new array with the specified component type and
length.

Creates a new array
with the specified component type and dimensions.

Sets the value of the indexed component of the specified array
object to the specified new value.

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

Sets the value of the indexed component of the specified array
object to the specified

char

value.

Sets the value of the indexed component of the specified array
object to the specified

double

value.

Sets the value of the indexed component of the specified array
object to the specified

float

value.

Sets the value of the indexed component of the specified array
object to the specified

int

value.

Sets the value of the indexed component of the specified array
object to the specified

long

value.

Sets the value of the indexed component of the specified array
object to the specified

short

value.

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

- newInstance

```java
public static
Object
newInstance​(
Class
<?> componentType,
int length)
throws
NegativeArraySizeException
```

Creates a new array with the specified component type and
length.
Invoking this method is equivalent to creating an array
as follows:

```java
int[] x = {length};
Array.newInstance(componentType, x);
```

The number of dimensions of the new array must not
exceed 255.

**Parameters:** componentType

- the

Class

object representing the
component type of the new array
**Parameters:** length

- the length of the new array
**Returns:** the new array
**Throws:** NullPointerException

- if the specified

componentType

parameter is null
**Throws:** IllegalArgumentException

- if componentType is

Void.TYPE

or if the number of dimensions of the requested array
instance exceed 255.
**Throws:** NegativeArraySizeException

- if the specified

length

is negative

- newInstance

```java
public static
Object
newInstance​(
Class
<?> componentType,
int... dimensions)
throws
IllegalArgumentException
,

NegativeArraySizeException
```

Creates a new array
with the specified component type and dimensions.
If

componentType

represents a non-array class or interface, the new array
has

dimensions.length

dimensions and

componentType

as its component type. If

componentType

represents an array class, the
number of dimensions of the new array is equal to the sum
of

dimensions.length

and the number of
dimensions of

componentType

. In this case, the
component type of the new array is the component type of

componentType

.

The number of dimensions of the new array must not
exceed 255.

**Parameters:** componentType

- the

Class

object representing the component
type of the new array
**Parameters:** dimensions

- an array of

int

representing the dimensions of
the new array
**Returns:** the new array
**Throws:** NullPointerException

- if the specified

componentType

argument is null
**Throws:** IllegalArgumentException

- if the specified

dimensions

argument is a zero-dimensional array, if componentType is

Void.TYPE

, or if the number of dimensions of the requested array
instance exceed 255.
**Throws:** NegativeArraySizeException

- if any of the components in
the specified

dimensions

argument is negative.

- getLength

```java
public static int getLength​(
Object
array)
throws
IllegalArgumentException
```

Returns the length of the specified array object, as an

int

.

**Parameters:** array

- the array
**Returns:** the length of the array
**Throws:** IllegalArgumentException

- if the object argument is not
an array

- get

```java
public static
Object
get​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object. The value is automatically wrapped in an object
if it has a primitive type.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the (possibly wrapped) value of the indexed component in
the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

- getBoolean

```java
public static boolean getBoolean​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

boolean

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getByte

```java
public static byte getByte​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

byte

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getChar

```java
public static char getChar​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

char

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getShort

```java
public static short getShort​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

short

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getInt

```java
public static int getInt​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as an

int

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getLong

```java
public static long getLong​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

long

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getFloat

```java
public static float getFloat​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

float

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getDouble

```java
public static double getDouble​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

double

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- set

```java
public static void set​(
Object
array,
int index,

Object
value)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified new value. The new value is first
automatically unwrapped if the array has a primitive component
type.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** value

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the array component type is primitive and
an unwrapping conversion fails
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

- setBoolean

```java
public static void setBoolean​(
Object
array,
int index,
boolean z)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** z

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setByte

```java
public static void setByte​(
Object
array,
int index,
byte b)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** b

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setChar

```java
public static void setChar​(
Object
array,
int index,
char c)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

char

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** c

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setShort

```java
public static void setShort​(
Object
array,
int index,
short s)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

short

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** s

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setInt

```java
public static void setInt​(
Object
array,
int index,
int i)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

int

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** i

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setLong

```java
public static void setLong​(
Object
array,
int index,
long l)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

long

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** l

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setFloat

```java
public static void setFloat​(
Object
array,
int index,
float f)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

float

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** f

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setDouble

```java
public static void setDouble​(
Object
array,
int index,
double d)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

double

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** d

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

Method Detail

- newInstance

```java
public static
Object
newInstance​(
Class
<?> componentType,
int length)
throws
NegativeArraySizeException
```

Creates a new array with the specified component type and
length.
Invoking this method is equivalent to creating an array
as follows:

```java
int[] x = {length};
Array.newInstance(componentType, x);
```

The number of dimensions of the new array must not
exceed 255.

**Parameters:** componentType

- the

Class

object representing the
component type of the new array
**Parameters:** length

- the length of the new array
**Returns:** the new array
**Throws:** NullPointerException

- if the specified

componentType

parameter is null
**Throws:** IllegalArgumentException

- if componentType is

Void.TYPE

or if the number of dimensions of the requested array
instance exceed 255.
**Throws:** NegativeArraySizeException

- if the specified

length

is negative

- newInstance

```java
public static
Object
newInstance​(
Class
<?> componentType,
int... dimensions)
throws
IllegalArgumentException
,

NegativeArraySizeException
```

Creates a new array
with the specified component type and dimensions.
If

componentType

represents a non-array class or interface, the new array
has

dimensions.length

dimensions and

componentType

as its component type. If

componentType

represents an array class, the
number of dimensions of the new array is equal to the sum
of

dimensions.length

and the number of
dimensions of

componentType

. In this case, the
component type of the new array is the component type of

componentType

.

The number of dimensions of the new array must not
exceed 255.

**Parameters:** componentType

- the

Class

object representing the component
type of the new array
**Parameters:** dimensions

- an array of

int

representing the dimensions of
the new array
**Returns:** the new array
**Throws:** NullPointerException

- if the specified

componentType

argument is null
**Throws:** IllegalArgumentException

- if the specified

dimensions

argument is a zero-dimensional array, if componentType is

Void.TYPE

, or if the number of dimensions of the requested array
instance exceed 255.
**Throws:** NegativeArraySizeException

- if any of the components in
the specified

dimensions

argument is negative.

- getLength

```java
public static int getLength​(
Object
array)
throws
IllegalArgumentException
```

Returns the length of the specified array object, as an

int

.

**Parameters:** array

- the array
**Returns:** the length of the array
**Throws:** IllegalArgumentException

- if the object argument is not
an array

- get

```java
public static
Object
get​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object. The value is automatically wrapped in an object
if it has a primitive type.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the (possibly wrapped) value of the indexed component in
the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

- getBoolean

```java
public static boolean getBoolean​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

boolean

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getByte

```java
public static byte getByte​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

byte

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getChar

```java
public static char getChar​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

char

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getShort

```java
public static short getShort​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

short

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getInt

```java
public static int getInt​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as an

int

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getLong

```java
public static long getLong​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

long

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getFloat

```java
public static float getFloat​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

float

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- getDouble

```java
public static double getDouble​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

double

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

- set

```java
public static void set​(
Object
array,
int index,

Object
value)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified new value. The new value is first
automatically unwrapped if the array has a primitive component
type.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** value

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the array component type is primitive and
an unwrapping conversion fails
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

- setBoolean

```java
public static void setBoolean​(
Object
array,
int index,
boolean z)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** z

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setByte

```java
public static void setByte​(
Object
array,
int index,
byte b)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** b

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setChar

```java
public static void setChar​(
Object
array,
int index,
char c)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

char

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** c

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setShort

```java
public static void setShort​(
Object
array,
int index,
short s)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

short

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** s

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setInt

```java
public static void setInt​(
Object
array,
int index,
int i)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

int

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** i

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setLong

```java
public static void setLong​(
Object
array,
int index,
long l)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

long

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** l

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setFloat

```java
public static void setFloat​(
Object
array,
int index,
float f)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

float

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** f

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

- setDouble

```java
public static void setDouble​(
Object
array,
int index,
double d)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

double

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** d

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### Method Detail

newInstance

```java
public static
Object
newInstance​(
Class
<?> componentType,
int length)
throws
NegativeArraySizeException
```

Creates a new array with the specified component type and
length.
Invoking this method is equivalent to creating an array
as follows:

```java
int[] x = {length};
Array.newInstance(componentType, x);
```

The number of dimensions of the new array must not
exceed 255.

**Parameters:** componentType

- the

Class

object representing the
component type of the new array
**Parameters:** length

- the length of the new array
**Returns:** the new array
**Throws:** NullPointerException

- if the specified

componentType

parameter is null
**Throws:** IllegalArgumentException

- if componentType is

Void.TYPE

or if the number of dimensions of the requested array
instance exceed 255.
**Throws:** NegativeArraySizeException

- if the specified

length

is negative

---

#### newInstance

public static

Object

newInstance​(

Class

<?> componentType,
int length)
throws

NegativeArraySizeException

Creates a new array with the specified component type and
length.
Invoking this method is equivalent to creating an array
as follows:

```java
int[] x = {length};
Array.newInstance(componentType, x);
```

The number of dimensions of the new array must not
exceed 255.

int[] x = {length};
Array.newInstance(componentType, x);

The number of dimensions of the new array must not
exceed 255.

newInstance

```java
public static
Object
newInstance​(
Class
<?> componentType,
int... dimensions)
throws
IllegalArgumentException
,

NegativeArraySizeException
```

Creates a new array
with the specified component type and dimensions.
If

componentType

represents a non-array class or interface, the new array
has

dimensions.length

dimensions and

componentType

as its component type. If

componentType

represents an array class, the
number of dimensions of the new array is equal to the sum
of

dimensions.length

and the number of
dimensions of

componentType

. In this case, the
component type of the new array is the component type of

componentType

.

The number of dimensions of the new array must not
exceed 255.

**Parameters:** componentType

- the

Class

object representing the component
type of the new array
**Parameters:** dimensions

- an array of

int

representing the dimensions of
the new array
**Returns:** the new array
**Throws:** NullPointerException

- if the specified

componentType

argument is null
**Throws:** IllegalArgumentException

- if the specified

dimensions

argument is a zero-dimensional array, if componentType is

Void.TYPE

, or if the number of dimensions of the requested array
instance exceed 255.
**Throws:** NegativeArraySizeException

- if any of the components in
the specified

dimensions

argument is negative.

---

#### newInstance

public static

Object

newInstance​(

Class

<?> componentType,
int... dimensions)
throws

IllegalArgumentException

,

NegativeArraySizeException

Creates a new array
with the specified component type and dimensions.
If

componentType

represents a non-array class or interface, the new array
has

dimensions.length

dimensions and

componentType

as its component type. If

componentType

represents an array class, the
number of dimensions of the new array is equal to the sum
of

dimensions.length

and the number of
dimensions of

componentType

. In this case, the
component type of the new array is the component type of

componentType

.

The number of dimensions of the new array must not
exceed 255.

The number of dimensions of the new array must not
exceed 255.

getLength

```java
public static int getLength​(
Object
array)
throws
IllegalArgumentException
```

Returns the length of the specified array object, as an

int

.

**Parameters:** array

- the array
**Returns:** the length of the array
**Throws:** IllegalArgumentException

- if the object argument is not
an array

---

#### getLength

public static int getLength​(

Object

array)
throws

IllegalArgumentException

Returns the length of the specified array object, as an

int

.

get

```java
public static
Object
get​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object. The value is automatically wrapped in an object
if it has a primitive type.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the (possibly wrapped) value of the indexed component in
the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array

---

#### get

public static

Object

get​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object. The value is automatically wrapped in an object
if it has a primitive type.

getBoolean

```java
public static boolean getBoolean​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

boolean

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getBoolean

public static boolean getBoolean​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

boolean

.

getByte

```java
public static byte getByte​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

byte

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getByte

public static byte getByte​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

byte

.

getChar

```java
public static char getChar​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

char

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getChar

public static char getChar​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

char

.

getShort

```java
public static short getShort​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

short

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getShort

public static short getShort​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

short

.

getInt

```java
public static int getInt​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as an

int

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getInt

public static int getInt​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as an

int

.

getLong

```java
public static long getLong​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

long

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getLong

public static long getLong​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

long

.

getFloat

```java
public static float getFloat​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

float

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getFloat

public static float getFloat​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

float

.

getDouble

```java
public static double getDouble​(
Object
array,
int index)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Returns the value of the indexed component in the specified
array object, as a

double

.

**Parameters:** array

- the array
**Parameters:** index

- the index
**Returns:** the value of the indexed component in the specified array
**Throws:** NullPointerException

- If the specified object is null
**Throws:** IllegalArgumentException

- If the specified object is not
an array, or if the indexed element cannot be converted to the
return type by an identity or widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to the
length of the specified array
**See Also:** get(java.lang.Object, int)

---

#### getDouble

public static double getDouble​(

Object

array,
int index)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Returns the value of the indexed component in the specified
array object, as a

double

.

set

```java
public static void set​(
Object
array,
int index,

Object
value)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified new value. The new value is first
automatically unwrapped if the array has a primitive component
type.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** value

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the array component type is primitive and
an unwrapping conversion fails
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array

---

#### set

public static void set​(

Object

array,
int index,

Object

value)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified new value. The new value is first
automatically unwrapped if the array has a primitive component
type.

setBoolean

```java
public static void setBoolean​(
Object
array,
int index,
boolean z)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** z

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setBoolean

public static void setBoolean​(

Object

array,
int index,
boolean z)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

boolean

value.

setByte

```java
public static void setByte​(
Object
array,
int index,
byte b)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** b

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setByte

public static void setByte​(

Object

array,
int index,
byte b)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

byte

value.

setChar

```java
public static void setChar​(
Object
array,
int index,
char c)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

char

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** c

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setChar

public static void setChar​(

Object

array,
int index,
char c)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

char

value.

setShort

```java
public static void setShort​(
Object
array,
int index,
short s)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

short

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** s

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setShort

public static void setShort​(

Object

array,
int index,
short s)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

short

value.

setInt

```java
public static void setInt​(
Object
array,
int index,
int i)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

int

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** i

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setInt

public static void setInt​(

Object

array,
int index,
int i)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

int

value.

setLong

```java
public static void setLong​(
Object
array,
int index,
long l)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

long

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** l

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setLong

public static void setLong​(

Object

array,
int index,
long l)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

long

value.

setFloat

```java
public static void setFloat​(
Object
array,
int index,
float f)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

float

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** f

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setFloat

public static void setFloat​(

Object

array,
int index,
float f)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

float

value.

setDouble

```java
public static void setDouble​(
Object
array,
int index,
double d)
throws
IllegalArgumentException
,

ArrayIndexOutOfBoundsException
```

Sets the value of the indexed component of the specified array
object to the specified

double

value.

**Parameters:** array

- the array
**Parameters:** index

- the index into the array
**Parameters:** d

- the new value of the indexed component
**Throws:** NullPointerException

- If the specified object argument
is null
**Throws:** IllegalArgumentException

- If the specified object argument
is not an array, or if the specified value cannot be converted
to the underlying array's component type by an identity or a
primitive widening conversion
**Throws:** ArrayIndexOutOfBoundsException

- If the specified

index

argument is negative, or if it is greater than or equal to
the length of the specified array
**See Also:** set(java.lang.Object, int, java.lang.Object)

---

#### setDouble

public static void setDouble​(

Object

array,
int index,
double d)
throws

IllegalArgumentException

,

ArrayIndexOutOfBoundsException

Sets the value of the indexed component of the specified array
object to the specified

double

value.

---

