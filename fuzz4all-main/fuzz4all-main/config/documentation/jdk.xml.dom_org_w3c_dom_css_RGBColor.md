# Interface RGBColor

**Source:** `jdk.xml.dom\org\w3c\dom\css\RGBColor.html`

### Class Description

```java
public interface
RGBColor
```

The

RGBColor

interface is used to represent any RGB color
value. This interface reflects the values in the underlying style
property. Hence, modifications made to the

CSSPrimitiveValue

objects modify the style property.

A specified RGB color is not clipped (even if the number is outside the
range 0-255 or 0%-100%). A computed RGB color is clipped depending on the
device.

Even if a style sheet can only contain an integer for a color value,
the internal storage of this integer is a float, and this can be used as
a float in the specified or the computed style.

A color percentage value can always be converted to a number and vice
versa.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CSSPrimitiveValue
getRed()

This attribute is used for the red value of the RGB color.

---

#### CSSPrimitiveValue
getGreen()

This attribute is used for the green value of the RGB color.

---

#### CSSPrimitiveValue
getBlue()

This attribute is used for the blue value of the RGB color.

---

### Additional Sections

#### Interface RGBColor

```java
public interface
RGBColor
```

The

RGBColor

interface is used to represent any RGB color
value. This interface reflects the values in the underlying style
property. Hence, modifications made to the

CSSPrimitiveValue

objects modify the style property.

A specified RGB color is not clipped (even if the number is outside the
range 0-255 or 0%-100%). A computed RGB color is clipped depending on the
device.

Even if a style sheet can only contain an integer for a color value,
the internal storage of this integer is a float, and this can be used as
a float in the specified or the computed style.

A color percentage value can always be converted to a number and vice
versa.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

RGBColor

The

RGBColor

interface is used to represent any RGB color
value. This interface reflects the values in the underlying style
property. Hence, modifications made to the

CSSPrimitiveValue

objects modify the style property.

A specified RGB color is not clipped (even if the number is outside the
range 0-255 or 0%-100%). A computed RGB color is clipped depending on the
device.

Even if a style sheet can only contain an integer for a color value,
the internal storage of this integer is a float, and this can be used as
a float in the specified or the computed style.

A color percentage value can always be converted to a number and vice
versa.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

A specified RGB color is not clipped (even if the number is outside the
range 0-255 or 0%-100%). A computed RGB color is clipped depending on the
device.

Even if a style sheet can only contain an integer for a color value,
the internal storage of this integer is a float, and this can be used as
a float in the specified or the computed style.

A color percentage value can always be converted to a number and vice
versa.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

Even if a style sheet can only contain an integer for a color value,
the internal storage of this integer is a float, and this can be used as
a float in the specified or the computed style.

A color percentage value can always be converted to a number and vice
versa.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

A color percentage value can always be converted to a number and vice
versa.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CSSPrimitiveValue

getBlue

()

This attribute is used for the blue value of the RGB color.

CSSPrimitiveValue

getGreen

()

This attribute is used for the green value of the RGB color.

CSSPrimitiveValue

getRed

()

This attribute is used for the red value of the RGB color.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CSSPrimitiveValue

getBlue

()

This attribute is used for the blue value of the RGB color.

CSSPrimitiveValue

getGreen

()

This attribute is used for the green value of the RGB color.

CSSPrimitiveValue

getRed

()

This attribute is used for the red value of the RGB color.

---

#### Method Summary

This attribute is used for the blue value of the RGB color.

This attribute is used for the green value of the RGB color.

This attribute is used for the red value of the RGB color.

============ METHOD DETAIL ==========

- Method Detail

- getRed

```java
CSSPrimitiveValue
getRed()
```

This attribute is used for the red value of the RGB color.

- getGreen

```java
CSSPrimitiveValue
getGreen()
```

This attribute is used for the green value of the RGB color.

- getBlue

```java
CSSPrimitiveValue
getBlue()
```

This attribute is used for the blue value of the RGB color.

Method Detail

- getRed

```java
CSSPrimitiveValue
getRed()
```

This attribute is used for the red value of the RGB color.

- getGreen

```java
CSSPrimitiveValue
getGreen()
```

This attribute is used for the green value of the RGB color.

- getBlue

```java
CSSPrimitiveValue
getBlue()
```

This attribute is used for the blue value of the RGB color.

---

#### Method Detail

getRed

```java
CSSPrimitiveValue
getRed()
```

This attribute is used for the red value of the RGB color.

---

#### getRed

CSSPrimitiveValue

getRed()

This attribute is used for the red value of the RGB color.

getGreen

```java
CSSPrimitiveValue
getGreen()
```

This attribute is used for the green value of the RGB color.

---

#### getGreen

CSSPrimitiveValue

getGreen()

This attribute is used for the green value of the RGB color.

getBlue

```java
CSSPrimitiveValue
getBlue()
```

This attribute is used for the blue value of the RGB color.

---

#### getBlue

CSSPrimitiveValue

getBlue()

This attribute is used for the blue value of the RGB color.

---

