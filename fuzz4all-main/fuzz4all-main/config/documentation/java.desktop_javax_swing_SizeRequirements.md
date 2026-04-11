# Class SizeRequirements

**Source:** `java.desktop\javax\swing\SizeRequirements.html`

### Class Description

```java
public class
SizeRequirements

extends
Object

implements
Serializable
```

For the convenience of layout managers,
calculates information about the size and position of components.
All size and position calculation methods are class methods
that take arrays of SizeRequirements as arguments.
The SizeRequirements class supports two types of layout:

Each SizeRequirements object contains information
about either the width (and X alignment)
or height (and Y alignment)
of a single component or a group of components:

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public int minimum

The minimum size required.
For a component

comp

, this should be equal to either

comp.getMinimumSize().width

or

comp.getMinimumSize().height

.

---

#### public int preferred

The preferred (natural) size.
For a component

comp

, this should be equal to either

comp.getPreferredSize().width

or

comp.getPreferredSize().height

.

---

#### public int maximum

The maximum size allowed.
For a component

comp

, this should be equal to either

comp.getMaximumSize().width

or

comp.getMaximumSize().height

.

---

#### public float alignment

The alignment, specified as a value between 0.0 and 1.0,
inclusive.
To specify centering, the alignment should be 0.5.

---

### Constructor Details

#### public SizeRequirements()

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

---

#### public SizeRequirements​(int min,
int pref,
int max,
float a)

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

**Parameters:**
- min

- the minimum size >= 0
- pref

- the preferred size >= 0
- max

- the maximum size >= 0
- a

- the alignment >= 0.0f && <= 1.0f

---

### Method Details

#### public
String
toString()

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string

---

#### public static
SizeRequirements
getTiledSizeRequirements​(
SizeRequirements
[] children)

Determines the total space necessary to
place a set of components end-to-end. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array.
The returned SizeRequirements object has an alignment of 0.5
(centered). The space requirement is never more than
Integer.MAX_VALUE.

**Parameters:**
- children

- the space requirements for a set of components.
The vector may be of zero length, which will result in a
default SizeRequirements object instance being passed back.

**Returns:**
- the total space requirements.

---

#### public static
SizeRequirements
getAlignedSizeRequirements​(
SizeRequirements
[] children)

Determines the total space necessary to
align a set of components. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array. The total space required will
never be more than Integer.MAX_VALUE.

**Parameters:**
- children

- the set of child requirements. If of zero length,
the returns result will be a default instance of SizeRequirements.

**Returns:**
- the total space requirements.

---

#### public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method. The components
will be tiled in the forward direction with offsets increasing from 0.

**Parameters:**
- allocated

- the total span to be allocated >= 0.
- total

- the total of the children requests. This argument
is optional and may be null.
- children

- the size requirements for each component.
- offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
- spans

- the span allocated for each child to make the
total target span.

---

#### public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean forward)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method.

This method also requires a flag indicating whether components
should be tiled in the forward direction (offsets increasing
from 0) or reverse direction (offsets decreasing from the end
of the allocated space). The forward direction represents
components tiled from left to right or top to bottom. The
reverse direction represents components tiled from right to left
or bottom to top.

**Parameters:**
- allocated

- the total span to be allocated >= 0.
- total

- the total of the children requests. This argument
is optional and may be null.
- children

- the size requirements for each component.
- offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
- spans

- the span allocated for each child to make the
total target span.
- forward

- tile with offsets increasing from 0 if true
and with offsets decreasing from the end of the allocated space
if false.

**Since:**
- 1.4

---

#### public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used).
You can get the total size requirement by invoking
getAlignedSizeRequirements.

Normal alignment will be done with an alignment value of 0.0f
representing the left/top edge of a component.

**Parameters:**
- allocated

- the total span to be allocated >= 0.
- total

- the total of the children requests.
- children

- the size requirements for each component.
- offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
- spans

- the span allocated for each child to make the
total target span.

---

#### public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean normal)

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used)
You can get the total size requirement by invoking
getAlignedSizeRequirements.

