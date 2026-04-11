# Class BasicGraphicsUtils

**Source:** `java.desktop\javax\swing\plaf\basic\BasicGraphicsUtils.html`

### Class Description

```java
public class
BasicGraphicsUtils

extends
Object
```

Convenient util class.

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicGraphicsUtils()

*No description found.*

---

### Method Details

#### public static void drawEtchedRect​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)

Draws an etched rectangle.

**Parameters:**
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- shadow

- a color of shadow
- darkShadow

- a color of dark shadow
- highlight

- a color highlighting
- lightHighlight

- a color of light highlighting

---

#### public static
Insets
getEtchedInsets()

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

**Returns:**
- the inset of an etched rect

---

#### public static void drawGroove​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
highlight)

Draws a groove.

**Parameters:**
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- shadow

- a color of shadow
- highlight

- a color highlighting

---

#### public static
Insets
getGrooveInsets()

Returns the amount of space taken up by a border drawn by

drawGroove()

**Returns:**
- the inset of a groove border

---

#### public static void drawBezel​(
Graphics
g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)

Draws a bezel.

**Parameters:**
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- isPressed

- is component pressed
- isDefault

- is default drawing
- shadow

- a color of shadow
- darkShadow

- a color of dark shadow
- highlight

- a color highlighting
- lightHighlight

- a color of light highlighting

---

#### public static void drawLoweredBezel​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)

Draws a lowered bezel.

**Parameters:**
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- shadow

- a color of shadow
- darkShadow

- a color of dark shadow
- highlight

- a color highlighting
- lightHighlight

- a color of light highlighting

---

#### public static void drawString​(
Graphics
g,

String
text,
int underlinedChar,
int x,
int y)

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would. The first occurrence
of

underlineChar

in text will be underlined.
The matching algorithm is not case sensitive.

**Parameters:**
- g

- an instance of

Graphics
- text

- a text
- underlinedChar

- an underlined char
- x

- an X coordinate
- y

- an Y coordinate

---

#### public static void drawStringUnderlineCharAt​(
Graphics
g,

String
text,
int underlinedIndex,
int x,
int y)

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.
The character at index

underlinedIndex

in text will be underlined. If

index

is beyond the
bounds of

text

(including < 0), nothing will be
underlined.

**Parameters:**
- g

- Graphics to draw with
- text

- String to draw
- underlinedIndex

- Index of character in text to underline
- x

- x coordinate to draw at
- y

- y coordinate to draw at

**Since:**
- 1.4

---

#### public static void drawDashedRect​(
Graphics
g,
int x,
int y,
int width,
int height)

Draws dashed rectangle.

**Parameters:**
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- width

- a width of rectangle
- height

- a height of rectangle

---

#### public static
Dimension
getPreferredButtonSize​(
AbstractButton
b,
int textIconGap)

Returns the preferred size of the button.

**Parameters:**
- b

- an instance of

AbstractButton
- textIconGap

- a gap between text and icon

**Returns:**
- the preferred size of the button

---

#### public static void drawString​(
JComponent
c,

Graphics2D
g,

String
string,
float x,
float y)

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.
Nothing is drawn for the null string.

**Parameters:**
- c

- the component that will display the string, may be null
- g

- the graphics context, must not be null
- string

- the string to display, may be null
- x

- the x coordinate to draw the text at
- y

- the y coordinate to draw the text at

**Throws:**
- NullPointerException

- if the specified

g

is

null

**Since:**
- 9

---

#### public static void drawStringUnderlineCharAt​(
JComponent
c,

Graphics2D
g,

String
string,
int underlinedIndex,
float x,
float y)

Draws the given string at the specified location underlining
the specified character. The provided component is used to query text
properties and anti-aliasing hints.

The

underlinedIndex

parameter points to a char value
(Unicode code unit) in the given string.
If the char value specified at the underlined index is in
the high-surrogate range and the char value at the following index is in
the low-surrogate range then the supplementary character corresponding
to this surrogate pair is underlined.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

**Parameters:**
- c

- the component that will display the string, may be null
- g

- the graphics context, must not be null
- string

- the string to display, may be null
- underlinedIndex

- index of a a char value (Unicode code unit)
in the string to underline
- x

- the x coordinate to draw the text at
- y

