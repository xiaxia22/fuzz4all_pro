# Interface MultipleMaster

**Source:** `java.desktop\java\awt\font\MultipleMaster.html`

### Class Description

```java
public interface
MultipleMaster
```

The

MultipleMaster

interface represents Type 1
Multiple Master fonts.
A particular

Font

object can implement this interface.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getNumDesignAxes()

Returns the number of multiple master design controls.
Design axes include things like width, weight and optical scaling.

**Returns:**
- the number of multiple master design controls

---

#### float[] getDesignAxisRanges()

Returns an array of design limits interleaved in the form [from→to]
for each axis. For example,
design limits for weight could be from 0.1 to 1.0. The values are
returned in the same order returned by

getDesignAxisNames

.

**Returns:**
- an array of design limits for each axis.

---

#### float[] getDesignAxisDefaults()

Returns an array of default design values for each axis. For example,
the default value for weight could be 1.6. The values are returned
in the same order returned by

getDesignAxisNames

.

**Returns:**
- an array of default design values for each axis.

---

#### String
[] getDesignAxisNames()

Returns the name for each design axis. This also determines the order in
which the values for each axis are returned.

**Returns:**
- an array containing the names of each design axis.

---

#### Font
deriveMMFont​(float[] axes)

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array. The size of the array
must correspond to the value returned from

getNumDesignAxes

and the values of the array elements
must fall within limits specified by

getDesignAxesLimits

. In case of an error,

null

is returned.

**Parameters:**
- axes

- an array containing axis values

**Returns:**
- a

Font

object that is an instance of

MultipleMaster

and is based on the design axis values
provided by

axes

.

---

#### Font
deriveMMFont​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)

Creates a new instance of a multiple master font based on detailed metric
information. In case of an error,

null

is returned.

**Parameters:**
- glyphWidths

- an array of floats representing the desired width
of each glyph in font space
- avgStemWidth

- the average stem width for the overall font in
font space
- typicalCapHeight

- the height of a typical upper case char
- typicalXHeight

- the height of a typical lower case char
- italicAngle

- the angle at which the italics lean, in degrees
counterclockwise from vertical

**Returns:**
- a

Font

object that is an instance of

MultipleMaster

and is based on the specified metric
information.

---

### Additional Sections

#### Interface MultipleMaster

```java
public interface
MultipleMaster
```

The

MultipleMaster

interface represents Type 1
Multiple Master fonts.
A particular

Font

object can implement this interface.

public interface

MultipleMaster

The

MultipleMaster

interface represents Type 1
Multiple Master fonts.
A particular

Font

object can implement this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Font

deriveMMFont

​(float[] axes)

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array.

Font

deriveMMFont

​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)

Creates a new instance of a multiple master font based on detailed metric
information.

float[]

getDesignAxisDefaults

()

Returns an array of default design values for each axis.

String

[]

getDesignAxisNames

()

Returns the name for each design axis.

float[]

getDesignAxisRanges

()

Returns an array of design limits interleaved in the form [from→to]
for each axis.

int

getNumDesignAxes

()

Returns the number of multiple master design controls.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Font

deriveMMFont

​(float[] axes)

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array.

Font

deriveMMFont

​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)

Creates a new instance of a multiple master font based on detailed metric
information.

float[]

getDesignAxisDefaults

()

Returns an array of default design values for each axis.

String

[]

getDesignAxisNames

()

Returns the name for each design axis.

float[]

getDesignAxisRanges

()

Returns an array of design limits interleaved in the form [from→to]
for each axis.

int

getNumDesignAxes

()

Returns the number of multiple master design controls.

---

#### Method Summary

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array.

Creates a new instance of a multiple master font based on detailed metric
information.

Returns an array of default design values for each axis.

Returns the name for each design axis.

Returns an array of design limits interleaved in the form [from→to]
for each axis.

Returns the number of multiple master design controls.

============ METHOD DETAIL ==========

