# Interface Transparency

**Source:** `java.desktop\java\awt\Transparency.html`

### Class Description

```java
public interface
Transparency
```

The

Transparency

interface defines the common transparency
modes for implementing classes.

**All Known Subinterfaces:** Paint

---

### Field Details

#### @Native

static final int OPAQUE

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

**See Also:**
- Constant Field Values

---

#### @Native

static final int BITMASK

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

**See Also:**
- Constant Field Values

---

#### @Native

static final int TRANSLUCENT

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getTransparency()

Returns the type of this

Transparency

.

**Returns:**
- the field type of this

Transparency

, which is
either OPAQUE, BITMASK or TRANSLUCENT.

---

### Additional Sections

#### Interface Transparency

**All Known Subinterfaces:** Paint

**All Known Implementing Classes:** BufferedImage

,

Color

,

ColorModel

,

ColorUIResource

,

ComponentColorModel

,

DirectColorModel

,

GradientPaint

,

IndexColorModel

,

LinearGradientPaint

,

MultipleGradientPaint

,

PackedColorModel

,

RadialGradientPaint

,

SystemColor

,

TexturePaint

,

VolatileImage

```java
public interface
Transparency
```

The

Transparency

interface defines the common transparency
modes for implementing classes.

public interface

Transparency

The

Transparency

interface defines the common transparency
modes for implementing classes.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BITMASK

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

static int

OPAQUE

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

static int

TRANSLUCENT

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getTransparency

()

Returns the type of this

Transparency

.

Field Summary

Fields

Modifier and Type

Field

Description

static int

BITMASK

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

static int

OPAQUE

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

static int

TRANSLUCENT

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

---

#### Field Summary

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getTransparency

()

Returns the type of this

Transparency

.

---

#### Method Summary

Returns the type of this

Transparency

.

============ FIELD DETAIL ===========

- Field Detail

- OPAQUE

```java
@Native

static final int OPAQUE
```

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

**See Also:** Constant Field Values

- BITMASK

```java
@Native

static final int BITMASK
```

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

**See Also:** Constant Field Values

- TRANSLUCENT

```java
@Native

static final int TRANSLUCENT
```

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getTransparency

```java
int getTransparency()
```

Returns the type of this

Transparency

.

**Returns:** the field type of this

Transparency

, which is
either OPAQUE, BITMASK or TRANSLUCENT.

Field Detail

- OPAQUE

```java
@Native

static final int OPAQUE
```

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

**See Also:** Constant Field Values

- BITMASK

```java
@Native

static final int BITMASK
```

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

**See Also:** Constant Field Values

- TRANSLUCENT

```java
@Native

static final int TRANSLUCENT
```

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

**See Also:** Constant Field Values

---

#### Field Detail

OPAQUE

```java
@Native

static final int OPAQUE
```

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

**See Also:** Constant Field Values

---

#### OPAQUE

@Native

static final int OPAQUE

Represents image data that is guaranteed to be completely opaque,
meaning that all pixels have an alpha value of 1.0.

BITMASK

```java
@Native

static final int BITMASK
```

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

**See Also:** Constant Field Values

---

#### BITMASK

@Native

static final int BITMASK

Represents image data that is guaranteed to be either completely
opaque, with an alpha value of 1.0, or completely transparent,
with an alpha value of 0.0.

TRANSLUCENT

```java
@Native

static final int TRANSLUCENT
```

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

**See Also:** Constant Field Values

---

#### TRANSLUCENT

@Native

static final int TRANSLUCENT

Represents image data that contains or might contain arbitrary
alpha values between and including 0.0 and 1.0.

Method Detail

- getTransparency

```java
int getTransparency()
```

Returns the type of this

Transparency

.

**Returns:** the field type of this

Transparency

, which is
either OPAQUE, BITMASK or TRANSLUCENT.

---

#### Method Detail

getTransparency

```java
int getTransparency()
```

Returns the type of this

Transparency

.

**Returns:** the field type of this

Transparency

, which is
either OPAQUE, BITMASK or TRANSLUCENT.

---

#### getTransparency

int getTransparency()

Returns the type of this

Transparency

.

---

