# Interface TabExpander

**Source:** `java.desktop\javax\swing\text\TabExpander.html`

### Class Description

```java
public interface
TabExpander
```

Simple interface to allow for different types of
implementations of tab expansion.

**All Known Implementing Classes:** FieldView

,

ParagraphView

,

ParagraphView

,

PasswordView

,

PlainView

,

WrappedPlainView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### float nextTabStop​(float x,
int tabOffset)

Returns the next tab stop position given a reference
position. Values are expressed in points.

**Parameters:**
- x

- the position in points >= 0
- tabOffset

- the position within the text stream
that the tab occurred at >= 0.

**Returns:**
- the next tab stop >= 0

---

### Additional Sections

#### Interface TabExpander

**All Known Implementing Classes:** FieldView

,

ParagraphView

,

ParagraphView

,

PasswordView

,

PlainView

,

WrappedPlainView

```java
public interface
TabExpander
```

Simple interface to allow for different types of
implementations of tab expansion.

public interface

TabExpander

Simple interface to allow for different types of
implementations of tab expansion.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

float

nextTabStop

​(float x,
int tabOffset)

Returns the next tab stop position given a reference
position.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

float

nextTabStop

​(float x,
int tabOffset)

Returns the next tab stop position given a reference
position.

---

#### Method Summary

Returns the next tab stop position given a reference
position.

============ METHOD DETAIL ==========

- Method Detail

- nextTabStop

```java
float nextTabStop​(float x,
int tabOffset)
```

Returns the next tab stop position given a reference
position. Values are expressed in points.

**Parameters:** x

- the position in points >= 0
**Parameters:** tabOffset

- the position within the text stream
that the tab occurred at >= 0.
**Returns:** the next tab stop >= 0

Method Detail

- nextTabStop

```java
float nextTabStop​(float x,
int tabOffset)
```

Returns the next tab stop position given a reference
position. Values are expressed in points.

**Parameters:** x

- the position in points >= 0
**Parameters:** tabOffset

- the position within the text stream
that the tab occurred at >= 0.
**Returns:** the next tab stop >= 0

---

#### Method Detail

nextTabStop

```java
float nextTabStop​(float x,
int tabOffset)
```

Returns the next tab stop position given a reference
position. Values are expressed in points.

**Parameters:** x

- the position in points >= 0
**Parameters:** tabOffset

- the position within the text stream
that the tab occurred at >= 0.
**Returns:** the next tab stop >= 0

---

#### nextTabStop

float nextTabStop​(float x,
int tabOffset)

Returns the next tab stop position given a reference
position. Values are expressed in points.

---