- Method Detail

- getNumDesignAxes

```java
int getNumDesignAxes()
```

Returns the number of multiple master design controls.
Design axes include things like width, weight and optical scaling.

**Returns:** the number of multiple master design controls

- getDesignAxisRanges

```java
float[] getDesignAxisRanges()
```

Returns an array of design limits interleaved in the form [from→to]
for each axis. For example,
design limits for weight could be from 0.1 to 1.0. The values are
returned in the same order returned by

getDesignAxisNames

.

**Returns:** an array of design limits for each axis.

- getDesignAxisDefaults

```java
float[] getDesignAxisDefaults()
```

Returns an array of default design values for each axis. For example,
the default value for weight could be 1.6. The values are returned
in the same order returned by

getDesignAxisNames

.

**Returns:** an array of default design values for each axis.

- getDesignAxisNames

```java
String
[] getDesignAxisNames()
```

Returns the name for each design axis. This also determines the order in
which the values for each axis are returned.

**Returns:** an array containing the names of each design axis.

- deriveMMFont

```java
Font
deriveMMFont​(float[] axes)
```

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array. The size of the array
must correspond to the value returned from

getNumDesignAxes

and the values of the array elements
must fall within limits specified by

getDesignAxesLimits

. In case of an error,

null

is returned.

**Parameters:** axes

- an array containing axis values
**Returns:** a

Font

object that is an instance of

MultipleMaster

and is based on the design axis values
provided by

axes

.

- deriveMMFont

```java
Font
deriveMMFont​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)
```

Creates a new instance of a multiple master font based on detailed metric
information. In case of an error,

null

is returned.

**Parameters:** glyphWidths

- an array of floats representing the desired width
of each glyph in font space
**Parameters:** avgStemWidth

- the average stem width for the overall font in
font space
**Parameters:** typicalCapHeight

- the height of a typical upper case char
**Parameters:** typicalXHeight

- the height of a typical lower case char
**Parameters:** italicAngle

- the angle at which the italics lean, in degrees
counterclockwise from vertical
**Returns:** a

Font

object that is an instance of

MultipleMaster

and is based on the specified metric
information.

Method Detail

- getNumDesignAxes

```java
int getNumDesignAxes()
```

Returns the number of multiple master design controls.
Design axes include things like width, weight and optical scaling.

**Returns:** the number of multiple master design controls

- getDesignAxisRanges

```java
float[] getDesignAxisRanges()
```

Returns an array of design limits interleaved in the form [from→to]
for each axis. For example,
design limits for weight could be from 0.1 to 1.0. The values are
returned in the same order returned by

getDesignAxisNames

.

**Returns:** an array of design limits for each axis.

- getDesignAxisDefaults

```java
float[] getDesignAxisDefaults()
```

Returns an array of default design values for each axis. For example,
the default value for weight could be 1.6. The values are returned
in the same order returned by

getDesignAxisNames

.

**Returns:** an array of default design values for each axis.

- getDesignAxisNames

```java
String
[] getDesignAxisNames()
```

Returns the name for each design axis. This also determines the order in
which the values for each axis are returned.

**Returns:** an array containing the names of each design axis.

- deriveMMFont

```java
Font
deriveMMFont​(float[] axes)
```

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array. The size of the array
must correspond to the value returned from

getNumDesignAxes

and the values of the array elements
must fall within limits specified by

getDesignAxesLimits

. In case of an error,

null

is returned.

**Parameters:** axes

- an array containing axis values
**Returns:** a

Font

object that is an instance of

MultipleMaster

and is based on the design axis values
provided by

axes

.

- deriveMMFont

```java
Font
deriveMMFont​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)
```

Creates a new instance of a multiple master font based on detailed metric
information. In case of an error,

null

is returned.

**Parameters:** glyphWidths

- an array of floats representing the desired width
of each glyph in font space
**Parameters:** avgStemWidth

