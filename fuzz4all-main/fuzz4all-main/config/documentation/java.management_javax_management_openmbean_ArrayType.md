# Class ArrayType<T>

**Source:** `java.management\javax\management\openmbean\ArrayType.html`

### Class Description

```java
public class
ArrayType<T>

extends
OpenType
<T>
```

The

ArrayType

class is the

open type

class whose instances describe
all

open data

values which are n-dimensional arrays of

open data

values.

Examples of valid

ArrayType

instances are:

```java
// 2-dimension array of java.lang.String
ArrayType<String[][]> a1 = new ArrayType<String[][]>(2, SimpleType.STRING);

// 1-dimension array of int
ArrayType<int[]> a2 = new ArrayType<int[]>(SimpleType.INTEGER, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a3 = new ArrayType<Integer[]>(SimpleType.INTEGER, false);

// 4-dimension array of int
ArrayType<int[][][][]> a4 = new ArrayType<int[][][][]>(3, a2);

// 4-dimension array of java.lang.Integer
ArrayType<Integer[][][][]> a5 = new ArrayType<Integer[][][][]>(3, a3);

// 1-dimension array of java.lang.String
ArrayType<String[]> a6 = new ArrayType<String[]>(SimpleType.STRING, false);

// 1-dimension array of long
ArrayType<long[]> a7 = new ArrayType<long[]>(SimpleType.LONG, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a8 = ArrayType.getArrayType(SimpleType.INTEGER);

// 2-dimension array of java.lang.Integer
ArrayType<Integer[][]> a9 = ArrayType.getArrayType(a8);

// 2-dimension array of int
ArrayType<int[][]> a10 = ArrayType.getPrimitiveArrayType(int[][].class);

// 3-dimension array of int
ArrayType<int[][][]> a11 = ArrayType.getArrayType(a10);

// 1-dimension array of float
ArrayType<float[]> a12 = ArrayType.getPrimitiveArrayType(float[].class);

// 2-dimension array of float
ArrayType<float[][]> a13 = ArrayType.getArrayType(a12);

// 1-dimension array of javax.management.ObjectName
ArrayType<ObjectName[]> a14 = ArrayType.getArrayType(SimpleType.OBJECTNAME);

// 2-dimension array of javax.management.ObjectName
ArrayType<ObjectName[][]> a15 = ArrayType.getArrayType(a14);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a16 = new ArrayType<String[][][]>(3, SimpleType.STRING);

// 1-dimension array of java.lang.String
ArrayType<String[]> a17 = new ArrayType<String[]>(1, SimpleType.STRING);

// 2-dimension array of java.lang.String
ArrayType<String[][]> a18 = new ArrayType<String[][]>(1, a17);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a19 = new ArrayType<String[][][]>(1, a18);
```

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ArrayType​(int dimension,

OpenType
<?> elementType)
throws
OpenDataException

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

**Parameters:**
- dimension

- the dimension of arrays described by this

ArrayType

instance;
must be greater than or equal to 1.
- elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.

**Throws:**
- IllegalArgumentException

- if

dimension

is not a positive
integer.
- OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.

---

#### public ArrayType​(
SimpleType
<?> elementType,
boolean primitiveArray)
throws
OpenDataException

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

This constructor supports the creation of arrays of primitive
types when

primitiveArray

is

true

.

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

**Parameters:**
- elementType

- the

SimpleType

of the element values
contained in the arrays described by this

ArrayType

instance.
- primitiveArray

-

true

when this array describes
primitive arrays.

**Throws:**
- IllegalArgumentException

- if

dimension

is not a positive
integer.
- OpenDataException

- if

primitiveArray

is

true

and

elementType

is not a valid

SimpleType

for a primitive
type.

**Since:**
- 1.6

---

### Method Details

#### public int getDimension()

Returns the dimension of arrays described by this

ArrayType

instance.

**Returns:**
- the dimension.

---

#### public
OpenType
<?> getElementOpenType()

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

**Returns:**
- the element type.

---

#### public boolean isPrimitiveArray()

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

**Returns:**
- true if this is a primitive array type.

**Since:**
- 1.6

---

#### public boolean isValue​(
Object
obj)

Tests whether

obj

is a value for this

ArrayType

instance.

This method returns

true

if and only if

obj

is not null,

obj

is an array and any one of the following
is

true

:

- if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),
- if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

**Specified by:**
- isValue

in class

OpenType

<

T

>

**Parameters:**
- obj

- the object to be tested.

**Returns:**
- true

if

obj

is a value for this

ArrayType

instance.

---

#### public boolean equals​(
Object
obj)

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

Two

ArrayType

instances are equal if and only if they
describe array instances which have the same dimension, elements'
open type and primitive array flag.

**Specified by:**
- equals

in class

OpenType

<

T

>

**Parameters:**
- obj

- the object to be compared for equality with this

ArrayType

instance; if

obj

is

null

or is not an instance of the
class

ArrayType

this method returns

false