- the y coordinate to draw the text at

**Throws:**
- NullPointerException

- if the specified

g

is

null

**See Also:**
- getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

**Since:**
- 9

---

#### public static
String
getClippedString​(
JComponent
c,

FontMetrics
fm,

String
string,
int availTextWidth)

Clips the passed in string to the space provided.
The provided component is used to query text properties and anti-aliasing hints.
The unchanged string is returned if the space provided is greater than
the string width.

**Parameters:**
- c

- the component, may be null
- fm

- the FontMetrics used to measure the string width, must be
obtained from the correct font and graphics. Must not be null.
- string

- the string to clip, may be null
- availTextWidth

- the amount of space that the string can be drawn in

**Returns:**
- the clipped string that fits in the provided space, an empty
string if the given string argument is

null

or empty

**Throws:**
- NullPointerException

- if the specified

fm

is

null

**See Also:**
- getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

**Since:**
- 9

---

#### public static float getStringWidth​(
JComponent
c,

FontMetrics
fm,

String
string)

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.
If the passed string is

null

, returns zero.

**Parameters:**
- c

- the component, may be null
- fm

- the FontMetrics used to measure the advance string width, must
be obtained from the correct font and graphics. Must not be null.
- string

- the string to get the advance width of, may be null

**Returns:**
- the advance width of the specified string, zero is returned for

null

string

**Throws:**
- NullPointerException

- if the specified

fm

is

null

**Since:**
- 9

---

### Additional Sections

#### Class BasicGraphicsUtils

java.lang.Object

- javax.swing.plaf.basic.BasicGraphicsUtils

javax.swing.plaf.basic.BasicGraphicsUtils

```java
public class
BasicGraphicsUtils

extends
Object
```

Convenient util class.

public class

BasicGraphicsUtils

extends

Object

Convenient util class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicGraphicsUtils

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

drawBezel

​(

Graphics

g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws a bezel.

static void

drawDashedRect

​(

Graphics

g,
int x,
int y,
int width,
int height)

Draws dashed rectangle.

static void

drawEtchedRect

​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws an etched rectangle.

static void

drawGroove

​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

highlight)

Draws a groove.

static void

drawLoweredBezel

​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws a lowered bezel.

static void

drawString

​(

Graphics

g,

String

text,
int underlinedChar,
int x,
int y)

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would.

static void

drawString

​(

JComponent

c,

Graphics2D

g,

String

string,
float x,
float y)

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.

static void

drawStringUnderlineCharAt

​(

Graphics

g,

String

text,
int underlinedIndex,
int x,
int y)

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.

static void

drawStringUnderlineCharAt

​(

JComponent

c,

Graphics2D

g,

String

string,
int underlinedIndex,
float x,
float y)

Draws the given string at the specified location underlining
the specified character.

static

String

getClippedString

​(

JComponent

c,

FontMetrics

fm,

String

string,
int availTextWidth)

Clips the passed in string to the space provided.

static

Insets

getEtchedInsets

()

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

static

Insets

getGrooveInsets

()

Returns the amount of space taken up by a border drawn by

drawGroove()

static

Dimension

getPreferredButtonSize

​(

AbstractButton

b,
int textIconGap)

Returns the preferred size of the button.

static float

getStringWidth

​(

JComponent

c,

FontMetrics

fm,

String

string)

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.

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

Constructor Summary

Constructors

Constructor

Description

BasicGraphicsUtils

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

drawBezel

​(

Graphics

g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws a bezel.

static void

drawDashedRect

​(

Graphics

g,
int x,
int y,
int width,
int height)

Draws dashed rectangle.

static void

drawEtchedRect

​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws an etched rectangle.

static void

drawGroove

​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

highlight)

Draws a groove.

static void

drawLoweredBezel

​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws a lowered bezel.

static void

drawString

​(

Graphics

g,

String

text,
int underlinedChar,
int x,
int y)

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would.

static void

drawString

​(

JComponent

c,

Graphics2D

g,

String

string,
float x,
float y)

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.

static void

drawStringUnderlineCharAt

​(

Graphics

g,

String

text,
int underlinedIndex,
int x,
int y)

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.

static void

drawStringUnderlineCharAt

​(

JComponent

c,

Graphics2D

g,

String

string,
int underlinedIndex,
float x,
float y)

