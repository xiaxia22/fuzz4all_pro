# Class ResolutionSyntax

**Source:** `java.desktop\javax\print\attribute\ResolutionSyntax.html`

### Class Description

```java
public abstract class
ResolutionSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

ResolutionSyntax

is an abstract base class providing the common
implementation of all attributes denoting a printer resolution.

A resolution attribute's value consists of two items, the cross feed
direction resolution and the feed direction resolution. A resolution
attribute may be constructed by supplying the two values and indicating the
units in which the values are measured. Methods are provided to return a
resolution attribute's values, indicating the units in which the values are
to be returned. The two most common resolution units are dots per inch (dpi)
and dots per centimeter (dpcm), and exported constants

DPI

and

DPCM

are provided for indicating those units.

Once constructed, a resolution attribute's value is immutable.

Design

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final int DPI

Value to indicate units of dots per inch (dpi). It is actually the
conversion factor by which to multiply dpi to yield dphi (100).

**See Also:**
- Constant Field Values

---

#### public static final int DPCM

Value to indicate units of dots per centimeter (dpcm). It is actually the
conversion factor by which to multiply dpcm to yield dphi (254).

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ResolutionSyntax​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new resolution attribute from the given items.

**Parameters:**
- crossFeedResolution

- cross feed direction resolution
- feedResolution

- feed direction resolution
- units

- unit conversion factor, e.g.

DPI

or

DPCM

**Throws:**
- IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

---

### Method Details

#### public int[] getResolution​(int units)

Get this resolution attribute's resolution values in the given units. The
values are rounded to the nearest integer.

**Parameters:**
- units

- unit conversion factor, e.g.

DPI

or

DPCM

**Returns:**
- a two-element array with the cross feed direction resolution at
index 0 and the feed direction resolution at index 1

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public int getCrossFeedResolution​(int units)

Returns this resolution attribute's cross feed direction resolution in
the given units. The value is rounded to the nearest integer.

**Parameters:**
- units

- unit conversion factor, e.g.

DPI

or

DPCM

**Returns:**
- cross feed direction resolution

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public int getFeedResolution​(int units)

Returns this resolution attribute's feed direction resolution in the
given units. The value is rounded to the nearest integer.

**Parameters:**
- units

- unit conversion factor, e.g.

DPI

or

DPCM

**Returns:**
- feed direction resolution

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

Returns a string version of this resolution attribute in the given units.
The string takes the form

"

C

x

F

U

"

,
where

C

is the cross feed direction resolution,

F

is the
feed direction resolution, and

U

is the units name. The values are
rounded to the nearest integer.

**Parameters:**
- units

- unit conversion factor, e.g.

CODE>DPI

or

DPCM
- unitsName

- units name string, e.g.

"dpi"

or

"dpcm"

. If

null

, no units name is appended to the
result.

**Returns:**
- string version of this resolution attribute

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public boolean lessThanOrEquals​(
ResolutionSyntax
other)

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value. This is true if all of the
following conditions are true:

- This attribute's cross feed direction resolution is less than or
equal to the

other

attribute's cross feed direction resolution.

This attribute's feed direction resolution is less than or equal to
the

other

attribute's feed direction resolution.

**Parameters:**
- other

- resolution attribute to compare with

**Returns:**
- true

if this resolution attribute is less than or equal
to the

other

resolution attribute,

false

otherwise

**Throws:**
- NullPointerException

- if

other

is

null

---

#### public boolean equals​(
Object
object)

Returns whether this resolution attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

ResolutionSyntax

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

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

is equivalent to this resolution
attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this resolution attribute.

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

Returns a string version of this resolution attribute. The string takes
the form

"

C

x

F

dphi"

, where

C

is the
cross feed direction resolution and

F

is the feed direction
resolution. The values are reported in the internal units of dphi.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### protected int getCrossFeedResolutionDphi()

Returns this resolution attribute's cross feed direction resolution in
units of dphi. (For use in a subclass.)

**Returns:**
- cross feed direction resolution

---

#### protected int getFeedResolutionDphi()

Returns this resolution attribute's feed direction resolution in units of
dphi. (For use in a subclass.)

**Returns:**
- feed direction resolution

---

### Additional Sections

#### Class ResolutionSyntax

java.lang.Object

- javax.print.attribute.ResolutionSyntax

javax.print.attribute.ResolutionSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** PrinterResolution

```java
public abstract class
ResolutionSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

