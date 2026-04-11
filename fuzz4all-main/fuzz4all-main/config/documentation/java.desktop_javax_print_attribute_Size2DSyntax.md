# Class Size2DSyntax

**Source:** `java.desktop\javax\print\attribute\Size2DSyntax.html`

### Class Description

```java
public abstract class
Size2DSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

Size2DSyntax

is an abstract base class providing the common
implementation of all attributes denoting a size in two dimensions.

A two-dimensional size attribute's value consists of two items, the

X

dimension and the

Y

dimension. A two-dimensional size attribute may
be constructed by supplying the two values and indicating the units in which
the values are measured. Methods are provided to return a two-dimensional
size attribute's values, indicating the units in which the values are to be
returned. The two most common size units are inches (in) and millimeters
(mm), and exported constants

INCH

and

MM

are
provided for indicating those units.

Once constructed, a two-dimensional size attribute's value is immutable.

Design

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final int INCH

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:**
- Constant Field Values

---

#### public static final int MM

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected Size2DSyntax​(float x,
float y,
int units)

Construct a new two-dimensional size attribute from the given
floating-point values.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

INCH

or

MM

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

---

#### protected Size2DSyntax​(int x,
int y,
int units)

Construct a new two-dimensional size attribute from the given integer
values.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

INCH

or

MM

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

---

### Method Details

#### public float[] getSize​(int units)

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- a two-element array with the

X

dimension at index 0 and
the

Y

dimension at index 1

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public float getX​(int units)

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- X

dimension

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public float getY​(int units)

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- Y

dimension

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public
String
toString​(int units,

String
unitsName)

Returns a string version of this two-dimensional size attribute in the
given units. The string takes the form

"

X

x

Y

U

"

, where

X

is the

X

dimension,

Y

is
the

Y

dimension, and

U

is the units name. The values are
displayed in floating point.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM
- unitsName

- units name string, e.g.

in

or

mm

. If

null

, no units name is appended to the result

**Returns:**
- String

version of this two-dimensional size attribute

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public boolean equals​(
Object
object)

Returns whether this two-dimensional size attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

Size2DSyntax

This attribute's

X

dimension is equal to

object

's

X

dimension.

This attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this
two-dimensional size attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this two-dimensional size attribute.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string version of this two-dimensional size attribute. The
string takes the form

"

X

x

Y

um"

, where

X

is the

X

dimension and

Y

is the

Y

dimension. The
values are reported in the internal units of micrometers.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### protected int getXMicrometers()

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:**
- X

dimension (µm)

---

#### protected int getYMicrometers()

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:**
- Y

dimension (µm)

---

### Additional Sections

#### Class Size2DSyntax

java.lang.Object

- javax.print.attribute.Size2DSyntax

javax.print.attribute.Size2DSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** MediaSize

```java
public abstract class
Size2DSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

Size2DSyntax

is an abstract base class providing the common
implementation of all attributes denoting a size in two dimensions.

A two-dimensional size attribute's value consists of two items, the

X

dimension and the

Y

dimension. A two-dimensional size attribute may
be constructed by supplying the two values and indicating the units in which
the values are measured. Methods are provided to return a two-dimensional
size attribute's values, indicating the units in which the values are to be
returned. The two most common size units are inches (in) and millimeters
(mm), and exported constants

INCH

and

MM

are
provided for indicating those units.

Once constructed, a two-dimensional size attribute's value is immutable.

Design

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

**See Also:** Serialized Form

public abstract class

Size2DSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

Size2DSyntax

is an abstract base class providing the common
implementation of all attributes denoting a size in two dimensions.

A two-dimensional size attribute's value consists of two items, the

X

dimension and the

Y

dimension. A two-dimensional size attribute may
be constructed by supplying the two values and indicating the units in which
the values are measured. Methods are provided to return a two-dimensional
size attribute's values, indicating the units in which the values are to be
returned. The two most common size units are inches (in) and millimeters
(mm), and exported constants

INCH

and

MM

are
provided for indicating those units.

Once constructed, a two-dimensional size attribute's value is immutable.

Design

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

A two-dimensional size attribute's value consists of two items, the

X

dimension and the

