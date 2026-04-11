# Interface CSSPrimitiveValue

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSPrimitiveValue.html`

### Class Description

```java
public interface
CSSPrimitiveValue

extends
CSSValue
```

The

CSSPrimitiveValue

interface represents a single CSS value
. This interface may be used to determine the value of a specific style
property currently set in a block or to set a specific style property
explicitly within the block. An instance of this interface might be
obtained from the

getPropertyCSSValue

method of the

CSSStyleDeclaration

interface. A

CSSPrimitiveValue

object only occurs in a context of a CSS
property.

Conversions are allowed between absolute values (from millimeters to
centimeters, from degrees to radians, and so on) but not between relative
values. (For example, a pixel value cannot be converted to a centimeter
value.) Percentage values can't be converted since they are relative to
the parent value (or another property value). There is one exception for
color percentage values: since a color percentage value is relative to
the range 0-255, a color percentage value can be converted to a number;
(see also the

RGBColor

interface).

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** CSSValue

---

### Field Details

#### static final short CSS_UNKNOWN

The value is not a recognized CSS2 value. The value can only be
obtained by using the

cssText

attribute.

**See Also:**
- Constant Field Values

---

#### static final short CSS_NUMBER

The value is a simple number. The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_PERCENTAGE

The value is a percentage. The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_EMS

The value is a length (ems). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_EXS

The value is a length (exs). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_PX

The value is a length (px). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_CM

The value is a length (cm). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_MM

The value is a length (mm). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_IN

The value is a length (in). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_PT

The value is a length (pt). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_PC

The value is a length (pc). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_DEG

The value is an angle (deg). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_RAD

The value is an angle (rad). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_GRAD

The value is an angle (grad). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_MS

The value is a time (ms). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_S

The value is a time (s). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_HZ

The value is a frequency (Hz). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_KHZ

The value is a frequency (kHz). The value can be obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_DIMENSION

The value is a number with an unknown dimension. The value can be
obtained by using the

getFloatValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_STRING

The value is a STRING. The value can be obtained by using the

getStringValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_URI

The value is a URI. The value can be obtained by using the

getStringValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_IDENT

The value is an identifier. The value can be obtained by using the

getStringValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_ATTR

The value is a attribute function. The value can be obtained by using
the

getStringValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_COUNTER

The value is a counter or counters function. The value can be obtained
by using the

getCounterValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_RECT

The value is a rect function. The value can be obtained by using the

getRectValue

method.

**See Also:**
- Constant Field Values

---

#### static final short CSS_RGBCOLOR

The value is a RGB color. The value can be obtained by using the

getRGBColorValue

method.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### short getPrimitiveType()

The type of the value as defined by the constants specified above.

---

#### void setFloatValue​(short unitType,
float floatValue)
throws
DOMException

A method to set the float value with a specified unit. If the property
attached with this value can not accept the specified unit or the
float value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:**
- unitType

- A unit code as defined above. The unit code can only
be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
- floatValue

- The new float value.

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the attached property doesn't support
the float value or the unit type.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### float getFloatValue​(short unitType)
throws
DOMException

This method is used to get a float value in a specified unit. If this
CSS value doesn't contain a float value or can't be converted into
the specified unit, a

DOMException

is raised.

**Parameters:**
- unitType

- A unit code to get the float value. The unit code can
only be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).

**Returns:**
- The float value in the specified unit.

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a float
value or if the float value can't be converted into the specified
unit.

---

#### void setStringValue​(short stringType,

String
stringValue)
throws
DOMException

A method to set the string value with the specified unit. If the
property attached to this value can't accept the specified unit or
the string value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:**
- stringType

- A string code as defined above. The string code can
only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

, and

CSS_ATTR

).
- stringValue

- The new string value.

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value or if the string value can't be converted into the specified
unit.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getStringValue()
throws
DOMException

This method is used to get the string value. If the CSS value doesn't
contain a string value, a

DOMException

is raised. Some
properties (like 'font-family' or 'voice-family') convert a
whitespace separated list of idents to a string.

**Returns:**
- The string value in the current unit. The current

primitiveType

can only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

and

CSS_ATTR

).

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value.

---

#### Counter
getCounterValue()
throws
DOMException

This method is used to get the Counter value. If this CSS value
doesn't contain a counter value, a

DOMException

is
raised. Modification to the corresponding style property can be
achieved using the

Counter

interface.

**Returns:**
- The Counter value.

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a
Counter value (e.g. this is not

CSS_COUNTER

).

---

#### Rect
getRectValue()
throws
DOMException

This method is used to get the Rect value. If this CSS value doesn't
contain a rect value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

Rect

interface.

**Returns:**
- The Rect value.

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a Rect
value. (e.g. this is not

CSS_RECT

).

---

#### RGBColor
getRGBColorValue()
throws
DOMException

This method is used to get the RGB color. If this CSS value doesn't
contain a RGB color value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

RGBColor

interface.

**Returns:**
- the RGB color value.

**Throws:**
- DOMException

- INVALID_ACCESS_ERR: Raised if the attached property can't return a
RGB color value (e.g. this is not

CSS_RGBCOLOR

).

---

### Additional Sections

#### Interface CSSPrimitiveValue

**All Superinterfaces:** CSSValue

```java
public interface
CSSPrimitiveValue

