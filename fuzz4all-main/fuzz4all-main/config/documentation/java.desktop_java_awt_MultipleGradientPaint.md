# Class MultipleGradientPaint

**Source:** `java.desktop\java\awt\MultipleGradientPaint.html`

### Class Description

```java
public abstract class
MultipleGradientPaint

extends
Object

implements
Paint
```

This is the superclass for Paints which use a multiple color
gradient to fill in their raster. It provides storage for variables and
enumerated values common to

LinearGradientPaint

and

RadialGradientPaint

.

**All Implemented Interfaces:** Paint

,

Transparency

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public final float[] getFractions()

Returns a copy of the array of floats used by this gradient
to calculate color distribution.
The returned array always has 0 as its first value and 1 as its
last value, with increasing values in between.

**Returns:**
- a copy of the array of floats used by this gradient to
calculate color distribution

---

#### public final
Color
[] getColors()

Returns a copy of the array of colors used by this gradient.
The first color maps to the first value in the fractions array,
and the last color maps to the last value in the fractions array.

**Returns:**
- a copy of the array of colors used by this gradient

---

#### public final
MultipleGradientPaint.CycleMethod
getCycleMethod()

Returns the enumerated type which specifies cycling behavior.

**Returns:**
- the enumerated type which specifies cycling behavior

---

#### public final
MultipleGradientPaint.ColorSpaceType
getColorSpace()

Returns the enumerated type which specifies color space for
interpolation.

**Returns:**
- the enumerated type which specifies color space for
interpolation

---

#### public final
AffineTransform
getTransform()

Returns a copy of the transform applied to the gradient.

Note that if no transform is applied to the gradient
when it is created, the identity transform is used.

**Returns:**
- a copy of the transform applied to the gradient

---

#### public final int getTransparency()

Returns the transparency mode for this

Paint

object.

**Specified by:**
- getTransparency

in interface

Transparency

**Returns:**
- OPAQUE

if all colors used by this

Paint

object are opaque,

TRANSLUCENT

if at least one of the
colors used by this

Paint

object is not opaque.

**See Also:**
- Transparency

---

### Additional Sections

#### Class MultipleGradientPaint

java.lang.Object

- java.awt.MultipleGradientPaint

java.awt.MultipleGradientPaint

**All Implemented Interfaces:** Paint

,

Transparency

**Direct Known Subclasses:** LinearGradientPaint

,

RadialGradientPaint

```java
public abstract class
MultipleGradientPaint

extends
Object

implements
Paint
```

This is the superclass for Paints which use a multiple color
gradient to fill in their raster. It provides storage for variables and
enumerated values common to

LinearGradientPaint

and

RadialGradientPaint

.

**Since:** 1.6

public abstract class

MultipleGradientPaint

extends

Object

implements

Paint

This is the superclass for Paints which use a multiple color
gradient to fill in their raster. It provides storage for variables and
enumerated values common to

LinearGradientPaint

and

RadialGradientPaint

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

MultipleGradientPaint.ColorSpaceType

The color space in which to perform the gradient interpolation.

static class

MultipleGradientPaint.CycleMethod

The method to use when painting outside the gradient bounds.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Color

[]

getColors

()

Returns a copy of the array of colors used by this gradient.

MultipleGradientPaint.ColorSpaceType

getColorSpace

()

Returns the enumerated type which specifies color space for
interpolation.

MultipleGradientPaint.CycleMethod

getCycleMethod

()

Returns the enumerated type which specifies cycling behavior.

float[]

getFractions

()

Returns a copy of the array of floats used by this gradient
to calculate color distribution.

AffineTransform

getTransform

()

Returns a copy of the transform applied to the gradient.

int

getTransparency

()

Returns the transparency mode for this

Paint

object.

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

- Methods declared in interface java.awt.

Paint

createContext

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

MultipleGradientPaint.ColorSpaceType

The color space in which to perform the gradient interpolation.

static class

MultipleGradientPaint.CycleMethod

The method to use when painting outside the gradient bounds.

---

#### Nested Class Summary

The color space in which to perform the gradient interpolation.

The method to use when painting outside the gradient bounds.

Field Summary

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Fields declared in interface java.awt. Transparency

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Color

[]

getColors

()

Returns a copy of the array of colors used by this gradient.

MultipleGradientPaint.ColorSpaceType

getColorSpace

()

Returns the enumerated type which specifies color space for
interpolation.

MultipleGradientPaint.CycleMethod

getCycleMethod

()

Returns the enumerated type which specifies cycling behavior.

float[]

getFractions

()

Returns a copy of the array of floats used by this gradient
to calculate color distribution.

AffineTransform

getTransform

()

Returns a copy of the transform applied to the gradient.

int

getTransparency

()

Returns the transparency mode for this

Paint

object.

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

- Methods declared in interface java.awt.

Paint

createContext

---

#### Method Summary

Returns a copy of the array of colors used by this gradient.

Returns the enumerated type which specifies color space for
interpolation.

Returns the enumerated type which specifies cycling behavior.

Returns a copy of the array of floats used by this gradient
to calculate color distribution.

Returns a copy of the transform applied to the gradient.

Returns the transparency mode for this

Paint

object.

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

Methods declared in interface java.awt.

Paint

createContext

---

#### Methods declared in interface java.awt. Paint

============ METHOD DETAIL ==========

- Method Detail

- getFractions

```java
public final float[] getFractions()
```

Returns a copy of the array of floats used by this gradient
to calculate color distribution.
The returned array always has 0 as its first value and 1 as its
last value, with increasing values in between.