- the average stem width for the overall font in
font space
**Parameters:** typicalCapHeight

- the height of a typical upper case char
**Parameters:** typicalXHeight

- the height of a typical lower case char
**Parameters:** italicAngle

- the angle at which the italics lean, in degrees
counterclockwise from vertical
**Returns:** a

Font

object that is an instance of

MultipleMaster

and is based on the specified metric
information.

---

#### Method Detail

getNumDesignAxes

```java
int getNumDesignAxes()
```

Returns the number of multiple master design controls.
Design axes include things like width, weight and optical scaling.

**Returns:** the number of multiple master design controls

---

#### getNumDesignAxes

int getNumDesignAxes()

Returns the number of multiple master design controls.
Design axes include things like width, weight and optical scaling.

getDesignAxisRanges

```java
float[] getDesignAxisRanges()
```

Returns an array of design limits interleaved in the form [from→to]
for each axis. For example,
design limits for weight could be from 0.1 to 1.0. The values are
returned in the same order returned by

getDesignAxisNames

.

**Returns:** an array of design limits for each axis.

---

#### getDesignAxisRanges

float[] getDesignAxisRanges()

Returns an array of design limits interleaved in the form [from→to]
for each axis. For example,
design limits for weight could be from 0.1 to 1.0. The values are
returned in the same order returned by

getDesignAxisNames

.

getDesignAxisDefaults

```java
float[] getDesignAxisDefaults()
```

Returns an array of default design values for each axis. For example,
the default value for weight could be 1.6. The values are returned
in the same order returned by

getDesignAxisNames

.

**Returns:** an array of default design values for each axis.

---

#### getDesignAxisDefaults

float[] getDesignAxisDefaults()

Returns an array of default design values for each axis. For example,
the default value for weight could be 1.6. The values are returned
in the same order returned by

getDesignAxisNames

.

getDesignAxisNames

```java
String
[] getDesignAxisNames()
```

Returns the name for each design axis. This also determines the order in
which the values for each axis are returned.

**Returns:** an array containing the names of each design axis.

---

#### getDesignAxisNames

String

[] getDesignAxisNames()

Returns the name for each design axis. This also determines the order in
which the values for each axis are returned.

deriveMMFont

```java
Font
deriveMMFont​(float[] axes)
```

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array. The size of the array
must correspond to the value returned from

getNumDesignAxes

and the values of the array elements
must fall within limits specified by

getDesignAxesLimits

. In case of an error,

null

is returned.

**Parameters:** axes

- an array containing axis values
**Returns:** a

Font

object that is an instance of

MultipleMaster

and is based on the design axis values
provided by

axes

.

---

#### deriveMMFont

Font

deriveMMFont​(float[] axes)

Creates a new instance of a multiple master font based on the design
axis values contained in the specified array. The size of the array
must correspond to the value returned from

getNumDesignAxes

and the values of the array elements
must fall within limits specified by

getDesignAxesLimits

. In case of an error,

null

is returned.

deriveMMFont

```java
Font
deriveMMFont​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)
```

Creates a new instance of a multiple master font based on detailed metric
information. In case of an error,

null

is returned.

**Parameters:** glyphWidths

- an array of floats representing the desired width
of each glyph in font space
**Parameters:** avgStemWidth

- the average stem width for the overall font in
font space
**Parameters:** typicalCapHeight

- the height of a typical upper case char
**Parameters:** typicalXHeight

- the height of a typical lower case char
**Parameters:** italicAngle

- the angle at which the italics lean, in degrees
counterclockwise from vertical
**Returns:** a

Font

object that is an instance of

MultipleMaster

and is based on the specified metric
information.

---

#### deriveMMFont

Font

deriveMMFont​(float[] glyphWidths,
float avgStemWidth,
float typicalCapHeight,
float typicalXHeight,
float italicAngle)

Creates a new instance of a multiple master font based on detailed metric
information. In case of an error,

null

is returned.

---