.

**Returns:**
- true

if the specified object is equal to
this

ArrayType

instance.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this

ArrayType

instance.

The hash code of an

ArrayType

instance is the sum of the
hash codes of all the elements of information used in

equals

comparisons (i.e. dimension, elements' open type and primitive array flag).
The hashcode for a primitive value is the hashcode of the corresponding boxed
object (e.g. the hashcode for

true

is

Boolean.TRUE.hashCode()

).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

ArrayType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code value for this

ArrayType

instance

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this

ArrayType

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.ArrayType

), the type name,
the dimension, the elements' open type and the primitive array flag
defined for this instance.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:**
- toString

in class

OpenType

<

T

>

**Returns:**
- a string representation of this

ArrayType

instance

---

#### public static <E>
ArrayType
<E[]> getArrayType​(
OpenType
<E> elementType)
throws
OpenDataException

Create an

ArrayType

instance in a type-safe manner.

Multidimensional arrays can be built up by calling this method as many
times as necessary.

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

**Parameters:**
- elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.

**Returns:**
- an

ArrayType

instance

**Throws:**
- OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.

**Since:**
- 1.6

**Type Parameters:**
- E

- the Java type that described instances must have

---

#### public static <T>
ArrayType
<T> getPrimitiveArrayType​(
Class
<T> arrayClass)

Create an

ArrayType

instance in a type-safe manner.

Calling this method twice with the same parameters may return the
same object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

**Parameters:**
- arrayClass

- a primitive array class such as

int[].class

,

boolean[][].class

, etc. The

getElementOpenType()

method of the returned

ArrayType

returns the

SimpleType

corresponding to the wrapper type of the primitive
type of the array.

**Returns:**
- an

ArrayType

instance

**Throws:**
- IllegalArgumentException

- if

arrayClass

is not
a primitive array.

**Since:**
- 1.6

**Type Parameters:**
- T

- the Java type that described instances must have

---

### Additional Sections

#### Class ArrayType<T>

java.lang.Object

- javax.management.openmbean.OpenType

<T>
- - javax.management.openmbean.ArrayType<T>

javax.management.openmbean.OpenType

<T>

- javax.management.openmbean.ArrayType<T>

javax.management.openmbean.ArrayType<T>

**All Implemented Interfaces:** Serializable

```java
public class
ArrayType<T>

extends
OpenType
<T>
```

The

ArrayType

class is the

open type

class whose instances describe
all

open data

values which are n-dimensional arrays of

open data

values.

Examples of valid

ArrayType

instances are:

```java
// 2-dimension array of java.lang.String
ArrayType<String[][]> a1 = new ArrayType<String[][]>(2, SimpleType.STRING);

// 1-dimension array of int
ArrayType<int[]> a2 = new ArrayType<int[]>(SimpleType.INTEGER, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a3 = new ArrayType<Integer[]>(SimpleType.INTEGER, false);

// 4-dimension array of int
ArrayType<int[][][][]> a4 = new ArrayType<int[][][][]>(3, a2);

// 4-dimension array of java.lang.Integer
ArrayType<Integer[][][][]> a5 = new ArrayType<Integer[][][][]>(3, a3);

// 1-dimension array of java.lang.String
ArrayType<String[]> a6 = new ArrayType<String[]>(SimpleType.STRING, false);

// 1-dimension array of long
ArrayType<long[]> a7 = new ArrayType<long[]>(SimpleType.LONG, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a8 = ArrayType.getArrayType(SimpleType.INTEGER);

// 2-dimension array of java.lang.Integer
ArrayType<Integer[][]> a9 = ArrayType.getArrayType(a8);

// 2-dimension array of int
ArrayType<int[][]> a10 = ArrayType.getPrimitiveArrayType(int[][].class);

// 3-dimension array of int
ArrayType<int[][][]> a11 = ArrayType.getArrayType(a10);

// 1-dimension array of float
ArrayType<float[]> a12 = ArrayType.getPrimitiveArrayType(float[].class);

// 2-dimension array of float
ArrayType<float[][]> a13 = ArrayType.getArrayType(a12);

// 1-dimension array of javax.management.ObjectName
ArrayType<ObjectName[]> a14 = ArrayType.getArrayType(SimpleType.OBJECTNAME);

// 2-dimension array of javax.management.ObjectName
ArrayType<ObjectName[][]> a15 = ArrayType.getArrayType(a14);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a16 = new ArrayType<String[][][]>(3, SimpleType.STRING);

// 1-dimension array of java.lang.String
ArrayType<String[]> a17 = new ArrayType<String[]>(1, SimpleType.STRING);

// 2-dimension array of java.lang.String
ArrayType<String[][]> a18 = new ArrayType<String[][]>(1, a17);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a19 = new ArrayType<String[][][]>(1, a18);
```

**Since:** 1.5
**See Also:** Serialized Form

public class

ArrayType<T>

extends

OpenType

<T>

The

ArrayType

class is the

open type