Y

dimension. A two-dimensional size attribute may
be constructed by supplying the two values and indicating the units in which
the values are measured. Methods are provided to return a two-dimensional
size attribute's values, indicating the units in which the values are to be
returned. The two most common size units are inches (in) and millimeters
(mm), and exported constants

INCH

and

MM

are
provided for indicating those units.

Once constructed, a two-dimensional size attribute's value is immutable.

Design

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

Once constructed, a two-dimensional size attribute's value is immutable.

Design

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

Design

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

A two-dimensional size attribute's

X

and

Y

dimension values
are stored internally as integers in units of micrometers (µm), where 1
micrometer = 10

-6

meter = 1/1000 millimeter = 1/25400 inch. This
permits dimensions to be represented exactly to a precision of 1/1000 mm (= 1
µm) or 1/100 inch (= 254 µm). If fractional inches are expressed in
negative powers of two, this permits dimensions to be represented exactly to
a precision of 1/8 inch (= 3175 µm) but not 1/16 inch (because 1/16 inch
does not equal an integral number of µm).

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

Storing the dimensions internally in common units of µm lets two size
attributes be compared without regard to the units in which they were
created; for example, 8.5 in will compare equal to 215.9 mm, as they both are
stored as 215900 µm. For example, a lookup service can match resolution
attributes based on equality of their serialized representations regardless
of the units in which they were created. Using integers for internal storage
allows precise equality comparisons to be done, which would not be guaranteed
if an internal floating point representation were used. Note that if you're
looking for

U.S. letter

sized media in metric units, you have to
search for a media size of 215.9 x 279.4 mm; rounding off to an integral
216 x 279 mm will not match.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

The exported constant

INCH

is actually the conversion factor by
which to multiply a value in inches to get the value in µm. Likewise,
the exported constant

MM

is the conversion factor by which to
multiply a value in mm to get the value in µm. A client can specify a
resolution value in units other than inches or mm by supplying its own
conversion factor. However, since the internal units of µm was chosen
with supporting only the external units of inch and mm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

INCH

Value to indicate units of inches (in).

static int

MM

Value to indicate units of millimeters (mm).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Size2DSyntax

​(float x,
float y,
int units)

Construct a new two-dimensional size attribute from the given
floating-point values.

protected

Size2DSyntax

​(int x,
int y,
int units)

Construct a new two-dimensional size attribute from the given integer
values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this two-dimensional size attribute is equivalent to the
passed in object.

float[]

getSize

​(int units)

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

float

getX

​(int units)

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

protected int

getXMicrometers

()

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm).

float

getY

​(int units)

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

protected int

getYMicrometers

()

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm).

int

hashCode

()

Returns a hash code value for this two-dimensional size attribute.

String

toString

()

Returns a string version of this two-dimensional size attribute.

String

toString

​(int units,

String

unitsName)

Returns a string version of this two-dimensional size attribute in the
given units.

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

Fields

Modifier and Type

Field

Description

static int

INCH

Value to indicate units of inches (in).

static int

MM

Value to indicate units of millimeters (mm).

---

#### Field Summary

Value to indicate units of inches (in).

Value to indicate units of millimeters (mm).

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Size2DSyntax

​(float x,
float y,
int units)

Construct a new two-dimensional size attribute from the given
floating-point values.

protected

Size2DSyntax

​(int x,
int y,
int units)

Construct a new two-dimensional size attribute from the given integer
values.

---

#### Constructor Summary

Construct a new two-dimensional size attribute from the given
floating-point values.

Construct a new two-dimensional size attribute from the given integer
values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this two-dimensional size attribute is equivalent to the
passed in object.

float[]

getSize

​(int units)

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

float

getX

​(int units)

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

protected int

getXMicrometers

()

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm).

float

getY

​(int units)

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

protected int

getYMicrometers

()

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm).

int

hashCode

()

Returns a hash code value for this two-dimensional size attribute.

String

toString

()

Returns a string version of this two-dimensional size attribute.

String

toString

​(int units,

String

unitsName)

Returns a string version of this two-dimensional size attribute in the
given units.

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

Returns whether this two-dimensional size attribute is equivalent to the
passed in object.

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm).

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm).