ResolutionSyntax

is an abstract base class providing the common
implementation of all attributes denoting a printer resolution.

A resolution attribute's value consists of two items, the cross feed
direction resolution and the feed direction resolution. A resolution
attribute may be constructed by supplying the two values and indicating the
units in which the values are measured. Methods are provided to return a
resolution attribute's values, indicating the units in which the values are
to be returned. The two most common resolution units are dots per inch (dpi)
and dots per centimeter (dpcm), and exported constants

DPI

and

DPCM

are provided for indicating those units.

Once constructed, a resolution attribute's value is immutable.

Design

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

**See Also:** Serialized Form

public abstract class

ResolutionSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

ResolutionSyntax

is an abstract base class providing the common
implementation of all attributes denoting a printer resolution.

A resolution attribute's value consists of two items, the cross feed
direction resolution and the feed direction resolution. A resolution
attribute may be constructed by supplying the two values and indicating the
units in which the values are measured. Methods are provided to return a
resolution attribute's values, indicating the units in which the values are
to be returned. The two most common resolution units are dots per inch (dpi)
and dots per centimeter (dpcm), and exported constants

DPI

and

DPCM

are provided for indicating those units.

Once constructed, a resolution attribute's value is immutable.

Design

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

A resolution attribute's value consists of two items, the cross feed
direction resolution and the feed direction resolution. A resolution
attribute may be constructed by supplying the two values and indicating the
units in which the values are measured. Methods are provided to return a
resolution attribute's values, indicating the units in which the values are
to be returned. The two most common resolution units are dots per inch (dpi)
and dots per centimeter (dpcm), and exported constants

DPI

and

DPCM

are provided for indicating those units.

Once constructed, a resolution attribute's value is immutable.

Design

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

Once constructed, a resolution attribute's value is immutable.

Design

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

Design

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

A resolution attribute's cross feed direction resolution and feed direction
resolution values are stored internally using units of dots per 100 inches
(dphi). Storing the values in dphi rather than, say, metric units allows
precise integer arithmetic conversions between dpi and dphi and between dpcm
and dphi: 1 dpi = 100 dphi, 1 dpcm = 254 dphi. Thus, the values can be stored
into and retrieved back from a resolution attribute in either units with no
loss of precision. This would not be guaranteed if a floating point
representation were used. However, roundoff error will in general occur if a
resolution attribute's values are created in one units and retrieved in
different units; for example, 600 dpi will be rounded to 236 dpcm, whereas
the true value (to five figures) is 236.22 dpcm.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

Storing the values internally in common units of dphi lets two resolution
attributes be compared without regard to the units in which they were
created; for example, 300 dpcm will compare equal to 762 dpi, as they both
are stored as 76200 dphi. In particular, a lookup service can match
resolution attributes based on equality of their serialized representations
regardless of the units in which they were created. Again, using integers for
internal storage allows precise equality comparisons to be done, which would
not be guaranteed if a floating point representation were used.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
guarantee that the conversion factor for the client's units will be an exact
integer. If the conversion factor isn't an exact integer, resolution values
in the client's units won't be stored precisely.

The exported constant

DPI

is actually the conversion factor by
which to multiply a value in dpi to get the value in dphi. Likewise, the
exported constant

DPCM

is the conversion factor by which to
multiply a value in dpcm to get the value in dphi. A client can specify a
resolution value in units other than dpi or dpcm by supplying its own
conversion factor. However, since the internal units of dphi was chosen with
supporting only the external units of dpi and dpcm in mind, there is no
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