This method also requires a flag indicating whether normal or
reverse alignment should be performed. With normal alignment
the value 0.0f represents the left/top edge of the component
to be aligned. With reverse alignment, 0.0f represents the
right/bottom edge.

**Parameters:**
- allocated

- the total span to be allocated >= 0.
- total

- the total of the children requests.
- children

- the size requirements for each component.
- offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
- spans

- the span allocated for each child to make the
total target span.
- normal

- when true, the alignment value 0.0f means
left/top; when false, it means right/bottom.

**Since:**
- 1.4

---

#### public static int[] adjustSizes​(int delta,

SizeRequirements
[] children)

Adjust a specified array of sizes by a given amount.

**Parameters:**
- delta

- an int specifying the size difference
- children

- an array of SizeRequirements objects

**Returns:**
- an array of ints containing the final size for each item

---

### Additional Sections

#### Class SizeRequirements

java.lang.Object

- javax.swing.SizeRequirements

javax.swing.SizeRequirements

**All Implemented Interfaces:** Serializable

```java
public class
SizeRequirements

extends
Object

implements
Serializable
```

For the convenience of layout managers,
calculates information about the size and position of components.
All size and position calculation methods are class methods
that take arrays of SizeRequirements as arguments.
The SizeRequirements class supports two types of layout:

Each SizeRequirements object contains information
about either the width (and X alignment)
or height (and Y alignment)
of a single component or a group of components:

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** Component.getMinimumSize()

,

Component.getPreferredSize()

,

Component.getMaximumSize()

,

Component.getAlignmentX()

,

Component.getAlignmentY()

,

Serialized Form

public class

SizeRequirements

extends

Object

implements

Serializable

For the convenience of layout managers,
calculates information about the size and position of components.
All size and position calculation methods are class methods
that take arrays of SizeRequirements as arguments.
The SizeRequirements class supports two types of layout:

Each SizeRequirements object contains information
about either the width (and X alignment)
or height (and Y alignment)
of a single component or a group of components:

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Each SizeRequirements object contains information
about either the width (and X alignment)
or height (and Y alignment)
of a single component or a group of components:

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

float

alignment

The alignment, specified as a value between 0.0 and 1.0,
inclusive.

int

maximum

The maximum size allowed.

int

minimum

The minimum size required.

int

preferred

The preferred (natural) size.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SizeRequirements

()

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

SizeRequirements

​(int min,
int pref,
int max,
float a)

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static int[]

adjustSizes

​(int delta,

SizeRequirements

[] children)

Adjust a specified array of sizes by a given amount.

static void

calculateAlignedPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans)

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.

static void

calculateAlignedPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans,
boolean normal)

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.

static void

calculateTiledPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.

static void

calculateTiledPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans,
boolean forward)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.

static

SizeRequirements

getAlignedSizeRequirements

​(

SizeRequirements

[] children)

Determines the total space necessary to
align a set of components.

static

SizeRequirements

getTiledSizeRequirements

​(

SizeRequirements

[] children)

Determines the total space necessary to
place a set of components end-to-end.

String

toString

()

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

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

Field Summary

Fields

Modifier and Type

Field

Description

float

alignment

The alignment, specified as a value between 0.0 and 1.0,
inclusive.

int

maximum

The maximum size allowed.

int

minimum

The minimum size required.

int

preferred

The preferred (natural) size.

---

#### Field Summary

The alignment, specified as a value between 0.0 and 1.0,
inclusive.

The maximum size allowed.

The minimum size required.

The preferred (natural) size.

Constructor Summary

Constructors

Constructor

Description

SizeRequirements

()

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

SizeRequirements

​(int min,
int pref,
int max,
float a)

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

---

#### Constructor Summary

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static int[]

adjustSizes

​(int delta,

SizeRequirements

[] children)

Adjust a specified array of sizes by a given amount.

static void

calculateAlignedPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans)

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.

static void

calculateAlignedPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans,
boolean normal)

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.

static void

calculateTiledPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.

static void

calculateTiledPositions

​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans,
boolean forward)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.

static

SizeRequirements

getAlignedSizeRequirements

​(

SizeRequirements

[] children)

