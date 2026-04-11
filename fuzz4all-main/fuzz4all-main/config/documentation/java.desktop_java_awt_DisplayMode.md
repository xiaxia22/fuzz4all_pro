# Class DisplayMode

**Source:** `java.desktop\java\awt\DisplayMode.html`

### Class Description

```java
public final class
DisplayMode

extends
Object
```

The

DisplayMode

class encapsulates the bit depth, height,
width, and refresh rate of a

GraphicsDevice

. The ability to
change graphics device's display mode is platform- and
configuration-dependent and may not always be available
(see

GraphicsDevice.isDisplayChangeSupported()

).

For more information on full-screen exclusive mode API, see the

Full-Screen Exclusive Mode API Tutorial

.

**Since:** 1.4
**See Also:** GraphicsDevice

,

GraphicsDevice.isDisplayChangeSupported()

,

GraphicsDevice.getDisplayModes()

,

GraphicsDevice.setDisplayMode(java.awt.DisplayMode)

---

### Field Details

#### @Native

public static final int BIT_DEPTH_MULTI

Value of the bit depth if multiple bit depths are supported in this
display mode.

**See Also:**
- getBitDepth()

,

Constant Field Values

---

#### @Native

public static final int REFRESH_RATE_UNKNOWN

Value of the refresh rate if not known.

**See Also:**
- getRefreshRate()

,

Constant Field Values

---

### Constructor Details

#### public DisplayMode​(int width,
int height,
int bitDepth,
int refreshRate)

Create a new display mode object with the supplied parameters.

**Parameters:**
- width

- the width of the display, in pixels
- height

- the height of the display, in pixels
- bitDepth

- the bit depth of the display, in bits per
pixel. This can be

BIT_DEPTH_MULTI

if multiple
bit depths are available.
- refreshRate

- the refresh rate of the display, in hertz.
This can be

REFRESH_RATE_UNKNOWN

if the
information is not available.

**See Also:**
- BIT_DEPTH_MULTI

,

REFRESH_RATE_UNKNOWN

---

### Method Details

#### public int getHeight()

Returns the height of the display, in pixels.

**Returns:**
- the height of the display, in pixels

---

#### public int getWidth()

Returns the width of the display, in pixels.

**Returns:**
- the width of the display, in pixels

---

#### public int getBitDepth()

Returns the bit depth of the display, in bits per pixel. This may be

BIT_DEPTH_MULTI

if multiple bit depths are supported in
this display mode.

**Returns:**
- the bit depth of the display, in bits per pixel.

**See Also:**
- BIT_DEPTH_MULTI

---

#### public int getRefreshRate()

Returns the refresh rate of the display, in hertz. This may be

REFRESH_RATE_UNKNOWN

if the information is not available.

**Returns:**
- the refresh rate of the display, in hertz.

**See Also:**
- REFRESH_RATE_UNKNOWN

---

#### public boolean equals​(
DisplayMode
dm)

Returns whether the two display modes are equal.

**Parameters:**
- dm

- the display mode to compare to

**Returns:**
- whether the two display modes are equal

---

### Additional Sections

#### Class DisplayMode

java.lang.Object

- java.awt.DisplayMode

java.awt.DisplayMode

```java
public final class
DisplayMode

extends
Object
```

The

DisplayMode

class encapsulates the bit depth, height,
width, and refresh rate of a

GraphicsDevice

. The ability to
change graphics device's display mode is platform- and
configuration-dependent and may not always be available
(see

GraphicsDevice.isDisplayChangeSupported()

).

For more information on full-screen exclusive mode API, see the

Full-Screen Exclusive Mode API Tutorial

.

**Since:** 1.4
**See Also:** GraphicsDevice

,

GraphicsDevice.isDisplayChangeSupported()

,

GraphicsDevice.getDisplayModes()

,

GraphicsDevice.setDisplayMode(java.awt.DisplayMode)

public final class

DisplayMode

extends

Object

The

DisplayMode

class encapsulates the bit depth, height,
width, and refresh rate of a

GraphicsDevice

. The ability to
change graphics device's display mode is platform- and
configuration-dependent and may not always be available
(see

GraphicsDevice.isDisplayChangeSupported()

).

For more information on full-screen exclusive mode API, see the

Full-Screen Exclusive Mode API Tutorial

.

For more information on full-screen exclusive mode API, see the

Full-Screen Exclusive Mode API Tutorial

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BIT_DEPTH_MULTI

Value of the bit depth if multiple bit depths are supported in this
display mode.

static int

REFRESH_RATE_UNKNOWN

Value of the refresh rate if not known.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DisplayMode

​(int width,
int height,
int bitDepth,
int refreshRate)

Create a new display mode object with the supplied parameters.

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

DisplayMode