class whose instances describe
all

open data

values which are n-dimensional arrays of

open data

values.

Examples of valid

ArrayType

instances are:

```java
// 2-dimension array of java.lang.String
ArrayType<String[][]> a1 = new ArrayType<String[][]>(2, SimpleType.STRING);

// 1-dimension array of int
ArrayType<int[]> a2 = new ArrayType<int[]>(SimpleType.INTEGER, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a3 = new ArrayType<Integer[]>(SimpleType.INTEGER, false);

// 4-dimension array of int
ArrayType<int[][][][]> a4 = new ArrayType<int[][][][]>(3, a2);

// 4-dimension array of java.lang.Integer
ArrayType<Integer[][][][]> a5 = new ArrayType<Integer[][][][]>(3, a3);

// 1-dimension array of java.lang.String
ArrayType<String[]> a6 = new ArrayType<String[]>(SimpleType.STRING, false);

// 1-dimension array of long
ArrayType<long[]> a7 = new ArrayType<long[]>(SimpleType.LONG, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a8 = ArrayType.getArrayType(SimpleType.INTEGER);

// 2-dimension array of java.lang.Integer
ArrayType<Integer[][]> a9 = ArrayType.getArrayType(a8);

// 2-dimension array of int
ArrayType<int[][]> a10 = ArrayType.getPrimitiveArrayType(int[][].class);

// 3-dimension array of int
ArrayType<int[][][]> a11 = ArrayType.getArrayType(a10);

// 1-dimension array of float
ArrayType<float[]> a12 = ArrayType.getPrimitiveArrayType(float[].class);

// 2-dimension array of float
ArrayType<float[][]> a13 = ArrayType.getArrayType(a12);

// 1-dimension array of javax.management.ObjectName
ArrayType<ObjectName[]> a14 = ArrayType.getArrayType(SimpleType.OBJECTNAME);

// 2-dimension array of javax.management.ObjectName
ArrayType<ObjectName[][]> a15 = ArrayType.getArrayType(a14);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a16 = new ArrayType<String[][][]>(3, SimpleType.STRING);

// 1-dimension array of java.lang.String
ArrayType<String[]> a17 = new ArrayType<String[]>(1, SimpleType.STRING);

// 2-dimension array of java.lang.String
ArrayType<String[][]> a18 = new ArrayType<String[][]>(1, a17);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a19 = new ArrayType<String[][][]>(1, a18);
```

Examples of valid

ArrayType

instances are:

```java
// 2-dimension array of java.lang.String
ArrayType<String[][]> a1 = new ArrayType<String[][]>(2, SimpleType.STRING);

// 1-dimension array of int
ArrayType<int[]> a2 = new ArrayType<int[]>(SimpleType.INTEGER, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a3 = new ArrayType<Integer[]>(SimpleType.INTEGER, false);

// 4-dimension array of int
ArrayType<int[][][][]> a4 = new ArrayType<int[][][][]>(3, a2);

// 4-dimension array of java.lang.Integer
ArrayType<Integer[][][][]> a5 = new ArrayType<Integer[][][][]>(3, a3);

// 1-dimension array of java.lang.String
ArrayType<String[]> a6 = new ArrayType<String[]>(SimpleType.STRING, false);

// 1-dimension array of long
ArrayType<long[]> a7 = new ArrayType<long[]>(SimpleType.LONG, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a8 = ArrayType.getArrayType(SimpleType.INTEGER);

// 2-dimension array of java.lang.Integer
ArrayType<Integer[][]> a9 = ArrayType.getArrayType(a8);

// 2-dimension array of int
ArrayType<int[][]> a10 = ArrayType.getPrimitiveArrayType(int[][].class);

// 3-dimension array of int
ArrayType<int[][][]> a11 = ArrayType.getArrayType(a10);

// 1-dimension array of float
ArrayType<float[]> a12 = ArrayType.getPrimitiveArrayType(float[].class);

// 2-dimension array of float
ArrayType<float[][]> a13 = ArrayType.getArrayType(a12);

// 1-dimension array of javax.management.ObjectName
ArrayType<ObjectName[]> a14 = ArrayType.getArrayType(SimpleType.OBJECTNAME);

// 2-dimension array of javax.management.ObjectName
ArrayType<ObjectName[][]> a15 = ArrayType.getArrayType(a14);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a16 = new ArrayType<String[][][]>(3, SimpleType.STRING);

// 1-dimension array of java.lang.String
ArrayType<String[]> a17 = new ArrayType<String[]>(1, SimpleType.STRING);

// 2-dimension array of java.lang.String
ArrayType<String[][]> a18 = new ArrayType<String[][]>(1, a17);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a19 = new ArrayType<String[][][]>(1, a18);
```

// 2-dimension array of java.lang.String
ArrayType<String[][]> a1 = new ArrayType<String[][]>(2, SimpleType.STRING);