Determines the total space necessary to
align a set of components.

static

SizeRequirements

getTiledSizeRequirements

​(

SizeRequirements

[] children)

Determines the total space necessary to
place a set of components end-to-end.

String

toString

()

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

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

Adjust a specified array of sizes by a given amount.

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.

Determines the total space necessary to
align a set of components.

Determines the total space necessary to
place a set of components end-to-end.

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

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

============ FIELD DETAIL ===========

- Field Detail

- minimum

```java
public int minimum
```

The minimum size required.
For a component

comp

, this should be equal to either

comp.getMinimumSize().width

or

comp.getMinimumSize().height

.

- preferred

```java
public int preferred
```

The preferred (natural) size.
For a component

comp

, this should be equal to either

comp.getPreferredSize().width

or

comp.getPreferredSize().height

.

- maximum

```java
public int maximum
```

The maximum size allowed.
For a component

comp

, this should be equal to either

comp.getMaximumSize().width

or

comp.getMaximumSize().height

.

- alignment

```java
public float alignment
```

The alignment, specified as a value between 0.0 and 1.0,
inclusive.
To specify centering, the alignment should be 0.5.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SizeRequirements

```java
public SizeRequirements()
```

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

- SizeRequirements

```java
public SizeRequirements​(int min,
int pref,
int max,
float a)
```

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

**Parameters:** min

- the minimum size >= 0
**Parameters:** pref

- the preferred size >= 0
**Parameters:** max

- the maximum size >= 0
**Parameters:** a

- the alignment >= 0.0f && <= 1.0f

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

**Overrides:** toString

in class

Object
**Returns:** the string

- getTiledSizeRequirements

```java
public static
SizeRequirements
getTiledSizeRequirements​(
SizeRequirements
[] children)
```

Determines the total space necessary to
place a set of components end-to-end. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array.
The returned SizeRequirements object has an alignment of 0.5
(centered). The space requirement is never more than
Integer.MAX_VALUE.

**Parameters:** children

- the space requirements for a set of components.
The vector may be of zero length, which will result in a
default SizeRequirements object instance being passed back.
**Returns:** the total space requirements.

- getAlignedSizeRequirements

```java
public static
SizeRequirements
getAlignedSizeRequirements​(
SizeRequirements
[] children)
```

Determines the total space necessary to
align a set of components. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array. The total space required will
never be more than Integer.MAX_VALUE.

**Parameters:** children

- the set of child requirements. If of zero length,
the returns result will be a default instance of SizeRequirements.
**Returns:** the total space requirements.

- calculateTiledPositions

```java
public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)
```

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method. The components
will be tiled in the forward direction with offsets increasing from 0.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests. This argument
is optional and may be null.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.

- calculateTiledPositions

```java
public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean forward)
```

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method.

This method also requires a flag indicating whether components
should be tiled in the forward direction (offsets increasing
from 0) or reverse direction (offsets decreasing from the end
of the allocated space). The forward direction represents
components tiled from left to right or top to bottom. The
reverse direction represents components tiled from right to left
or bottom to top.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests. This argument
is optional and may be null.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.
**Parameters:** forward

- tile with offsets increasing from 0 if true
and with offsets decreasing from the end of the allocated space
if false.
**Since:** 1.4

- calculateAlignedPositions

```java
public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)
```

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used).
You can get the total size requirement by invoking
getAlignedSizeRequirements.

Normal alignment will be done with an alignment value of 0.0f
representing the left/top edge of a component.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.

- calculateAlignedPositions

```java
public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean normal)
```

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used)
You can get the total size requirement by invoking
getAlignedSizeRequirements.

This method also requires a flag indicating whether normal or
reverse alignment should be performed. With normal alignment
the value 0.0f represents the left/top edge of the component
to be aligned. With reverse alignment, 0.0f represents the
right/bottom edge.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.
**Parameters:** normal

- when true, the alignment value 0.0f means
left/top; when false, it means right/bottom.
**Since:** 1.4

- adjustSizes

```java
public static int[] adjustSizes​(int delta,

SizeRequirements
[] children)
```

