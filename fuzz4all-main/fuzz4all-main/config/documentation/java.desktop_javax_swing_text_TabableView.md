# Interface TabableView

**Source:** `java.desktop\javax\swing\text\TabableView.html`

### Class Description

```java
public interface
TabableView
```

Interface for

View

s that have size dependent upon tabs.

**All Known Implementing Classes:** GlyphView

,

InlineView

,

LabelView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### float getTabbedSpan​(float x,

TabExpander
e)

Determines the desired span when using the given
tab expansion implementation. If a container
calls this method, it will do so prior to the
normal layout which would call getPreferredSpan.
A view implementing this should give the same
result in any subsequent calls to getPreferredSpan
along the axis of tab expansion.

**Parameters:**
- x

- the position the view would be located
at for the purpose of tab expansion >= 0.
- e

- how to expand the tabs when encountered.

**Returns:**
- the desired span >= 0

---

#### float getPartialSpan​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

**Parameters:**
- p0

- the starting location in the text document >= 0
- p1

- the ending location in the text document >= p0

**Returns:**
- the span >= 0

---

### Additional Sections

#### Interface TabableView

**All Known Implementing Classes:** GlyphView

,

InlineView

,

LabelView

```java
public interface
TabableView
```

Interface for

View

s that have size dependent upon tabs.

**See Also:** TabExpander

,

LabelView

,

ParagraphView

public interface

TabableView

Interface for

View

s that have size dependent upon tabs.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

float

getPartialSpan

​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view.

float

getTabbedSpan

​(float x,

TabExpander

e)

Determines the desired span when using the given
tab expansion implementation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

float

getPartialSpan

​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view.

float

getTabbedSpan

​(float x,

TabExpander

e)

Determines the desired span when using the given
tab expansion implementation.

---

#### Method Summary

Determines the span along the same axis as tab
expansion for a portion of the view.

Determines the desired span when using the given
tab expansion implementation.

============ METHOD DETAIL ==========

- Method Detail

- getTabbedSpan

```java
float getTabbedSpan​(float x,

TabExpander
e)
```

Determines the desired span when using the given
tab expansion implementation. If a container
calls this method, it will do so prior to the
normal layout which would call getPreferredSpan.
A view implementing this should give the same
result in any subsequent calls to getPreferredSpan
along the axis of tab expansion.

**Parameters:** x

- the position the view would be located
at for the purpose of tab expansion >= 0.
**Parameters:** e

- how to expand the tabs when encountered.
**Returns:** the desired span >= 0

- getPartialSpan

```java
float getPartialSpan​(int p0,
int p1)
```

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

**Parameters:** p0

- the starting location in the text document >= 0
**Parameters:** p1

- the ending location in the text document >= p0
**Returns:** the span >= 0

Method Detail

- getTabbedSpan

```java
float getTabbedSpan​(float x,

TabExpander
e)
```

Determines the desired span when using the given
tab expansion implementation. If a container
calls this method, it will do so prior to the
normal layout which would call getPreferredSpan.
A view implementing this should give the same
result in any subsequent calls to getPreferredSpan
along the axis of tab expansion.

**Parameters:** x

- the position the view would be located
at for the purpose of tab expansion >= 0.
**Parameters:** e

- how to expand the tabs when encountered.
**Returns:** the desired span >= 0

- getPartialSpan

```java
float getPartialSpan​(int p0,
int p1)
```

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

**Parameters:** p0

- the starting location in the text document >= 0
**Parameters:** p1

- the ending location in the text document >= p0
**Returns:** the span >= 0

---

#### Method Detail

getTabbedSpan

```java
float getTabbedSpan​(float x,

TabExpander
e)
```

Determines the desired span when using the given
tab expansion implementation. If a container
calls this method, it will do so prior to the
normal layout which would call getPreferredSpan.
A view implementing this should give the same
result in any subsequent calls to getPreferredSpan
along the axis of tab expansion.

**Parameters:** x

- the position the view would be located
at for the purpose of tab expansion >= 0.
**Parameters:** e

- how to expand the tabs when encountered.
**Returns:** the desired span >= 0

---

#### getTabbedSpan

float getTabbedSpan​(float x,

TabExpander

e)

Determines the desired span when using the given
tab expansion implementation. If a container
calls this method, it will do so prior to the
normal layout which would call getPreferredSpan.
A view implementing this should give the same
result in any subsequent calls to getPreferredSpan
along the axis of tab expansion.

getPartialSpan

```java
float getPartialSpan​(int p0,
int p1)
```

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

**Parameters:** p0

- the starting location in the text document >= 0
**Parameters:** p1

- the ending location in the text document >= p0
**Returns:** the span >= 0

---

#### getPartialSpan

float getPartialSpan​(int p0,
int p1)

Determines the span along the same axis as tab
expansion for a portion of the view. This is
intended for use by the TabExpander for cases
where the tab expansion involves aligning the
portion of text that doesn't have whitespace
relative to the tab stop. There is therefore
an assumption that the range given does not
contain tabs.

---