// 1-dimension array of int
ArrayType<int[]> a2 = new ArrayType<int[]>(SimpleType.INTEGER, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a3 = new ArrayType<Integer[]>(SimpleType.INTEGER, false);

// 4-dimension array of int
ArrayType<int[][][][]> a4 = new ArrayType<int[][][][]>(3, a2);

// 4-dimension array of java.lang.Integer
ArrayType<Integer[][][][]> a5 = new ArrayType<Integer[][][][]>(3, a3);

// 1-dimension array of java.lang.String
ArrayType<String[]> a6 = new ArrayType<String[]>(SimpleType.STRING, false);

// 1-dimension array of long
ArrayType<long[]> a7 = new ArrayType<long[]>(SimpleType.LONG, true);

// 1-dimension array of java.lang.Integer
ArrayType<Integer[]> a8 = ArrayType.getArrayType(SimpleType.INTEGER);

// 2-dimension array of java.lang.Integer
ArrayType<Integer[][]> a9 = ArrayType.getArrayType(a8);

// 2-dimension array of int
ArrayType<int[][]> a10 = ArrayType.getPrimitiveArrayType(int[][].class);

// 3-dimension array of int
ArrayType<int[][][]> a11 = ArrayType.getArrayType(a10);

// 1-dimension array of float
ArrayType<float[]> a12 = ArrayType.getPrimitiveArrayType(float[].class);

// 2-dimension array of float
ArrayType<float[][]> a13 = ArrayType.getArrayType(a12);

// 1-dimension array of javax.management.ObjectName
ArrayType<ObjectName[]> a14 = ArrayType.getArrayType(SimpleType.OBJECTNAME);

// 2-dimension array of javax.management.ObjectName
ArrayType<ObjectName[][]> a15 = ArrayType.getArrayType(a14);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a16 = new ArrayType<String[][][]>(3, SimpleType.STRING);

// 1-dimension array of java.lang.String
ArrayType<String[]> a17 = new ArrayType<String[]>(1, SimpleType.STRING);

// 2-dimension array of java.lang.String
ArrayType<String[][]> a18 = new ArrayType<String[][]>(1, a17);

// 3-dimension array of java.lang.String
ArrayType<String[][][]> a19 = new ArrayType<String[][][]>(1, a18);

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ArrayType

​(int dimension,

OpenType

<?> elementType)

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

ArrayType

​(

SimpleType

<?> elementType,
boolean primitiveArray)

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

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

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

static <E>

ArrayType

<E[]>

getArrayType

​(

OpenType

<E> elementType)

Create an

ArrayType

instance in a type-safe manner.

int

getDimension

()

Returns the dimension of arrays described by this

ArrayType

instance.

OpenType

<?>

getElementOpenType

()

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

static <T>

ArrayType

<T>

getPrimitiveArrayType

​(

Class

<T> arrayClass)

Create an

ArrayType

instance in a type-safe manner.

int

hashCode

()

Returns the hash code value for this

ArrayType

instance.

boolean

isPrimitiveArray

()

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value for this

ArrayType

instance.

String

toString

()

Returns a string representation of this

ArrayType

instance.

- Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

- Methods declared in class java.lang.

Object

clone

,

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

Field Summary

- Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

---

#### Field Summary

Fields declared in class javax.management.openmbean.

OpenType

ALLOWED_CLASSNAMES

,

ALLOWED_CLASSNAMES_LIST

---

#### Fields declared in class javax.management.openmbean. OpenType

Constructor Summary

Constructors

Constructor

Description

ArrayType

​(int dimension,

OpenType

<?> elementType)

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

ArrayType

​(

SimpleType

<?> elementType,
boolean primitiveArray)

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

---

#### Constructor Summary

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

static <E>

ArrayType

<E[]>

getArrayType

​(

OpenType

<E> elementType)

Create an

ArrayType

instance in a type-safe manner.

int

getDimension

()

Returns the dimension of arrays described by this

ArrayType

instance.

OpenType

<?>

getElementOpenType

()

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

static <T>

ArrayType

<T>

getPrimitiveArrayType

​(

Class

<T> arrayClass)

Create an

ArrayType

instance in a type-safe manner.

int

hashCode

()

Returns the hash code value for this

ArrayType

instance.

boolean

isPrimitiveArray

()

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

boolean

isValue

​(

Object

obj)

Tests whether

obj

is a value for this

ArrayType

instance.

String

toString

()

Returns a string representation of this

ArrayType

instance.

- Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

- Methods declared in class java.lang.

Object

clone

,

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

#### Method Summary

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

Create an

ArrayType

instance in a type-safe manner.

Returns the dimension of arrays described by this

ArrayType

instance.

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

Returns the hash code value for this

ArrayType

instance.

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

Tests whether

obj

is a value for this

ArrayType

instance.

Returns a string representation of this

ArrayType

instance.

Methods declared in class javax.management.openmbean.

OpenType

getClassName

,

getDescription

,

getTypeName

,

isArray

---

#### Methods declared in class javax.management.openmbean. OpenType

Methods declared in class java.lang.

Object

clone

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ArrayType

```java
public ArrayType​(int dimension,

OpenType
<?> elementType)
throws
OpenDataException
```

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

**Parameters:** dimension

- the dimension of arrays described by this

ArrayType

instance;
must be greater than or equal to 1.
**Parameters:** elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.
**Throws:** IllegalArgumentException

- if

dimension

is not a positive
integer.
**Throws:** OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.

- ArrayType

```java
public ArrayType​(
SimpleType
<?> elementType,
boolean primitiveArray)
throws
OpenDataException
```

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

This constructor supports the creation of arrays of primitive
types when

primitiveArray

is

true

.

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

**Parameters:** elementType

- the

SimpleType

of the element values
contained in the arrays described by this

ArrayType

instance.
**Parameters:** primitiveArray

-

true

when this array describes
primitive arrays.
**Throws:** IllegalArgumentException

- if

dimension

is not a positive
integer.
**Throws:** OpenDataException

- if

primitiveArray

is

true

and

elementType

is not a valid

SimpleType

for a primitive
type.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getDimension

```java
public int getDimension()
```

Returns the dimension of arrays described by this

ArrayType

instance.

**Returns:** the dimension.

- getElementOpenType

```java
public
OpenType
<?> getElementOpenType()
```

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

**Returns:** the element type.

- isPrimitiveArray

```java
public boolean isPrimitiveArray()
```

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

**Returns:** true if this is a primitive array type.
**Since:** 1.6

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this

ArrayType

instance.

This method returns

true

if and only if

obj

is not null,

obj

is an array and any one of the following
is

true

:

- if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),
- if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