DPCM

Value to indicate units of dots per centimeter (dpcm).

static int

DPI

Value to indicate units of dots per inch (dpi).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ResolutionSyntax

​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new resolution attribute from the given items.

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

Returns whether this resolution attribute is equivalent to the passed in
object.

int

getCrossFeedResolution

​(int units)

Returns this resolution attribute's cross feed direction resolution in
the given units.

protected int

getCrossFeedResolutionDphi

()

Returns this resolution attribute's cross feed direction resolution in
units of dphi.

int

getFeedResolution

​(int units)

Returns this resolution attribute's feed direction resolution in the
given units.

protected int

getFeedResolutionDphi

()

Returns this resolution attribute's feed direction resolution in units of
dphi.

int[]

getResolution

​(int units)

Get this resolution attribute's resolution values in the given units.

int

hashCode

()

Returns a hash code value for this resolution attribute.

boolean

lessThanOrEquals

​(

ResolutionSyntax

other)

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value.

String

toString

()

Returns a string version of this resolution attribute.

String

toString

​(int units,

String

unitsName)

Returns a string version of this resolution attribute in the given units.

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

DPCM

Value to indicate units of dots per centimeter (dpcm).

static int

DPI

Value to indicate units of dots per inch (dpi).

---

#### Field Summary

Value to indicate units of dots per centimeter (dpcm).

Value to indicate units of dots per inch (dpi).

Constructor Summary

Constructors

Constructor

Description

ResolutionSyntax

​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new resolution attribute from the given items.

---

#### Constructor Summary

Construct a new resolution attribute from the given items.

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

Returns whether this resolution attribute is equivalent to the passed in
object.

int

getCrossFeedResolution

​(int units)

Returns this resolution attribute's cross feed direction resolution in
the given units.

protected int

getCrossFeedResolutionDphi

()

Returns this resolution attribute's cross feed direction resolution in
units of dphi.

int

getFeedResolution

​(int units)

Returns this resolution attribute's feed direction resolution in the
given units.

protected int

getFeedResolutionDphi

()

Returns this resolution attribute's feed direction resolution in units of
dphi.

int[]

getResolution

​(int units)

Get this resolution attribute's resolution values in the given units.

int

hashCode

()

Returns a hash code value for this resolution attribute.

boolean

lessThanOrEquals

​(

ResolutionSyntax

other)

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value.

String

toString

()

Returns a string version of this resolution attribute.

String

toString

​(int units,

String

unitsName)

Returns a string version of this resolution attribute in the given units.

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

Returns whether this resolution attribute is equivalent to the passed in
object.

Returns this resolution attribute's cross feed direction resolution in
the given units.

Returns this resolution attribute's cross feed direction resolution in
units of dphi.

Returns this resolution attribute's feed direction resolution in the
given units.

Returns this resolution attribute's feed direction resolution in units of
dphi.

Get this resolution attribute's resolution values in the given units.

Returns a hash code value for this resolution attribute.

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value.

Returns a string version of this resolution attribute.

Returns a string version of this resolution attribute in the given units.

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

- DPI

```java
public static final int DPI
```

Value to indicate units of dots per inch (dpi). It is actually the
conversion factor by which to multiply dpi to yield dphi (100).

**See Also:** Constant Field Values

- DPCM

```java
public static final int DPCM
```

Value to indicate units of dots per centimeter (dpcm). It is actually the
conversion factor by which to multiply dpcm to yield dphi (254).

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ResolutionSyntax

```java
public ResolutionSyntax​(int crossFeedResolution,
int feedResolution,
int units)
```

Construct a new resolution attribute from the given items.

**Parameters:** crossFeedResolution

- cross feed direction resolution
**Parameters:** feedResolution

- feed direction resolution
**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Throws:** IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

============ METHOD DETAIL ==========

- Method Detail

- getResolution

