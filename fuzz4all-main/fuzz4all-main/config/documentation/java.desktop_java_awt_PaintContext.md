# Interface PaintContext

**Source:** `java.desktop\java\awt\PaintContext.html`

### Class Description

```java
public interface
PaintContext
```

The

PaintContext

interface defines the encapsulated
and optimized environment to generate color patterns in device
space for fill or stroke operations on a

Graphics2D

. The

PaintContext

provides
the necessary colors for

Graphics2D

operations in the
form of a

Raster

associated with a

ColorModel

.
The

PaintContext

maintains state for a particular paint
operation. In a multi-threaded environment, several
contexts can exist simultaneously for a single

Paint

object.

**See Also:** Paint

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dispose()

Releases the resources allocated for the operation.

---

#### ColorModel
getColorModel()

Returns the

ColorModel

of the output. Note that
this

ColorModel

might be different from the hint
specified in the

createContext

method of

Paint

. Not all

PaintContext

objects are
capable of generating color patterns in an arbitrary

ColorModel

.

**Returns:**
- the

ColorModel

of the output.

---

#### Raster
getRaster​(int x,
int y,
int w,
int h)

Returns a

Raster

containing the colors generated for
the graphics operation.

**Parameters:**
- x

- the x coordinate of the area in device space
for which colors are generated.
- y

- the y coordinate of the area in device space
for which colors are generated.
- w

- the width of the area in device space
- h

- the height of the area in device space

**Returns:**
- a

Raster

representing the specified
rectangular area and containing the colors generated for
the graphics operation.

---

### Additional Sections

#### Interface PaintContext

```java
public interface
PaintContext
```

The

PaintContext

interface defines the encapsulated
and optimized environment to generate color patterns in device
space for fill or stroke operations on a

Graphics2D

. The

PaintContext

provides
the necessary colors for

Graphics2D

operations in the
form of a

Raster

associated with a

ColorModel

.
The

PaintContext

maintains state for a particular paint
operation. In a multi-threaded environment, several
contexts can exist simultaneously for a single

Paint

object.

**See Also:** Paint

public interface

PaintContext

The

PaintContext

interface defines the encapsulated
and optimized environment to generate color patterns in device
space for fill or stroke operations on a

Graphics2D

. The

PaintContext

provides
the necessary colors for

Graphics2D

operations in the
form of a

Raster

associated with a

ColorModel

.
The

PaintContext

maintains state for a particular paint
operation. In a multi-threaded environment, several
contexts can exist simultaneously for a single

Paint

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dispose

()

Releases the resources allocated for the operation.

ColorModel

getColorModel

()

Returns the

ColorModel

of the output.

Raster

getRaster

​(int x,
int y,
int w,
int h)

Returns a

Raster

containing the colors generated for
the graphics operation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dispose

()

Releases the resources allocated for the operation.

ColorModel

getColorModel

()

Returns the

ColorModel

of the output.

Raster

getRaster

​(int x,
int y,
int w,
int h)

Returns a

Raster

containing the colors generated for
the graphics operation.

---

#### Method Summary

Releases the resources allocated for the operation.

Returns the

ColorModel

of the output.

Returns a

Raster

containing the colors generated for
the graphics operation.

============ METHOD DETAIL ==========

- Method Detail

- dispose

```java
void dispose()
```

Releases the resources allocated for the operation.

- getColorModel

```java
ColorModel
getColorModel()
```

Returns the

ColorModel

of the output. Note that
this

ColorModel

might be different from the hint
specified in the

createContext

method of

Paint

. Not all

PaintContext

objects are
capable of generating color patterns in an arbitrary

ColorModel

.

**Returns:** the

ColorModel

of the output.

- getRaster

```java
Raster
getRaster​(int x,
int y,
int w,
int h)
```

Returns a

Raster

containing the colors generated for
the graphics operation.

**Parameters:** x

- the x coordinate of the area in device space
for which colors are generated.
**Parameters:** y

- the y coordinate of the area in device space
for which colors are generated.
**Parameters:** w

- the width of the area in device space
**Parameters:** h

- the height of the area in device space
**Returns:** a

Raster

representing the specified
rectangular area and containing the colors generated for
the graphics operation.

Method Detail

- dispose

```java
void dispose()
```

Releases the resources allocated for the operation.

- getColorModel

```java
ColorModel
getColorModel()
```

Returns the

ColorModel

of the output. Note that
this

ColorModel

might be different from the hint
specified in the

createContext

method of

Paint

. Not all

PaintContext

objects are
capable of generating color patterns in an arbitrary

ColorModel

.

**Returns:** the

ColorModel

of the output.

- getRaster

```java
Raster
getRaster​(int x,
int y,
int w,
int h)
```

Returns a

Raster

containing the colors generated for
the graphics operation.

**Parameters:** x

- the x coordinate of the area in device space
for which colors are generated.
**Parameters:** y

- the y coordinate of the area in device space
for which colors are generated.
**Parameters:** w

- the width of the area in device space
**Parameters:** h

- the height of the area in device space
**Returns:** a

Raster

representing the specified
rectangular area and containing the colors generated for
the graphics operation.

---

#### Method Detail

dispose

```java
void dispose()
```

Releases the resources allocated for the operation.

---

#### dispose

void dispose()

Releases the resources allocated for the operation.

getColorModel

```java
ColorModel
getColorModel()
```

Returns the

ColorModel

of the output. Note that
this

ColorModel

might be different from the hint
specified in the

createContext

method of

Paint

. Not all

PaintContext

objects are
capable of generating color patterns in an arbitrary

ColorModel

.

**Returns:** the

ColorModel

of the output.

---

#### getColorModel

ColorModel

getColorModel()

Returns the

ColorModel

of the output. Note that
this

ColorModel

might be different from the hint
specified in the

createContext

method of

Paint

. Not all

PaintContext

objects are
capable of generating color patterns in an arbitrary

ColorModel

.

getRaster

```java
Raster
getRaster​(int x,
int y,
int w,
int h)
```

Returns a

Raster

containing the colors generated for
the graphics operation.

**Parameters:** x

- the x coordinate of the area in device space
for which colors are generated.
**Parameters:** y

- the y coordinate of the area in device space
for which colors are generated.
**Parameters:** w

- the width of the area in device space
**Parameters:** h

- the height of the area in device space
**Returns:** a

Raster

representing the specified
rectangular area and containing the colors generated for
the graphics operation.

---

#### getRaster

Raster

getRaster​(int x,
int y,
int w,
int h)

Returns a

Raster

containing the colors generated for
the graphics operation.

---