Draws the given string at the specified location underlining
the specified character.

static

String

getClippedString

​(

JComponent

c,

FontMetrics

fm,

String

string,
int availTextWidth)

Clips the passed in string to the space provided.

static

Insets

getEtchedInsets

()

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

static

Insets

getGrooveInsets

()

Returns the amount of space taken up by a border drawn by

drawGroove()

static

Dimension

getPreferredButtonSize

​(

AbstractButton

b,
int textIconGap)

Returns the preferred size of the button.

static float

getStringWidth

​(

JComponent

c,

FontMetrics

fm,

String

string)

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.

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

Draws a bezel.

Draws dashed rectangle.

Draws an etched rectangle.

Draws a groove.

Draws a lowered bezel.

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would.

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.

Draws the given string at the specified location underlining
the specified character.

Clips the passed in string to the space provided.

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

Returns the amount of space taken up by a border drawn by

drawGroove()

Returns the preferred size of the button.

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicGraphicsUtils

```java
public BasicGraphicsUtils()
```

============ METHOD DETAIL ==========

- Method Detail

- drawEtchedRect

```java
public static void drawEtchedRect​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws an etched rectangle.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

- getEtchedInsets

```java
public static
Insets
getEtchedInsets()
```

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

**Returns:** the inset of an etched rect

- drawGroove

```java
public static void drawGroove​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
highlight)
```

Draws a groove.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** highlight

- a color highlighting

- getGrooveInsets

```java
public static
Insets
getGrooveInsets()
```

Returns the amount of space taken up by a border drawn by

drawGroove()

**Returns:** the inset of a groove border

- drawBezel

```java
public static void drawBezel​(
Graphics
g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws a bezel.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** isPressed

- is component pressed
**Parameters:** isDefault

- is default drawing
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

- drawLoweredBezel

```java
public static void drawLoweredBezel​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws a lowered bezel.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

- drawString

```java
public static void drawString​(
Graphics
g,

String
text,
int underlinedChar,
int x,
int y)
```

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would. The first occurrence
of

underlineChar

in text will be underlined.
The matching algorithm is not case sensitive.

**Parameters:** g

- an instance of

Graphics
**Parameters:** text

- a text
**Parameters:** underlinedChar

- an underlined char
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

- drawStringUnderlineCharAt

```java
public static void drawStringUnderlineCharAt​(
Graphics
g,

String
text,
int underlinedIndex,
int x,
int y)
```

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.
The character at index

underlinedIndex

in text will be underlined. If

index

is beyond the
bounds of

text

(including < 0), nothing will be
underlined.

**Parameters:** g

- Graphics to draw with
**Parameters:** text

- String to draw
**Parameters:** underlinedIndex

- Index of character in text to underline
**Parameters:** x

- x coordinate to draw at
**Parameters:** y

- y coordinate to draw at
**Since:** 1.4

- drawDashedRect

```java
public static void drawDashedRect​(
Graphics
g,
int x,
int y,
int width,
int height)
```

Draws dashed rectangle.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** width

- a width of rectangle
**Parameters:** height

- a height of rectangle

- getPreferredButtonSize

```java
public static
Dimension
getPreferredButtonSize​(
AbstractButton
b,
int textIconGap)
```

Returns the preferred size of the button.

**Parameters:** b

- an instance of

AbstractButton
**Parameters:** textIconGap

- a gap between text and icon
**Returns:** the preferred size of the button

- drawString

```java
public static void drawString​(
JComponent
c,

Graphics2D
g,

String
string,
float x,
float y)
```

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.
Nothing is drawn for the null string.

**Parameters:** c

- the component that will display the string, may be null
**Parameters:** g

- the graphics context, must not be null
**Parameters:** string

- the string to display, may be null
**Parameters:** x

- the x coordinate to draw the text at
**Parameters:** y

- the y coordinate to draw the text at
**Throws:** NullPointerException

- if the specified

g

is

null
**Since:** 9

- drawStringUnderlineCharAt

```java
public static void drawStringUnderlineCharAt​(
JComponent
c,

Graphics2D
g,

String
string,
int underlinedIndex,
float x,
float y)
```

Draws the given string at the specified location underlining
the specified character. The provided component is used to query text
properties and anti-aliasing hints.

The

underlinedIndex

parameter points to a char value
(Unicode code unit) in the given string.
If the char value specified at the underlined index is in
the high-surrogate range and the char value at the following index is in
the low-surrogate range then the supplementary character corresponding
to this surrogate pair is underlined.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

**Parameters:** c

- the component that will display the string, may be null
**Parameters:** g

- the graphics context, must not be null
**Parameters:** string

- the string to display, may be null
**Parameters:** underlinedIndex

- index of a a char value (Unicode code unit)
in the string to underline
**Parameters:** x

- the x coordinate to draw the text at
**Parameters:** y

- the y coordinate to draw the text at
**Throws:** NullPointerException

- if the specified

g

is

null
**Since:** 9
**See Also:** getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

- getClippedString

```java
public static
String
getClippedString​(
JComponent
c,

FontMetrics
fm,

String
string,
int availTextWidth)
```

Clips the passed in string to the space provided.
The provided component is used to query text properties and anti-aliasing hints.
The unchanged string is returned if the space provided is greater than
the string width.

**Parameters:** c

- the component, may be null
**Parameters:** fm

- the FontMetrics used to measure the string width, must be
obtained from the correct font and graphics. Must not be null.
**Parameters:** string

- the string to clip, may be null
**Parameters:** availTextWidth

- the amount of space that the string can be drawn in
**Returns:** the clipped string that fits in the provided space, an empty
string if the given string argument is

null

or empty
**Throws:** NullPointerException

- if the specified

fm

is

null
**Since:** 9
**See Also:** getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

- getStringWidth

```java
public static float getStringWidth​(
JComponent
c,

FontMetrics
fm,

String
string)
```

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.
If the passed string is

null

, returns zero.

**Parameters:** c

- the component, may be null
**Parameters:** fm

- the FontMetrics used to measure the advance string width, must
be obtained from the correct font and graphics. Must not be null.
**Parameters:** string

- the string to get the advance width of, may be null
**Returns:** the advance width of the specified string, zero is returned for

null

string
**Throws:** NullPointerException

- if the specified

fm

is

null
**Since:** 9

Constructor Detail

- BasicGraphicsUtils

```java
public BasicGraphicsUtils()
```

---

#### Constructor Detail

BasicGraphicsUtils

```java
public BasicGraphicsUtils()
```

---

#### BasicGraphicsUtils

public BasicGraphicsUtils()

Method Detail

- drawEtchedRect

```java
public static void drawEtchedRect​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws an etched rectangle.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

- getEtchedInsets

```java
public static
Insets
getEtchedInsets()
```

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

**Returns:** the inset of an etched rect

- drawGroove

```java
public static void drawGroove​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
highlight)
```

Draws a groove.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** highlight

- a color highlighting

- getGrooveInsets

```java
public static
Insets
getGrooveInsets()
```

Returns the amount of space taken up by a border drawn by

drawGroove()

**Returns:** the inset of a groove border

- drawBezel

```java
public static void drawBezel​(
Graphics
g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws a bezel.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** isPressed

- is component pressed
**Parameters:** isDefault

- is default drawing
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

- drawLoweredBezel

```java
public static void drawLoweredBezel​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws a lowered bezel.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

- drawString

```java
public static void drawString​(
Graphics
g,

String
text,
int underlinedChar,
int x,
int y)
```

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would. The first occurrence
of

underlineChar

in text will be underlined.
The matching algorithm is not case sensitive.

**Parameters:** g

- an instance of

Graphics
**Parameters:** text

- a text
**Parameters:** underlinedChar

- an underlined char
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

- drawStringUnderlineCharAt

```java
public static void drawStringUnderlineCharAt​(
Graphics
g,

String
text,
int underlinedIndex,
int x,
int y)
```

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.
The character at index

underlinedIndex

in text will be underlined. If

index

is beyond the
bounds of

text

(including < 0), nothing will be
underlined.

**Parameters:** g

- Graphics to draw with
**Parameters:** text

- String to draw
**Parameters:** underlinedIndex

- Index of character in text to underline
**Parameters:** x

- x coordinate to draw at
**Parameters:** y

- y coordinate to draw at
**Since:** 1.4

- drawDashedRect

```java
public static void drawDashedRect​(
Graphics
g,
int x,
int y,
int width,
int height)
```

Draws dashed rectangle.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** width

- a width of rectangle
**Parameters:** height

- a height of rectangle

- getPreferredButtonSize

```java
public static
Dimension
getPreferredButtonSize​(
AbstractButton
b,
int textIconGap)
```

Returns the preferred size of the button.

**Parameters:** b

- an instance of

AbstractButton
**Parameters:** textIconGap

- a gap between text and icon
**Returns:** the preferred size of the button

- drawString

```java
public static void drawString​(
JComponent
c,

Graphics2D
g,

String
string,
float x,
float y)
```

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.
Nothing is drawn for the null string.

**Parameters:** c

- the component that will display the string, may be null
**Parameters:** g

- the graphics context, must not be null
**Parameters:** string

- the string to display, may be null
**Parameters:** x

- the x coordinate to draw the text at
**Parameters:** y

- the y coordinate to draw the text at
**Throws:** NullPointerException

- if the specified

g

is

null
**Since:** 9

- drawStringUnderlineCharAt

```java
public static void drawStringUnderlineCharAt​(
JComponent
c,

Graphics2D
g,

String
string,
int underlinedIndex,
float x,
float y)
```

Draws the given string at the specified location underlining
the specified character. The provided component is used to query text
properties and anti-aliasing hints.

The

underlinedIndex

parameter points to a char value
(Unicode code unit) in the given string.
If the char value specified at the underlined index is in
the high-surrogate range and the char value at the following index is in
the low-surrogate range then the supplementary character corresponding
to this surrogate pair is underlined.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

**Parameters:** c

- the component that will display the string, may be null
**Parameters:** g

- the graphics context, must not be null
**Parameters:** string

- the string to display, may be null
**Parameters:** underlinedIndex

- index of a a char value (Unicode code unit)
in the string to underline
**Parameters:** x

- the x coordinate to draw the text at
**Parameters:** y

- the y coordinate to draw the text at
**Throws:** NullPointerException

- if the specified

g

is

null
**Since:** 9
**See Also:** getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

- getClippedString

```java
public static
String
getClippedString​(
JComponent
c,

FontMetrics
fm,

String
string,
int availTextWidth)
```

Clips the passed in string to the space provided.
The provided component is used to query text properties and anti-aliasing hints.
The unchanged string is returned if the space provided is greater than
the string width.

**Parameters:** c

- the component, may be null
**Parameters:** fm

- the FontMetrics used to measure the string width, must be
obtained from the correct font and graphics. Must not be null.
**Parameters:** string

- the string to clip, may be null
**Parameters:** availTextWidth

- the amount of space that the string can be drawn in
**Returns:** the clipped string that fits in the provided space, an empty
string if the given string argument is

null

or empty
**Throws:** NullPointerException

- if the specified

fm

is

null
**Since:** 9
**See Also:** getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

- getStringWidth

```java
public static float getStringWidth​(
JComponent
c,

FontMetrics
fm,

String
string)
```

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.
If the passed string is

null

, returns zero.

**Parameters:** c

- the component, may be null
**Parameters:** fm

- the FontMetrics used to measure the advance string width, must
be obtained from the correct font and graphics. Must not be null.
**Parameters:** string

- the string to get the advance width of, may be null
**Returns:** the advance width of the specified string, zero is returned for

null

string
**Throws:** NullPointerException

- if the specified

fm

is

null
**Since:** 9

---

#### Method Detail

drawEtchedRect

```java
public static void drawEtchedRect​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws an etched rectangle.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

---

#### drawEtchedRect

public static void drawEtchedRect​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws an etched rectangle.

getEtchedInsets

```java
public static
Insets
getEtchedInsets()
```

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

**Returns:** the inset of an etched rect

---

#### getEtchedInsets

public static

Insets

getEtchedInsets()

Returns the amount of space taken up by a border drawn by

drawEtchedRect()

drawGroove

```java
public static void drawGroove​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
highlight)
```

Draws a groove.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** highlight

- a color highlighting

---

#### drawGroove

public static void drawGroove​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

highlight)

Draws a groove.

getGrooveInsets

```java
public static
Insets
getGrooveInsets()
```

Returns the amount of space taken up by a border drawn by

drawGroove()

**Returns:** the inset of a groove border

---

#### getGrooveInsets

public static

Insets

getGrooveInsets()

Returns the amount of space taken up by a border drawn by

drawGroove()

drawBezel

```java
public static void drawBezel​(
Graphics
g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws a bezel.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** isPressed

- is component pressed
**Parameters:** isDefault

- is default drawing
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

---

#### drawBezel

public static void drawBezel​(

Graphics

g,
int x,
int y,
int w,
int h,
boolean isPressed,
boolean isDefault,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws a bezel.

drawLoweredBezel

```java
public static void drawLoweredBezel​(
Graphics
g,
int x,
int y,
int w,
int h,

Color
shadow,

Color
darkShadow,

Color
highlight,

Color
lightHighlight)
```

Draws a lowered bezel.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** shadow

- a color of shadow
**Parameters:** darkShadow

- a color of dark shadow
**Parameters:** highlight

- a color highlighting
**Parameters:** lightHighlight

- a color of light highlighting

---

#### drawLoweredBezel

public static void drawLoweredBezel​(

Graphics

g,
int x,
int y,
int w,
int h,

Color

shadow,

Color

darkShadow,

Color

highlight,

Color

lightHighlight)

Draws a lowered bezel.

drawString

```java
public static void drawString​(
Graphics
g,

String
text,
int underlinedChar,
int x,
int y)
```

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would. The first occurrence
of

underlineChar

in text will be underlined.
The matching algorithm is not case sensitive.

**Parameters:** g

- an instance of

Graphics
**Parameters:** text

- a text
**Parameters:** underlinedChar

- an underlined char
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

---

#### drawString

public static void drawString​(

Graphics

g,

String

text,
int underlinedChar,
int x,
int y)

Draw a string with the graphics

g

at location (x,y)
just like

g.drawString

would. The first occurrence
of

underlineChar

in text will be underlined.
The matching algorithm is not case sensitive.

drawStringUnderlineCharAt

```java
public static void drawStringUnderlineCharAt​(
Graphics
g,

String
text,
int underlinedIndex,
int x,
int y)
```

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.
The character at index

underlinedIndex

in text will be underlined. If

index

is beyond the
bounds of

text

(including < 0), nothing will be
underlined.

**Parameters:** g

- Graphics to draw with
**Parameters:** text

- String to draw
**Parameters:** underlinedIndex

- Index of character in text to underline
**Parameters:** x

- x coordinate to draw at
**Parameters:** y

- y coordinate to draw at
**Since:** 1.4

---

#### drawStringUnderlineCharAt

public static void drawStringUnderlineCharAt​(

Graphics

g,

String

text,
int underlinedIndex,
int x,
int y)

Draw a string with the graphics

g

at location
(

x

,

y

)
just like

g.drawString

would.
The character at index

underlinedIndex

in text will be underlined. If

index

is beyond the
bounds of

text

(including < 0), nothing will be
underlined.

drawDashedRect

```java
public static void drawDashedRect​(
Graphics
g,
int x,
int y,
int width,
int height)
```

Draws dashed rectangle.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** width

- a width of rectangle
**Parameters:** height

- a height of rectangle

---

#### drawDashedRect

public static void drawDashedRect​(

Graphics

g,
int x,
int y,
int width,
int height)

Draws dashed rectangle.

getPreferredButtonSize

```java
public static
Dimension
getPreferredButtonSize​(
AbstractButton
b,
int textIconGap)
```

Returns the preferred size of the button.

**Parameters:** b

- an instance of

AbstractButton
**Parameters:** textIconGap

- a gap between text and icon
**Returns:** the preferred size of the button

---

#### getPreferredButtonSize

public static

Dimension

getPreferredButtonSize​(

AbstractButton

b,
int textIconGap)

Returns the preferred size of the button.

drawString

```java
public static void drawString​(
JComponent
c,

Graphics2D
g,

String
string,
float x,
float y)
```

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.
Nothing is drawn for the null string.

**Parameters:** c

- the component that will display the string, may be null
**Parameters:** g

- the graphics context, must not be null
**Parameters:** string

- the string to display, may be null
**Parameters:** x

- the x coordinate to draw the text at
**Parameters:** y

- the y coordinate to draw the text at
**Throws:** NullPointerException

- if the specified

g

is

null
**Since:** 9

---

#### drawString

public static void drawString​(

JComponent

c,

Graphics2D

g,

String

string,
float x,
float y)

Draws the given string at the specified location using text properties
and anti-aliasing hints from the provided component.
Nothing is drawn for the null string.

drawStringUnderlineCharAt

```java
public static void drawStringUnderlineCharAt​(
JComponent
c,

Graphics2D
g,

String
string,
int underlinedIndex,
float x,
float y)
```

Draws the given string at the specified location underlining
the specified character. The provided component is used to query text
properties and anti-aliasing hints.

The

underlinedIndex

parameter points to a char value
(Unicode code unit) in the given string.
If the char value specified at the underlined index is in
the high-surrogate range and the char value at the following index is in
the low-surrogate range then the supplementary character corresponding
to this surrogate pair is underlined.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

**Parameters:** c

- the component that will display the string, may be null
**Parameters:** g

- the graphics context, must not be null
**Parameters:** string

- the string to display, may be null
**Parameters:** underlinedIndex

- index of a a char value (Unicode code unit)
in the string to underline
**Parameters:** x

- the x coordinate to draw the text at
**Parameters:** y

- the y coordinate to draw the text at
**Throws:** NullPointerException

- if the specified

g

is

null
**Since:** 9
**See Also:** getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

---

#### drawStringUnderlineCharAt

public static void drawStringUnderlineCharAt​(

JComponent

c,

Graphics2D

g,

String

string,
int underlinedIndex,
float x,
float y)

Draws the given string at the specified location underlining
the specified character. The provided component is used to query text
properties and anti-aliasing hints.

The

underlinedIndex

parameter points to a char value
(Unicode code unit) in the given string.
If the char value specified at the underlined index is in
the high-surrogate range and the char value at the following index is in
the low-surrogate range then the supplementary character corresponding
to this surrogate pair is underlined.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

The

underlinedIndex

parameter points to a char value
(Unicode code unit) in the given string.
If the char value specified at the underlined index is in
the high-surrogate range and the char value at the following index is in
the low-surrogate range then the supplementary character corresponding
to this surrogate pair is underlined.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

No character is underlined if the index is negative or greater
than the string length

(index < 0 || index >= string.length())

or if the char value specified at the given index
is in the low-surrogate range.

getClippedString

```java
public static
String
getClippedString​(
JComponent
c,

FontMetrics
fm,

String
string,
int availTextWidth)
```

Clips the passed in string to the space provided.
The provided component is used to query text properties and anti-aliasing hints.
The unchanged string is returned if the space provided is greater than
the string width.

**Parameters:** c

- the component, may be null
**Parameters:** fm

- the FontMetrics used to measure the string width, must be
obtained from the correct font and graphics. Must not be null.
**Parameters:** string

- the string to clip, may be null
**Parameters:** availTextWidth

- the amount of space that the string can be drawn in
**Returns:** the clipped string that fits in the provided space, an empty
string if the given string argument is

null

or empty
**Throws:** NullPointerException

- if the specified

fm

is

null
**Since:** 9
**See Also:** getStringWidth(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String)

---

#### getClippedString

public static

String

getClippedString​(

JComponent

c,

FontMetrics

fm,

String

string,
int availTextWidth)

Clips the passed in string to the space provided.
The provided component is used to query text properties and anti-aliasing hints.
The unchanged string is returned if the space provided is greater than
the string width.

getStringWidth

```java
public static float getStringWidth​(
JComponent
c,

FontMetrics
fm,

String
string)
```

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.
If the passed string is

null

, returns zero.

**Parameters:** c

- the component, may be null
**Parameters:** fm

- the FontMetrics used to measure the advance string width, must
be obtained from the correct font and graphics. Must not be null.
**Parameters:** string

- the string to get the advance width of, may be null
**Returns:** the advance width of the specified string, zero is returned for

null

string
**Throws:** NullPointerException

- if the specified

fm

is

null
**Since:** 9

---

#### getStringWidth

public static float getStringWidth​(

JComponent

c,

FontMetrics

fm,

String

string)

Returns the width of the passed in string using text properties
and anti-aliasing hints from the provided component.
If the passed string is

null

, returns zero.

---