```java
public int[] getResolution​(int units)
```

Get this resolution attribute's resolution values in the given units. The
values are rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** a two-element array with the cross feed direction resolution at
index 0 and the feed direction resolution at index 1
**Throws:** IllegalArgumentException

- if

units < 1

- getCrossFeedResolution

```java
public int getCrossFeedResolution​(int units)
```

Returns this resolution attribute's cross feed direction resolution in
the given units. The value is rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** cross feed direction resolution
**Throws:** IllegalArgumentException

- if

units < 1

- getFeedResolution

```java
public int getFeedResolution​(int units)
```

Returns this resolution attribute's feed direction resolution in the
given units. The value is rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** feed direction resolution
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

Returns a string version of this resolution attribute in the given units.
The string takes the form

"

C

x

F

U

"

,
where

C

is the cross feed direction resolution,

F

is the
feed direction resolution, and

U

is the units name. The values are
rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

CODE>DPI

or

DPCM
**Parameters:** unitsName

- units name string, e.g.

"dpi"

or

"dpcm"

. If

null

, no units name is appended to the
result.
**Returns:** string version of this resolution attribute
**Throws:** IllegalArgumentException

- if

units < 1

- lessThanOrEquals

```java
public boolean lessThanOrEquals​(
ResolutionSyntax
other)
```

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value. This is true if all of the
following conditions are true:

- This attribute's cross feed direction resolution is less than or
equal to the

other

attribute's cross feed direction resolution.

This attribute's feed direction resolution is less than or equal to
the

other

attribute's feed direction resolution.

**Parameters:** other

- resolution attribute to compare with
**Returns:** true

if this resolution attribute is less than or equal
to the

other

resolution attribute,

false

otherwise
**Throws:** NullPointerException

- if

other

is

null

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this resolution attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

ResolutionSyntax

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

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

is equivalent to this resolution
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this resolution attribute.

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

Returns a string version of this resolution attribute. The string takes
the form

"

C

x

F

dphi"

, where

C

is the
cross feed direction resolution and

F

is the feed direction
resolution. The values are reported in the internal units of dphi.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getCrossFeedResolutionDphi

```java
protected int getCrossFeedResolutionDphi()
```

Returns this resolution attribute's cross feed direction resolution in
units of dphi. (For use in a subclass.)

**Returns:** cross feed direction resolution

- getFeedResolutionDphi

```java
protected int getFeedResolutionDphi()
```

Returns this resolution attribute's feed direction resolution in units of
dphi. (For use in a subclass.)

**Returns:** feed direction resolution

Field Detail

- DPI

```java
public static final int DPI
```

Value to indicate units of dots per inch (dpi). It is actually the
conversion factor by which to multiply dpi to yield dphi (100).

**See Also:** Constant Field Values

- DPCM

```java
public static final int DPCM
```

Value to indicate units of dots per centimeter (dpcm). It is actually the
conversion factor by which to multiply dpcm to yield dphi (254).

**See Also:** Constant Field Values

---

#### Field Detail

DPI

```java
public static final int DPI
```

Value to indicate units of dots per inch (dpi). It is actually the
conversion factor by which to multiply dpi to yield dphi (100).

**See Also:** Constant Field Values

---

#### DPI

public static final int DPI

Value to indicate units of dots per inch (dpi). It is actually the
conversion factor by which to multiply dpi to yield dphi (100).

DPCM

```java
public static final int DPCM
```

Value to indicate units of dots per centimeter (dpcm). It is actually the
conversion factor by which to multiply dpcm to yield dphi (254).

**See Also:** Constant Field Values

---

#### DPCM

public static final int DPCM

Value to indicate units of dots per centimeter (dpcm). It is actually the
conversion factor by which to multiply dpcm to yield dphi (254).

Constructor Detail

- ResolutionSyntax

```java
public ResolutionSyntax​(int crossFeedResolution,
int feedResolution,
int units)
```

Construct a new resolution attribute from the given items.

