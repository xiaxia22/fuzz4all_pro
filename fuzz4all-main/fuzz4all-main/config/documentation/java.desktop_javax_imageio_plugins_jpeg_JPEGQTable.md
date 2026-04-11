# Class JPEGQTable

**Source:** `java.desktop\javax\imageio\plugins\jpeg\JPEGQTable.html`

### Class Description

```java
public class
JPEGQTable

extends
Object
```

A class encapsulating a single JPEG quantization table.
The elements appear in natural order (as opposed to zig-zag order).
Static variables are provided for the "standard" tables taken from
Annex K of the JPEG specification, as well as the default tables
conventionally used for visually lossless encoding.

For more information about the operation of the standard JPEG plug-in,
see the

JPEG
metadata format specification and usage notes

---

### Field Details

#### public static final
JPEGQTable
K1Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1. According to the specification,
these values produce "good" quality output.

**See Also:**
- K1Div2Luminance

---

#### public static final
JPEGQTable
K1Div2Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default luminance table used if the default
tables and quality settings are used.

**See Also:**
- K1Luminance

---

#### public static final
JPEGQTable
K2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.2. According to the specification,
these values produce "good" quality output.

**See Also:**
- K2Div2Chrominance

---

#### public static final
JPEGQTable
K2Div2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default chrominance table used if the default
tables and quality settings are used.

**See Also:**
- K2Chrominance

---

### Constructor Details

#### public JPEGQTable​(int[] table)

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).
A copy is made of the input array.

**Parameters:**
- table

- the quantization table, as an

int

array.

**Throws:**
- IllegalArgumentException

- if

table

is

null

or

table.length

is not equal to 64.

---

### Method Details

#### public int[] getTable()

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

**Returns:**
- A copy of the current quantization table.

---

#### public
JPEGQTable
getScaledInstance​(float scaleFactor,
boolean forceBaseline)

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

Values of

scaleFactor

less than 1 tend to improve
the quality level of the table, and values greater than 1.0
degrade the quality level of the table.

**Parameters:**
- scaleFactor

- multiplication factor for the table.
- forceBaseline

- if

true

,
the values will be clamped to the range 1..255

**Returns:**
- a new quantization table that is a linear multiple
of the current table.

---

#### public
String
toString()

Returns a

String

representing this quantization table.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

representing this quantization table.

---

### Additional Sections

#### Class JPEGQTable

java.lang.Object

- javax.imageio.plugins.jpeg.JPEGQTable

javax.imageio.plugins.jpeg.JPEGQTable

```java
public class
JPEGQTable

extends
Object
```

A class encapsulating a single JPEG quantization table.
The elements appear in natural order (as opposed to zig-zag order).
Static variables are provided for the "standard" tables taken from
Annex K of the JPEG specification, as well as the default tables
conventionally used for visually lossless encoding.

For more information about the operation of the standard JPEG plug-in,
see the

JPEG
metadata format specification and usage notes

public class

JPEGQTable

extends

Object

A class encapsulating a single JPEG quantization table.
The elements appear in natural order (as opposed to zig-zag order).
Static variables are provided for the "standard" tables taken from
Annex K of the JPEG specification, as well as the default tables
conventionally used for visually lossless encoding.

For more information about the operation of the standard JPEG plug-in,
see the

JPEG
metadata format specification and usage notes

For more information about the operation of the standard JPEG plug-in,
see the

JPEG
metadata format specification and usage notes

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

JPEGQTable

K1Div2Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.

static

JPEGQTable

K1Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1.

static

JPEGQTable

K2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.2.

static

JPEGQTable

K2Div2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JPEGQTable

​(int[] table)

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JPEGQTable

getScaledInstance

​(float scaleFactor,
boolean forceBaseline)

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

int[]

getTable

()

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

String

toString

()

Returns a

String

representing this quantization table.

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

static

JPEGQTable

K1Div2Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.

static

JPEGQTable

K1Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1.

static

JPEGQTable

K2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.2.

static

JPEGQTable

K2Div2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.

