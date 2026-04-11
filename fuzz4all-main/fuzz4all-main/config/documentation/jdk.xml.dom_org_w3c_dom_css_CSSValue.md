# Interface CSSValue

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSValue.html`

### Class Description

```java
public interface
CSSValue
```

The

CSSValue

interface represents a simple or a complex
value. A

CSSValue

object only occurs in a context of a CSS
property.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Known Subinterfaces:** CSSPrimitiveValue

,

CSSValueList

---

### Field Details

#### static final short CSS_INHERIT

The value is inherited and the

cssText

contains "inherit".

**See Also:**
- Constant Field Values

---

#### static final short CSS_PRIMITIVE_VALUE

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:**
- Constant Field Values

---

#### static final short CSS_VALUE_LIST

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:**
- Constant Field Values

---

#### static final short CSS_CUSTOM

The value is a custom value.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getCssText()

A string representation of the current value.

---

#### void setCssText​(
String
cssText)
throws
DOMException

A string representation of the current value.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error (according to the attached property) or is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of values than the values allowed
by the CSS property.

NO_MODIFICATION_ALLOWED_ERR: Raised if this value is readonly.

---

#### short getCssValueType()

A code defining the type of the value as defined above.

---

### Additional Sections

#### Interface CSSValue

**All Known Subinterfaces:** CSSPrimitiveValue

,

CSSValueList

```java
public interface
CSSValue
```

The

CSSValue

interface represents a simple or a complex
value. A

CSSValue

object only occurs in a context of a CSS
property.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSValue

The

CSSValue

interface represents a simple or a complex
value. A

CSSValue

object only occurs in a context of a CSS
property.

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

CSS_CUSTOM

The value is a custom value.

static short

CSS_INHERIT

The value is inherited and the

cssText

contains "inherit".

static short

CSS_PRIMITIVE_VALUE

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

static short

CSS_VALUE_LIST

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCssText

()

A string representation of the current value.

short

getCssValueType

()

A code defining the type of the value as defined above.

void

setCssText

​(

String

cssText)

A string representation of the current value.

Field Summary

Fields

Modifier and Type

Field

Description

static short

CSS_CUSTOM

The value is a custom value.

static short

CSS_INHERIT

The value is inherited and the

cssText

contains "inherit".

static short

CSS_PRIMITIVE_VALUE

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

static short

CSS_VALUE_LIST

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

---

#### Field Summary

The value is a custom value.

The value is inherited and the

cssText

contains "inherit".

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCssText

()

A string representation of the current value.

short

getCssValueType

()

A code defining the type of the value as defined above.

void

setCssText

​(

String

cssText)

A string representation of the current value.

---

#### Method Summary

A string representation of the current value.

A code defining the type of the value as defined above.

============ FIELD DETAIL ===========

- Field Detail

- CSS_INHERIT

```java
static final short CSS_INHERIT
```

The value is inherited and the

cssText

contains "inherit".

**See Also:** Constant Field Values

- CSS_PRIMITIVE_VALUE

```java
static final short CSS_PRIMITIVE_VALUE
```

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:** Constant Field Values

- CSS_VALUE_LIST

```java
static final short CSS_VALUE_LIST
```

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:** Constant Field Values

- CSS_CUSTOM

```java
static final short CSS_CUSTOM
```

The value is a custom value.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getCssText

```java
String
getCssText()
```

A string representation of the current value.

- setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

A string representation of the current value.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error (according to the attached property) or is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of values than the values allowed
by the CSS property.

NO_MODIFICATION_ALLOWED_ERR: Raised if this value is readonly.

- getCssValueType

```java
short getCssValueType()
```

A code defining the type of the value as defined above.

Field Detail

- CSS_INHERIT

```java
static final short CSS_INHERIT
```

The value is inherited and the

cssText

contains "inherit".

**See Also:** Constant Field Values

- CSS_PRIMITIVE_VALUE

```java
static final short CSS_PRIMITIVE_VALUE
```

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:** Constant Field Values

- CSS_VALUE_LIST

```java
static final short CSS_VALUE_LIST
```

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:** Constant Field Values

- CSS_CUSTOM

```java
static final short CSS_CUSTOM
```

The value is a custom value.

**See Also:** Constant Field Values

---

#### Field Detail

CSS_INHERIT

```java
static final short CSS_INHERIT
```

The value is inherited and the

cssText

contains "inherit".

**See Also:** Constant Field Values

---

#### CSS_INHERIT

static final short CSS_INHERIT

The value is inherited and the

cssText

contains "inherit".

CSS_PRIMITIVE_VALUE

```java
static final short CSS_PRIMITIVE_VALUE
```

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:** Constant Field Values

---

#### CSS_PRIMITIVE_VALUE

static final short CSS_PRIMITIVE_VALUE

The value is a primitive value and an instance of the

CSSPrimitiveValue

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

CSS_VALUE_LIST

```java
static final short CSS_VALUE_LIST
```

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

**See Also:** Constant Field Values

---

#### CSS_VALUE_LIST

static final short CSS_VALUE_LIST

The value is a

CSSValue

list and an instance of the

CSSValueList

interface can be obtained by using
binding-specific casting methods on this instance of the

CSSValue

interface.

CSS_CUSTOM

```java
static final short CSS_CUSTOM
```

The value is a custom value.

**See Also:** Constant Field Values

---

#### CSS_CUSTOM

static final short CSS_CUSTOM

The value is a custom value.

Method Detail

- getCssText

```java
String
getCssText()
```

A string representation of the current value.

- setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

A string representation of the current value.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error (according to the attached property) or is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of values than the values allowed
by the CSS property.

NO_MODIFICATION_ALLOWED_ERR: Raised if this value is readonly.

- getCssValueType

```java
short getCssValueType()
```

A code defining the type of the value as defined above.

---

#### Method Detail

getCssText

```java
String
getCssText()
```

A string representation of the current value.

---

#### getCssText

String

getCssText()

A string representation of the current value.

setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

A string representation of the current value.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error (according to the attached property) or is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of values than the values allowed
by the CSS property.

NO_MODIFICATION_ALLOWED_ERR: Raised if this value is readonly.

---

#### setCssText

void setCssText​(

String

cssText)
throws

DOMException

A string representation of the current value.

getCssValueType

```java
short getCssValueType()
```

A code defining the type of the value as defined above.

---

#### getCssValueType

short getCssValueType()

A code defining the type of the value as defined above.

---