Returns a hash code value for this two-dimensional size attribute.

Returns a string version of this two-dimensional size attribute.

Returns a string version of this two-dimensional size attribute in the
given units.

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

============ FIELD DETAIL ===========

- Field Detail

- INCH

```java
public static final int INCH
```

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:** Constant Field Values

- MM

```java
public static final int MM
```

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Size2DSyntax

```java
protected Size2DSyntax​(float x,
float y,
int units)
```

Construct a new two-dimensional size attribute from the given
floating-point values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

- Size2DSyntax

```java
protected Size2DSyntax​(int x,
int y,
int units)
```

Construct a new two-dimensional size attribute from the given integer
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

============ METHOD DETAIL ==========

- Method Detail

- getSize

```java
public float[] getSize​(int units)
```

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** a two-element array with the

X

dimension at index 0 and
the

Y

dimension at index 1
**Throws:** IllegalArgumentException

- if

units < 1

- getX

```java
public float getX​(int units)
```

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** X

dimension
**Throws:** IllegalArgumentException

- if

units < 1

- getY

```java
public float getY​(int units)
```

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** Y

dimension
**Throws:** IllegalArgumentException

- if

units < 1

- toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this two-dimensional size attribute in the
given units. The string takes the form

"

X

x

Y

U

"

, where

X

is the

X

dimension,

Y

is
the

Y

dimension, and

U

is the units name. The values are
displayed in floating point.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Parameters:** unitsName

- units name string, e.g.

in

or

mm

. If

null

, no units name is appended to the result
**Returns:** String

version of this two-dimensional size attribute
**Throws:** IllegalArgumentException

- if

units < 1

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this two-dimensional size attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

Size2DSyntax

This attribute's

X

dimension is equal to

object

's

X

dimension.

This attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this
two-dimensional size attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this two-dimensional size attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string version of this two-dimensional size attribute. The
string takes the form

"

X

x

Y

um"

, where

X

is the

X

dimension and

Y

is the

Y

dimension. The
values are reported in the internal units of micrometers.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getXMicrometers

```java
protected int getXMicrometers()
```

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:** X

dimension (µm)

- getYMicrometers

```java
protected int getYMicrometers()
```

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:** Y

dimension (µm)

Field Detail

- INCH

```java
public static final int INCH
```

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:** Constant Field Values

- MM

```java
public static final int MM
```

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:** Constant Field Values

---

#### Field Detail

INCH

```java
public static final int INCH
```

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:** Constant Field Values

---

#### INCH

public static final int INCH

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

MM

```java
public static final int MM
```

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:** Constant Field Values

---

#### MM

public static final int MM

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

Constructor Detail

- Size2DSyntax

```java
protected Size2DSyntax​(float x,
float y,
int units)
```

Construct a new two-dimensional size attribute from the given
floating-point values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

- Size2DSyntax

```java
protected Size2DSyntax​(int x,
int y,
int units)
```

Construct a new two-dimensional size attribute from the given integer
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

---

#### Constructor Detail

Size2DSyntax

```java
protected Size2DSyntax​(float x,
float y,
int units)
```

Construct a new two-dimensional size attribute from the given
floating-point values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

---

#### Size2DSyntax

protected Size2DSyntax​(float x,
float y,
int units)

Construct a new two-dimensional size attribute from the given
floating-point values.

Size2DSyntax

```java
protected Size2DSyntax​(int x,
int y,
int units)
```

Construct a new two-dimensional size attribute from the given integer
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

---

#### Size2DSyntax

protected Size2DSyntax​(int x,
int y,
int units)

Construct a new two-dimensional size attribute from the given integer
values.

Method Detail

- getSize

```java
public float[] getSize​(int units)
```

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** a two-element array with the

X

dimension at index 0 and
the

Y

dimension at index 1
**Throws:** IllegalArgumentException

- if

units < 1

- getX

```java
public float getX​(int units)
```

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** X

dimension
**Throws:** IllegalArgumentException

- if

units < 1

- getY

```java
public float getY​(int units)
```

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** Y

dimension
**Throws:** IllegalArgumentException

- if

units < 1

- toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this two-dimensional size attribute in the
given units. The string takes the form

"

X

x

Y

U

"

, where

X

is the

X

dimension,

Y

is
the

Y

dimension, and

U

is the units name. The values are
displayed in floating point.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Parameters:** unitsName

- units name string, e.g.

in

or

mm

. If

null

, no units name is appended to the result
**Returns:** String

version of this two-dimensional size attribute
**Throws:** IllegalArgumentException

- if

units < 1

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this two-dimensional size attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

Size2DSyntax

This attribute's

X

dimension is equal to

object

's

X

dimension.

This attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this
two-dimensional size attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this two-dimensional size attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string version of this two-dimensional size attribute. The
string takes the form

"

X

x

Y

um"

, where

X

is the

X

dimension and

Y

is the

Y

dimension. The
values are reported in the internal units of micrometers.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getXMicrometers

```java
protected int getXMicrometers()
```

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:** X

dimension (µm)

- getYMicrometers

```java
protected int getYMicrometers()
```

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:** Y

dimension (µm)

---

#### Method Detail

getSize

```java
public float[] getSize​(int units)
```

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** a two-element array with the

X

dimension at index 0 and
the

Y

dimension at index 1
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getSize

public float[] getSize​(int units)

Get this two-dimensional size attribute's dimensions in the given units
as floating-point values.

getX

```java
public float getX​(int units)
```

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** X

dimension
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getX

public float getX​(int units)

Returns this two-dimensional size attribute's

X

dimension in the
given units as a floating-point value.

getY

```java
public float getY​(int units)
```

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** Y

dimension
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getY

public float getY​(int units)

Returns this two-dimensional size attribute's

Y

dimension in the
given units as a floating-point value.

toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this two-dimensional size attribute in the
given units. The string takes the form

"

X

x

Y

U

"

, where

X

is the

X

dimension,

Y

is
the

Y

dimension, and

U

is the units name. The values are
displayed in floating point.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Parameters:** unitsName

- units name string, e.g.

in

or

mm

. If

null

, no units name is appended to the result
**Returns:** String

version of this two-dimensional size attribute
**Throws:** IllegalArgumentException

- if

units < 1

---

#### toString

public

String

toString​(int units,

String

unitsName)

Returns a string version of this two-dimensional size attribute in the
given units. The string takes the form

"

X

x

Y

U

"

, where

X

is the

X

dimension,

Y

is
the

Y

dimension, and

U

is the units name. The values are
displayed in floating point.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this two-dimensional size attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

Size2DSyntax

This attribute's

X

dimension is equal to

object

's

X

dimension.

This attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this
two-dimensional size attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Returns whether this two-dimensional size attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

Size2DSyntax

This attribute's

X

dimension is equal to

object

's

X

dimension.

This attribute's

Y

dimension is equal to

object

's

Y

dimension.

object

is not

null

.

object

is an instance of class

Size2DSyntax

This attribute's

X

dimension is equal to

object

's

X

dimension.

This attribute's

Y

dimension is equal to

object

's

Y

dimension.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this two-dimensional size attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this two-dimensional size attribute.

toString

```java
public
String
toString()
```

Returns a string version of this two-dimensional size attribute. The
string takes the form

"

X

x

Y

um"

, where

X

is the

X

dimension and

Y

is the

Y

dimension. The
values are reported in the internal units of micrometers.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string version of this two-dimensional size attribute. The
string takes the form

"

X

x

Y

um"

, where

X

is the

X

dimension and

Y

is the

Y

dimension. The
values are reported in the internal units of micrometers.

getXMicrometers

```java
protected int getXMicrometers()
```

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:** X

dimension (µm)

---

#### getXMicrometers

protected int getXMicrometers()

Returns this two-dimensional size attribute's

X

dimension in
units of micrometers (µm). (For use in a subclass.)

getYMicrometers

```java
protected int getYMicrometers()
```

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm). (For use in a subclass.)

**Returns:** Y

dimension (µm)

---

#### getYMicrometers

protected int getYMicrometers()

Returns this two-dimensional size attribute's

Y

dimension in
units of micrometers (µm). (For use in a subclass.)

---