**Specified by:** isValue

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a value for this

ArrayType

instance.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

Two

ArrayType

instances are equal if and only if they
describe array instances which have the same dimension, elements'
open type and primitive array flag.

**Specified by:** equals

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be compared for equality with this

ArrayType

instance; if

obj

is

null

or is not an instance of the
class

ArrayType

this method returns

false

.
**Returns:** true

if the specified object is equal to
this

ArrayType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

ArrayType

instance.

The hash code of an

ArrayType

instance is the sum of the
hash codes of all the elements of information used in

equals

comparisons (i.e. dimension, elements' open type and primitive array flag).
The hashcode for a primitive value is the hashcode of the corresponding boxed
object (e.g. the hashcode for

true

is

Boolean.TRUE.hashCode()

).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

ArrayType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

ArrayType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

ArrayType

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.ArrayType

), the type name,
the dimension, the elements' open type and the primitive array flag
defined for this instance.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

T

>
**Returns:** a string representation of this

ArrayType

instance

- getArrayType

```java
public static <E>
ArrayType
<E[]> getArrayType​(
OpenType
<E> elementType)
throws
OpenDataException
```

Create an

ArrayType

instance in a type-safe manner.

Multidimensional arrays can be built up by calling this method as many
times as necessary.

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

**Type Parameters:** E

- the Java type that described instances must have
**Parameters:** elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.
**Returns:** an

ArrayType

instance
**Throws:** OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.
**Since:** 1.6

- getPrimitiveArrayType

```java
public static <T>
ArrayType
<T> getPrimitiveArrayType​(
Class
<T> arrayClass)
```

Create an

ArrayType

instance in a type-safe manner.

Calling this method twice with the same parameters may return the
same object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

**Type Parameters:** T

- the Java type that described instances must have
**Parameters:** arrayClass

- a primitive array class such as

int[].class

,

boolean[][].class

, etc. The

getElementOpenType()

method of the returned

ArrayType

returns the

SimpleType

corresponding to the wrapper type of the primitive
type of the array.
**Returns:** an

ArrayType

instance
**Throws:** IllegalArgumentException

- if

arrayClass

is not
a primitive array.
**Since:** 1.6

Constructor Detail

- ArrayType

```java
public ArrayType​(int dimension,

OpenType
<?> elementType)
throws
OpenDataException
```

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

**Parameters:** dimension

- the dimension of arrays described by this

ArrayType

instance;
must be greater than or equal to 1.
**Parameters:** elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.
**Throws:** IllegalArgumentException

- if

dimension

is not a positive
integer.
**Throws:** OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.

- ArrayType

```java
public ArrayType​(
SimpleType
<?> elementType,
boolean primitiveArray)
throws
OpenDataException
```

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

This constructor supports the creation of arrays of primitive
types when

primitiveArray

is

true

.

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

**Parameters:** elementType

- the

SimpleType

of the element values
contained in the arrays described by this

ArrayType

instance.
**Parameters:** primitiveArray

-

true

when this array describes
primitive arrays.
**Throws:** IllegalArgumentException

- if

dimension

is not a positive
integer.
**Throws:** OpenDataException

- if

primitiveArray

is

true

and

elementType

is not a valid

SimpleType

for a primitive
type.
**Since:** 1.6

---

#### Constructor Detail

ArrayType