Adjust a specified array of sizes by a given amount.

**Parameters:** delta

- an int specifying the size difference
**Parameters:** children

- an array of SizeRequirements objects
**Returns:** an array of ints containing the final size for each item

Field Detail

- minimum

```java
public int minimum
```

The minimum size required.
For a component

comp

, this should be equal to either

comp.getMinimumSize().width

or

comp.getMinimumSize().height

.

- preferred

```java
public int preferred
```

The preferred (natural) size.
For a component

comp

, this should be equal to either

comp.getPreferredSize().width

or

comp.getPreferredSize().height

.

- maximum

```java
public int maximum
```

The maximum size allowed.
For a component

comp

, this should be equal to either

comp.getMaximumSize().width

or

comp.getMaximumSize().height

.

- alignment

```java
public float alignment
```

The alignment, specified as a value between 0.0 and 1.0,
inclusive.
To specify centering, the alignment should be 0.5.

---

#### Field Detail

minimum

```java
public int minimum
```

The minimum size required.
For a component

comp

, this should be equal to either

comp.getMinimumSize().width

or

comp.getMinimumSize().height

.

---

#### minimum

public int minimum

The minimum size required.
For a component

comp

, this should be equal to either

comp.getMinimumSize().width

or

comp.getMinimumSize().height

.

preferred

```java
public int preferred
```

The preferred (natural) size.
For a component

comp

, this should be equal to either

comp.getPreferredSize().width

or

comp.getPreferredSize().height

.

---

#### preferred

public int preferred

The preferred (natural) size.
For a component

comp

, this should be equal to either

comp.getPreferredSize().width

or

comp.getPreferredSize().height

.

maximum

```java
public int maximum
```

The maximum size allowed.
For a component

comp

, this should be equal to either

comp.getMaximumSize().width

or

comp.getMaximumSize().height

.

---

#### maximum

public int maximum

The maximum size allowed.
For a component

comp

, this should be equal to either

comp.getMaximumSize().width

or

comp.getMaximumSize().height

.

alignment

```java
public float alignment
```

The alignment, specified as a value between 0.0 and 1.0,
inclusive.
To specify centering, the alignment should be 0.5.

---

#### alignment

public float alignment

The alignment, specified as a value between 0.0 and 1.0,
inclusive.
To specify centering, the alignment should be 0.5.

Constructor Detail

- SizeRequirements

```java
public SizeRequirements()
```

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

- SizeRequirements

```java
public SizeRequirements​(int min,
int pref,
int max,
float a)
```

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

**Parameters:** min

- the minimum size >= 0
**Parameters:** pref

- the preferred size >= 0
**Parameters:** max

- the maximum size >= 0
**Parameters:** a

- the alignment >= 0.0f && <= 1.0f

---

#### Constructor Detail

SizeRequirements

```java
public SizeRequirements()
```

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

---

#### SizeRequirements

public SizeRequirements()

Creates a SizeRequirements object with the minimum, preferred,
and maximum sizes set to zero and an alignment value of 0.5
(centered).

SizeRequirements

```java
public SizeRequirements​(int min,
int pref,
int max,
float a)
```

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

**Parameters:** min

- the minimum size >= 0
**Parameters:** pref

- the preferred size >= 0
**Parameters:** max

- the maximum size >= 0
**Parameters:** a

- the alignment >= 0.0f && <= 1.0f

---

#### SizeRequirements

public SizeRequirements​(int min,
int pref,
int max,
float a)

Creates a SizeRequirements object with the specified minimum, preferred,
and maximum sizes and the specified alignment.

Method Detail

- toString

```java
public
String
toString()
```

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

**Overrides:** toString

in class

Object
**Returns:** the string

- getTiledSizeRequirements

```java
public static
SizeRequirements
getTiledSizeRequirements​(
SizeRequirements
[] children)
```

Determines the total space necessary to
place a set of components end-to-end. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array.
The returned SizeRequirements object has an alignment of 0.5
(centered). The space requirement is never more than
Integer.MAX_VALUE.

**Parameters:** children