extends
CSSValue
```

The

CSSPrimitiveValue

interface represents a single CSS value
. This interface may be used to determine the value of a specific style
property currently set in a block or to set a specific style property
explicitly within the block. An instance of this interface might be
obtained from the

getPropertyCSSValue

method of the

CSSStyleDeclaration

interface. A

CSSPrimitiveValue

object only occurs in a context of a CSS
property.

Conversions are allowed between absolute values (from millimeters to
centimeters, from degrees to radians, and so on) but not between relative
values. (For example, a pixel value cannot be converted to a centimeter
value.) Percentage values can't be converted since they are relative to
the parent value (or another property value). There is one exception for
color percentage values: since a color percentage value is relative to
the range 0-255, a color percentage value can be converted to a number;
(see also the

RGBColor

interface).

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSPrimitiveValue

extends

CSSValue

The

CSSPrimitiveValue

interface represents a single CSS value
. This interface may be used to determine the value of a specific style
property currently set in a block or to set a specific style property
explicitly within the block. An instance of this interface might be
obtained from the

getPropertyCSSValue

method of the

CSSStyleDeclaration

interface. A

CSSPrimitiveValue

object only occurs in a context of a CSS
property.

Conversions are allowed between absolute values (from millimeters to
centimeters, from degrees to radians, and so on) but not between relative
values. (For example, a pixel value cannot be converted to a centimeter
value.) Percentage values can't be converted since they are relative to
the parent value (or another property value). There is one exception for
color percentage values: since a color percentage value is relative to
the range 0-255, a color percentage value can be converted to a number;
(see also the

RGBColor

interface).

See also the

Document Object Model (DOM) Level 2 Style Specification

.

Conversions are allowed between absolute values (from millimeters to
centimeters, from degrees to radians, and so on) but not between relative
values. (For example, a pixel value cannot be converted to a centimeter
value.) Percentage values can't be converted since they are relative to
the parent value (or another property value). There is one exception for
color percentage values: since a color percentage value is relative to
the range 0-255, a color percentage value can be converted to a number;
(see also the

RGBColor

interface).

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

CSS_ATTR

The value is a attribute function.

static short

CSS_CM

The value is a length (cm).

static short

CSS_COUNTER

The value is a counter or counters function.

static short

CSS_DEG

The value is an angle (deg).

static short

CSS_DIMENSION

The value is a number with an unknown dimension.

static short

CSS_EMS

The value is a length (ems).

static short

CSS_EXS

The value is a length (exs).

static short

CSS_GRAD

The value is an angle (grad).

static short

CSS_HZ

The value is a frequency (Hz).

static short

CSS_IDENT

The value is an identifier.

static short

CSS_IN

The value is a length (in).

static short

CSS_KHZ

The value is a frequency (kHz).

static short

CSS_MM

The value is a length (mm).

static short

CSS_MS

The value is a time (ms).

static short

CSS_NUMBER

The value is a simple number.

static short

CSS_PC

The value is a length (pc).

static short

CSS_PERCENTAGE

The value is a percentage.

static short

CSS_PT

The value is a length (pt).

static short

CSS_PX

The value is a length (px).

static short

CSS_RAD

The value is an angle (rad).

static short

CSS_RECT

The value is a rect function.

static short

CSS_RGBCOLOR

The value is a RGB color.

static short

CSS_S

The value is a time (s).

static short

CSS_STRING

The value is a STRING.

static short

CSS_UNKNOWN

The value is not a recognized CSS2 value.

static short

CSS_URI

The value is a URI.

- Fields declared in interface org.w3c.dom.css.

CSSValue

CSS_CUSTOM

,

CSS_INHERIT

,

CSS_PRIMITIVE_VALUE

,

CSS_VALUE_LIST

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Counter

getCounterValue

()

This method is used to get the Counter value.

float

getFloatValue

​(short unitType)

This method is used to get a float value in a specified unit.

short

getPrimitiveType

()

The type of the value as defined by the constants specified above.

Rect

getRectValue

()

This method is used to get the Rect value.

RGBColor

getRGBColorValue

()

This method is used to get the RGB color.

String

getStringValue

()

This method is used to get the string value.

void

setFloatValue

​(short unitType,
float floatValue)

A method to set the float value with a specified unit.

void

setStringValue

​(short stringType,

String

stringValue)

A method to set the string value with the specified unit.

- Methods declared in interface org.w3c.dom.css.

CSSValue

getCssText

,

getCssValueType

,

setCssText

Field Summary

Fields

Modifier and Type

Field

Description

static short

CSS_ATTR

The value is a attribute function.

static short

CSS_CM

The value is a length (cm).

static short

CSS_COUNTER

The value is a counter or counters function.

static short

CSS_DEG

The value is an angle (deg).

static short

CSS_DIMENSION

The value is a number with an unknown dimension.

static short

CSS_EMS

The value is a length (ems).

static short

CSS_EXS

The value is a length (exs).

static short

CSS_GRAD

The value is an angle (grad).

static short

CSS_HZ

The value is a frequency (Hz).

static short

CSS_IDENT

The value is an identifier.

static short

CSS_IN

The value is a length (in).

static short

CSS_KHZ

The value is a frequency (kHz).

static short

CSS_MM

The value is a length (mm).

static short

CSS_MS

The value is a time (ms).

static short

CSS_NUMBER

The value is a simple number.

static short

CSS_PC

The value is a length (pc).

static short

CSS_PERCENTAGE

The value is a percentage.

static short

CSS_PT

The value is a length (pt).

static short

CSS_PX

The value is a length (px).

static short

CSS_RAD

The value is an angle (rad).

static short

CSS_RECT

The value is a rect function.

static short

CSS_RGBCOLOR

The value is a RGB color.

static short

CSS_S

The value is a time (s).

static short

CSS_STRING

The value is a STRING.

static short

CSS_UNKNOWN

The value is not a recognized CSS2 value.

static short

CSS_URI

The value is a URI.

- Fields declared in interface org.w3c.dom.css.

CSSValue

CSS_CUSTOM

,

CSS_INHERIT

,

CSS_PRIMITIVE_VALUE

,

CSS_VALUE_LIST

---

#### Field Summary

The value is a attribute function.

The value is a length (cm).

The value is a counter or counters function.

The value is an angle (deg).

The value is a number with an unknown dimension.

The value is a length (ems).

The value is a length (exs).

The value is an angle (grad).

The value is a frequency (Hz).

The value is an identifier.

The value is a length (in).

The value is a frequency (kHz).

The value is a length (mm).

The value is a time (ms).

The value is a simple number.

The value is a length (pc).

The value is a percentage.

The value is a length (pt).

The value is a length (px).

The value is an angle (rad).

The value is a rect function.

The value is a RGB color.

The value is a time (s).

The value is a STRING.

The value is not a recognized CSS2 value.

The value is a URI.

Fields declared in interface org.w3c.dom.css.

CSSValue

CSS_CUSTOM

,

CSS_INHERIT

,

CSS_PRIMITIVE_VALUE

,

CSS_VALUE_LIST

---

#### Fields declared in interface org.w3c.dom.css. CSSValue

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Counter

getCounterValue

()

This method is used to get the Counter value.

float

getFloatValue

​(short unitType)

This method is used to get a float value in a specified unit.

short

getPrimitiveType

()

The type of the value as defined by the constants specified above.

Rect

getRectValue

()

This method is used to get the Rect value.

RGBColor

getRGBColorValue

()

This method is used to get the RGB color.

String

getStringValue

()

This method is used to get the string value.

void

setFloatValue

​(short unitType,
float floatValue)

A method to set the float value with a specified unit.

void

setStringValue

​(short stringType,

String

stringValue)

A method to set the string value with the specified unit.

- Methods declared in interface org.w3c.dom.css.

CSSValue

getCssText

,

getCssValueType

,

setCssText

---

#### Method Summary

This method is used to get the Counter value.

This method is used to get a float value in a specified unit.

The type of the value as defined by the constants specified above.

This method is used to get the Rect value.

This method is used to get the RGB color.

This method is used to get the string value.

A method to set the float value with a specified unit.

A method to set the string value with the specified unit.

Methods declared in interface org.w3c.dom.css.

CSSValue

getCssText

,

getCssValueType

,

setCssText

---

#### Methods declared in interface org.w3c.dom.css. CSSValue

============ FIELD DETAIL ===========

- Field Detail

- CSS_UNKNOWN

```java
static final short CSS_UNKNOWN
```

The value is not a recognized CSS2 value. The value can only be
obtained by using the

cssText

attribute.

**See Also:** Constant Field Values

- CSS_NUMBER

```java
static final short CSS_NUMBER
```

The value is a simple number. The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PERCENTAGE

```java
static final short CSS_PERCENTAGE
```

The value is a percentage. The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_EMS

```java
static final short CSS_EMS
```

The value is a length (ems). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_EXS

```java
static final short CSS_EXS
```

The value is a length (exs). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PX

```java
static final short CSS_PX
```

The value is a length (px). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_CM

```java
static final short CSS_CM
```

The value is a length (cm). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_MM

```java
static final short CSS_MM
```

The value is a length (mm). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_IN

```java
static final short CSS_IN
```

The value is a length (in). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PT

```java
static final short CSS_PT
```

The value is a length (pt). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PC

```java
static final short CSS_PC
```

The value is a length (pc). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_DEG

```java
static final short CSS_DEG
```

The value is an angle (deg). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_RAD

```java
static final short CSS_RAD
```

The value is an angle (rad). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_GRAD

```java
static final short CSS_GRAD
```

The value is an angle (grad). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_MS

```java
static final short CSS_MS
```

The value is a time (ms). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_S

```java
static final short CSS_S
```

The value is a time (s). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_HZ

```java
static final short CSS_HZ
```

The value is a frequency (Hz). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_KHZ

```java
static final short CSS_KHZ
```

The value is a frequency (kHz). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_DIMENSION

```java
static final short CSS_DIMENSION
```

The value is a number with an unknown dimension. The value can be
obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_STRING

```java
static final short CSS_STRING
```

The value is a STRING. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_URI

```java
static final short CSS_URI
```

The value is a URI. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_IDENT

```java
static final short CSS_IDENT
```

The value is an identifier. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_ATTR

```java
static final short CSS_ATTR
```

The value is a attribute function. The value can be obtained by using
the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_COUNTER

```java
static final short CSS_COUNTER
```

The value is a counter or counters function. The value can be obtained
by using the

getCounterValue

method.

**See Also:** Constant Field Values

- CSS_RECT

```java
static final short CSS_RECT
```

The value is a rect function. The value can be obtained by using the

getRectValue

method.

**See Also:** Constant Field Values

- CSS_RGBCOLOR

```java
static final short CSS_RGBCOLOR
```

The value is a RGB color. The value can be obtained by using the

getRGBColorValue

method.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getPrimitiveType

```java
short getPrimitiveType()
```

The type of the value as defined by the constants specified above.

- setFloatValue

```java
void setFloatValue​(short unitType,
float floatValue)
throws
DOMException
```

A method to set the float value with a specified unit. If the property
attached with this value can not accept the specified unit or the
float value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:** unitType

- A unit code as defined above. The unit code can only
be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
**Parameters:** floatValue

- The new float value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the attached property doesn't support
the float value or the unit type.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFloatValue

```java
float getFloatValue​(short unitType)
throws
DOMException
```

This method is used to get a float value in a specified unit. If this
CSS value doesn't contain a float value or can't be converted into
the specified unit, a

DOMException

is raised.

**Parameters:** unitType

- A unit code to get the float value. The unit code can
only be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
**Returns:** The float value in the specified unit.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a float
value or if the float value can't be converted into the specified
unit.

- setStringValue

```java
void setStringValue​(short stringType,

String
stringValue)
throws
DOMException
```

A method to set the string value with the specified unit. If the
property attached to this value can't accept the specified unit or
the string value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:** stringType

- A string code as defined above. The string code can
only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

, and

CSS_ATTR

).
**Parameters:** stringValue

- The new string value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value or if the string value can't be converted into the specified
unit.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getStringValue

```java
String
getStringValue()
throws
DOMException
```

This method is used to get the string value. If the CSS value doesn't
contain a string value, a

DOMException

is raised. Some
properties (like 'font-family' or 'voice-family') convert a
whitespace separated list of idents to a string.

**Returns:** The string value in the current unit. The current

primitiveType

can only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

and

CSS_ATTR

).
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value.

- getCounterValue

```java
Counter
getCounterValue()
throws
DOMException
```

This method is used to get the Counter value. If this CSS value
doesn't contain a counter value, a

DOMException

is
raised. Modification to the corresponding style property can be
achieved using the

Counter

interface.

**Returns:** The Counter value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a
Counter value (e.g. this is not

CSS_COUNTER

).

- getRectValue

```java
Rect
getRectValue()
throws
DOMException
```

This method is used to get the Rect value. If this CSS value doesn't
contain a rect value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

Rect

interface.

**Returns:** The Rect value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a Rect
value. (e.g. this is not

CSS_RECT

).

- getRGBColorValue

```java
RGBColor
getRGBColorValue()
throws
DOMException
```

This method is used to get the RGB color. If this CSS value doesn't
contain a RGB color value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

RGBColor

interface.

**Returns:** the RGB color value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the attached property can't return a
RGB color value (e.g. this is not

CSS_RGBCOLOR

).

Field Detail

- CSS_UNKNOWN

```java
static final short CSS_UNKNOWN
```

The value is not a recognized CSS2 value. The value can only be
obtained by using the

cssText

attribute.

**See Also:** Constant Field Values

- CSS_NUMBER

```java
static final short CSS_NUMBER
```

The value is a simple number. The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PERCENTAGE

```java
static final short CSS_PERCENTAGE
```

The value is a percentage. The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_EMS

```java
static final short CSS_EMS
```

The value is a length (ems). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_EXS

```java
static final short CSS_EXS
```

The value is a length (exs). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PX

```java
static final short CSS_PX
```

The value is a length (px). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_CM

```java
static final short CSS_CM
```

The value is a length (cm). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_MM

```java
static final short CSS_MM
```

The value is a length (mm). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_IN

```java
static final short CSS_IN
```

The value is a length (in). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PT

```java
static final short CSS_PT
```

The value is a length (pt). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_PC

```java
static final short CSS_PC
```

The value is a length (pc). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_DEG

```java
static final short CSS_DEG
```

The value is an angle (deg). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_RAD

```java
static final short CSS_RAD
```

The value is an angle (rad). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_GRAD

```java
static final short CSS_GRAD
```

The value is an angle (grad). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_MS

```java
static final short CSS_MS
```

The value is a time (ms). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_S

```java
static final short CSS_S
```

The value is a time (s). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_HZ

```java
static final short CSS_HZ
```

The value is a frequency (Hz). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_KHZ

```java
static final short CSS_KHZ
```

The value is a frequency (kHz). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_DIMENSION

```java
static final short CSS_DIMENSION
```

The value is a number with an unknown dimension. The value can be
obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

- CSS_STRING

```java
static final short CSS_STRING
```

The value is a STRING. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_URI

```java
static final short CSS_URI
```

The value is a URI. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_IDENT

```java
static final short CSS_IDENT
```

The value is an identifier. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_ATTR

```java
static final short CSS_ATTR
```

The value is a attribute function. The value can be obtained by using
the

getStringValue

method.

**See Also:** Constant Field Values

- CSS_COUNTER

```java
static final short CSS_COUNTER
```

The value is a counter or counters function. The value can be obtained
by using the

getCounterValue

method.

**See Also:** Constant Field Values

- CSS_RECT

```java
static final short CSS_RECT
```

The value is a rect function. The value can be obtained by using the

getRectValue

method.

**See Also:** Constant Field Values

- CSS_RGBCOLOR

```java
static final short CSS_RGBCOLOR
```

The value is a RGB color. The value can be obtained by using the

getRGBColorValue

method.

**See Also:** Constant Field Values

---

#### Field Detail

CSS_UNKNOWN

```java
static final short CSS_UNKNOWN
```

The value is not a recognized CSS2 value. The value can only be
obtained by using the

cssText

attribute.

**See Also:** Constant Field Values

---

#### CSS_UNKNOWN

static final short CSS_UNKNOWN

The value is not a recognized CSS2 value. The value can only be
obtained by using the

cssText

attribute.

CSS_NUMBER

```java
static final short CSS_NUMBER
```

The value is a simple number. The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_NUMBER

static final short CSS_NUMBER

The value is a simple number. The value can be obtained by using the

getFloatValue

method.

CSS_PERCENTAGE

```java
static final short CSS_PERCENTAGE
```

The value is a percentage. The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_PERCENTAGE

static final short CSS_PERCENTAGE

The value is a percentage. The value can be obtained by using the

getFloatValue

method.

CSS_EMS

```java
static final short CSS_EMS
```

The value is a length (ems). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_EMS

static final short CSS_EMS

The value is a length (ems). The value can be obtained by using the

getFloatValue

method.

CSS_EXS

```java
static final short CSS_EXS
```

The value is a length (exs). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_EXS

static final short CSS_EXS

The value is a length (exs). The value can be obtained by using the

getFloatValue

method.

CSS_PX

```java
static final short CSS_PX
```

The value is a length (px). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_PX

static final short CSS_PX

The value is a length (px). The value can be obtained by using the

getFloatValue

method.

CSS_CM

```java
static final short CSS_CM
```

The value is a length (cm). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_CM

static final short CSS_CM

The value is a length (cm). The value can be obtained by using the

getFloatValue

method.

CSS_MM

```java
static final short CSS_MM
```

The value is a length (mm). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_MM

static final short CSS_MM

The value is a length (mm). The value can be obtained by using the

getFloatValue

method.

CSS_IN

```java
static final short CSS_IN
```

The value is a length (in). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_IN

static final short CSS_IN

The value is a length (in). The value can be obtained by using the

getFloatValue

method.

CSS_PT

```java
static final short CSS_PT
```

The value is a length (pt). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_PT

static final short CSS_PT

The value is a length (pt). The value can be obtained by using the

getFloatValue

method.

CSS_PC

```java
static final short CSS_PC
```

The value is a length (pc). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_PC

static final short CSS_PC

The value is a length (pc). The value can be obtained by using the

getFloatValue

method.

CSS_DEG

```java
static final short CSS_DEG
```

The value is an angle (deg). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_DEG

static final short CSS_DEG

The value is an angle (deg). The value can be obtained by using the

getFloatValue

method.

CSS_RAD

```java
static final short CSS_RAD
```

The value is an angle (rad). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_RAD

static final short CSS_RAD

The value is an angle (rad). The value can be obtained by using the

getFloatValue

method.

CSS_GRAD

```java
static final short CSS_GRAD
```

The value is an angle (grad). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_GRAD

static final short CSS_GRAD

The value is an angle (grad). The value can be obtained by using the

getFloatValue

method.

CSS_MS

```java
static final short CSS_MS
```

The value is a time (ms). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_MS

static final short CSS_MS

The value is a time (ms). The value can be obtained by using the

getFloatValue

method.

CSS_S

```java
static final short CSS_S
```

The value is a time (s). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_S

static final short CSS_S

The value is a time (s). The value can be obtained by using the

getFloatValue

method.

CSS_HZ

```java
static final short CSS_HZ
```

The value is a frequency (Hz). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_HZ

static final short CSS_HZ

The value is a frequency (Hz). The value can be obtained by using the

getFloatValue

method.

CSS_KHZ

```java
static final short CSS_KHZ
```

The value is a frequency (kHz). The value can be obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_KHZ

static final short CSS_KHZ

The value is a frequency (kHz). The value can be obtained by using the

getFloatValue

method.

CSS_DIMENSION

```java
static final short CSS_DIMENSION
```

The value is a number with an unknown dimension. The value can be
obtained by using the

getFloatValue

method.

**See Also:** Constant Field Values

---

#### CSS_DIMENSION

static final short CSS_DIMENSION

The value is a number with an unknown dimension. The value can be
obtained by using the

getFloatValue

method.

CSS_STRING

```java
static final short CSS_STRING
```

The value is a STRING. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

---

#### CSS_STRING

static final short CSS_STRING

The value is a STRING. The value can be obtained by using the

getStringValue

method.

CSS_URI

```java
static final short CSS_URI
```

The value is a URI. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

---

#### CSS_URI

static final short CSS_URI

The value is a URI. The value can be obtained by using the

getStringValue

method.

CSS_IDENT

```java
static final short CSS_IDENT
```

The value is an identifier. The value can be obtained by using the

getStringValue

method.

**See Also:** Constant Field Values

---

#### CSS_IDENT

static final short CSS_IDENT

The value is an identifier. The value can be obtained by using the

getStringValue

method.

CSS_ATTR

```java
static final short CSS_ATTR
```

The value is a attribute function. The value can be obtained by using
the

getStringValue

method.

**See Also:** Constant Field Values

---

#### CSS_ATTR

static final short CSS_ATTR

The value is a attribute function. The value can be obtained by using
the

getStringValue

method.

CSS_COUNTER

```java
static final short CSS_COUNTER
```

The value is a counter or counters function. The value can be obtained
by using the

getCounterValue

method.

**See Also:** Constant Field Values

---

#### CSS_COUNTER

static final short CSS_COUNTER

The value is a counter or counters function. The value can be obtained
by using the

getCounterValue

method.

CSS_RECT

```java
static final short CSS_RECT
```

The value is a rect function. The value can be obtained by using the

getRectValue

method.

**See Also:** Constant Field Values

---

#### CSS_RECT

static final short CSS_RECT

The value is a rect function. The value can be obtained by using the

getRectValue

method.

CSS_RGBCOLOR

```java
static final short CSS_RGBCOLOR
```

The value is a RGB color. The value can be obtained by using the

getRGBColorValue

method.

**See Also:** Constant Field Values

---

#### CSS_RGBCOLOR

static final short CSS_RGBCOLOR

The value is a RGB color. The value can be obtained by using the

getRGBColorValue

method.

Method Detail

- getPrimitiveType

```java
short getPrimitiveType()
```

The type of the value as defined by the constants specified above.

- setFloatValue

```java
void setFloatValue​(short unitType,
float floatValue)
throws
DOMException
```

A method to set the float value with a specified unit. If the property
attached with this value can not accept the specified unit or the
float value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:** unitType

- A unit code as defined above. The unit code can only
be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
**Parameters:** floatValue

- The new float value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the attached property doesn't support
the float value or the unit type.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFloatValue

```java
float getFloatValue​(short unitType)
throws
DOMException
```

This method is used to get a float value in a specified unit. If this
CSS value doesn't contain a float value or can't be converted into
the specified unit, a

DOMException

is raised.

**Parameters:** unitType

- A unit code to get the float value. The unit code can
only be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
**Returns:** The float value in the specified unit.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a float
value or if the float value can't be converted into the specified
unit.

- setStringValue

```java
void setStringValue​(short stringType,

String
stringValue)
throws
DOMException
```

A method to set the string value with the specified unit. If the
property attached to this value can't accept the specified unit or
the string value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:** stringType

- A string code as defined above. The string code can
only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

, and

CSS_ATTR

).
**Parameters:** stringValue

- The new string value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value or if the string value can't be converted into the specified
unit.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getStringValue

```java
String
getStringValue()
throws
DOMException
```

This method is used to get the string value. If the CSS value doesn't
contain a string value, a

DOMException

is raised. Some
properties (like 'font-family' or 'voice-family') convert a
whitespace separated list of idents to a string.

**Returns:** The string value in the current unit. The current

primitiveType

can only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

and

CSS_ATTR

).
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value.

- getCounterValue

```java
Counter
getCounterValue()
throws
DOMException
```

This method is used to get the Counter value. If this CSS value
doesn't contain a counter value, a

DOMException

is
raised. Modification to the corresponding style property can be
achieved using the

Counter

interface.

**Returns:** The Counter value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a
Counter value (e.g. this is not

CSS_COUNTER

).

- getRectValue

```java
Rect
getRectValue()
throws
DOMException
```

This method is used to get the Rect value. If this CSS value doesn't
contain a rect value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

Rect

interface.

**Returns:** The Rect value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a Rect
value. (e.g. this is not

CSS_RECT

).

- getRGBColorValue

```java
RGBColor
getRGBColorValue()
throws
DOMException
```

This method is used to get the RGB color. If this CSS value doesn't
contain a RGB color value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

RGBColor

interface.

**Returns:** the RGB color value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the attached property can't return a
RGB color value (e.g. this is not

CSS_RGBCOLOR

).

---

#### Method Detail

getPrimitiveType

```java
short getPrimitiveType()
```

The type of the value as defined by the constants specified above.

---

#### getPrimitiveType

short getPrimitiveType()

The type of the value as defined by the constants specified above.

setFloatValue

```java
void setFloatValue​(short unitType,
float floatValue)
throws
DOMException
```

A method to set the float value with a specified unit. If the property
attached with this value can not accept the specified unit or the
float value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:** unitType

- A unit code as defined above. The unit code can only
be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
**Parameters:** floatValue

- The new float value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the attached property doesn't support
the float value or the unit type.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFloatValue

void setFloatValue​(short unitType,
float floatValue)
throws

DOMException

A method to set the float value with a specified unit. If the property
attached with this value can not accept the specified unit or the
float value, the value will be unchanged and a

DOMException

will be raised.

getFloatValue

```java
float getFloatValue​(short unitType)
throws
DOMException
```

This method is used to get a float value in a specified unit. If this
CSS value doesn't contain a float value or can't be converted into
the specified unit, a

DOMException

is raised.

**Parameters:** unitType

- A unit code to get the float value. The unit code can
only be a float unit type (i.e.

CSS_NUMBER

,

CSS_PERCENTAGE

,

CSS_EMS

,

CSS_EXS

,

CSS_PX

,

CSS_CM

,

CSS_MM

,

CSS_IN

,

CSS_PT

,

CSS_PC

,

CSS_DEG

,

CSS_RAD

,

CSS_GRAD

,

CSS_MS

,

CSS_S

,

CSS_HZ

,

CSS_KHZ

,

CSS_DIMENSION

).
**Returns:** The float value in the specified unit.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a float
value or if the float value can't be converted into the specified
unit.

---

#### getFloatValue

float getFloatValue​(short unitType)
throws

DOMException

This method is used to get a float value in a specified unit. If this
CSS value doesn't contain a float value or can't be converted into
the specified unit, a

DOMException

is raised.

setStringValue

```java
void setStringValue​(short stringType,

String
stringValue)
throws
DOMException
```

A method to set the string value with the specified unit. If the
property attached to this value can't accept the specified unit or
the string value, the value will be unchanged and a

DOMException

will be raised.

**Parameters:** stringType

- A string code as defined above. The string code can
only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

, and

CSS_ATTR

).
**Parameters:** stringValue

- The new string value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value or if the string value can't be converted into the specified
unit.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setStringValue

void setStringValue​(short stringType,

String

stringValue)
throws

DOMException

A method to set the string value with the specified unit. If the
property attached to this value can't accept the specified unit or
the string value, the value will be unchanged and a

DOMException

will be raised.

getStringValue

```java
String
getStringValue()
throws
DOMException
```

This method is used to get the string value. If the CSS value doesn't
contain a string value, a

DOMException

is raised. Some
properties (like 'font-family' or 'voice-family') convert a
whitespace separated list of idents to a string.

**Returns:** The string value in the current unit. The current

primitiveType

can only be a string unit type (i.e.

CSS_STRING

,

CSS_URI

,

CSS_IDENT

and

CSS_ATTR

).
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a string
value.

---

#### getStringValue

String

getStringValue()
throws

DOMException

This method is used to get the string value. If the CSS value doesn't
contain a string value, a

DOMException

is raised. Some
properties (like 'font-family' or 'voice-family') convert a
whitespace separated list of idents to a string.

getCounterValue

```java
Counter
getCounterValue()
throws
DOMException
```

This method is used to get the Counter value. If this CSS value
doesn't contain a counter value, a

DOMException

is
raised. Modification to the corresponding style property can be
achieved using the

Counter

interface.

**Returns:** The Counter value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a
Counter value (e.g. this is not

CSS_COUNTER

).

---

#### getCounterValue

Counter

getCounterValue()
throws

DOMException

This method is used to get the Counter value. If this CSS value
doesn't contain a counter value, a

DOMException

is
raised. Modification to the corresponding style property can be
achieved using the

Counter

interface.

getRectValue

```java
Rect
getRectValue()
throws
DOMException
```

This method is used to get the Rect value. If this CSS value doesn't
contain a rect value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

Rect

interface.

**Returns:** The Rect value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the CSS value doesn't contain a Rect
value. (e.g. this is not

CSS_RECT

).

---

#### getRectValue

Rect

getRectValue()
throws

DOMException

This method is used to get the Rect value. If this CSS value doesn't
contain a rect value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

Rect

interface.

getRGBColorValue

```java
RGBColor
getRGBColorValue()
throws
DOMException
```

This method is used to get the RGB color. If this CSS value doesn't
contain a RGB color value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

RGBColor

interface.

**Returns:** the RGB color value.
**Throws:** DOMException

- INVALID_ACCESS_ERR: Raised if the attached property can't return a
RGB color value (e.g. this is not

CSS_RGBCOLOR

).

---

#### getRGBColorValue

RGBColor

getRGBColorValue()
throws

DOMException

This method is used to get the RGB color. If this CSS value doesn't
contain a RGB color value, a

DOMException

is raised.
Modification to the corresponding style property can be achieved
using the

RGBColor

interface.

---