**Returns:** a copy of the array of floats used by this gradient to
calculate color distribution

- getColors

```java
public final
Color
[] getColors()
```

Returns a copy of the array of colors used by this gradient.
The first color maps to the first value in the fractions array,
and the last color maps to the last value in the fractions array.

**Returns:** a copy of the array of colors used by this gradient

- getCycleMethod

```java
public final
MultipleGradientPaint.CycleMethod
getCycleMethod()
```

Returns the enumerated type which specifies cycling behavior.

**Returns:** the enumerated type which specifies cycling behavior

- getColorSpace

```java
public final
MultipleGradientPaint.ColorSpaceType
getColorSpace()
```

Returns the enumerated type which specifies color space for
interpolation.

**Returns:** the enumerated type which specifies color space for
interpolation

- getTransform

```java
public final
AffineTransform
getTransform()
```

Returns a copy of the transform applied to the gradient.

Note that if no transform is applied to the gradient
when it is created, the identity transform is used.

**Returns:** a copy of the transform applied to the gradient

- getTransparency

```java
public final int getTransparency()
```

Returns the transparency mode for this

Paint

object.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** OPAQUE

if all colors used by this

Paint

object are opaque,

TRANSLUCENT

if at least one of the
colors used by this

Paint

object is not opaque.
**See Also:** Transparency

Method Detail

- getFractions

```java
public final float[] getFractions()
```

Returns a copy of the array of floats used by this gradient
to calculate color distribution.
The returned array always has 0 as its first value and 1 as its
last value, with increasing values in between.

**Returns:** a copy of the array of floats used by this gradient to
calculate color distribution

- getColors

```java
public final
Color
[] getColors()
```

Returns a copy of the array of colors used by this gradient.
The first color maps to the first value in the fractions array,
and the last color maps to the last value in the fractions array.

**Returns:** a copy of the array of colors used by this gradient

- getCycleMethod

```java
public final
MultipleGradientPaint.CycleMethod
getCycleMethod()
```

Returns the enumerated type which specifies cycling behavior.

**Returns:** the enumerated type which specifies cycling behavior

- getColorSpace

```java
public final
MultipleGradientPaint.ColorSpaceType
getColorSpace()
```

Returns the enumerated type which specifies color space for
interpolation.

**Returns:** the enumerated type which specifies color space for
interpolation

- getTransform

```java
public final
AffineTransform
getTransform()
```

Returns a copy of the transform applied to the gradient.

Note that if no transform is applied to the gradient
when it is created, the identity transform is used.

**Returns:** a copy of the transform applied to the gradient

- getTransparency

```java
public final int getTransparency()
```

Returns the transparency mode for this

Paint

object.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** OPAQUE

if all colors used by this

Paint

object are opaque,

TRANSLUCENT

if at least one of the
colors used by this

Paint

object is not opaque.
**See Also:** Transparency

---

#### Method Detail

getFractions

```java
public final float[] getFractions()
```

Returns a copy of the array of floats used by this gradient
to calculate color distribution.
The returned array always has 0 as its first value and 1 as its
last value, with increasing values in between.

**Returns:** a copy of the array of floats used by this gradient to
calculate color distribution

---

#### getFractions

public final float[] getFractions()

Returns a copy of the array of floats used by this gradient
to calculate color distribution.
The returned array always has 0 as its first value and 1 as its
last value, with increasing values in between.

getColors

```java
public final
Color
[] getColors()
```

Returns a copy of the array of colors used by this gradient.
The first color maps to the first value in the fractions array,
and the last color maps to the last value in the fractions array.

**Returns:** a copy of the array of colors used by this gradient

---

#### getColors

public final

Color

[] getColors()

Returns a copy of the array of colors used by this gradient.
The first color maps to the first value in the fractions array,
and the last color maps to the last value in the fractions array.

getCycleMethod

```java
public final
MultipleGradientPaint.CycleMethod
getCycleMethod()
```

Returns the enumerated type which specifies cycling behavior.

**Returns:** the enumerated type which specifies cycling behavior

---

#### getCycleMethod

public final

MultipleGradientPaint.CycleMethod

getCycleMethod()

Returns the enumerated type which specifies cycling behavior.

getColorSpace

```java
public final
MultipleGradientPaint.ColorSpaceType
getColorSpace()
```

Returns the enumerated type which specifies color space for
interpolation.

**Returns:** the enumerated type which specifies color space for
interpolation

---

#### getColorSpace

public final

MultipleGradientPaint.ColorSpaceType

getColorSpace()

Returns the enumerated type which specifies color space for
interpolation.

getTransform

```java
public final
AffineTransform
getTransform()
```

Returns a copy of the transform applied to the gradient.

Note that if no transform is applied to the gradient
when it is created, the identity transform is used.

**Returns:** a copy of the transform applied to the gradient

---

#### getTransform

public final

AffineTransform

getTransform()

Returns a copy of the transform applied to the gradient.

Note that if no transform is applied to the gradient
when it is created, the identity transform is used.

Note that if no transform is applied to the gradient
when it is created, the identity transform is used.

getTransparency

```java
public final int getTransparency()
```

Returns the transparency mode for this

Paint

object.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** OPAQUE

if all colors used by this

Paint

object are opaque,

TRANSLUCENT

if at least one of the
colors used by this

Paint

object is not opaque.
**See Also:** Transparency

---

#### getTransparency

public final int getTransparency()

Returns the transparency mode for this

Paint

object.

---