```java
public ArrayType​(int dimension,

OpenType
<?> elementType)
throws
OpenDataException
```

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

**Parameters:** dimension

- the dimension of arrays described by this

ArrayType

instance;
must be greater than or equal to 1.
**Parameters:** elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.
**Throws:** IllegalArgumentException

- if

dimension

is not a positive
integer.
**Throws:** OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.

---

#### ArrayType

public ArrayType​(int dimension,

OpenType

<?> elementType)
throws

OpenDataException

Constructs an

ArrayType

instance describing

open data

values which are
arrays with dimension

dimension

of elements
whose

open type

is

elementType

.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>
- if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

if non-primitive array:

<dimension>

-dimension array
of

<element_class_name>

if primitive array:

<dimension>

-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

And the following piece of code which is equivalent to the one listed
above would also produce the same output:

```java
ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

ArrayType<String[][][]> t = new ArrayType<String[][][]>(3, SimpleType.STRING);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());

array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String

ArrayType<String[]> t1 = new ArrayType<String[]>(1, SimpleType.STRING);
ArrayType<String[][]> t2 = new ArrayType<String[][]>(1, t1);
ArrayType<String[][][]> t3 = new ArrayType<String[][][]>(1, t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());

ArrayType

```java
public ArrayType​(
SimpleType
<?> elementType,
boolean primitiveArray)
throws
OpenDataException
```

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

This constructor supports the creation of arrays of primitive
types when

primitiveArray

is

true

.

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

**Parameters:** elementType

- the

SimpleType

of the element values
contained in the arrays described by this

ArrayType

instance.
**Parameters:** primitiveArray

-

true

when this array describes
primitive arrays.
**Throws:** IllegalArgumentException

- if

dimension

is not a positive
integer.
**Throws:** OpenDataException

- if

primitiveArray

is

true

and

elementType

is not a valid

SimpleType

for a primitive
type.
**Since:** 1.6

---

#### ArrayType

public ArrayType​(

SimpleType

<?> elementType,
boolean primitiveArray)
throws

OpenDataException

Constructs a unidimensional

ArrayType

instance for the
supplied

SimpleType

.

This constructor supports the creation of arrays of primitive
types when

primitiveArray

is

true

.

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

This constructor supports the creation of arrays of primitive
types when

primitiveArray

is

true

.

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

For primitive arrays the

getElementOpenType()

method
returns the

SimpleType

corresponding to the wrapper
type of the primitive type of the array.

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

When invoked on an

ArrayType

instance,
the

getClassName

method
returns the class name of the array instances it describes
(following the rules defined by the

getName

method of

java.lang.Class

),
not the class name of the array elements
(which is returned by a call to

getElementOpenType().getClassName()

).

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

The internal field corresponding to the type name of this

ArrayType

instance is also set to
the class name of the array instances it describes.
In other words, the methods

getClassName

and

getTypeName

return the same string value.
The internal field corresponding to the description
of this

ArrayType

instance is set to a string value
which follows the following template:

- if non-primitive array:

1-dimension array
of

<element_class_name>
- if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

if non-primitive array:

1-dimension array
of

<element_class_name>

if primitive array:

1-dimension array
of

<primitive_type_of_the_element_class_name>

As an example, the following piece of code:

```java
ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int
```

ArrayType<int[]> t = new ArrayType<int[]>(SimpleType.INTEGER, true);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());

array class name = [I
element class name = java.lang.Integer
array type name = [I
array type description = 1-dimension array of int

Method Detail

- getDimension

```java
public int getDimension()
```

Returns the dimension of arrays described by this

ArrayType

instance.

**Returns:** the dimension.

- getElementOpenType

```java
public
OpenType
<?> getElementOpenType()
```

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

**Returns:** the element type.

- isPrimitiveArray

```java
public boolean isPrimitiveArray()
```

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

**Returns:** true if this is a primitive array type.
**Since:** 1.6

- isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this

ArrayType

instance.

This method returns

true

if and only if

obj

is not null,

obj

is an array and any one of the following
is

true

:

- if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),
- if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

**Specified by:** isValue

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a value for this

ArrayType

instance.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

Two

ArrayType

instances are equal if and only if they
describe array instances which have the same dimension, elements'
open type and primitive array flag.

**Specified by:** equals

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be compared for equality with this

ArrayType

instance; if

obj

is

null

or is not an instance of the
class

ArrayType

this method returns

false

.
**Returns:** true

if the specified object is equal to
this

ArrayType

instance.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this

ArrayType

instance.

The hash code of an

ArrayType

instance is the sum of the
hash codes of all the elements of information used in

equals

comparisons (i.e. dimension, elements' open type and primitive array flag).
The hashcode for a primitive value is the hashcode of the corresponding boxed
object (e.g. the hashcode for

true

is

Boolean.TRUE.hashCode()

).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

ArrayType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

ArrayType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this

ArrayType

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.ArrayType

), the type name,
the dimension, the elements' open type and the primitive array flag
defined for this instance.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

T

>
**Returns:** a string representation of this

ArrayType

instance

- getArrayType

```java
public static <E>
ArrayType
<E[]> getArrayType​(
OpenType
<E> elementType)
throws
OpenDataException
```

Create an

ArrayType

instance in a type-safe manner.

Multidimensional arrays can be built up by calling this method as many
times as necessary.

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

**Type Parameters:** E

- the Java type that described instances must have
**Parameters:** elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.
**Returns:** an

ArrayType

instance
**Throws:** OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.
**Since:** 1.6

- getPrimitiveArrayType

```java
public static <T>
ArrayType
<T> getPrimitiveArrayType​(
Class
<T> arrayClass)
```

Create an

ArrayType

instance in a type-safe manner.

Calling this method twice with the same parameters may return the
same object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

**Type Parameters:** T

- the Java type that described instances must have
**Parameters:** arrayClass

- a primitive array class such as

int[].class

,

boolean[][].class

, etc. The

getElementOpenType()

method of the returned

ArrayType

returns the

SimpleType

corresponding to the wrapper type of the primitive
type of the array.
**Returns:** an

ArrayType

instance
**Throws:** IllegalArgumentException

- if

arrayClass

is not
a primitive array.
**Since:** 1.6

---

#### Method Detail

getDimension

```java
public int getDimension()
```

Returns the dimension of arrays described by this

ArrayType

instance.

**Returns:** the dimension.

---

#### getDimension

public int getDimension()

Returns the dimension of arrays described by this

ArrayType

instance.

getElementOpenType

```java
public
OpenType
<?> getElementOpenType()
```

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

**Returns:** the element type.

---

#### getElementOpenType

public

OpenType

<?> getElementOpenType()

Returns the

open type

of element values contained
in the arrays described by this

ArrayType

instance.

isPrimitiveArray

```java
public boolean isPrimitiveArray()
```

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

**Returns:** true if this is a primitive array type.
**Since:** 1.6

---

#### isPrimitiveArray

public boolean isPrimitiveArray()

Returns

true

if the open data values this open
type describes are primitive arrays,

false

otherwise.

isValue

```java
public boolean isValue​(
Object
obj)
```

Tests whether

obj

is a value for this

ArrayType

instance.

This method returns

true

if and only if

obj

is not null,

obj

is an array and any one of the following
is

true

:

- if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),
- if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

**Specified by:** isValue

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be tested.
**Returns:** true

if

obj

is a value for this

ArrayType

instance.

---

#### isValue

public boolean isValue​(

Object

obj)

Tests whether

obj

is a value for this

ArrayType

instance.

This method returns

true

if and only if

obj

is not null,

obj

is an array and any one of the following
is

true

:

- if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),
- if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

This method returns

true

if and only if

obj

is not null,

obj

is an array and any one of the following
is

true

:

- if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),
- if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

if this

ArrayType

instance describes an array of

SimpleType

elements or their corresponding primitive types,

obj

's class name is the same as the className field defined
for this

ArrayType

instance (i.e. the class name returned
by the

getClassName

method, which
includes the dimension information),

if this

ArrayType

instance describes an array of
classes implementing the

TabularData

interface or the

CompositeData

interface,

obj

is assignable to
such a declared array, and each element contained in {

obj

is either null or a valid value for the element's open type specified
by this

ArrayType

instance.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

Two

ArrayType

instances are equal if and only if they
describe array instances which have the same dimension, elements'
open type and primitive array flag.

**Specified by:** equals

in class

OpenType

<

T

>
**Parameters:** obj

- the object to be compared for equality with this

ArrayType

instance; if

obj

is

null

or is not an instance of the
class

ArrayType

this method returns

false

.
**Returns:** true

if the specified object is equal to
this

ArrayType

instance.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified

obj

parameter with this

ArrayType

instance for equality.

Two

ArrayType

instances are equal if and only if they
describe array instances which have the same dimension, elements'
open type and primitive array flag.

Two

ArrayType

instances are equal if and only if they
describe array instances which have the same dimension, elements'
open type and primitive array flag.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this

ArrayType

instance.

The hash code of an

ArrayType

instance is the sum of the
hash codes of all the elements of information used in

equals

comparisons (i.e. dimension, elements' open type and primitive array flag).
The hashcode for a primitive value is the hashcode of the corresponding boxed
object (e.g. the hashcode for

true

is

Boolean.TRUE.hashCode()

).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

ArrayType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code value for this

ArrayType

instance
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this

ArrayType

instance.

The hash code of an

ArrayType

instance is the sum of the
hash codes of all the elements of information used in

equals

comparisons (i.e. dimension, elements' open type and primitive array flag).
The hashcode for a primitive value is the hashcode of the corresponding boxed
object (e.g. the hashcode for

true

is

Boolean.TRUE.hashCode()

).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

ArrayType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

The hash code of an

ArrayType

instance is the sum of the
hash codes of all the elements of information used in

equals

comparisons (i.e. dimension, elements' open type and primitive array flag).
The hashcode for a primitive value is the hashcode of the corresponding boxed
object (e.g. the hashcode for

true

is

Boolean.TRUE.hashCode()

).
This ensures that

t1.equals(t2)

implies that

t1.hashCode()==t2.hashCode()

for any two

ArrayType

instances

t1

and

t2

,
as required by the general contract of the method

Object.hashCode()

.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

As

ArrayType

instances are immutable, the hash
code for this instance is calculated once, on the first call
to

hashCode

, and then the same value is returned
for subsequent calls.

toString

```java
public
String
toString()
```

Returns a string representation of this

ArrayType

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.ArrayType

), the type name,
the dimension, the elements' open type and the primitive array flag
defined for this instance.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

**Specified by:** toString

in class

OpenType

<

T

>
**Returns:** a string representation of this

ArrayType

instance

---

#### toString

public

String

toString()

Returns a string representation of this

ArrayType

instance.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.ArrayType

), the type name,
the dimension, the elements' open type and the primitive array flag
defined for this instance.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

The string representation consists of the name of this class (i.e.

javax.management.openmbean.ArrayType

), the type name,
the dimension, the elements' open type and the primitive array flag
defined for this instance.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

As

ArrayType

instances are immutable, the
string representation for this instance is calculated
once, on the first call to

toString

, and
then the same value is returned for subsequent calls.

getArrayType

```java
public static <E>
ArrayType
<E[]> getArrayType​(
OpenType
<E> elementType)
throws
OpenDataException
```

Create an

ArrayType

instance in a type-safe manner.

Multidimensional arrays can be built up by calling this method as many
times as necessary.

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

**Type Parameters:** E

- the Java type that described instances must have
**Parameters:** elementType

- the

open type

of element values contained
in the arrays described by this

ArrayType

instance; must be an instance of either

SimpleType

,

CompositeType

,

TabularType

or another

ArrayType

with a

SimpleType

,

CompositeType

or

TabularType

as its

elementType

.
**Returns:** an

ArrayType

instance
**Throws:** OpenDataException

- if

elementType's className

is not
one of the allowed Java class names for open
data.
**Since:** 1.6

---

#### getArrayType

public static <E>

ArrayType

<E[]> getArrayType​(

OpenType

<E> elementType)
throws

OpenDataException

Create an

ArrayType

instance in a type-safe manner.

Multidimensional arrays can be built up by calling this method as many
times as necessary.

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

Multidimensional arrays can be built up by calling this method as many
times as necessary.

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

Calling this method twice with the same parameters may return the same
object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

As an example, the following piece of code:

```java
ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());
```

would produce the following output:

```java
array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String
```

ArrayType<String[]> t1 = ArrayType.getArrayType(SimpleType.STRING);
ArrayType<String[][]> t2 = ArrayType.getArrayType(t1);
ArrayType<String[][][]> t3 = ArrayType.getArrayType(t2);
System.out.println("array class name = " + t3.getClassName());
System.out.println("element class name = " + t3.getElementOpenType().getClassName());
System.out.println("array type name = " + t3.getTypeName());
System.out.println("array type description = " + t3.getDescription());

array class name = [[[Ljava.lang.String;
element class name = java.lang.String
array type name = [[[Ljava.lang.String;
array type description = 3-dimension array of java.lang.String

getPrimitiveArrayType

```java
public static <T>
ArrayType
<T> getPrimitiveArrayType​(
Class
<T> arrayClass)
```

Create an

ArrayType

instance in a type-safe manner.

Calling this method twice with the same parameters may return the
same object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

**Type Parameters:** T

- the Java type that described instances must have
**Parameters:** arrayClass

- a primitive array class such as

int[].class

,

boolean[][].class

, etc. The

getElementOpenType()

method of the returned

ArrayType

returns the

SimpleType

corresponding to the wrapper type of the primitive
type of the array.
**Returns:** an

ArrayType

instance
**Throws:** IllegalArgumentException

- if

arrayClass

is not
a primitive array.
**Since:** 1.6

---

#### getPrimitiveArrayType

public static <T>

ArrayType

<T> getPrimitiveArrayType​(

Class

<T> arrayClass)

Create an

ArrayType

instance in a type-safe manner.

Calling this method twice with the same parameters may return the
same object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

Calling this method twice with the same parameters may return the
same object or two equal but not identical objects.

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

As an example, the following piece of code:

```java
ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());
```

would produce the following output:

```java
array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int
```

ArrayType<int[][][]> t = ArrayType.getPrimitiveArrayType(int[][][].class);
System.out.println("array class name = " + t.getClassName());
System.out.println("element class name = " + t.getElementOpenType().getClassName());
System.out.println("array type name = " + t.getTypeName());
System.out.println("array type description = " + t.getDescription());

array class name = [[[I
element class name = java.lang.Integer
array type name = [[[I
array type description = 3-dimension array of int

---