**Parameters:** crossFeedResolution

- cross feed direction resolution
**Parameters:** feedResolution

- feed direction resolution
**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Throws:** IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

---

#### Constructor Detail

ResolutionSyntax

```java
public ResolutionSyntax​(int crossFeedResolution,
int feedResolution,
int units)
```

Construct a new resolution attribute from the given items.

**Parameters:** crossFeedResolution

- cross feed direction resolution
**Parameters:** feedResolution

- feed direction resolution
**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Throws:** IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

---

#### ResolutionSyntax

public ResolutionSyntax​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new resolution attribute from the given items.

Method Detail

- getResolution

```java
public int[] getResolution​(int units)
```

Get this resolution attribute's resolution values in the given units. The
values are rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** a two-element array with the cross feed direction resolution at
index 0 and the feed direction resolution at index 1
**Throws:** IllegalArgumentException

- if

units < 1

- getCrossFeedResolution

```java
public int getCrossFeedResolution​(int units)
```

Returns this resolution attribute's cross feed direction resolution in
the given units. The value is rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** cross feed direction resolution
**Throws:** IllegalArgumentException

- if

units < 1

- getFeedResolution

```java
public int getFeedResolution​(int units)
```

Returns this resolution attribute's feed direction resolution in the
given units. The value is rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** feed direction resolution
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

Returns a string version of this resolution attribute in the given units.
The string takes the form

"

C

x

F

U

"

,
where

C

is the cross feed direction resolution,

F

is the
feed direction resolution, and

U

is the units name. The values are
rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

CODE>DPI

or

DPCM
**Parameters:** unitsName

- units name string, e.g.

"dpi"

or

"dpcm"

. If

null

, no units name is appended to the
result.
**Returns:** string version of this resolution attribute
**Throws:** IllegalArgumentException

- if

units < 1

- lessThanOrEquals

```java
public boolean lessThanOrEquals​(
ResolutionSyntax
other)
```

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value. This is true if all of the
following conditions are true:

- This attribute's cross feed direction resolution is less than or
equal to the

other

attribute's cross feed direction resolution.

This attribute's feed direction resolution is less than or equal to
the

other

attribute's feed direction resolution.

**Parameters:** other

- resolution attribute to compare with
**Returns:** true

if this resolution attribute is less than or equal
to the

other

resolution attribute,

false

otherwise
**Throws:** NullPointerException

- if

other

is

null

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this resolution attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

ResolutionSyntax

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

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

is equivalent to this resolution
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this resolution attribute.

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

Returns a string version of this resolution attribute. The string takes
the form

"

C

x

F

dphi"

, where

C

is the
cross feed direction resolution and

F

is the feed direction
resolution. The values are reported in the internal units of dphi.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getCrossFeedResolutionDphi

```java
protected int getCrossFeedResolutionDphi()
```

Returns this resolution attribute's cross feed direction resolution in
units of dphi. (For use in a subclass.)

**Returns:** cross feed direction resolution

- getFeedResolutionDphi

```java
protected int getFeedResolutionDphi()
```

Returns this resolution attribute's feed direction resolution in units of
dphi. (For use in a subclass.)

**Returns:** feed direction resolution

---

#### Method Detail

getResolution

```java
public int[] getResolution​(int units)
```

Get this resolution attribute's resolution values in the given units. The
values are rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** a two-element array with the cross feed direction resolution at
index 0 and the feed direction resolution at index 1
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getResolution

public int[] getResolution​(int units)

Get this resolution attribute's resolution values in the given units. The
values are rounded to the nearest integer.

getCrossFeedResolution

```java
public int getCrossFeedResolution​(int units)
```

Returns this resolution attribute's cross feed direction resolution in
the given units. The value is rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** cross feed direction resolution
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getCrossFeedResolution

public int getCrossFeedResolution​(int units)

Returns this resolution attribute's cross feed direction resolution in
the given units. The value is rounded to the nearest integer.