- the space requirements for a set of components.
The vector may be of zero length, which will result in a
default SizeRequirements object instance being passed back.
**Returns:** the total space requirements.

- getAlignedSizeRequirements

```java
public static
SizeRequirements
getAlignedSizeRequirements​(
SizeRequirements
[] children)
```

Determines the total space necessary to
align a set of components. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array. The total space required will
never be more than Integer.MAX_VALUE.

**Parameters:** children

- the set of child requirements. If of zero length,
the returns result will be a default instance of SizeRequirements.
**Returns:** the total space requirements.

- calculateTiledPositions

```java
public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)
```

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method. The components
will be tiled in the forward direction with offsets increasing from 0.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests. This argument
is optional and may be null.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.

- calculateTiledPositions

```java
public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean forward)
```

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method.

This method also requires a flag indicating whether components
should be tiled in the forward direction (offsets increasing
from 0) or reverse direction (offsets decreasing from the end
of the allocated space). The forward direction represents
components tiled from left to right or top to bottom. The
reverse direction represents components tiled from right to left
or bottom to top.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests. This argument
is optional and may be null.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.
**Parameters:** forward

- tile with offsets increasing from 0 if true
and with offsets decreasing from the end of the allocated space
if false.
**Since:** 1.4

- calculateAlignedPositions

```java
public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)
```

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used).
You can get the total size requirement by invoking
getAlignedSizeRequirements.

Normal alignment will be done with an alignment value of 0.0f
representing the left/top edge of a component.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.

- calculateAlignedPositions

```java
public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean normal)
```

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used)
You can get the total size requirement by invoking
getAlignedSizeRequirements.

This method also requires a flag indicating whether normal or
reverse alignment should be performed. With normal alignment
the value 0.0f represents the left/top edge of the component
to be aligned. With reverse alignment, 0.0f represents the
right/bottom edge.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.
**Parameters:** normal

- when true, the alignment value 0.0f means
left/top; when false, it means right/bottom.
**Since:** 1.4

- adjustSizes

```java
public static int[] adjustSizes​(int delta,

SizeRequirements
[] children)
```

Adjust a specified array of sizes by a given amount.

**Parameters:** delta

- an int specifying the size difference
**Parameters:** children

- an array of SizeRequirements objects
**Returns:** an array of ints containing the final size for each item

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### toString

public

String

toString()

Returns a string describing the minimum, preferred, and maximum
size requirements, along with the alignment.

getTiledSizeRequirements

```java
public static
SizeRequirements
getTiledSizeRequirements​(
SizeRequirements
[] children)
```

Determines the total space necessary to
place a set of components end-to-end. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array.
The returned SizeRequirements object has an alignment of 0.5
(centered). The space requirement is never more than
Integer.MAX_VALUE.

**Parameters:** children

- the space requirements for a set of components.
The vector may be of zero length, which will result in a
default SizeRequirements object instance being passed back.
**Returns:** the total space requirements.

---

#### getTiledSizeRequirements

public static

SizeRequirements

getTiledSizeRequirements​(

SizeRequirements

[] children)

Determines the total space necessary to
place a set of components end-to-end. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array.
The returned SizeRequirements object has an alignment of 0.5
(centered). The space requirement is never more than
Integer.MAX_VALUE.

getAlignedSizeRequirements

```java
public static
SizeRequirements
getAlignedSizeRequirements​(
SizeRequirements
[] children)
```

Determines the total space necessary to
align a set of components. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array. The total space required will
never be more than Integer.MAX_VALUE.

**Parameters:** children

- the set of child requirements. If of zero length,
the returns result will be a default instance of SizeRequirements.
**Returns:** the total space requirements.

---

#### getAlignedSizeRequirements

public static

SizeRequirements

getAlignedSizeRequirements​(

SizeRequirements

[] children)

Determines the total space necessary to
align a set of components. The needs
of each component in the set are represented by an entry in the
passed-in SizeRequirements array. The total space required will
never be more than Integer.MAX_VALUE.

calculateTiledPositions

```java
public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)
```

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method. The components
will be tiled in the forward direction with offsets increasing from 0.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests. This argument
is optional and may be null.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.