---

#### Field Summary

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.

The sample luminance quantization table given in the JPEG
specification, table K.1.

The sample chrominance quantization table given in the JPEG
specification, table K.2.

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.

Constructor Summary

Constructors

Constructor

Description

JPEGQTable

​(int[] table)

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).

---

#### Constructor Summary

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JPEGQTable

getScaledInstance

​(float scaleFactor,
boolean forceBaseline)

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

int[]

getTable

()

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

String

toString

()

Returns a

String

representing this quantization table.

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

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

Returns a

String

representing this quantization table.

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

- K1Luminance

```java
public static final
JPEGQTable
K1Luminance
```

The sample luminance quantization table given in the JPEG
specification, table K.1. According to the specification,
these values produce "good" quality output.

**See Also:** K1Div2Luminance

- K1Div2Luminance

```java
public static final
JPEGQTable
K1Div2Luminance
```

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default luminance table used if the default
tables and quality settings are used.

**See Also:** K1Luminance

- K2Chrominance

```java
public static final
JPEGQTable
K2Chrominance
```

The sample chrominance quantization table given in the JPEG
specification, table K.2. According to the specification,
these values produce "good" quality output.

**See Also:** K2Div2Chrominance

- K2Div2Chrominance

```java
public static final
JPEGQTable
K2Div2Chrominance
```

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default chrominance table used if the default
tables and quality settings are used.

**See Also:** K2Chrominance

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JPEGQTable

```java
public JPEGQTable​(int[] table)
```

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).
A copy is made of the input array.

**Parameters:** table

- the quantization table, as an

int

array.
**Throws:** IllegalArgumentException

- if

table

is

null

or

table.length

is not equal to 64.

============ METHOD DETAIL ==========

- Method Detail

- getTable

```java
public int[] getTable()
```

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

**Returns:** A copy of the current quantization table.

- getScaledInstance

```java
public
JPEGQTable
getScaledInstance​(float scaleFactor,
boolean forceBaseline)
```

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

Values of

scaleFactor

less than 1 tend to improve
the quality level of the table, and values greater than 1.0
degrade the quality level of the table.

**Parameters:** scaleFactor

- multiplication factor for the table.
**Parameters:** forceBaseline

- if

true

,
the values will be clamped to the range 1..255
**Returns:** a new quantization table that is a linear multiple
of the current table.

- toString

```java
public
String
toString()
```

Returns a

String

representing this quantization table.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing this quantization table.

Field Detail

- K1Luminance

```java
public static final
JPEGQTable
K1Luminance
```

The sample luminance quantization table given in the JPEG
specification, table K.1. According to the specification,
these values produce "good" quality output.

**See Also:** K1Div2Luminance

- K1Div2Luminance

```java
public static final
JPEGQTable
K1Div2Luminance
```

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default luminance table used if the default
tables and quality settings are used.

**See Also:** K1Luminance

- K2Chrominance

```java
public static final
JPEGQTable
K2Chrominance
```

The sample chrominance quantization table given in the JPEG
specification, table K.2. According to the specification,
these values produce "good" quality output.

**See Also:** K2Div2Chrominance

- K2Div2Chrominance

```java
public static final
JPEGQTable
K2Div2Chrominance
```

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default chrominance table used if the default
tables and quality settings are used.

**See Also:** K2Chrominance

---

#### Field Detail

K1Luminance

```java
public static final
JPEGQTable
K1Luminance
```

The sample luminance quantization table given in the JPEG
specification, table K.1. According to the specification,
these values produce "good" quality output.

**See Also:** K1Div2Luminance

---

#### K1Luminance

public static final

JPEGQTable

K1Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1. According to the specification,
these values produce "good" quality output.

K1Div2Luminance

```java
public static final
JPEGQTable
K1Div2Luminance
```

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default luminance table used if the default
tables and quality settings are used.

**See Also:** K1Luminance

---

#### K1Div2Luminance

public static final

JPEGQTable

K1Div2Luminance