getFeedResolution

```java
public int getFeedResolution​(int units)
```

Returns this resolution attribute's feed direction resolution in the
given units. The value is rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

DPI

or

DPCM
**Returns:** feed direction resolution
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getFeedResolution

public int getFeedResolution​(int units)

Returns this resolution attribute's feed direction resolution in the
given units. The value is rounded to the nearest integer.

toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this resolution attribute in the given units.
The string takes the form

"

C

x

F

U

"

,
where

C

is the cross feed direction resolution,

F

is the
feed direction resolution, and

U

is the units name. The values are
rounded to the nearest integer.

**Parameters:** units

- unit conversion factor, e.g.

CODE>DPI

or

DPCM
**Parameters:** unitsName

- units name string, e.g.

"dpi"

or

"dpcm"

. If

null

, no units name is appended to the
result.
**Returns:** string version of this resolution attribute
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

Returns a string version of this resolution attribute in the given units.
The string takes the form

"

C

x

F

U

"

,
where

C

is the cross feed direction resolution,

F

is the
feed direction resolution, and

U

is the units name. The values are
rounded to the nearest integer.

lessThanOrEquals

```java
public boolean lessThanOrEquals​(
ResolutionSyntax
other)
```

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value. This is true if all of the
following conditions are true:

- This attribute's cross feed direction resolution is less than or
equal to the

other

attribute's cross feed direction resolution.

This attribute's feed direction resolution is less than or equal to
the

other

attribute's feed direction resolution.

**Parameters:** other

- resolution attribute to compare with
**Returns:** true

if this resolution attribute is less than or equal
to the

other

resolution attribute,

false

otherwise
**Throws:** NullPointerException

- if

other

is

null

---

#### lessThanOrEquals

public boolean lessThanOrEquals​(

ResolutionSyntax

other)

Determine whether this resolution attribute's value is less than or equal
to the given resolution attribute's value. This is true if all of the
following conditions are true:

- This attribute's cross feed direction resolution is less than or
equal to the

other

attribute's cross feed direction resolution.

This attribute's feed direction resolution is less than or equal to
the

other

attribute's feed direction resolution.

This attribute's cross feed direction resolution is less than or
equal to the

other

attribute's cross feed direction resolution.

This attribute's feed direction resolution is less than or equal to
the

other

attribute's feed direction resolution.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this resolution attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

ResolutionSyntax

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

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

is equivalent to this resolution
attribute,

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

Returns whether this resolution attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

ResolutionSyntax

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

object

is not

null

.

object

is an instance of class

ResolutionSyntax

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this resolution attribute.

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

Returns a hash code value for this resolution attribute.

toString

```java
public
String
toString()
```

Returns a string version of this resolution attribute. The string takes
the form

"

C

x

F

dphi"

, where

C

is the
cross feed direction resolution and

F

is the feed direction
resolution. The values are reported in the internal units of dphi.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string version of this resolution attribute. The string takes
the form

"

C

x

F

dphi"

, where

C

is the
cross feed direction resolution and

F

is the feed direction
resolution. The values are reported in the internal units of dphi.

getCrossFeedResolutionDphi

```java
protected int getCrossFeedResolutionDphi()
```

Returns this resolution attribute's cross feed direction resolution in
units of dphi. (For use in a subclass.)

**Returns:** cross feed direction resolution

---

#### getCrossFeedResolutionDphi

protected int getCrossFeedResolutionDphi()

Returns this resolution attribute's cross feed direction resolution in
units of dphi. (For use in a subclass.)

getFeedResolutionDphi

```java
protected int getFeedResolutionDphi()
```

Returns this resolution attribute's feed direction resolution in units of
dphi. (For use in a subclass.)

**Returns:** feed direction resolution

---

#### getFeedResolutionDphi

protected int getFeedResolutionDphi()

Returns this resolution attribute's feed direction resolution in units of
dphi. (For use in a subclass.)

---