---

#### calculateTiledPositions

public static void calculateTiledPositions​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method. The components
will be tiled in the forward direction with offsets increasing from 0.

calculateTiledPositions

```java
public static void calculateTiledPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean forward)
```

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method.

This method also requires a flag indicating whether components
should be tiled in the forward direction (offsets increasing
from 0) or reverse direction (offsets decreasing from the end
of the allocated space). The forward direction represents
components tiled from left to right or top to bottom. The
reverse direction represents components tiled from right to left
or bottom to top.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests. This argument
is optional and may be null.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.
**Parameters:** forward

- tile with offsets increasing from 0 if true
and with offsets decreasing from the end of the allocated space
if false.
**Since:** 1.4

---

#### calculateTiledPositions

public static void calculateTiledPositions​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans,
boolean forward)

Creates a set of offset/span pairs representing how to
lay out a set of components end-to-end.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirement of the set of components.
You can get the total size requirement
by invoking the getTiledSizeRequirements method.

This method also requires a flag indicating whether components
should be tiled in the forward direction (offsets increasing
from 0) or reverse direction (offsets decreasing from the end
of the allocated space). The forward direction represents
components tiled from left to right or top to bottom. The
reverse direction represents components tiled from right to left
or bottom to top.

calculateAlignedPositions

```java
public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans)
```

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used).
You can get the total size requirement by invoking
getAlignedSizeRequirements.

Normal alignment will be done with an alignment value of 0.0f
representing the left/top edge of a component.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.

---

#### calculateAlignedPositions

public static void calculateAlignedPositions​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans)

Creates a bunch of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used).
You can get the total size requirement by invoking
getAlignedSizeRequirements.

Normal alignment will be done with an alignment value of 0.0f
representing the left/top edge of a component.

calculateAlignedPositions

```java
public static void calculateAlignedPositions​(int allocated,

SizeRequirements
total,

SizeRequirements
[] children,
int[] offsets,
int[] spans,
boolean normal)
```

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used)
You can get the total size requirement by invoking
getAlignedSizeRequirements.

This method also requires a flag indicating whether normal or
reverse alignment should be performed. With normal alignment
the value 0.0f represents the left/top edge of the component
to be aligned. With reverse alignment, 0.0f represents the
right/bottom edge.

**Parameters:** allocated

- the total span to be allocated >= 0.
**Parameters:** total

- the total of the children requests.
**Parameters:** children

- the size requirements for each component.
**Parameters:** offsets

- the offset from 0 for each child where
the spans were allocated (determines placement of the span).
**Parameters:** spans

- the span allocated for each child to make the
total target span.
**Parameters:** normal

- when true, the alignment value 0.0f means
left/top; when false, it means right/bottom.
**Since:** 1.4

---

#### calculateAlignedPositions

public static void calculateAlignedPositions​(int allocated,

SizeRequirements

total,

SizeRequirements

[] children,
int[] offsets,
int[] spans,
boolean normal)

Creates a set of offset/span pairs specifying how to
lay out a set of components with the specified alignments.
The resulting span allocations will overlap, with each one
fitting as well as possible into the given total allocation.
This method requires that you specify
the total amount of space to be allocated,
the size requirements for each component to be placed
(specified as an array of SizeRequirements), and
the total size requirements of the set of components
(only the alignment field of which is actually used)
You can get the total size requirement by invoking
getAlignedSizeRequirements.

This method also requires a flag indicating whether normal or
reverse alignment should be performed. With normal alignment
the value 0.0f represents the left/top edge of the component
to be aligned. With reverse alignment, 0.0f represents the
right/bottom edge.

adjustSizes

```java
public static int[] adjustSizes​(int delta,

SizeRequirements
[] children)
```

Adjust a specified array of sizes by a given amount.

**Parameters:** delta

- an int specifying the size difference
**Parameters:** children

- an array of SizeRequirements objects
**Returns:** an array of ints containing the final size for each item

---

#### adjustSizes

public static int[] adjustSizes​(int delta,

SizeRequirements

[] children)

Adjust a specified array of sizes by a given amount.

---