dm)

Returns whether the two display modes are equal.

int

getBitDepth

()

Returns the bit depth of the display, in bits per pixel.

int

getHeight

()

Returns the height of the display, in pixels.

int

getRefreshRate

()

Returns the refresh rate of the display, in hertz.

int

getWidth

()

Returns the width of the display, in pixels.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

BIT_DEPTH_MULTI

Value of the bit depth if multiple bit depths are supported in this
display mode.

static int

REFRESH_RATE_UNKNOWN

Value of the refresh rate if not known.

---

#### Field Summary

Value of the bit depth if multiple bit depths are supported in this
display mode.

Value of the refresh rate if not known.

Constructor Summary

Constructors

Constructor

Description

DisplayMode

​(int width,
int height,
int bitDepth,
int refreshRate)

Create a new display mode object with the supplied parameters.

---

#### Constructor Summary

Create a new display mode object with the supplied parameters.

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

DisplayMode

dm)

Returns whether the two display modes are equal.

int

getBitDepth

()

Returns the bit depth of the display, in bits per pixel.

int

getHeight

()

Returns the height of the display, in pixels.

int

getRefreshRate

()

Returns the refresh rate of the display, in hertz.

int

getWidth

()

Returns the width of the display, in pixels.

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

Returns whether the two display modes are equal.

Returns the bit depth of the display, in bits per pixel.

Returns the height of the display, in pixels.

Returns the refresh rate of the display, in hertz.

Returns the width of the display, in pixels.

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

============ FIELD DETAIL ===========

- Field Detail

- BIT_DEPTH_MULTI

```java
@Native

public static final int BIT_DEPTH_MULTI
```

Value of the bit depth if multiple bit depths are supported in this
display mode.

**See Also:** getBitDepth()

,

Constant Field Values

- REFRESH_RATE_UNKNOWN

```java
@Native

public static final int REFRESH_RATE_UNKNOWN
```

Value of the refresh rate if not known.

**See Also:** getRefreshRate()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DisplayMode

```java
public DisplayMode​(int width,
int height,
int bitDepth,
int refreshRate)
```

Create a new display mode object with the supplied parameters.

**Parameters:** width

- the width of the display, in pixels
**Parameters:** height

- the height of the display, in pixels
**Parameters:** bitDepth

- the bit depth of the display, in bits per
pixel. This can be

BIT_DEPTH_MULTI

if multiple
bit depths are available.
**Parameters:** refreshRate

- the refresh rate of the display, in hertz.
This can be

REFRESH_RATE_UNKNOWN

if the
information is not available.
**See Also:** BIT_DEPTH_MULTI

,

REFRESH_RATE_UNKNOWN

============ METHOD DETAIL ==========

- Method Detail

- getHeight

```java
public int getHeight()
```

Returns the height of the display, in pixels.

**Returns:** the height of the display, in pixels

- getWidth

```java
public int getWidth()
```

Returns the width of the display, in pixels.

**Returns:** the width of the display, in pixels

- getBitDepth

```java
public int getBitDepth()
```

Returns the bit depth of the display, in bits per pixel. This may be

BIT_DEPTH_MULTI

if multiple bit depths are supported in
this display mode.

**Returns:** the bit depth of the display, in bits per pixel.
**See Also:** BIT_DEPTH_MULTI

- getRefreshRate

```java
public int getRefreshRate()
```

Returns the refresh rate of the display, in hertz. This may be

REFRESH_RATE_UNKNOWN

if the information is not available.

**Returns:** the refresh rate of the display, in hertz.
**See Also:** REFRESH_RATE_UNKNOWN

- equals

```java
public boolean equals​(
DisplayMode
dm)
```

Returns whether the two display modes are equal.

**Parameters:** dm

- the display mode to compare to
**Returns:** whether the two display modes are equal

Field Detail

- BIT_DEPTH_MULTI

```java
@Native

public static final int BIT_DEPTH_MULTI
```

Value of the bit depth if multiple bit depths are supported in this
display mode.

**See Also:** getBitDepth()

,

Constant Field Values

- REFRESH_RATE_UNKNOWN

```java
@Native

public static final int REFRESH_RATE_UNKNOWN
```

Value of the refresh rate if not known.

**See Also:** getRefreshRate()

,

Constant Field Values

---

#### Field Detail

BIT_DEPTH_MULTI

```java
@Native

public static final int BIT_DEPTH_MULTI
```

Value of the bit depth if multiple bit depths are supported in this
display mode.

**See Also:** getBitDepth()

,

Constant Field Values

---

#### BIT_DEPTH_MULTI

@Native

public static final int BIT_DEPTH_MULTI

Value of the bit depth if multiple bit depths are supported in this
display mode.

REFRESH_RATE_UNKNOWN

