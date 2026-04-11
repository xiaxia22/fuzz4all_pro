# Class StyleSheet.BoxPainter

**Source:** `java.desktop\javax\swing\text\html\StyleSheet.BoxPainter.html`

### Class Description

```java
public static class
StyleSheet.BoxPainter

extends
Object

implements
Serializable
```

Class to carry out some of the duties of
CSS formatting. Implementations of this
class enable views to present the CSS formatting
while not knowing anything about how the CSS values
are being cached.

As a delegate of Views, this object is responsible for
the insets of a View and making sure the background
is maintained according to the CSS attributes.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public float getInset​(int side,

View
v)

Fetches the inset needed on a given side to
account for the margin, border, and padding.

**Parameters:**
- side

- The size of the box to fetch the
inset for. This can be View.TOP,
View.LEFT, View.BOTTOM, or View.RIGHT.
- v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.

**Returns:**
- the inset needed for the margin, border and padding.

**Throws:**
- IllegalArgumentException

- for an invalid direction

---

#### public void paint​(
Graphics
g,
float x,
float y,
float w,
float h,

View
v)

Paints the CSS box according to the attributes
given. This should paint the border, padding,
and background.

**Parameters:**
- g

- the rendering surface.
- x

- the x coordinate of the allocated area to
render into.
- y

- the y coordinate of the allocated area to
render into.
- w

- the width of the allocated area to render into.
- h

- the height of the allocated area to render into.
- v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.

---

### Additional Sections

#### Class StyleSheet.BoxPainter

java.lang.Object

- javax.swing.text.html.StyleSheet.BoxPainter

javax.swing.text.html.StyleSheet.BoxPainter

**All Implemented Interfaces:** Serializable

**Enclosing class:** StyleSheet

```java
public static class
StyleSheet.BoxPainter

extends
Object

implements
Serializable
```

Class to carry out some of the duties of
CSS formatting. Implementations of this
class enable views to present the CSS formatting
while not knowing anything about how the CSS values
are being cached.

As a delegate of Views, this object is responsible for
the insets of a View and making sure the background
is maintained according to the CSS attributes.

**See Also:** Serialized Form

public static class

StyleSheet.BoxPainter

extends

Object

implements

Serializable

Class to carry out some of the duties of
CSS formatting. Implementations of this
class enable views to present the CSS formatting
while not knowing anything about how the CSS values
are being cached.

As a delegate of Views, this object is responsible for
the insets of a View and making sure the background
is maintained according to the CSS attributes.

As a delegate of Views, this object is responsible for
the insets of a View and making sure the background
is maintained according to the CSS attributes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getInset

​(int side,

View

v)

Fetches the inset needed on a given side to
account for the margin, border, and padding.

void

paint

​(

Graphics

g,
float x,
float y,
float w,
float h,

View

v)

Paints the CSS box according to the attributes
given.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

float

getInset

​(int side,

View

v)

Fetches the inset needed on a given side to
account for the margin, border, and padding.

void

paint

​(

Graphics

g,
float x,
float y,
float w,
float h,

View

v)

Paints the CSS box according to the attributes
given.

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

Fetches the inset needed on a given side to
account for the margin, border, and padding.

Paints the CSS box according to the attributes
given.

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

============ METHOD DETAIL ==========

- Method Detail

- getInset

```java
public float getInset​(int side,

View
v)
```

Fetches the inset needed on a given side to
account for the margin, border, and padding.

**Parameters:** side

- The size of the box to fetch the
inset for. This can be View.TOP,
View.LEFT, View.BOTTOM, or View.RIGHT.
**Parameters:** v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.
**Returns:** the inset needed for the margin, border and padding.
**Throws:** IllegalArgumentException

- for an invalid direction

- paint

```java
public void paint​(
Graphics
g,
float x,
float y,
float w,
float h,

View
v)
```

Paints the CSS box according to the attributes
given. This should paint the border, padding,
and background.

**Parameters:** g

- the rendering surface.
**Parameters:** x

- the x coordinate of the allocated area to
render into.
**Parameters:** y

- the y coordinate of the allocated area to
render into.
**Parameters:** w

- the width of the allocated area to render into.
**Parameters:** h

- the height of the allocated area to render into.
**Parameters:** v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.

Method Detail

- getInset

```java
public float getInset​(int side,

View
v)
```

Fetches the inset needed on a given side to
account for the margin, border, and padding.

**Parameters:** side

- The size of the box to fetch the
inset for. This can be View.TOP,
View.LEFT, View.BOTTOM, or View.RIGHT.
**Parameters:** v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.
**Returns:** the inset needed for the margin, border and padding.
**Throws:** IllegalArgumentException

- for an invalid direction

- paint

```java
public void paint​(
Graphics
g,
float x,
float y,
float w,
float h,

View
v)
```

Paints the CSS box according to the attributes
given. This should paint the border, padding,
and background.

**Parameters:** g

- the rendering surface.
**Parameters:** x

- the x coordinate of the allocated area to
render into.
**Parameters:** y

- the y coordinate of the allocated area to
render into.
**Parameters:** w

- the width of the allocated area to render into.
**Parameters:** h

- the height of the allocated area to render into.
**Parameters:** v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.

---

#### Method Detail

getInset

```java
public float getInset​(int side,

View
v)
```

Fetches the inset needed on a given side to
account for the margin, border, and padding.

**Parameters:** side

- The size of the box to fetch the
inset for. This can be View.TOP,
View.LEFT, View.BOTTOM, or View.RIGHT.
**Parameters:** v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.
**Returns:** the inset needed for the margin, border and padding.
**Throws:** IllegalArgumentException

- for an invalid direction

---

#### getInset

public float getInset​(int side,

View

v)

Fetches the inset needed on a given side to
account for the margin, border, and padding.

paint

```java
public void paint​(
Graphics
g,
float x,
float y,
float w,
float h,

View
v)
```

Paints the CSS box according to the attributes
given. This should paint the border, padding,
and background.

**Parameters:** g

- the rendering surface.
**Parameters:** x

- the x coordinate of the allocated area to
render into.
**Parameters:** y

- the y coordinate of the allocated area to
render into.
**Parameters:** w

- the width of the allocated area to render into.
**Parameters:** h

- the height of the allocated area to render into.
**Parameters:** v

- the view making the request. This is
used to get the AttributeSet, and may be used to
resolve percentage arguments.

---

#### paint

public void paint​(

Graphics

g,
float x,
float y,
float w,
float h,

View

v)

Paints the CSS box according to the attributes
given. This should paint the border, padding,
and background.

---