The sample luminance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default luminance table used if the default
tables and quality settings are used.

K2Chrominance

```java
public static final
JPEGQTable
K2Chrominance
```

The sample chrominance quantization table given in the JPEG
specification, table K.2. According to the specification,
these values produce "good" quality output.

**See Also:** K2Div2Chrominance

---

#### K2Chrominance

public static final

JPEGQTable

K2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.2. According to the specification,
these values produce "good" quality output.

K2Div2Chrominance

```java
public static final
JPEGQTable
K2Div2Chrominance
```

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default chrominance table used if the default
tables and quality settings are used.

**See Also:** K2Chrominance

---

#### K2Div2Chrominance

public static final

JPEGQTable

K2Div2Chrominance

The sample chrominance quantization table given in the JPEG
specification, table K.1, with all elements divided by 2.
According to the specification, these values produce "very good"
quality output. This is the table usually used for "visually lossless"
encoding, and is the default chrominance table used if the default
tables and quality settings are used.

Constructor Detail

- JPEGQTable

```java
public JPEGQTable​(int[] table)
```

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).
A copy is made of the input array.

**Parameters:** table

- the quantization table, as an

int

array.
**Throws:** IllegalArgumentException

- if

table

is

null

or

table.length

is not equal to 64.

---

#### Constructor Detail

JPEGQTable

```java
public JPEGQTable​(int[] table)
```

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).
A copy is made of the input array.

**Parameters:** table

- the quantization table, as an

int

array.
**Throws:** IllegalArgumentException

- if

table

is

null

or

table.length

is not equal to 64.

---

#### JPEGQTable

public JPEGQTable​(int[] table)

Constructs a quantization table from the argument, which must
contain 64 elements in natural order (not zig-zag order).
A copy is made of the input array.

Method Detail

- getTable

```java
public int[] getTable()
```

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

**Returns:** A copy of the current quantization table.

- getScaledInstance

```java
public
JPEGQTable
getScaledInstance​(float scaleFactor,
boolean forceBaseline)
```

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

Values of

scaleFactor

less than 1 tend to improve
the quality level of the table, and values greater than 1.0
degrade the quality level of the table.

**Parameters:** scaleFactor

- multiplication factor for the table.
**Parameters:** forceBaseline

- if

true

,
the values will be clamped to the range 1..255
**Returns:** a new quantization table that is a linear multiple
of the current table.

- toString

```java
public
String
toString()
```

Returns a

String

representing this quantization table.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing this quantization table.

---

#### Method Detail

getTable

```java
public int[] getTable()
```

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

**Returns:** A copy of the current quantization table.

---

#### getTable

public int[] getTable()

Returns a copy of the current quantization table as an array
of

int

s in natural (not zig-zag) order.

getScaledInstance

```java
public
JPEGQTable
getScaledInstance​(float scaleFactor,
boolean forceBaseline)
```

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

Values of

scaleFactor

less than 1 tend to improve
the quality level of the table, and values greater than 1.0
degrade the quality level of the table.

**Parameters:** scaleFactor

- multiplication factor for the table.
**Parameters:** forceBaseline

- if

true

,
the values will be clamped to the range 1..255
**Returns:** a new quantization table that is a linear multiple
of the current table.

---

#### getScaledInstance

public

JPEGQTable

getScaledInstance​(float scaleFactor,
boolean forceBaseline)

Returns a new quantization table where the values are multiplied
by

scaleFactor

and then clamped to the range 1..32767
(or to 1..255 if

forceBaseline

is true).

Values of

scaleFactor

less than 1 tend to improve
the quality level of the table, and values greater than 1.0
degrade the quality level of the table.

Values of

scaleFactor

less than 1 tend to improve
the quality level of the table, and values greater than 1.0
degrade the quality level of the table.

toString

```java
public
String
toString()
```

Returns a

String

representing this quantization table.

**Overrides:** toString

in class

Object
**Returns:** a

String

representing this quantization table.

---

#### toString

public

String

toString()

Returns a

String

representing this quantization table.

---