```java
@Native

public static final int REFRESH_RATE_UNKNOWN
```

Value of the refresh rate if not known.

**See Also:** getRefreshRate()

,

Constant Field Values

---

#### REFRESH_RATE_UNKNOWN

@Native

public static final int REFRESH_RATE_UNKNOWN

Value of the refresh rate if not known.

Constructor Detail

- DisplayMode

```java
public DisplayMode​(int width,
int height,
int bitDepth,
int refreshRate)
```

Create a new display mode object with the supplied parameters.

**Parameters:** width

- the width of the display, in pixels
**Parameters:** height

- the height of the display, in pixels
**Parameters:** bitDepth

- the bit depth of the display, in bits per
pixel. This can be

BIT_DEPTH_MULTI

if multiple
bit depths are available.
**Parameters:** refreshRate

- the refresh rate of the display, in hertz.
This can be

REFRESH_RATE_UNKNOWN

if the
information is not available.
**See Also:** BIT_DEPTH_MULTI

,

REFRESH_RATE_UNKNOWN

---

#### Constructor Detail

DisplayMode

```java
public DisplayMode​(int width,
int height,
int bitDepth,
int refreshRate)
```

Create a new display mode object with the supplied parameters.

**Parameters:** width

- the width of the display, in pixels
**Parameters:** height

- the height of the display, in pixels
**Parameters:** bitDepth

- the bit depth of the display, in bits per
pixel. This can be

BIT_DEPTH_MULTI

if multiple
bit depths are available.
**Parameters:** refreshRate

- the refresh rate of the display, in hertz.
This can be

REFRESH_RATE_UNKNOWN

if the
information is not available.
**See Also:** BIT_DEPTH_MULTI

,

REFRESH_RATE_UNKNOWN

---

#### DisplayMode

public DisplayMode​(int width,
int height,
int bitDepth,
int refreshRate)

Create a new display mode object with the supplied parameters.

Method Detail

- getHeight

```java
public int getHeight()
```

Returns the height of the display, in pixels.

**Returns:** the height of the display, in pixels

- getWidth

```java
public int getWidth()
```

Returns the width of the display, in pixels.

**Returns:** the width of the display, in pixels

- getBitDepth

```java
public int getBitDepth()
```

Returns the bit depth of the display, in bits per pixel. This may be

BIT_DEPTH_MULTI

if multiple bit depths are supported in
this display mode.

**Returns:** the bit depth of the display, in bits per pixel.
**See Also:** BIT_DEPTH_MULTI

- getRefreshRate

```java
public int getRefreshRate()
```

Returns the refresh rate of the display, in hertz. This may be

REFRESH_RATE_UNKNOWN

if the information is not available.

**Returns:** the refresh rate of the display, in hertz.
**See Also:** REFRESH_RATE_UNKNOWN

- equals

```java
public boolean equals​(
DisplayMode
dm)
```

Returns whether the two display modes are equal.

**Parameters:** dm

- the display mode to compare to
**Returns:** whether the two display modes are equal

---

#### Method Detail

getHeight

```java
public int getHeight()
```

Returns the height of the display, in pixels.

**Returns:** the height of the display, in pixels

---

#### getHeight

public int getHeight()

Returns the height of the display, in pixels.

getWidth

```java
public int getWidth()
```

Returns the width of the display, in pixels.

**Returns:** the width of the display, in pixels

---

#### getWidth

public int getWidth()

Returns the width of the display, in pixels.

getBitDepth

```java
public int getBitDepth()
```

Returns the bit depth of the display, in bits per pixel. This may be

BIT_DEPTH_MULTI

if multiple bit depths are supported in
this display mode.

**Returns:** the bit depth of the display, in bits per pixel.
**See Also:** BIT_DEPTH_MULTI

---

#### getBitDepth

public int getBitDepth()

Returns the bit depth of the display, in bits per pixel. This may be

BIT_DEPTH_MULTI

if multiple bit depths are supported in
this display mode.

getRefreshRate

```java
public int getRefreshRate()
```

Returns the refresh rate of the display, in hertz. This may be

REFRESH_RATE_UNKNOWN

if the information is not available.

**Returns:** the refresh rate of the display, in hertz.
**See Also:** REFRESH_RATE_UNKNOWN

---

#### getRefreshRate

public int getRefreshRate()

Returns the refresh rate of the display, in hertz. This may be

REFRESH_RATE_UNKNOWN

if the information is not available.

equals

```java
public boolean equals​(
DisplayMode
dm)
```

Returns whether the two display modes are equal.

**Parameters:** dm

- the display mode to compare to
**Returns:** whether the two display modes are equal

---

#### equals

public boolean equals​(

DisplayMode

dm)

Returns whether the two display modes are equal.

---

