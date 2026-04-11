# Interface CSS2Properties

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSS2Properties.html`

### Class Description

```java
public interface
CSS2Properties
```

The

CSS2Properties

interface represents a convenience
mechanism for retrieving and setting properties within a

CSSStyleDeclaration

. The attributes of this interface
correspond to all the properties specified in CSS2. Getting an attribute
of this interface is equivalent to calling the

getPropertyValue

method of the

CSSStyleDeclaration

interface. Setting an attribute of this
interface is equivalent to calling the

setProperty

method of
the

CSSStyleDeclaration

interface.

A conformant implementation of the CSS module is not required to
implement the

CSS2Properties

interface. If an implementation
does implement this interface, the expectation is that language-specific
methods can be used to cast from an instance of the

CSSStyleDeclaration

interface to the

CSS2Properties

interface.

If an implementation does implement this interface, it is expected to
understand the specific syntax of the shorthand properties, and apply
their semantics; when the

margin

property is set, for
example, the

marginTop

,

marginRight

,

marginBottom

and

marginLeft

properties are
actually being set by the underlying implementation.

When dealing with CSS "shorthand" properties, the shorthand properties
should be decomposed into their component longhand properties as
appropriate, and when querying for their value, the form returned should
be the shortest form exactly equivalent to the declarations made in the
ruleset. However, if there is no shorthand declaration that could be
added to the ruleset without changing in any way the rules already
declared in the ruleset (i.e., by adding longhand rules that were
previously not declared in the ruleset), then the empty string should be
returned for the shorthand property.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

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

#### String
getAzimuth()

See the azimuth property definition in CSS2.

---

#### void setAzimuth​(
String
azimuth)
throws
DOMException

See the azimuth property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBackground()

See the background property definition in CSS2.

---

#### void setBackground​(
String
background)
throws
DOMException

See the background property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBackgroundAttachment()

See the background-attachment property definition in CSS2.

---

#### void setBackgroundAttachment​(
String
backgroundAttachment)
throws
DOMException

See the background-attachment property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBackgroundColor()

See the background-color property definition in CSS2.

---

#### void setBackgroundColor​(
String
backgroundColor)
throws
DOMException

See the background-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBackgroundImage()

See the background-image property definition in CSS2.

---

#### void setBackgroundImage​(
String
backgroundImage)
throws
DOMException

See the background-image property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBackgroundPosition()

See the background-position property definition in CSS2.

---

#### void setBackgroundPosition​(
String
backgroundPosition)
throws
DOMException

See the background-position property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBackgroundRepeat()

See the background-repeat property definition in CSS2.

---

#### void setBackgroundRepeat​(
String
backgroundRepeat)
throws
DOMException

See the background-repeat property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorder()

See the border property definition in CSS2.

---

#### void setBorder​(
String
border)
throws
DOMException

See the border property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderCollapse()

See the border-collapse property definition in CSS2.

---

#### void setBorderCollapse​(
String
borderCollapse)
throws
DOMException

See the border-collapse property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderColor()

See the border-color property definition in CSS2.

---

#### void setBorderColor​(
String
borderColor)
throws
DOMException

See the border-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderSpacing()

See the border-spacing property definition in CSS2.

---

#### void setBorderSpacing​(
String
borderSpacing)
throws
DOMException

See the border-spacing property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderStyle()

See the border-style property definition in CSS2.

---

#### void setBorderStyle​(
String
borderStyle)
throws
DOMException

See the border-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderTop()

See the border-top property definition in CSS2.

---

#### void setBorderTop​(
String
borderTop)
throws
DOMException

See the border-top property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderRight()

See the border-right property definition in CSS2.

---

#### void setBorderRight​(
String
borderRight)
throws
DOMException

See the border-right property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderBottom()

See the border-bottom property definition in CSS2.

---

#### void setBorderBottom​(
String
borderBottom)
throws
DOMException

See the border-bottom property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderLeft()

See the border-left property definition in CSS2.

---

#### void setBorderLeft​(
String
borderLeft)
throws
DOMException

See the border-left property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderTopColor()

See the border-top-color property definition in CSS2.

---

#### void setBorderTopColor​(
String
borderTopColor)
throws
DOMException

See the border-top-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderRightColor()

See the border-right-color property definition in CSS2.

---

#### void setBorderRightColor​(
String
borderRightColor)
throws
DOMException

See the border-right-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderBottomColor()

See the border-bottom-color property definition in CSS2.

---

#### void setBorderBottomColor​(
String
borderBottomColor)
throws
DOMException

See the border-bottom-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderLeftColor()

See the border-left-color property definition in CSS2.

---

#### void setBorderLeftColor​(
String
borderLeftColor)
throws
DOMException

See the border-left-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderTopStyle()

See the border-top-style property definition in CSS2.

---

#### void setBorderTopStyle​(
String
borderTopStyle)
throws
DOMException

See the border-top-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderRightStyle()

See the border-right-style property definition in CSS2.

---

#### void setBorderRightStyle​(
String
borderRightStyle)
throws
DOMException

See the border-right-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderBottomStyle()

See the border-bottom-style property definition in CSS2.

---

#### void setBorderBottomStyle​(
String
borderBottomStyle)
throws
DOMException

See the border-bottom-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderLeftStyle()

See the border-left-style property definition in CSS2.

---

#### void setBorderLeftStyle​(
String
borderLeftStyle)
throws
DOMException

See the border-left-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderTopWidth()

See the border-top-width property definition in CSS2.

---

#### void setBorderTopWidth​(
String
borderTopWidth)
throws
DOMException

See the border-top-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderRightWidth()

See the border-right-width property definition in CSS2.

---

#### void setBorderRightWidth​(
String
borderRightWidth)
throws
DOMException

See the border-right-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderBottomWidth()

See the border-bottom-width property definition in CSS2.

---

#### void setBorderBottomWidth​(
String
borderBottomWidth)
throws
DOMException

See the border-bottom-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderLeftWidth()

See the border-left-width property definition in CSS2.

---

#### void setBorderLeftWidth​(
String
borderLeftWidth)
throws
DOMException

See the border-left-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBorderWidth()

See the border-width property definition in CSS2.

---

#### void setBorderWidth​(
String
borderWidth)
throws
DOMException

See the border-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getBottom()

See the bottom property definition in CSS2.

---

#### void setBottom​(
String
bottom)
throws
DOMException

See the bottom property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCaptionSide()

See the caption-side property definition in CSS2.

---

#### void setCaptionSide​(
String
captionSide)
throws
DOMException

See the caption-side property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getClear()

See the clear property definition in CSS2.

---

#### void setClear​(
String
clear)
throws
DOMException

See the clear property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getClip()

See the clip property definition in CSS2.

---

#### void setClip​(
String
clip)
throws
DOMException

See the clip property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getColor()

See the color property definition in CSS2.

---

#### void setColor​(
String
color)
throws
DOMException

See the color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getContent()

See the content property definition in CSS2.

---

#### void setContent​(
String
content)
throws
DOMException

See the content property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCounterIncrement()

See the counter-increment property definition in CSS2.

---

#### void setCounterIncrement​(
String
counterIncrement)
throws
DOMException

See the counter-increment property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCounterReset()

See the counter-reset property definition in CSS2.

---

#### void setCounterReset​(
String
counterReset)
throws
DOMException

See the counter-reset property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCue()

See the cue property definition in CSS2.

---

#### void setCue​(
String
cue)
throws
DOMException

See the cue property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCueAfter()

See the cue-after property definition in CSS2.

---

#### void setCueAfter​(
String
cueAfter)
throws
DOMException

See the cue-after property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCueBefore()

See the cue-before property definition in CSS2.

---

#### void setCueBefore​(
String
cueBefore)
throws
DOMException

See the cue-before property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCursor()

See the cursor property definition in CSS2.

---

#### void setCursor​(
String
cursor)
throws
DOMException

See the cursor property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getDirection()

See the direction property definition in CSS2.

---

#### void setDirection​(
String
direction)
throws
DOMException

See the direction property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getDisplay()

See the display property definition in CSS2.

---

#### void setDisplay​(
String
display)
throws
DOMException

See the display property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getElevation()

See the elevation property definition in CSS2.

---

#### void setElevation​(
String
elevation)
throws
DOMException

See the elevation property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getEmptyCells()

See the empty-cells property definition in CSS2.

---

#### void setEmptyCells​(
String
emptyCells)
throws
DOMException

See the empty-cells property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getCssFloat()

See the float property definition in CSS2.

---

#### void setCssFloat​(
String
cssFloat)
throws
DOMException

See the float property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFont()

See the font property definition in CSS2.

---

#### void setFont​(
String
font)
throws
DOMException

See the font property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontFamily()

See the font-family property definition in CSS2.

---

#### void setFontFamily​(
String
fontFamily)
throws
DOMException

See the font-family property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontSize()

See the font-size property definition in CSS2.

---

#### void setFontSize​(
String
fontSize)
throws
DOMException

See the font-size property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontSizeAdjust()

See the font-size-adjust property definition in CSS2.

---

#### void setFontSizeAdjust​(
String
fontSizeAdjust)
throws
DOMException

See the font-size-adjust property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontStretch()

See the font-stretch property definition in CSS2.

---

#### void setFontStretch​(
String
fontStretch)
throws
DOMException

See the font-stretch property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontStyle()

See the font-style property definition in CSS2.

---

#### void setFontStyle​(
String
fontStyle)
throws
DOMException

See the font-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontVariant()

See the font-variant property definition in CSS2.

---

#### void setFontVariant​(
String
fontVariant)
throws
DOMException

See the font-variant property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getFontWeight()

See the font-weight property definition in CSS2.

---

#### void setFontWeight​(
String
fontWeight)
throws
DOMException

See the font-weight property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getHeight()

See the height property definition in CSS2.

---

#### void setHeight​(
String
height)
throws
DOMException

See the height property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getLeft()

See the left property definition in CSS2.

---

#### void setLeft​(
String
left)
throws
DOMException

See the left property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getLetterSpacing()

See the letter-spacing property definition in CSS2.

---

#### void setLetterSpacing​(
String
letterSpacing)
throws
DOMException

See the letter-spacing property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getLineHeight()

See the line-height property definition in CSS2.

---

#### void setLineHeight​(
String
lineHeight)
throws
DOMException

See the line-height property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getListStyle()

See the list-style property definition in CSS2.

---

#### void setListStyle​(
String
listStyle)
throws
DOMException

See the list-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getListStyleImage()

See the list-style-image property definition in CSS2.

---

#### void setListStyleImage​(
String
listStyleImage)
throws
DOMException

See the list-style-image property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getListStylePosition()

See the list-style-position property definition in CSS2.

---

#### void setListStylePosition​(
String
listStylePosition)
throws
DOMException

See the list-style-position property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getListStyleType()

See the list-style-type property definition in CSS2.

---

#### void setListStyleType​(
String
listStyleType)
throws
DOMException

See the list-style-type property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMargin()

See the margin property definition in CSS2.

---

#### void setMargin​(
String
margin)
throws
DOMException

See the margin property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMarginTop()

See the margin-top property definition in CSS2.

---

#### void setMarginTop​(
String
marginTop)
throws
DOMException

See the margin-top property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMarginRight()

See the margin-right property definition in CSS2.

---

#### void setMarginRight​(
String
marginRight)
throws
DOMException

See the margin-right property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMarginBottom()

See the margin-bottom property definition in CSS2.

---

#### void setMarginBottom​(
String
marginBottom)
throws
DOMException

See the margin-bottom property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMarginLeft()

See the margin-left property definition in CSS2.

---

#### void setMarginLeft​(
String
marginLeft)
throws
DOMException

See the margin-left property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMarkerOffset()

See the marker-offset property definition in CSS2.

---

#### void setMarkerOffset​(
String
markerOffset)
throws
DOMException

See the marker-offset property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMarks()

See the marks property definition in CSS2.

---

#### void setMarks​(
String
marks)
throws
DOMException

See the marks property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMaxHeight()

See the max-height property definition in CSS2.

---

#### void setMaxHeight​(
String
maxHeight)
throws
DOMException

See the max-height property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMaxWidth()

See the max-width property definition in CSS2.

---

#### void setMaxWidth​(
String
maxWidth)
throws
DOMException

See the max-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMinHeight()

See the min-height property definition in CSS2.

---

#### void setMinHeight​(
String
minHeight)
throws
DOMException

See the min-height property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getMinWidth()

See the min-width property definition in CSS2.

---

#### void setMinWidth​(
String
minWidth)
throws
DOMException

See the min-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getOrphans()

See the orphans property definition in CSS2.

---

#### void setOrphans​(
String
orphans)
throws
DOMException

See the orphans property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getOutline()

See the outline property definition in CSS2.

---

#### void setOutline​(
String
outline)
throws
DOMException

See the outline property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getOutlineColor()

See the outline-color property definition in CSS2.

---

#### void setOutlineColor​(
String
outlineColor)
throws
DOMException

See the outline-color property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getOutlineStyle()

See the outline-style property definition in CSS2.

---

#### void setOutlineStyle​(
String
outlineStyle)
throws
DOMException

See the outline-style property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getOutlineWidth()

See the outline-width property definition in CSS2.

---

#### void setOutlineWidth​(
String
outlineWidth)
throws
DOMException

See the outline-width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getOverflow()

See the overflow property definition in CSS2.

---

#### void setOverflow​(
String
overflow)
throws
DOMException

See the overflow property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPadding()

See the padding property definition in CSS2.

---

#### void setPadding​(
String
padding)
throws
DOMException

See the padding property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPaddingTop()

See the padding-top property definition in CSS2.

---

#### void setPaddingTop​(
String
paddingTop)
throws
DOMException

See the padding-top property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPaddingRight()

See the padding-right property definition in CSS2.

---

#### void setPaddingRight​(
String
paddingRight)
throws
DOMException

See the padding-right property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPaddingBottom()

See the padding-bottom property definition in CSS2.

---

#### void setPaddingBottom​(
String
paddingBottom)
throws
DOMException

See the padding-bottom property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPaddingLeft()

See the padding-left property definition in CSS2.

---

#### void setPaddingLeft​(
String
paddingLeft)
throws
DOMException

See the padding-left property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPage()

See the page property definition in CSS2.

---

#### void setPage​(
String
page)
throws
DOMException

See the page property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPageBreakAfter()

See the page-break-after property definition in CSS2.

---

#### void setPageBreakAfter​(
String
pageBreakAfter)
throws
DOMException

See the page-break-after property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPageBreakBefore()

See the page-break-before property definition in CSS2.

---

#### void setPageBreakBefore​(
String
pageBreakBefore)
throws
DOMException

See the page-break-before property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPageBreakInside()

See the page-break-inside property definition in CSS2.

---

#### void setPageBreakInside​(
String
pageBreakInside)
throws
DOMException

See the page-break-inside property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPause()

See the pause property definition in CSS2.

---

#### void setPause​(
String
pause)
throws
DOMException

See the pause property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPauseAfter()

See the pause-after property definition in CSS2.

---

#### void setPauseAfter​(
String
pauseAfter)
throws
DOMException

See the pause-after property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPauseBefore()

See the pause-before property definition in CSS2.

---

#### void setPauseBefore​(
String
pauseBefore)
throws
DOMException

See the pause-before property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPitch()

See the pitch property definition in CSS2.

---

#### void setPitch​(
String
pitch)
throws
DOMException

See the pitch property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPitchRange()

See the pitch-range property definition in CSS2.

---

#### void setPitchRange​(
String
pitchRange)
throws
DOMException

See the pitch-range property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPlayDuring()

See the play-during property definition in CSS2.

---

#### void setPlayDuring​(
String
playDuring)
throws
DOMException

See the play-during property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getPosition()

See the position property definition in CSS2.

---

#### void setPosition​(
String
position)
throws
DOMException

See the position property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getQuotes()

See the quotes property definition in CSS2.

---

#### void setQuotes​(
String
quotes)
throws
DOMException

See the quotes property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getRichness()

See the richness property definition in CSS2.

---

#### void setRichness​(
String
richness)
throws
DOMException

See the richness property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getRight()

See the right property definition in CSS2.

---

#### void setRight​(
String
right)
throws
DOMException

See the right property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getSize()

See the size property definition in CSS2.

---

#### void setSize​(
String
size)
throws
DOMException

See the size property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getSpeak()

See the speak property definition in CSS2.

---

#### void setSpeak​(
String
speak)
throws
DOMException

See the speak property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getSpeakHeader()

See the speak-header property definition in CSS2.

---

#### void setSpeakHeader​(
String
speakHeader)
throws
DOMException

See the speak-header property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getSpeakNumeral()

See the speak-numeral property definition in CSS2.

---

#### void setSpeakNumeral​(
String
speakNumeral)
throws
DOMException

See the speak-numeral property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getSpeakPunctuation()

See the speak-punctuation property definition in CSS2.

---

#### void setSpeakPunctuation​(
String
speakPunctuation)
throws
DOMException

See the speak-punctuation property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getSpeechRate()

See the speech-rate property definition in CSS2.

---

#### void setSpeechRate​(
String
speechRate)
throws
DOMException

See the speech-rate property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getStress()

See the stress property definition in CSS2.

---

#### void setStress​(
String
stress)
throws
DOMException

See the stress property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTableLayout()

See the table-layout property definition in CSS2.

---

#### void setTableLayout​(
String
tableLayout)
throws
DOMException

See the table-layout property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTextAlign()

See the text-align property definition in CSS2.

---

#### void setTextAlign​(
String
textAlign)
throws
DOMException

See the text-align property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTextDecoration()

See the text-decoration property definition in CSS2.

---

#### void setTextDecoration​(
String
textDecoration)
throws
DOMException

See the text-decoration property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTextIndent()

See the text-indent property definition in CSS2.

---

#### void setTextIndent​(
String
textIndent)
throws
DOMException

See the text-indent property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTextShadow()

See the text-shadow property definition in CSS2.

---

#### void setTextShadow​(
String
textShadow)
throws
DOMException

See the text-shadow property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTextTransform()

See the text-transform property definition in CSS2.

---

#### void setTextTransform​(
String
textTransform)
throws
DOMException

See the text-transform property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getTop()

See the top property definition in CSS2.

---

#### void setTop​(
String
top)
throws
DOMException

See the top property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getUnicodeBidi()

See the unicode-bidi property definition in CSS2.

---

#### void setUnicodeBidi​(
String
unicodeBidi)
throws
DOMException

See the unicode-bidi property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getVerticalAlign()

See the vertical-align property definition in CSS2.

---

#### void setVerticalAlign​(
String
verticalAlign)
throws
DOMException

See the vertical-align property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getVisibility()

See the visibility property definition in CSS2.

---

#### void setVisibility​(
String
visibility)
throws
DOMException

See the visibility property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getVoiceFamily()

See the voice-family property definition in CSS2.

---

#### void setVoiceFamily​(
String
voiceFamily)
throws
DOMException

See the voice-family property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getVolume()

See the volume property definition in CSS2.

---

#### void setVolume​(
String
volume)
throws
DOMException

See the volume property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getWhiteSpace()

See the white-space property definition in CSS2.

---

#### void setWhiteSpace​(
String
whiteSpace)
throws
DOMException

See the white-space property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getWidows()

See the widows property definition in CSS2.

---

#### void setWidows​(
String
widows)
throws
DOMException

See the widows property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getWidth()

See the width property definition in CSS2.

---

#### void setWidth​(
String
width)
throws
DOMException

See the width property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getWordSpacing()

See the word-spacing property definition in CSS2.

---

#### void setWordSpacing​(
String
wordSpacing)
throws
DOMException

See the word-spacing property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### String
getZIndex()

See the z-index property definition in CSS2.

---

#### void setZIndex​(
String
zIndex)
throws
DOMException

See the z-index property definition in CSS2.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

### Additional Sections

#### Interface CSS2Properties

```java
public interface
CSS2Properties
```

The

CSS2Properties

interface represents a convenience
mechanism for retrieving and setting properties within a

CSSStyleDeclaration

. The attributes of this interface
correspond to all the properties specified in CSS2. Getting an attribute
of this interface is equivalent to calling the

getPropertyValue

method of the

CSSStyleDeclaration

interface. Setting an attribute of this
interface is equivalent to calling the

setProperty

method of
the

CSSStyleDeclaration

interface.

A conformant implementation of the CSS module is not required to
implement the

CSS2Properties

interface. If an implementation
does implement this interface, the expectation is that language-specific
methods can be used to cast from an instance of the

CSSStyleDeclaration

interface to the

CSS2Properties

interface.

If an implementation does implement this interface, it is expected to
understand the specific syntax of the shorthand properties, and apply
their semantics; when the

margin

property is set, for
example, the

marginTop

,

marginRight

,

marginBottom

and

marginLeft

properties are
actually being set by the underlying implementation.

When dealing with CSS "shorthand" properties, the shorthand properties
should be decomposed into their component longhand properties as
appropriate, and when querying for their value, the form returned should
be the shortest form exactly equivalent to the declarations made in the
ruleset. However, if there is no shorthand declaration that could be
added to the ruleset without changing in any way the rules already
declared in the ruleset (i.e., by adding longhand rules that were
previously not declared in the ruleset), then the empty string should be
returned for the shorthand property.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSS2Properties

The

CSS2Properties

interface represents a convenience
mechanism for retrieving and setting properties within a

CSSStyleDeclaration

. The attributes of this interface
correspond to all the properties specified in CSS2. Getting an attribute
of this interface is equivalent to calling the

getPropertyValue

method of the

CSSStyleDeclaration

interface. Setting an attribute of this
interface is equivalent to calling the

setProperty

method of
the

CSSStyleDeclaration

interface.

A conformant implementation of the CSS module is not required to
implement the

CSS2Properties

interface. If an implementation
does implement this interface, the expectation is that language-specific
methods can be used to cast from an instance of the

CSSStyleDeclaration

interface to the

CSS2Properties

interface.

If an implementation does implement this interface, it is expected to
understand the specific syntax of the shorthand properties, and apply
their semantics; when the

margin

property is set, for
example, the

marginTop

,

marginRight

,

marginBottom

and

marginLeft

properties are
actually being set by the underlying implementation.

When dealing with CSS "shorthand" properties, the shorthand properties
should be decomposed into their component longhand properties as
appropriate, and when querying for their value, the form returned should
be the shortest form exactly equivalent to the declarations made in the
ruleset. However, if there is no shorthand declaration that could be
added to the ruleset without changing in any way the rules already
declared in the ruleset (i.e., by adding longhand rules that were
previously not declared in the ruleset), then the empty string should be
returned for the shorthand property.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

A conformant implementation of the CSS module is not required to
implement the

CSS2Properties

interface. If an implementation
does implement this interface, the expectation is that language-specific
methods can be used to cast from an instance of the

CSSStyleDeclaration

interface to the

CSS2Properties

interface.

If an implementation does implement this interface, it is expected to
understand the specific syntax of the shorthand properties, and apply
their semantics; when the

margin

property is set, for
example, the

marginTop

,

marginRight

,

marginBottom

and

marginLeft

properties are
actually being set by the underlying implementation.

When dealing with CSS "shorthand" properties, the shorthand properties
should be decomposed into their component longhand properties as
appropriate, and when querying for their value, the form returned should
be the shortest form exactly equivalent to the declarations made in the
ruleset. However, if there is no shorthand declaration that could be
added to the ruleset without changing in any way the rules already
declared in the ruleset (i.e., by adding longhand rules that were
previously not declared in the ruleset), then the empty string should be
returned for the shorthand property.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

If an implementation does implement this interface, it is expected to
understand the specific syntax of the shorthand properties, and apply
their semantics; when the

margin

property is set, for
example, the

marginTop

,

marginRight

,

marginBottom

and

marginLeft

properties are
actually being set by the underlying implementation.

When dealing with CSS "shorthand" properties, the shorthand properties
should be decomposed into their component longhand properties as
appropriate, and when querying for their value, the form returned should
be the shortest form exactly equivalent to the declarations made in the
ruleset. However, if there is no shorthand declaration that could be
added to the ruleset without changing in any way the rules already
declared in the ruleset (i.e., by adding longhand rules that were
previously not declared in the ruleset), then the empty string should be
returned for the shorthand property.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

When dealing with CSS "shorthand" properties, the shorthand properties
should be decomposed into their component longhand properties as
appropriate, and when querying for their value, the form returned should
be the shortest form exactly equivalent to the declarations made in the
ruleset. However, if there is no shorthand declaration that could be
added to the ruleset without changing in any way the rules already
declared in the ruleset (i.e., by adding longhand rules that were
previously not declared in the ruleset), then the empty string should be
returned for the shorthand property.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

For example, querying for the

font

property should not
return "normal normal normal 14pt/normal Arial, sans-serif", when "14pt
Arial, sans-serif" suffices. (The normals are initial values, and are
implied by use of the longhand property.)

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

If the values for all the longhand properties that compose a particular
string are the initial values, then a string consisting of all the
initial values should be returned (e.g. a

border-width

value
of "medium" should be returned as such, not as "").

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

For some shorthand properties that take missing values from other
sides, such as the

margin

,

padding

, and

border-[width|style|color]

properties, the minimum number of
sides possible should be used; i.e., "0px 10px" will be returned instead
of "0px 10px 0px 10px".

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

If the value of a shorthand property can not be decomposed into its
component longhand properties, as is the case for the

font

property with a value of "menu", querying for the values of the component
longhand properties should return the empty string.

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

String

getAzimuth

()

See the azimuth property definition in CSS2.

String

getBackground

()

See the background property definition in CSS2.

String

getBackgroundAttachment

()

See the background-attachment property definition in CSS2.

String

getBackgroundColor

()

See the background-color property definition in CSS2.

String

getBackgroundImage

()

See the background-image property definition in CSS2.

String

getBackgroundPosition

()

See the background-position property definition in CSS2.

String

getBackgroundRepeat

()

See the background-repeat property definition in CSS2.

String

getBorder

()

See the border property definition in CSS2.

String

getBorderBottom

()

See the border-bottom property definition in CSS2.

String

getBorderBottomColor

()

See the border-bottom-color property definition in CSS2.

String

getBorderBottomStyle

()

See the border-bottom-style property definition in CSS2.

String

getBorderBottomWidth

()

See the border-bottom-width property definition in CSS2.

String

getBorderCollapse

()

See the border-collapse property definition in CSS2.

String

getBorderColor

()

See the border-color property definition in CSS2.

String

getBorderLeft

()

See the border-left property definition in CSS2.

String

getBorderLeftColor

()

See the border-left-color property definition in CSS2.

String

getBorderLeftStyle

()

See the border-left-style property definition in CSS2.

String

getBorderLeftWidth

()

See the border-left-width property definition in CSS2.

String

getBorderRight

()

See the border-right property definition in CSS2.

String

getBorderRightColor

()

See the border-right-color property definition in CSS2.

String

getBorderRightStyle

()

See the border-right-style property definition in CSS2.

String

getBorderRightWidth

()

See the border-right-width property definition in CSS2.

String

getBorderSpacing

()

See the border-spacing property definition in CSS2.

String

getBorderStyle

()

See the border-style property definition in CSS2.

String

getBorderTop

()

See the border-top property definition in CSS2.

String

getBorderTopColor

()

See the border-top-color property definition in CSS2.

String

getBorderTopStyle

()

See the border-top-style property definition in CSS2.

String

getBorderTopWidth

()

See the border-top-width property definition in CSS2.

String

getBorderWidth

()

See the border-width property definition in CSS2.

String

getBottom

()

See the bottom property definition in CSS2.

String

getCaptionSide

()

See the caption-side property definition in CSS2.

String

getClear

()

See the clear property definition in CSS2.

String

getClip

()

See the clip property definition in CSS2.

String

getColor

()

See the color property definition in CSS2.

String

getContent

()

See the content property definition in CSS2.

String

getCounterIncrement

()

See the counter-increment property definition in CSS2.

String

getCounterReset

()

See the counter-reset property definition in CSS2.

String

getCssFloat

()

See the float property definition in CSS2.

String

getCue

()

See the cue property definition in CSS2.

String

getCueAfter

()

See the cue-after property definition in CSS2.

String

getCueBefore

()

See the cue-before property definition in CSS2.

String

getCursor

()

See the cursor property definition in CSS2.

String

getDirection

()

See the direction property definition in CSS2.

String

getDisplay

()

See the display property definition in CSS2.

String

getElevation

()

See the elevation property definition in CSS2.

String

getEmptyCells

()

See the empty-cells property definition in CSS2.

String

getFont

()

See the font property definition in CSS2.

String

getFontFamily

()

See the font-family property definition in CSS2.

String

getFontSize

()

See the font-size property definition in CSS2.

String

getFontSizeAdjust

()

See the font-size-adjust property definition in CSS2.

String

getFontStretch

()

See the font-stretch property definition in CSS2.

String

getFontStyle

()

See the font-style property definition in CSS2.

String

getFontVariant

()

See the font-variant property definition in CSS2.

String

getFontWeight

()

See the font-weight property definition in CSS2.

String

getHeight

()

See the height property definition in CSS2.

String

getLeft

()

See the left property definition in CSS2.

String

getLetterSpacing

()

See the letter-spacing property definition in CSS2.

String

getLineHeight

()

See the line-height property definition in CSS2.

String

getListStyle

()

See the list-style property definition in CSS2.

String

getListStyleImage

()

See the list-style-image property definition in CSS2.

String

getListStylePosition

()

See the list-style-position property definition in CSS2.

String

getListStyleType

()

See the list-style-type property definition in CSS2.

String

getMargin

()

See the margin property definition in CSS2.

String

getMarginBottom

()

See the margin-bottom property definition in CSS2.

String

getMarginLeft

()

See the margin-left property definition in CSS2.

String

getMarginRight

()

See the margin-right property definition in CSS2.

String

getMarginTop

()

See the margin-top property definition in CSS2.

String

getMarkerOffset

()

See the marker-offset property definition in CSS2.

String

getMarks

()

See the marks property definition in CSS2.

String

getMaxHeight

()

See the max-height property definition in CSS2.

String

getMaxWidth

()

See the max-width property definition in CSS2.

String

getMinHeight

()

See the min-height property definition in CSS2.

String

getMinWidth

()

See the min-width property definition in CSS2.

String

getOrphans

()

See the orphans property definition in CSS2.

String

getOutline

()

See the outline property definition in CSS2.

String

getOutlineColor

()

See the outline-color property definition in CSS2.

String

getOutlineStyle

()

See the outline-style property definition in CSS2.

String

getOutlineWidth

()

See the outline-width property definition in CSS2.

String

getOverflow

()

See the overflow property definition in CSS2.

String

getPadding

()

See the padding property definition in CSS2.

String

getPaddingBottom

()

See the padding-bottom property definition in CSS2.

String

getPaddingLeft

()

See the padding-left property definition in CSS2.

String

getPaddingRight

()

See the padding-right property definition in CSS2.

String

getPaddingTop

()

See the padding-top property definition in CSS2.

String

getPage

()

See the page property definition in CSS2.

String

getPageBreakAfter

()

See the page-break-after property definition in CSS2.

String

getPageBreakBefore

()

See the page-break-before property definition in CSS2.

String

getPageBreakInside

()

See the page-break-inside property definition in CSS2.

String

getPause

()

See the pause property definition in CSS2.

String

getPauseAfter

()

See the pause-after property definition in CSS2.

String

getPauseBefore

()

See the pause-before property definition in CSS2.

String

getPitch

()

See the pitch property definition in CSS2.

String

getPitchRange

()

See the pitch-range property definition in CSS2.

String

getPlayDuring

()

See the play-during property definition in CSS2.

String

getPosition

()

See the position property definition in CSS2.

String

getQuotes

()

See the quotes property definition in CSS2.

String

getRichness

()

See the richness property definition in CSS2.

String

getRight

()

See the right property definition in CSS2.

String

getSize

()

See the size property definition in CSS2.

String

getSpeak

()

See the speak property definition in CSS2.

String

getSpeakHeader

()

See the speak-header property definition in CSS2.

String

getSpeakNumeral

()

See the speak-numeral property definition in CSS2.

String

getSpeakPunctuation

()

See the speak-punctuation property definition in CSS2.

String

getSpeechRate

()

See the speech-rate property definition in CSS2.

String

getStress

()

See the stress property definition in CSS2.

String

getTableLayout

()

See the table-layout property definition in CSS2.

String

getTextAlign

()

See the text-align property definition in CSS2.

String

getTextDecoration

()

See the text-decoration property definition in CSS2.

String

getTextIndent

()

See the text-indent property definition in CSS2.

String

getTextShadow

()

See the text-shadow property definition in CSS2.

String

getTextTransform

()

See the text-transform property definition in CSS2.

String

getTop

()

See the top property definition in CSS2.

String

getUnicodeBidi

()

See the unicode-bidi property definition in CSS2.

String

getVerticalAlign

()

See the vertical-align property definition in CSS2.

String

getVisibility

()

See the visibility property definition in CSS2.

String

getVoiceFamily

()

See the voice-family property definition in CSS2.

String

getVolume

()

See the volume property definition in CSS2.

String

getWhiteSpace

()

See the white-space property definition in CSS2.

String

getWidows

()

See the widows property definition in CSS2.

String

getWidth

()

See the width property definition in CSS2.

String

getWordSpacing

()

See the word-spacing property definition in CSS2.

String

getZIndex

()

See the z-index property definition in CSS2.

void

setAzimuth

​(

String

azimuth)

See the azimuth property definition in CSS2.

void

setBackground

​(

String

background)

See the background property definition in CSS2.

void

setBackgroundAttachment

​(

String

backgroundAttachment)

See the background-attachment property definition in CSS2.

void

setBackgroundColor

​(

String

backgroundColor)

See the background-color property definition in CSS2.

void

setBackgroundImage

​(

String

backgroundImage)

See the background-image property definition in CSS2.

void

setBackgroundPosition

​(

String

backgroundPosition)

See the background-position property definition in CSS2.

void

setBackgroundRepeat

​(

String

backgroundRepeat)

See the background-repeat property definition in CSS2.

void

setBorder

​(

String

border)

See the border property definition in CSS2.

void

setBorderBottom

​(

String

borderBottom)

See the border-bottom property definition in CSS2.

void

setBorderBottomColor

​(

String

borderBottomColor)

See the border-bottom-color property definition in CSS2.

void

setBorderBottomStyle

​(

String

borderBottomStyle)

See the border-bottom-style property definition in CSS2.

void

setBorderBottomWidth

​(

String

borderBottomWidth)

See the border-bottom-width property definition in CSS2.

void

setBorderCollapse

​(

String

borderCollapse)

See the border-collapse property definition in CSS2.

void

setBorderColor

​(

String

borderColor)

See the border-color property definition in CSS2.

void

setBorderLeft

​(

String

borderLeft)

See the border-left property definition in CSS2.

void

setBorderLeftColor

​(

String

borderLeftColor)

See the border-left-color property definition in CSS2.

void

setBorderLeftStyle

​(

String

borderLeftStyle)

See the border-left-style property definition in CSS2.

void

setBorderLeftWidth

​(

String

borderLeftWidth)

See the border-left-width property definition in CSS2.

void

setBorderRight

​(

String

borderRight)

See the border-right property definition in CSS2.

void

setBorderRightColor

​(

String

borderRightColor)

See the border-right-color property definition in CSS2.

void

setBorderRightStyle

​(

String

borderRightStyle)

See the border-right-style property definition in CSS2.

void

setBorderRightWidth

​(

String

borderRightWidth)

See the border-right-width property definition in CSS2.

void

setBorderSpacing

​(

String

borderSpacing)

See the border-spacing property definition in CSS2.

void

setBorderStyle

​(

String

borderStyle)

See the border-style property definition in CSS2.

void

setBorderTop

​(

String

borderTop)

See the border-top property definition in CSS2.

void

setBorderTopColor

​(

String

borderTopColor)

See the border-top-color property definition in CSS2.

void

setBorderTopStyle

​(

String

borderTopStyle)

See the border-top-style property definition in CSS2.

void

setBorderTopWidth

​(

String

borderTopWidth)

See the border-top-width property definition in CSS2.

void

setBorderWidth

​(

String

borderWidth)

See the border-width property definition in CSS2.

void

setBottom

​(

String

bottom)

See the bottom property definition in CSS2.

void

setCaptionSide

​(

String

captionSide)

See the caption-side property definition in CSS2.

void

setClear

​(

String

clear)

See the clear property definition in CSS2.

void

setClip

​(

String

clip)

See the clip property definition in CSS2.

void

setColor

​(

String

color)

See the color property definition in CSS2.

void

setContent

​(

String

content)

See the content property definition in CSS2.

void

setCounterIncrement

​(

String

counterIncrement)

See the counter-increment property definition in CSS2.

void

setCounterReset

​(

String

counterReset)

See the counter-reset property definition in CSS2.

void

setCssFloat

​(

String

cssFloat)

See the float property definition in CSS2.

void

setCue

​(

String

cue)

See the cue property definition in CSS2.

void

setCueAfter

​(

String

cueAfter)

See the cue-after property definition in CSS2.

void

setCueBefore

​(

String

cueBefore)

See the cue-before property definition in CSS2.

void

setCursor

​(

String

cursor)

See the cursor property definition in CSS2.

void

setDirection

​(

String

direction)

See the direction property definition in CSS2.

void

setDisplay

​(

String

display)

See the display property definition in CSS2.

void

setElevation

​(

String

elevation)

See the elevation property definition in CSS2.

void

setEmptyCells

​(

String

emptyCells)

See the empty-cells property definition in CSS2.

void

setFont

​(

String

font)

See the font property definition in CSS2.

void

setFontFamily

​(

String

fontFamily)

See the font-family property definition in CSS2.

void

setFontSize

​(

String

fontSize)

See the font-size property definition in CSS2.

void

setFontSizeAdjust

​(

String

fontSizeAdjust)

See the font-size-adjust property definition in CSS2.

void

setFontStretch

​(

String

fontStretch)

See the font-stretch property definition in CSS2.

void

setFontStyle

​(

String

fontStyle)

See the font-style property definition in CSS2.

void

setFontVariant

​(

String

fontVariant)

See the font-variant property definition in CSS2.

void

setFontWeight

​(

String

fontWeight)

See the font-weight property definition in CSS2.

void

setHeight

​(

String

height)

See the height property definition in CSS2.

void

setLeft

​(

String

left)

See the left property definition in CSS2.

void

setLetterSpacing

​(

String

letterSpacing)

See the letter-spacing property definition in CSS2.

void

setLineHeight

​(

String

lineHeight)

See the line-height property definition in CSS2.

void

setListStyle

​(

String

listStyle)

See the list-style property definition in CSS2.

void

setListStyleImage

​(

String

listStyleImage)

See the list-style-image property definition in CSS2.

void

setListStylePosition

​(

String

listStylePosition)

See the list-style-position property definition in CSS2.

void

setListStyleType

​(

String

listStyleType)

See the list-style-type property definition in CSS2.

void

setMargin

​(

String

margin)

See the margin property definition in CSS2.

void

setMarginBottom

​(

String

marginBottom)

See the margin-bottom property definition in CSS2.

void

setMarginLeft

​(

String

marginLeft)

See the margin-left property definition in CSS2.

void

setMarginRight

​(

String

marginRight)

See the margin-right property definition in CSS2.

void

setMarginTop

​(

String

marginTop)

See the margin-top property definition in CSS2.

void

setMarkerOffset

​(

String

markerOffset)

See the marker-offset property definition in CSS2.

void

setMarks

​(

String

marks)

See the marks property definition in CSS2.

void

setMaxHeight

​(

String

maxHeight)

See the max-height property definition in CSS2.

void

setMaxWidth

​(

String

maxWidth)

See the max-width property definition in CSS2.

void

setMinHeight

​(

String

minHeight)

See the min-height property definition in CSS2.

void

setMinWidth

​(

String

minWidth)

See the min-width property definition in CSS2.

void

setOrphans

​(

String

orphans)

See the orphans property definition in CSS2.

void

setOutline

​(

String

outline)

See the outline property definition in CSS2.

void

setOutlineColor

​(

String

outlineColor)

See the outline-color property definition in CSS2.

void

setOutlineStyle

​(

String

outlineStyle)

See the outline-style property definition in CSS2.

void

setOutlineWidth

​(

String

outlineWidth)

See the outline-width property definition in CSS2.

void

setOverflow

​(

String

overflow)

See the overflow property definition in CSS2.

void

setPadding

​(

String

padding)

See the padding property definition in CSS2.

void

setPaddingBottom

​(

String

paddingBottom)

See the padding-bottom property definition in CSS2.

void

setPaddingLeft

​(

String

paddingLeft)

See the padding-left property definition in CSS2.

void

setPaddingRight

​(

String

paddingRight)

See the padding-right property definition in CSS2.

void

setPaddingTop

​(

String

paddingTop)

See the padding-top property definition in CSS2.

void

setPage

​(

String

page)

See the page property definition in CSS2.

void

setPageBreakAfter

​(

String

pageBreakAfter)

See the page-break-after property definition in CSS2.

void

setPageBreakBefore

​(

String

pageBreakBefore)

See the page-break-before property definition in CSS2.

void

setPageBreakInside

​(

String

pageBreakInside)

See the page-break-inside property definition in CSS2.

void

setPause

​(

String

pause)

See the pause property definition in CSS2.

void

setPauseAfter

​(

String

pauseAfter)

See the pause-after property definition in CSS2.

void

setPauseBefore

​(

String

pauseBefore)

See the pause-before property definition in CSS2.

void

setPitch

​(

String

pitch)

See the pitch property definition in CSS2.

void

setPitchRange

​(

String

pitchRange)

See the pitch-range property definition in CSS2.

void

setPlayDuring

​(

String

playDuring)

See the play-during property definition in CSS2.

void

setPosition

​(

String

position)

See the position property definition in CSS2.

void

setQuotes

​(

String

quotes)

See the quotes property definition in CSS2.

void

setRichness

​(

String

richness)

See the richness property definition in CSS2.

void

setRight

​(

String

right)

See the right property definition in CSS2.

void

setSize

​(

String

size)

See the size property definition in CSS2.

void

setSpeak

​(

String

speak)

See the speak property definition in CSS2.

void

setSpeakHeader

​(

String

speakHeader)

See the speak-header property definition in CSS2.

void

setSpeakNumeral

​(

String

speakNumeral)

See the speak-numeral property definition in CSS2.

void

setSpeakPunctuation

​(

String

speakPunctuation)

See the speak-punctuation property definition in CSS2.

void

setSpeechRate

​(

String

speechRate)

See the speech-rate property definition in CSS2.

void

setStress

​(

String

stress)

See the stress property definition in CSS2.

void

setTableLayout

​(

String

tableLayout)

See the table-layout property definition in CSS2.

void

setTextAlign

​(

String

textAlign)

See the text-align property definition in CSS2.

void

setTextDecoration

​(

String

textDecoration)

See the text-decoration property definition in CSS2.

void

setTextIndent

​(

String

textIndent)

See the text-indent property definition in CSS2.

void

setTextShadow

​(

String

textShadow)

See the text-shadow property definition in CSS2.

void

setTextTransform

​(

String

textTransform)

See the text-transform property definition in CSS2.

void

setTop

​(

String

top)

See the top property definition in CSS2.

void

setUnicodeBidi

​(

String

unicodeBidi)

See the unicode-bidi property definition in CSS2.

void

setVerticalAlign

​(

String

verticalAlign)

See the vertical-align property definition in CSS2.

void

setVisibility

​(

String

visibility)

See the visibility property definition in CSS2.

void

setVoiceFamily

​(

String

voiceFamily)

See the voice-family property definition in CSS2.

void

setVolume

​(

String

volume)

See the volume property definition in CSS2.

void

setWhiteSpace

​(

String

whiteSpace)

See the white-space property definition in CSS2.

void

setWidows

​(

String

widows)

See the widows property definition in CSS2.

void

setWidth

​(

String

width)

See the width property definition in CSS2.

void

setWordSpacing

​(

String

wordSpacing)

See the word-spacing property definition in CSS2.

void

setZIndex

​(

String

zIndex)

See the z-index property definition in CSS2.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAzimuth

()

See the azimuth property definition in CSS2.

String

getBackground

()

See the background property definition in CSS2.

String

getBackgroundAttachment

()

See the background-attachment property definition in CSS2.

String

getBackgroundColor

()

See the background-color property definition in CSS2.

String

getBackgroundImage

()

See the background-image property definition in CSS2.

String

getBackgroundPosition

()

See the background-position property definition in CSS2.

String

getBackgroundRepeat

()

See the background-repeat property definition in CSS2.

String

getBorder

()

See the border property definition in CSS2.

String

getBorderBottom

()

See the border-bottom property definition in CSS2.

String

getBorderBottomColor

()

See the border-bottom-color property definition in CSS2.

String

getBorderBottomStyle

()

See the border-bottom-style property definition in CSS2.

String

getBorderBottomWidth

()

See the border-bottom-width property definition in CSS2.

String

getBorderCollapse

()

See the border-collapse property definition in CSS2.

String

getBorderColor

()

See the border-color property definition in CSS2.

String

getBorderLeft

()

See the border-left property definition in CSS2.

String

getBorderLeftColor

()

See the border-left-color property definition in CSS2.

String

getBorderLeftStyle

()

See the border-left-style property definition in CSS2.

String

getBorderLeftWidth

()

See the border-left-width property definition in CSS2.

String

getBorderRight

()

See the border-right property definition in CSS2.

String

getBorderRightColor

()

See the border-right-color property definition in CSS2.

String

getBorderRightStyle

()

See the border-right-style property definition in CSS2.

String

getBorderRightWidth

()

See the border-right-width property definition in CSS2.

String

getBorderSpacing

()

See the border-spacing property definition in CSS2.

String

getBorderStyle

()

See the border-style property definition in CSS2.

String

getBorderTop

()

See the border-top property definition in CSS2.

String

getBorderTopColor

()

See the border-top-color property definition in CSS2.

String

getBorderTopStyle

()

See the border-top-style property definition in CSS2.

String

getBorderTopWidth

()

See the border-top-width property definition in CSS2.

String

getBorderWidth

()

See the border-width property definition in CSS2.

String

getBottom

()

See the bottom property definition in CSS2.

String

getCaptionSide

()

See the caption-side property definition in CSS2.

String

getClear

()

See the clear property definition in CSS2.

String

getClip

()

See the clip property definition in CSS2.

String

getColor

()

See the color property definition in CSS2.

String

getContent

()

See the content property definition in CSS2.

String

getCounterIncrement

()

See the counter-increment property definition in CSS2.

String

getCounterReset

()

See the counter-reset property definition in CSS2.

String

getCssFloat

()

See the float property definition in CSS2.

String

getCue

()

See the cue property definition in CSS2.

String

getCueAfter

()

See the cue-after property definition in CSS2.

String

getCueBefore

()

See the cue-before property definition in CSS2.

String

getCursor

()

See the cursor property definition in CSS2.

String

getDirection

()

See the direction property definition in CSS2.

String

getDisplay

()

See the display property definition in CSS2.

String

getElevation

()

See the elevation property definition in CSS2.

String

getEmptyCells

()

See the empty-cells property definition in CSS2.

String

getFont

()

See the font property definition in CSS2.

String

getFontFamily

()

See the font-family property definition in CSS2.

String

getFontSize

()

See the font-size property definition in CSS2.

String

getFontSizeAdjust

()

See the font-size-adjust property definition in CSS2.

String

getFontStretch

()

See the font-stretch property definition in CSS2.

String

getFontStyle

()

See the font-style property definition in CSS2.

String

getFontVariant

()

See the font-variant property definition in CSS2.

String

getFontWeight

()

See the font-weight property definition in CSS2.

String

getHeight

()

See the height property definition in CSS2.

String

getLeft

()

See the left property definition in CSS2.

String

getLetterSpacing

()

See the letter-spacing property definition in CSS2.

String

getLineHeight

()

See the line-height property definition in CSS2.

String

getListStyle

()

See the list-style property definition in CSS2.

String

getListStyleImage

()

See the list-style-image property definition in CSS2.

String

getListStylePosition

()

See the list-style-position property definition in CSS2.

String

getListStyleType

()

See the list-style-type property definition in CSS2.

String

getMargin

()

See the margin property definition in CSS2.

String

getMarginBottom

()

See the margin-bottom property definition in CSS2.

String

getMarginLeft

()

See the margin-left property definition in CSS2.

String

getMarginRight

()

See the margin-right property definition in CSS2.

String

getMarginTop

()

See the margin-top property definition in CSS2.

String

getMarkerOffset

()

See the marker-offset property definition in CSS2.

String

getMarks

()

See the marks property definition in CSS2.

String

getMaxHeight

()

See the max-height property definition in CSS2.

String

getMaxWidth

()

See the max-width property definition in CSS2.

String

getMinHeight

()

See the min-height property definition in CSS2.

String

getMinWidth

()

See the min-width property definition in CSS2.

String

getOrphans

()

See the orphans property definition in CSS2.

String

getOutline

()

See the outline property definition in CSS2.

String

getOutlineColor

()

See the outline-color property definition in CSS2.

String

getOutlineStyle

()

See the outline-style property definition in CSS2.

String

getOutlineWidth

()

See the outline-width property definition in CSS2.

String

getOverflow

()

See the overflow property definition in CSS2.

String

getPadding

()

See the padding property definition in CSS2.

String

getPaddingBottom

()

See the padding-bottom property definition in CSS2.

String

getPaddingLeft

()

See the padding-left property definition in CSS2.

String

getPaddingRight

()

See the padding-right property definition in CSS2.

String

getPaddingTop

()

See the padding-top property definition in CSS2.

String

getPage

()

See the page property definition in CSS2.

String

getPageBreakAfter

()

See the page-break-after property definition in CSS2.

String

getPageBreakBefore

()

See the page-break-before property definition in CSS2.

String

getPageBreakInside

()

See the page-break-inside property definition in CSS2.

String

getPause

()

See the pause property definition in CSS2.

String

getPauseAfter

()

See the pause-after property definition in CSS2.

String

getPauseBefore

()

See the pause-before property definition in CSS2.

String

getPitch

()

See the pitch property definition in CSS2.

String

getPitchRange

()

See the pitch-range property definition in CSS2.

String

getPlayDuring

()

See the play-during property definition in CSS2.

String

getPosition

()

See the position property definition in CSS2.

String

getQuotes

()

See the quotes property definition in CSS2.

String

getRichness

()

See the richness property definition in CSS2.

String

getRight

()

See the right property definition in CSS2.

String

getSize

()

See the size property definition in CSS2.

String

getSpeak

()

See the speak property definition in CSS2.

String

getSpeakHeader

()

See the speak-header property definition in CSS2.

String

getSpeakNumeral

()

See the speak-numeral property definition in CSS2.

String

getSpeakPunctuation

()

See the speak-punctuation property definition in CSS2.

String

getSpeechRate

()

See the speech-rate property definition in CSS2.

String

getStress

()

See the stress property definition in CSS2.

String

getTableLayout

()

See the table-layout property definition in CSS2.

String

getTextAlign

()

See the text-align property definition in CSS2.

String

getTextDecoration

()

See the text-decoration property definition in CSS2.

String

getTextIndent

()

See the text-indent property definition in CSS2.

String

getTextShadow

()

See the text-shadow property definition in CSS2.

String

getTextTransform

()

See the text-transform property definition in CSS2.

String

getTop

()

See the top property definition in CSS2.

String

getUnicodeBidi

()

See the unicode-bidi property definition in CSS2.

String

getVerticalAlign

()

See the vertical-align property definition in CSS2.

String

getVisibility

()

See the visibility property definition in CSS2.

String

getVoiceFamily

()

See the voice-family property definition in CSS2.

String

getVolume

()

See the volume property definition in CSS2.

String

getWhiteSpace

()

See the white-space property definition in CSS2.

String

getWidows

()

See the widows property definition in CSS2.

String

getWidth

()

See the width property definition in CSS2.

String

getWordSpacing

()

See the word-spacing property definition in CSS2.

String

getZIndex

()

See the z-index property definition in CSS2.

void

setAzimuth

​(

String

azimuth)

See the azimuth property definition in CSS2.

void

setBackground

​(

String

background)

See the background property definition in CSS2.

void

setBackgroundAttachment

​(

String

backgroundAttachment)

See the background-attachment property definition in CSS2.

void

setBackgroundColor

​(

String

backgroundColor)

See the background-color property definition in CSS2.

void

setBackgroundImage

​(

String

backgroundImage)

See the background-image property definition in CSS2.

void

setBackgroundPosition

​(

String

backgroundPosition)

See the background-position property definition in CSS2.

void

setBackgroundRepeat

​(

String

backgroundRepeat)

See the background-repeat property definition in CSS2.

void

setBorder

​(

String

border)

See the border property definition in CSS2.

void

setBorderBottom

​(

String

borderBottom)

See the border-bottom property definition in CSS2.

void

setBorderBottomColor

​(

String

borderBottomColor)

See the border-bottom-color property definition in CSS2.

void

setBorderBottomStyle

​(

String

borderBottomStyle)

See the border-bottom-style property definition in CSS2.

void

setBorderBottomWidth

​(

String

borderBottomWidth)

See the border-bottom-width property definition in CSS2.

void

setBorderCollapse

​(

String

borderCollapse)

See the border-collapse property definition in CSS2.

void

setBorderColor

​(

String

borderColor)

See the border-color property definition in CSS2.

void

setBorderLeft

​(

String

borderLeft)

See the border-left property definition in CSS2.

void

setBorderLeftColor

​(

String

borderLeftColor)

See the border-left-color property definition in CSS2.

void

setBorderLeftStyle

​(

String

borderLeftStyle)

See the border-left-style property definition in CSS2.

void

setBorderLeftWidth

​(

String

borderLeftWidth)

See the border-left-width property definition in CSS2.

void

setBorderRight

​(

String

borderRight)

See the border-right property definition in CSS2.

void

setBorderRightColor

​(

String

borderRightColor)

See the border-right-color property definition in CSS2.

void

setBorderRightStyle

​(

String

borderRightStyle)

See the border-right-style property definition in CSS2.

void

setBorderRightWidth

​(

String

borderRightWidth)

See the border-right-width property definition in CSS2.

void

setBorderSpacing

​(

String

borderSpacing)

See the border-spacing property definition in CSS2.

void

setBorderStyle

​(

String

borderStyle)

See the border-style property definition in CSS2.

void

setBorderTop

​(

String

borderTop)

See the border-top property definition in CSS2.

void

setBorderTopColor

​(

String

borderTopColor)

See the border-top-color property definition in CSS2.

void

setBorderTopStyle

​(

String

borderTopStyle)

See the border-top-style property definition in CSS2.

void

setBorderTopWidth

​(

String

borderTopWidth)

See the border-top-width property definition in CSS2.

void

setBorderWidth

​(

String

borderWidth)

See the border-width property definition in CSS2.

void

setBottom

​(

String

bottom)

See the bottom property definition in CSS2.

void

setCaptionSide

​(

String

captionSide)

See the caption-side property definition in CSS2.

void

setClear

​(

String

clear)

See the clear property definition in CSS2.

void

setClip

​(

String

clip)

See the clip property definition in CSS2.

void

setColor

​(

String

color)

See the color property definition in CSS2.

void

setContent

​(

String

content)

See the content property definition in CSS2.

void

setCounterIncrement

​(

String

counterIncrement)

See the counter-increment property definition in CSS2.

void

setCounterReset

​(

String

counterReset)

See the counter-reset property definition in CSS2.

void

setCssFloat

​(

String

cssFloat)

See the float property definition in CSS2.

void

setCue

​(

String

cue)

See the cue property definition in CSS2.

void

setCueAfter

​(

String

cueAfter)

See the cue-after property definition in CSS2.

void

setCueBefore

​(

String

cueBefore)

See the cue-before property definition in CSS2.

void

setCursor

​(

String

cursor)

See the cursor property definition in CSS2.

void

setDirection

​(

String

direction)

See the direction property definition in CSS2.

void

setDisplay

​(

String

display)

See the display property definition in CSS2.

void

setElevation

​(

String

elevation)

See the elevation property definition in CSS2.

void

setEmptyCells

​(

String

emptyCells)

See the empty-cells property definition in CSS2.

void

setFont

​(

String

font)

See the font property definition in CSS2.

void

setFontFamily

​(

String

fontFamily)

See the font-family property definition in CSS2.

void

setFontSize

​(

String

fontSize)

See the font-size property definition in CSS2.

void

setFontSizeAdjust

​(

String

fontSizeAdjust)

See the font-size-adjust property definition in CSS2.

void

setFontStretch

​(

String

fontStretch)

See the font-stretch property definition in CSS2.

void

setFontStyle

​(

String

fontStyle)

See the font-style property definition in CSS2.

void

setFontVariant

​(

String

fontVariant)

See the font-variant property definition in CSS2.

void

setFontWeight

​(

String

fontWeight)

See the font-weight property definition in CSS2.

void

setHeight

​(

String

height)

See the height property definition in CSS2.

void

setLeft

​(

String

left)

See the left property definition in CSS2.

void

setLetterSpacing

​(

String

letterSpacing)

See the letter-spacing property definition in CSS2.

void

setLineHeight

​(

String

lineHeight)

See the line-height property definition in CSS2.

void

setListStyle

​(

String

listStyle)

See the list-style property definition in CSS2.

void

setListStyleImage

​(

String

listStyleImage)

See the list-style-image property definition in CSS2.

void

setListStylePosition

​(

String

listStylePosition)

See the list-style-position property definition in CSS2.

void

setListStyleType

​(

String

listStyleType)

See the list-style-type property definition in CSS2.

void

setMargin

​(

String

margin)

See the margin property definition in CSS2.

void

setMarginBottom

​(

String

marginBottom)

See the margin-bottom property definition in CSS2.

void

setMarginLeft

​(

String

marginLeft)

See the margin-left property definition in CSS2.

void

setMarginRight

​(

String

marginRight)

See the margin-right property definition in CSS2.

void

setMarginTop

​(

String

marginTop)

See the margin-top property definition in CSS2.

void

setMarkerOffset

​(

String

markerOffset)

See the marker-offset property definition in CSS2.

void

setMarks

​(

String

marks)

See the marks property definition in CSS2.

void

setMaxHeight

​(

String

maxHeight)

See the max-height property definition in CSS2.

void

setMaxWidth

​(

String

maxWidth)

See the max-width property definition in CSS2.

void

setMinHeight

​(

String

minHeight)

See the min-height property definition in CSS2.

void

setMinWidth

​(

String

minWidth)

See the min-width property definition in CSS2.

void

setOrphans

​(

String

orphans)

See the orphans property definition in CSS2.

void

setOutline

​(

String

outline)

See the outline property definition in CSS2.

void

setOutlineColor

​(

String

outlineColor)

See the outline-color property definition in CSS2.

void

setOutlineStyle

​(

String

outlineStyle)

See the outline-style property definition in CSS2.

void

setOutlineWidth

​(

String

outlineWidth)

See the outline-width property definition in CSS2.

void

setOverflow

​(

String

overflow)

See the overflow property definition in CSS2.

void

setPadding

​(

String

padding)

See the padding property definition in CSS2.

void

setPaddingBottom

​(

String

paddingBottom)

See the padding-bottom property definition in CSS2.

void

setPaddingLeft

​(

String

paddingLeft)

See the padding-left property definition in CSS2.

void

setPaddingRight

​(

String

paddingRight)

See the padding-right property definition in CSS2.

void

setPaddingTop

​(

String

paddingTop)

See the padding-top property definition in CSS2.

void

setPage

​(

String

page)

See the page property definition in CSS2.

void

setPageBreakAfter

​(

String

pageBreakAfter)

See the page-break-after property definition in CSS2.

void

setPageBreakBefore

​(

String

pageBreakBefore)

See the page-break-before property definition in CSS2.

void

setPageBreakInside

​(

String

pageBreakInside)

See the page-break-inside property definition in CSS2.

void

setPause

​(

String

pause)

See the pause property definition in CSS2.

void

setPauseAfter

​(

String

pauseAfter)

See the pause-after property definition in CSS2.

void

setPauseBefore

​(

String

pauseBefore)

See the pause-before property definition in CSS2.

void

setPitch

​(

String

pitch)

See the pitch property definition in CSS2.

void

setPitchRange

​(

String

pitchRange)

See the pitch-range property definition in CSS2.

void

setPlayDuring

​(

String

playDuring)

See the play-during property definition in CSS2.

void

setPosition

​(

String

position)

See the position property definition in CSS2.

void

setQuotes

​(

String

quotes)

See the quotes property definition in CSS2.

void

setRichness

​(

String

richness)

See the richness property definition in CSS2.

void

setRight

​(

String

right)

See the right property definition in CSS2.

void

setSize

​(

String

size)

See the size property definition in CSS2.

void

setSpeak

​(

String

speak)

See the speak property definition in CSS2.

void

setSpeakHeader

​(

String

speakHeader)

See the speak-header property definition in CSS2.

void

setSpeakNumeral

​(

String

speakNumeral)

See the speak-numeral property definition in CSS2.

void

setSpeakPunctuation

​(

String

speakPunctuation)

See the speak-punctuation property definition in CSS2.

void

setSpeechRate

​(

String

speechRate)

See the speech-rate property definition in CSS2.

void

setStress

​(

String

stress)

See the stress property definition in CSS2.

void

setTableLayout

​(

String

tableLayout)

See the table-layout property definition in CSS2.

void

setTextAlign

​(

String

textAlign)

See the text-align property definition in CSS2.

void

setTextDecoration

​(

String

textDecoration)

See the text-decoration property definition in CSS2.

void

setTextIndent

​(

String

textIndent)

See the text-indent property definition in CSS2.

void

setTextShadow

​(

String

textShadow)

See the text-shadow property definition in CSS2.

void

setTextTransform

​(

String

textTransform)

See the text-transform property definition in CSS2.

void

setTop

​(

String

top)

See the top property definition in CSS2.

void

setUnicodeBidi

​(

String

unicodeBidi)

See the unicode-bidi property definition in CSS2.

void

setVerticalAlign

​(

String

verticalAlign)

See the vertical-align property definition in CSS2.

void

setVisibility

​(

String

visibility)

See the visibility property definition in CSS2.

void

setVoiceFamily

​(

String

voiceFamily)

See the voice-family property definition in CSS2.

void

setVolume

​(

String

volume)

See the volume property definition in CSS2.

void

setWhiteSpace

​(

String

whiteSpace)

See the white-space property definition in CSS2.

void

setWidows

​(

String

widows)

See the widows property definition in CSS2.

void

setWidth

​(

String

width)

See the width property definition in CSS2.

void

setWordSpacing

​(

String

wordSpacing)

See the word-spacing property definition in CSS2.

void

setZIndex

​(

String

zIndex)

See the z-index property definition in CSS2.

---

#### Method Summary

See the azimuth property definition in CSS2.

See the background property definition in CSS2.

See the background-attachment property definition in CSS2.

See the background-color property definition in CSS2.

See the background-image property definition in CSS2.

See the background-position property definition in CSS2.

See the background-repeat property definition in CSS2.

See the border property definition in CSS2.

See the border-bottom property definition in CSS2.

See the border-bottom-color property definition in CSS2.

See the border-bottom-style property definition in CSS2.

See the border-bottom-width property definition in CSS2.

See the border-collapse property definition in CSS2.

See the border-color property definition in CSS2.

See the border-left property definition in CSS2.

See the border-left-color property definition in CSS2.

See the border-left-style property definition in CSS2.

See the border-left-width property definition in CSS2.

See the border-right property definition in CSS2.

See the border-right-color property definition in CSS2.

See the border-right-style property definition in CSS2.

See the border-right-width property definition in CSS2.

See the border-spacing property definition in CSS2.

See the border-style property definition in CSS2.

See the border-top property definition in CSS2.

See the border-top-color property definition in CSS2.

See the border-top-style property definition in CSS2.

See the border-top-width property definition in CSS2.

See the border-width property definition in CSS2.

See the bottom property definition in CSS2.

See the caption-side property definition in CSS2.

See the clear property definition in CSS2.

See the clip property definition in CSS2.

See the color property definition in CSS2.

See the content property definition in CSS2.

See the counter-increment property definition in CSS2.

See the counter-reset property definition in CSS2.

See the float property definition in CSS2.

See the cue property definition in CSS2.

See the cue-after property definition in CSS2.

See the cue-before property definition in CSS2.

See the cursor property definition in CSS2.

See the direction property definition in CSS2.

See the display property definition in CSS2.

See the elevation property definition in CSS2.

See the empty-cells property definition in CSS2.

See the font property definition in CSS2.

See the font-family property definition in CSS2.

See the font-size property definition in CSS2.

See the font-size-adjust property definition in CSS2.

See the font-stretch property definition in CSS2.

See the font-style property definition in CSS2.

See the font-variant property definition in CSS2.

See the font-weight property definition in CSS2.

See the height property definition in CSS2.

See the left property definition in CSS2.

See the letter-spacing property definition in CSS2.

See the line-height property definition in CSS2.

See the list-style property definition in CSS2.

See the list-style-image property definition in CSS2.

See the list-style-position property definition in CSS2.

See the list-style-type property definition in CSS2.

See the margin property definition in CSS2.

See the margin-bottom property definition in CSS2.

See the margin-left property definition in CSS2.

See the margin-right property definition in CSS2.

See the margin-top property definition in CSS2.

See the marker-offset property definition in CSS2.

See the marks property definition in CSS2.

See the max-height property definition in CSS2.

See the max-width property definition in CSS2.

See the min-height property definition in CSS2.

See the min-width property definition in CSS2.

See the orphans property definition in CSS2.

See the outline property definition in CSS2.

See the outline-color property definition in CSS2.

See the outline-style property definition in CSS2.

See the outline-width property definition in CSS2.

See the overflow property definition in CSS2.

See the padding property definition in CSS2.

See the padding-bottom property definition in CSS2.

See the padding-left property definition in CSS2.

See the padding-right property definition in CSS2.

See the padding-top property definition in CSS2.

See the page property definition in CSS2.

See the page-break-after property definition in CSS2.

See the page-break-before property definition in CSS2.

See the page-break-inside property definition in CSS2.

See the pause property definition in CSS2.

See the pause-after property definition in CSS2.

See the pause-before property definition in CSS2.

See the pitch property definition in CSS2.

See the pitch-range property definition in CSS2.

See the play-during property definition in CSS2.

See the position property definition in CSS2.

See the quotes property definition in CSS2.

See the richness property definition in CSS2.

See the right property definition in CSS2.

See the size property definition in CSS2.

See the speak property definition in CSS2.

See the speak-header property definition in CSS2.

See the speak-numeral property definition in CSS2.

See the speak-punctuation property definition in CSS2.

See the speech-rate property definition in CSS2.

See the stress property definition in CSS2.

See the table-layout property definition in CSS2.

See the text-align property definition in CSS2.

See the text-decoration property definition in CSS2.

See the text-indent property definition in CSS2.

See the text-shadow property definition in CSS2.

See the text-transform property definition in CSS2.

See the top property definition in CSS2.

See the unicode-bidi property definition in CSS2.

See the vertical-align property definition in CSS2.

See the visibility property definition in CSS2.

See the voice-family property definition in CSS2.

See the volume property definition in CSS2.

See the white-space property definition in CSS2.

See the widows property definition in CSS2.

See the width property definition in CSS2.

See the word-spacing property definition in CSS2.

See the z-index property definition in CSS2.

============ METHOD DETAIL ==========

- Method Detail

- getAzimuth

```java
String
getAzimuth()
```

See the azimuth property definition in CSS2.

- setAzimuth

```java
void setAzimuth​(
String
azimuth)
throws
DOMException
```

See the azimuth property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackground

```java
String
getBackground()
```

See the background property definition in CSS2.

- setBackground

```java
void setBackground​(
String
background)
throws
DOMException
```

See the background property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundAttachment

```java
String
getBackgroundAttachment()
```

See the background-attachment property definition in CSS2.

- setBackgroundAttachment

```java
void setBackgroundAttachment​(
String
backgroundAttachment)
throws
DOMException
```

See the background-attachment property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundColor

```java
String
getBackgroundColor()
```

See the background-color property definition in CSS2.

- setBackgroundColor

```java
void setBackgroundColor​(
String
backgroundColor)
throws
DOMException
```

See the background-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundImage

```java
String
getBackgroundImage()
```

See the background-image property definition in CSS2.

- setBackgroundImage

```java
void setBackgroundImage​(
String
backgroundImage)
throws
DOMException
```

See the background-image property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundPosition

```java
String
getBackgroundPosition()
```

See the background-position property definition in CSS2.

- setBackgroundPosition

```java
void setBackgroundPosition​(
String
backgroundPosition)
throws
DOMException
```

See the background-position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundRepeat

```java
String
getBackgroundRepeat()
```

See the background-repeat property definition in CSS2.

- setBackgroundRepeat

```java
void setBackgroundRepeat​(
String
backgroundRepeat)
throws
DOMException
```

See the background-repeat property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorder

```java
String
getBorder()
```

See the border property definition in CSS2.

- setBorder

```java
void setBorder​(
String
border)
throws
DOMException
```

See the border property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderCollapse

```java
String
getBorderCollapse()
```

See the border-collapse property definition in CSS2.

- setBorderCollapse

```java
void setBorderCollapse​(
String
borderCollapse)
throws
DOMException
```

See the border-collapse property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderColor

```java
String
getBorderColor()
```

See the border-color property definition in CSS2.

- setBorderColor

```java
void setBorderColor​(
String
borderColor)
throws
DOMException
```

See the border-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderSpacing

```java
String
getBorderSpacing()
```

See the border-spacing property definition in CSS2.

- setBorderSpacing

```java
void setBorderSpacing​(
String
borderSpacing)
throws
DOMException
```

See the border-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderStyle

```java
String
getBorderStyle()
```

See the border-style property definition in CSS2.

- setBorderStyle

```java
void setBorderStyle​(
String
borderStyle)
throws
DOMException
```

See the border-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTop

```java
String
getBorderTop()
```

See the border-top property definition in CSS2.

- setBorderTop

```java
void setBorderTop​(
String
borderTop)
throws
DOMException
```

See the border-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRight

```java
String
getBorderRight()
```

See the border-right property definition in CSS2.

- setBorderRight

```java
void setBorderRight​(
String
borderRight)
throws
DOMException
```

See the border-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottom

```java
String
getBorderBottom()
```

See the border-bottom property definition in CSS2.

- setBorderBottom

```java
void setBorderBottom​(
String
borderBottom)
throws
DOMException
```

See the border-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeft

```java
String
getBorderLeft()
```

See the border-left property definition in CSS2.

- setBorderLeft

```java
void setBorderLeft​(
String
borderLeft)
throws
DOMException
```

See the border-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTopColor

```java
String
getBorderTopColor()
```

See the border-top-color property definition in CSS2.

- setBorderTopColor

```java
void setBorderTopColor​(
String
borderTopColor)
throws
DOMException
```

See the border-top-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRightColor

```java
String
getBorderRightColor()
```

See the border-right-color property definition in CSS2.

- setBorderRightColor

```java
void setBorderRightColor​(
String
borderRightColor)
throws
DOMException
```

See the border-right-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottomColor

```java
String
getBorderBottomColor()
```

See the border-bottom-color property definition in CSS2.

- setBorderBottomColor

```java
void setBorderBottomColor​(
String
borderBottomColor)
throws
DOMException
```

See the border-bottom-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeftColor

```java
String
getBorderLeftColor()
```

See the border-left-color property definition in CSS2.

- setBorderLeftColor

```java
void setBorderLeftColor​(
String
borderLeftColor)
throws
DOMException
```

See the border-left-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTopStyle

```java
String
getBorderTopStyle()
```

See the border-top-style property definition in CSS2.

- setBorderTopStyle

```java
void setBorderTopStyle​(
String
borderTopStyle)
throws
DOMException
```

See the border-top-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRightStyle

```java
String
getBorderRightStyle()
```

See the border-right-style property definition in CSS2.

- setBorderRightStyle

```java
void setBorderRightStyle​(
String
borderRightStyle)
throws
DOMException
```

See the border-right-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottomStyle

```java
String
getBorderBottomStyle()
```

See the border-bottom-style property definition in CSS2.

- setBorderBottomStyle

```java
void setBorderBottomStyle​(
String
borderBottomStyle)
throws
DOMException
```

See the border-bottom-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeftStyle

```java
String
getBorderLeftStyle()
```

See the border-left-style property definition in CSS2.

- setBorderLeftStyle

```java
void setBorderLeftStyle​(
String
borderLeftStyle)
throws
DOMException
```

See the border-left-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTopWidth

```java
String
getBorderTopWidth()
```

See the border-top-width property definition in CSS2.

- setBorderTopWidth

```java
void setBorderTopWidth​(
String
borderTopWidth)
throws
DOMException
```

See the border-top-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRightWidth

```java
String
getBorderRightWidth()
```

See the border-right-width property definition in CSS2.

- setBorderRightWidth

```java
void setBorderRightWidth​(
String
borderRightWidth)
throws
DOMException
```

See the border-right-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottomWidth

```java
String
getBorderBottomWidth()
```

See the border-bottom-width property definition in CSS2.

- setBorderBottomWidth

```java
void setBorderBottomWidth​(
String
borderBottomWidth)
throws
DOMException
```

See the border-bottom-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeftWidth

```java
String
getBorderLeftWidth()
```

See the border-left-width property definition in CSS2.

- setBorderLeftWidth

```java
void setBorderLeftWidth​(
String
borderLeftWidth)
throws
DOMException
```

See the border-left-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderWidth

```java
String
getBorderWidth()
```

See the border-width property definition in CSS2.

- setBorderWidth

```java
void setBorderWidth​(
String
borderWidth)
throws
DOMException
```

See the border-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBottom

```java
String
getBottom()
```

See the bottom property definition in CSS2.

- setBottom

```java
void setBottom​(
String
bottom)
throws
DOMException
```

See the bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCaptionSide

```java
String
getCaptionSide()
```

See the caption-side property definition in CSS2.

- setCaptionSide

```java
void setCaptionSide​(
String
captionSide)
throws
DOMException
```

See the caption-side property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getClear

```java
String
getClear()
```

See the clear property definition in CSS2.

- setClear

```java
void setClear​(
String
clear)
throws
DOMException
```

See the clear property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getClip

```java
String
getClip()
```

See the clip property definition in CSS2.

- setClip

```java
void setClip​(
String
clip)
throws
DOMException
```

See the clip property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getColor

```java
String
getColor()
```

See the color property definition in CSS2.

- setColor

```java
void setColor​(
String
color)
throws
DOMException
```

See the color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getContent

```java
String
getContent()
```

See the content property definition in CSS2.

- setContent

```java
void setContent​(
String
content)
throws
DOMException
```

See the content property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCounterIncrement

```java
String
getCounterIncrement()
```

See the counter-increment property definition in CSS2.

- setCounterIncrement

```java
void setCounterIncrement​(
String
counterIncrement)
throws
DOMException
```

See the counter-increment property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCounterReset

```java
String
getCounterReset()
```

See the counter-reset property definition in CSS2.

- setCounterReset

```java
void setCounterReset​(
String
counterReset)
throws
DOMException
```

See the counter-reset property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCue

```java
String
getCue()
```

See the cue property definition in CSS2.

- setCue

```java
void setCue​(
String
cue)
throws
DOMException
```

See the cue property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCueAfter

```java
String
getCueAfter()
```

See the cue-after property definition in CSS2.

- setCueAfter

```java
void setCueAfter​(
String
cueAfter)
throws
DOMException
```

See the cue-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCueBefore

```java
String
getCueBefore()
```

See the cue-before property definition in CSS2.

- setCueBefore

```java
void setCueBefore​(
String
cueBefore)
throws
DOMException
```

See the cue-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCursor

```java
String
getCursor()
```

See the cursor property definition in CSS2.

- setCursor

```java
void setCursor​(
String
cursor)
throws
DOMException
```

See the cursor property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getDirection

```java
String
getDirection()
```

See the direction property definition in CSS2.

- setDirection

```java
void setDirection​(
String
direction)
throws
DOMException
```

See the direction property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getDisplay

```java
String
getDisplay()
```

See the display property definition in CSS2.

- setDisplay

```java
void setDisplay​(
String
display)
throws
DOMException
```

See the display property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getElevation

```java
String
getElevation()
```

See the elevation property definition in CSS2.

- setElevation

```java
void setElevation​(
String
elevation)
throws
DOMException
```

See the elevation property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getEmptyCells

```java
String
getEmptyCells()
```

See the empty-cells property definition in CSS2.

- setEmptyCells

```java
void setEmptyCells​(
String
emptyCells)
throws
DOMException
```

See the empty-cells property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCssFloat

```java
String
getCssFloat()
```

See the float property definition in CSS2.

- setCssFloat

```java
void setCssFloat​(
String
cssFloat)
throws
DOMException
```

See the float property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFont

```java
String
getFont()
```

See the font property definition in CSS2.

- setFont

```java
void setFont​(
String
font)
throws
DOMException
```

See the font property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontFamily

```java
String
getFontFamily()
```

See the font-family property definition in CSS2.

- setFontFamily

```java
void setFontFamily​(
String
fontFamily)
throws
DOMException
```

See the font-family property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontSize

```java
String
getFontSize()
```

See the font-size property definition in CSS2.

- setFontSize

```java
void setFontSize​(
String
fontSize)
throws
DOMException
```

See the font-size property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontSizeAdjust

```java
String
getFontSizeAdjust()
```

See the font-size-adjust property definition in CSS2.

- setFontSizeAdjust

```java
void setFontSizeAdjust​(
String
fontSizeAdjust)
throws
DOMException
```

See the font-size-adjust property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontStretch

```java
String
getFontStretch()
```

See the font-stretch property definition in CSS2.

- setFontStretch

```java
void setFontStretch​(
String
fontStretch)
throws
DOMException
```

See the font-stretch property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontStyle

```java
String
getFontStyle()
```

See the font-style property definition in CSS2.

- setFontStyle

```java
void setFontStyle​(
String
fontStyle)
throws
DOMException
```

See the font-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontVariant

```java
String
getFontVariant()
```

See the font-variant property definition in CSS2.

- setFontVariant

```java
void setFontVariant​(
String
fontVariant)
throws
DOMException
```

See the font-variant property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontWeight

```java
String
getFontWeight()
```

See the font-weight property definition in CSS2.

- setFontWeight

```java
void setFontWeight​(
String
fontWeight)
throws
DOMException
```

See the font-weight property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getHeight

```java
String
getHeight()
```

See the height property definition in CSS2.

- setHeight

```java
void setHeight​(
String
height)
throws
DOMException
```

See the height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getLeft

```java
String
getLeft()
```

See the left property definition in CSS2.

- setLeft

```java
void setLeft​(
String
left)
throws
DOMException
```

See the left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getLetterSpacing

```java
String
getLetterSpacing()
```

See the letter-spacing property definition in CSS2.

- setLetterSpacing

```java
void setLetterSpacing​(
String
letterSpacing)
throws
DOMException
```

See the letter-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getLineHeight

```java
String
getLineHeight()
```

See the line-height property definition in CSS2.

- setLineHeight

```java
void setLineHeight​(
String
lineHeight)
throws
DOMException
```

See the line-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStyle

```java
String
getListStyle()
```

See the list-style property definition in CSS2.

- setListStyle

```java
void setListStyle​(
String
listStyle)
throws
DOMException
```

See the list-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStyleImage

```java
String
getListStyleImage()
```

See the list-style-image property definition in CSS2.

- setListStyleImage

```java
void setListStyleImage​(
String
listStyleImage)
throws
DOMException
```

See the list-style-image property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStylePosition

```java
String
getListStylePosition()
```

See the list-style-position property definition in CSS2.

- setListStylePosition

```java
void setListStylePosition​(
String
listStylePosition)
throws
DOMException
```

See the list-style-position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStyleType

```java
String
getListStyleType()
```

See the list-style-type property definition in CSS2.

- setListStyleType

```java
void setListStyleType​(
String
listStyleType)
throws
DOMException
```

See the list-style-type property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMargin

```java
String
getMargin()
```

See the margin property definition in CSS2.

- setMargin

```java
void setMargin​(
String
margin)
throws
DOMException
```

See the margin property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginTop

```java
String
getMarginTop()
```

See the margin-top property definition in CSS2.

- setMarginTop

```java
void setMarginTop​(
String
marginTop)
throws
DOMException
```

See the margin-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginRight

```java
String
getMarginRight()
```

See the margin-right property definition in CSS2.

- setMarginRight

```java
void setMarginRight​(
String
marginRight)
throws
DOMException
```

See the margin-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginBottom

```java
String
getMarginBottom()
```

See the margin-bottom property definition in CSS2.

- setMarginBottom

```java
void setMarginBottom​(
String
marginBottom)
throws
DOMException
```

See the margin-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginLeft

```java
String
getMarginLeft()
```

See the margin-left property definition in CSS2.

- setMarginLeft

```java
void setMarginLeft​(
String
marginLeft)
throws
DOMException
```

See the margin-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarkerOffset

```java
String
getMarkerOffset()
```

See the marker-offset property definition in CSS2.

- setMarkerOffset

```java
void setMarkerOffset​(
String
markerOffset)
throws
DOMException
```

See the marker-offset property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarks

```java
String
getMarks()
```

See the marks property definition in CSS2.

- setMarks

```java
void setMarks​(
String
marks)
throws
DOMException
```

See the marks property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMaxHeight

```java
String
getMaxHeight()
```

See the max-height property definition in CSS2.

- setMaxHeight

```java
void setMaxHeight​(
String
maxHeight)
throws
DOMException
```

See the max-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMaxWidth

```java
String
getMaxWidth()
```

See the max-width property definition in CSS2.

- setMaxWidth

```java
void setMaxWidth​(
String
maxWidth)
throws
DOMException
```

See the max-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMinHeight

```java
String
getMinHeight()
```

See the min-height property definition in CSS2.

- setMinHeight

```java
void setMinHeight​(
String
minHeight)
throws
DOMException
```

See the min-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMinWidth

```java
String
getMinWidth()
```

See the min-width property definition in CSS2.

- setMinWidth

```java
void setMinWidth​(
String
minWidth)
throws
DOMException
```

See the min-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOrphans

```java
String
getOrphans()
```

See the orphans property definition in CSS2.

- setOrphans

```java
void setOrphans​(
String
orphans)
throws
DOMException
```

See the orphans property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutline

```java
String
getOutline()
```

See the outline property definition in CSS2.

- setOutline

```java
void setOutline​(
String
outline)
throws
DOMException
```

See the outline property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutlineColor

```java
String
getOutlineColor()
```

See the outline-color property definition in CSS2.

- setOutlineColor

```java
void setOutlineColor​(
String
outlineColor)
throws
DOMException
```

See the outline-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutlineStyle

```java
String
getOutlineStyle()
```

See the outline-style property definition in CSS2.

- setOutlineStyle

```java
void setOutlineStyle​(
String
outlineStyle)
throws
DOMException
```

See the outline-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutlineWidth

```java
String
getOutlineWidth()
```

See the outline-width property definition in CSS2.

- setOutlineWidth

```java
void setOutlineWidth​(
String
outlineWidth)
throws
DOMException
```

See the outline-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOverflow

```java
String
getOverflow()
```

See the overflow property definition in CSS2.

- setOverflow

```java
void setOverflow​(
String
overflow)
throws
DOMException
```

See the overflow property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPadding

```java
String
getPadding()
```

See the padding property definition in CSS2.

- setPadding

```java
void setPadding​(
String
padding)
throws
DOMException
```

See the padding property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingTop

```java
String
getPaddingTop()
```

See the padding-top property definition in CSS2.

- setPaddingTop

```java
void setPaddingTop​(
String
paddingTop)
throws
DOMException
```

See the padding-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingRight

```java
String
getPaddingRight()
```

See the padding-right property definition in CSS2.

- setPaddingRight

```java
void setPaddingRight​(
String
paddingRight)
throws
DOMException
```

See the padding-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingBottom

```java
String
getPaddingBottom()
```

See the padding-bottom property definition in CSS2.

- setPaddingBottom

```java
void setPaddingBottom​(
String
paddingBottom)
throws
DOMException
```

See the padding-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingLeft

```java
String
getPaddingLeft()
```

See the padding-left property definition in CSS2.

- setPaddingLeft

```java
void setPaddingLeft​(
String
paddingLeft)
throws
DOMException
```

See the padding-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPage

```java
String
getPage()
```

See the page property definition in CSS2.

- setPage

```java
void setPage​(
String
page)
throws
DOMException
```

See the page property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPageBreakAfter

```java
String
getPageBreakAfter()
```

See the page-break-after property definition in CSS2.

- setPageBreakAfter

```java
void setPageBreakAfter​(
String
pageBreakAfter)
throws
DOMException
```

See the page-break-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPageBreakBefore

```java
String
getPageBreakBefore()
```

See the page-break-before property definition in CSS2.

- setPageBreakBefore

```java
void setPageBreakBefore​(
String
pageBreakBefore)
throws
DOMException
```

See the page-break-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPageBreakInside

```java
String
getPageBreakInside()
```

See the page-break-inside property definition in CSS2.

- setPageBreakInside

```java
void setPageBreakInside​(
String
pageBreakInside)
throws
DOMException
```

See the page-break-inside property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPause

```java
String
getPause()
```

See the pause property definition in CSS2.

- setPause

```java
void setPause​(
String
pause)
throws
DOMException
```

See the pause property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPauseAfter

```java
String
getPauseAfter()
```

See the pause-after property definition in CSS2.

- setPauseAfter

```java
void setPauseAfter​(
String
pauseAfter)
throws
DOMException
```

See the pause-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPauseBefore

```java
String
getPauseBefore()
```

See the pause-before property definition in CSS2.

- setPauseBefore

```java
void setPauseBefore​(
String
pauseBefore)
throws
DOMException
```

See the pause-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPitch

```java
String
getPitch()
```

See the pitch property definition in CSS2.

- setPitch

```java
void setPitch​(
String
pitch)
throws
DOMException
```

See the pitch property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPitchRange

```java
String
getPitchRange()
```

See the pitch-range property definition in CSS2.

- setPitchRange

```java
void setPitchRange​(
String
pitchRange)
throws
DOMException
```

See the pitch-range property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPlayDuring

```java
String
getPlayDuring()
```

See the play-during property definition in CSS2.

- setPlayDuring

```java
void setPlayDuring​(
String
playDuring)
throws
DOMException
```

See the play-during property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPosition

```java
String
getPosition()
```

See the position property definition in CSS2.

- setPosition

```java
void setPosition​(
String
position)
throws
DOMException
```

See the position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getQuotes

```java
String
getQuotes()
```

See the quotes property definition in CSS2.

- setQuotes

```java
void setQuotes​(
String
quotes)
throws
DOMException
```

See the quotes property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getRichness

```java
String
getRichness()
```

See the richness property definition in CSS2.

- setRichness

```java
void setRichness​(
String
richness)
throws
DOMException
```

See the richness property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getRight

```java
String
getRight()
```

See the right property definition in CSS2.

- setRight

```java
void setRight​(
String
right)
throws
DOMException
```

See the right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSize

```java
String
getSize()
```

See the size property definition in CSS2.

- setSize

```java
void setSize​(
String
size)
throws
DOMException
```

See the size property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeak

```java
String
getSpeak()
```

See the speak property definition in CSS2.

- setSpeak

```java
void setSpeak​(
String
speak)
throws
DOMException
```

See the speak property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeakHeader

```java
String
getSpeakHeader()
```

See the speak-header property definition in CSS2.

- setSpeakHeader

```java
void setSpeakHeader​(
String
speakHeader)
throws
DOMException
```

See the speak-header property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeakNumeral

```java
String
getSpeakNumeral()
```

See the speak-numeral property definition in CSS2.

- setSpeakNumeral

```java
void setSpeakNumeral​(
String
speakNumeral)
throws
DOMException
```

See the speak-numeral property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeakPunctuation

```java
String
getSpeakPunctuation()
```

See the speak-punctuation property definition in CSS2.

- setSpeakPunctuation

```java
void setSpeakPunctuation​(
String
speakPunctuation)
throws
DOMException
```

See the speak-punctuation property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeechRate

```java
String
getSpeechRate()
```

See the speech-rate property definition in CSS2.

- setSpeechRate

```java
void setSpeechRate​(
String
speechRate)
throws
DOMException
```

See the speech-rate property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getStress

```java
String
getStress()
```

See the stress property definition in CSS2.

- setStress

```java
void setStress​(
String
stress)
throws
DOMException
```

See the stress property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTableLayout

```java
String
getTableLayout()
```

See the table-layout property definition in CSS2.

- setTableLayout

```java
void setTableLayout​(
String
tableLayout)
throws
DOMException
```

See the table-layout property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextAlign

```java
String
getTextAlign()
```

See the text-align property definition in CSS2.

- setTextAlign

```java
void setTextAlign​(
String
textAlign)
throws
DOMException
```

See the text-align property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextDecoration

```java
String
getTextDecoration()
```

See the text-decoration property definition in CSS2.

- setTextDecoration

```java
void setTextDecoration​(
String
textDecoration)
throws
DOMException
```

See the text-decoration property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextIndent

```java
String
getTextIndent()
```

See the text-indent property definition in CSS2.

- setTextIndent

```java
void setTextIndent​(
String
textIndent)
throws
DOMException
```

See the text-indent property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextShadow

```java
String
getTextShadow()
```

See the text-shadow property definition in CSS2.

- setTextShadow

```java
void setTextShadow​(
String
textShadow)
throws
DOMException
```

See the text-shadow property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextTransform

```java
String
getTextTransform()
```

See the text-transform property definition in CSS2.

- setTextTransform

```java
void setTextTransform​(
String
textTransform)
throws
DOMException
```

See the text-transform property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTop

```java
String
getTop()
```

See the top property definition in CSS2.

- setTop

```java
void setTop​(
String
top)
throws
DOMException
```

See the top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getUnicodeBidi

```java
String
getUnicodeBidi()
```

See the unicode-bidi property definition in CSS2.

- setUnicodeBidi

```java
void setUnicodeBidi​(
String
unicodeBidi)
throws
DOMException
```

See the unicode-bidi property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVerticalAlign

```java
String
getVerticalAlign()
```

See the vertical-align property definition in CSS2.

- setVerticalAlign

```java
void setVerticalAlign​(
String
verticalAlign)
throws
DOMException
```

See the vertical-align property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVisibility

```java
String
getVisibility()
```

See the visibility property definition in CSS2.

- setVisibility

```java
void setVisibility​(
String
visibility)
throws
DOMException
```

See the visibility property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVoiceFamily

```java
String
getVoiceFamily()
```

See the voice-family property definition in CSS2.

- setVoiceFamily

```java
void setVoiceFamily​(
String
voiceFamily)
throws
DOMException
```

See the voice-family property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVolume

```java
String
getVolume()
```

See the volume property definition in CSS2.

- setVolume

```java
void setVolume​(
String
volume)
throws
DOMException
```

See the volume property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWhiteSpace

```java
String
getWhiteSpace()
```

See the white-space property definition in CSS2.

- setWhiteSpace

```java
void setWhiteSpace​(
String
whiteSpace)
throws
DOMException
```

See the white-space property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWidows

```java
String
getWidows()
```

See the widows property definition in CSS2.

- setWidows

```java
void setWidows​(
String
widows)
throws
DOMException
```

See the widows property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWidth

```java
String
getWidth()
```

See the width property definition in CSS2.

- setWidth

```java
void setWidth​(
String
width)
throws
DOMException
```

See the width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWordSpacing

```java
String
getWordSpacing()
```

See the word-spacing property definition in CSS2.

- setWordSpacing

```java
void setWordSpacing​(
String
wordSpacing)
throws
DOMException
```

See the word-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getZIndex

```java
String
getZIndex()
```

See the z-index property definition in CSS2.

- setZIndex

```java
void setZIndex​(
String
zIndex)
throws
DOMException
```

See the z-index property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

Method Detail

- getAzimuth

```java
String
getAzimuth()
```

See the azimuth property definition in CSS2.

- setAzimuth

```java
void setAzimuth​(
String
azimuth)
throws
DOMException
```

See the azimuth property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackground

```java
String
getBackground()
```

See the background property definition in CSS2.

- setBackground

```java
void setBackground​(
String
background)
throws
DOMException
```

See the background property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundAttachment

```java
String
getBackgroundAttachment()
```

See the background-attachment property definition in CSS2.

- setBackgroundAttachment

```java
void setBackgroundAttachment​(
String
backgroundAttachment)
throws
DOMException
```

See the background-attachment property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundColor

```java
String
getBackgroundColor()
```

See the background-color property definition in CSS2.

- setBackgroundColor

```java
void setBackgroundColor​(
String
backgroundColor)
throws
DOMException
```

See the background-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundImage

```java
String
getBackgroundImage()
```

See the background-image property definition in CSS2.

- setBackgroundImage

```java
void setBackgroundImage​(
String
backgroundImage)
throws
DOMException
```

See the background-image property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundPosition

```java
String
getBackgroundPosition()
```

See the background-position property definition in CSS2.

- setBackgroundPosition

```java
void setBackgroundPosition​(
String
backgroundPosition)
throws
DOMException
```

See the background-position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBackgroundRepeat

```java
String
getBackgroundRepeat()
```

See the background-repeat property definition in CSS2.

- setBackgroundRepeat

```java
void setBackgroundRepeat​(
String
backgroundRepeat)
throws
DOMException
```

See the background-repeat property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorder

```java
String
getBorder()
```

See the border property definition in CSS2.

- setBorder

```java
void setBorder​(
String
border)
throws
DOMException
```

See the border property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderCollapse

```java
String
getBorderCollapse()
```

See the border-collapse property definition in CSS2.

- setBorderCollapse

```java
void setBorderCollapse​(
String
borderCollapse)
throws
DOMException
```

See the border-collapse property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderColor

```java
String
getBorderColor()
```

See the border-color property definition in CSS2.

- setBorderColor

```java
void setBorderColor​(
String
borderColor)
throws
DOMException
```

See the border-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderSpacing

```java
String
getBorderSpacing()
```

See the border-spacing property definition in CSS2.

- setBorderSpacing

```java
void setBorderSpacing​(
String
borderSpacing)
throws
DOMException
```

See the border-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderStyle

```java
String
getBorderStyle()
```

See the border-style property definition in CSS2.

- setBorderStyle

```java
void setBorderStyle​(
String
borderStyle)
throws
DOMException
```

See the border-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTop

```java
String
getBorderTop()
```

See the border-top property definition in CSS2.

- setBorderTop

```java
void setBorderTop​(
String
borderTop)
throws
DOMException
```

See the border-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRight

```java
String
getBorderRight()
```

See the border-right property definition in CSS2.

- setBorderRight

```java
void setBorderRight​(
String
borderRight)
throws
DOMException
```

See the border-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottom

```java
String
getBorderBottom()
```

See the border-bottom property definition in CSS2.

- setBorderBottom

```java
void setBorderBottom​(
String
borderBottom)
throws
DOMException
```

See the border-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeft

```java
String
getBorderLeft()
```

See the border-left property definition in CSS2.

- setBorderLeft

```java
void setBorderLeft​(
String
borderLeft)
throws
DOMException
```

See the border-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTopColor

```java
String
getBorderTopColor()
```

See the border-top-color property definition in CSS2.

- setBorderTopColor

```java
void setBorderTopColor​(
String
borderTopColor)
throws
DOMException
```

See the border-top-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRightColor

```java
String
getBorderRightColor()
```

See the border-right-color property definition in CSS2.

- setBorderRightColor

```java
void setBorderRightColor​(
String
borderRightColor)
throws
DOMException
```

See the border-right-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottomColor

```java
String
getBorderBottomColor()
```

See the border-bottom-color property definition in CSS2.

- setBorderBottomColor

```java
void setBorderBottomColor​(
String
borderBottomColor)
throws
DOMException
```

See the border-bottom-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeftColor

```java
String
getBorderLeftColor()
```

See the border-left-color property definition in CSS2.

- setBorderLeftColor

```java
void setBorderLeftColor​(
String
borderLeftColor)
throws
DOMException
```

See the border-left-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTopStyle

```java
String
getBorderTopStyle()
```

See the border-top-style property definition in CSS2.

- setBorderTopStyle

```java
void setBorderTopStyle​(
String
borderTopStyle)
throws
DOMException
```

See the border-top-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRightStyle

```java
String
getBorderRightStyle()
```

See the border-right-style property definition in CSS2.

- setBorderRightStyle

```java
void setBorderRightStyle​(
String
borderRightStyle)
throws
DOMException
```

See the border-right-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottomStyle

```java
String
getBorderBottomStyle()
```

See the border-bottom-style property definition in CSS2.

- setBorderBottomStyle

```java
void setBorderBottomStyle​(
String
borderBottomStyle)
throws
DOMException
```

See the border-bottom-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeftStyle

```java
String
getBorderLeftStyle()
```

See the border-left-style property definition in CSS2.

- setBorderLeftStyle

```java
void setBorderLeftStyle​(
String
borderLeftStyle)
throws
DOMException
```

See the border-left-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderTopWidth

```java
String
getBorderTopWidth()
```

See the border-top-width property definition in CSS2.

- setBorderTopWidth

```java
void setBorderTopWidth​(
String
borderTopWidth)
throws
DOMException
```

See the border-top-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderRightWidth

```java
String
getBorderRightWidth()
```

See the border-right-width property definition in CSS2.

- setBorderRightWidth

```java
void setBorderRightWidth​(
String
borderRightWidth)
throws
DOMException
```

See the border-right-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderBottomWidth

```java
String
getBorderBottomWidth()
```

See the border-bottom-width property definition in CSS2.

- setBorderBottomWidth

```java
void setBorderBottomWidth​(
String
borderBottomWidth)
throws
DOMException
```

See the border-bottom-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderLeftWidth

```java
String
getBorderLeftWidth()
```

See the border-left-width property definition in CSS2.

- setBorderLeftWidth

```java
void setBorderLeftWidth​(
String
borderLeftWidth)
throws
DOMException
```

See the border-left-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBorderWidth

```java
String
getBorderWidth()
```

See the border-width property definition in CSS2.

- setBorderWidth

```java
void setBorderWidth​(
String
borderWidth)
throws
DOMException
```

See the border-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getBottom

```java
String
getBottom()
```

See the bottom property definition in CSS2.

- setBottom

```java
void setBottom​(
String
bottom)
throws
DOMException
```

See the bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCaptionSide

```java
String
getCaptionSide()
```

See the caption-side property definition in CSS2.

- setCaptionSide

```java
void setCaptionSide​(
String
captionSide)
throws
DOMException
```

See the caption-side property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getClear

```java
String
getClear()
```

See the clear property definition in CSS2.

- setClear

```java
void setClear​(
String
clear)
throws
DOMException
```

See the clear property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getClip

```java
String
getClip()
```

See the clip property definition in CSS2.

- setClip

```java
void setClip​(
String
clip)
throws
DOMException
```

See the clip property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getColor

```java
String
getColor()
```

See the color property definition in CSS2.

- setColor

```java
void setColor​(
String
color)
throws
DOMException
```

See the color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getContent

```java
String
getContent()
```

See the content property definition in CSS2.

- setContent

```java
void setContent​(
String
content)
throws
DOMException
```

See the content property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCounterIncrement

```java
String
getCounterIncrement()
```

See the counter-increment property definition in CSS2.

- setCounterIncrement

```java
void setCounterIncrement​(
String
counterIncrement)
throws
DOMException
```

See the counter-increment property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCounterReset

```java
String
getCounterReset()
```

See the counter-reset property definition in CSS2.

- setCounterReset

```java
void setCounterReset​(
String
counterReset)
throws
DOMException
```

See the counter-reset property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCue

```java
String
getCue()
```

See the cue property definition in CSS2.

- setCue

```java
void setCue​(
String
cue)
throws
DOMException
```

See the cue property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCueAfter

```java
String
getCueAfter()
```

See the cue-after property definition in CSS2.

- setCueAfter

```java
void setCueAfter​(
String
cueAfter)
throws
DOMException
```

See the cue-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCueBefore

```java
String
getCueBefore()
```

See the cue-before property definition in CSS2.

- setCueBefore

```java
void setCueBefore​(
String
cueBefore)
throws
DOMException
```

See the cue-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCursor

```java
String
getCursor()
```

See the cursor property definition in CSS2.

- setCursor

```java
void setCursor​(
String
cursor)
throws
DOMException
```

See the cursor property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getDirection

```java
String
getDirection()
```

See the direction property definition in CSS2.

- setDirection

```java
void setDirection​(
String
direction)
throws
DOMException
```

See the direction property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getDisplay

```java
String
getDisplay()
```

See the display property definition in CSS2.

- setDisplay

```java
void setDisplay​(
String
display)
throws
DOMException
```

See the display property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getElevation

```java
String
getElevation()
```

See the elevation property definition in CSS2.

- setElevation

```java
void setElevation​(
String
elevation)
throws
DOMException
```

See the elevation property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getEmptyCells

```java
String
getEmptyCells()
```

See the empty-cells property definition in CSS2.

- setEmptyCells

```java
void setEmptyCells​(
String
emptyCells)
throws
DOMException
```

See the empty-cells property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getCssFloat

```java
String
getCssFloat()
```

See the float property definition in CSS2.

- setCssFloat

```java
void setCssFloat​(
String
cssFloat)
throws
DOMException
```

See the float property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFont

```java
String
getFont()
```

See the font property definition in CSS2.

- setFont

```java
void setFont​(
String
font)
throws
DOMException
```

See the font property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontFamily

```java
String
getFontFamily()
```

See the font-family property definition in CSS2.

- setFontFamily

```java
void setFontFamily​(
String
fontFamily)
throws
DOMException
```

See the font-family property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontSize

```java
String
getFontSize()
```

See the font-size property definition in CSS2.

- setFontSize

```java
void setFontSize​(
String
fontSize)
throws
DOMException
```

See the font-size property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontSizeAdjust

```java
String
getFontSizeAdjust()
```

See the font-size-adjust property definition in CSS2.

- setFontSizeAdjust

```java
void setFontSizeAdjust​(
String
fontSizeAdjust)
throws
DOMException
```

See the font-size-adjust property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontStretch

```java
String
getFontStretch()
```

See the font-stretch property definition in CSS2.

- setFontStretch

```java
void setFontStretch​(
String
fontStretch)
throws
DOMException
```

See the font-stretch property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontStyle

```java
String
getFontStyle()
```

See the font-style property definition in CSS2.

- setFontStyle

```java
void setFontStyle​(
String
fontStyle)
throws
DOMException
```

See the font-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontVariant

```java
String
getFontVariant()
```

See the font-variant property definition in CSS2.

- setFontVariant

```java
void setFontVariant​(
String
fontVariant)
throws
DOMException
```

See the font-variant property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getFontWeight

```java
String
getFontWeight()
```

See the font-weight property definition in CSS2.

- setFontWeight

```java
void setFontWeight​(
String
fontWeight)
throws
DOMException
```

See the font-weight property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getHeight

```java
String
getHeight()
```

See the height property definition in CSS2.

- setHeight

```java
void setHeight​(
String
height)
throws
DOMException
```

See the height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getLeft

```java
String
getLeft()
```

See the left property definition in CSS2.

- setLeft

```java
void setLeft​(
String
left)
throws
DOMException
```

See the left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getLetterSpacing

```java
String
getLetterSpacing()
```

See the letter-spacing property definition in CSS2.

- setLetterSpacing

```java
void setLetterSpacing​(
String
letterSpacing)
throws
DOMException
```

See the letter-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getLineHeight

```java
String
getLineHeight()
```

See the line-height property definition in CSS2.

- setLineHeight

```java
void setLineHeight​(
String
lineHeight)
throws
DOMException
```

See the line-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStyle

```java
String
getListStyle()
```

See the list-style property definition in CSS2.

- setListStyle

```java
void setListStyle​(
String
listStyle)
throws
DOMException
```

See the list-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStyleImage

```java
String
getListStyleImage()
```

See the list-style-image property definition in CSS2.

- setListStyleImage

```java
void setListStyleImage​(
String
listStyleImage)
throws
DOMException
```

See the list-style-image property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStylePosition

```java
String
getListStylePosition()
```

See the list-style-position property definition in CSS2.

- setListStylePosition

```java
void setListStylePosition​(
String
listStylePosition)
throws
DOMException
```

See the list-style-position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getListStyleType

```java
String
getListStyleType()
```

See the list-style-type property definition in CSS2.

- setListStyleType

```java
void setListStyleType​(
String
listStyleType)
throws
DOMException
```

See the list-style-type property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMargin

```java
String
getMargin()
```

See the margin property definition in CSS2.

- setMargin

```java
void setMargin​(
String
margin)
throws
DOMException
```

See the margin property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginTop

```java
String
getMarginTop()
```

See the margin-top property definition in CSS2.

- setMarginTop

```java
void setMarginTop​(
String
marginTop)
throws
DOMException
```

See the margin-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginRight

```java
String
getMarginRight()
```

See the margin-right property definition in CSS2.

- setMarginRight

```java
void setMarginRight​(
String
marginRight)
throws
DOMException
```

See the margin-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginBottom

```java
String
getMarginBottom()
```

See the margin-bottom property definition in CSS2.

- setMarginBottom

```java
void setMarginBottom​(
String
marginBottom)
throws
DOMException
```

See the margin-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarginLeft

```java
String
getMarginLeft()
```

See the margin-left property definition in CSS2.

- setMarginLeft

```java
void setMarginLeft​(
String
marginLeft)
throws
DOMException
```

See the margin-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarkerOffset

```java
String
getMarkerOffset()
```

See the marker-offset property definition in CSS2.

- setMarkerOffset

```java
void setMarkerOffset​(
String
markerOffset)
throws
DOMException
```

See the marker-offset property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMarks

```java
String
getMarks()
```

See the marks property definition in CSS2.

- setMarks

```java
void setMarks​(
String
marks)
throws
DOMException
```

See the marks property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMaxHeight

```java
String
getMaxHeight()
```

See the max-height property definition in CSS2.

- setMaxHeight

```java
void setMaxHeight​(
String
maxHeight)
throws
DOMException
```

See the max-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMaxWidth

```java
String
getMaxWidth()
```

See the max-width property definition in CSS2.

- setMaxWidth

```java
void setMaxWidth​(
String
maxWidth)
throws
DOMException
```

See the max-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMinHeight

```java
String
getMinHeight()
```

See the min-height property definition in CSS2.

- setMinHeight

```java
void setMinHeight​(
String
minHeight)
throws
DOMException
```

See the min-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getMinWidth

```java
String
getMinWidth()
```

See the min-width property definition in CSS2.

- setMinWidth

```java
void setMinWidth​(
String
minWidth)
throws
DOMException
```

See the min-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOrphans

```java
String
getOrphans()
```

See the orphans property definition in CSS2.

- setOrphans

```java
void setOrphans​(
String
orphans)
throws
DOMException
```

See the orphans property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutline

```java
String
getOutline()
```

See the outline property definition in CSS2.

- setOutline

```java
void setOutline​(
String
outline)
throws
DOMException
```

See the outline property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutlineColor

```java
String
getOutlineColor()
```

See the outline-color property definition in CSS2.

- setOutlineColor

```java
void setOutlineColor​(
String
outlineColor)
throws
DOMException
```

See the outline-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutlineStyle

```java
String
getOutlineStyle()
```

See the outline-style property definition in CSS2.

- setOutlineStyle

```java
void setOutlineStyle​(
String
outlineStyle)
throws
DOMException
```

See the outline-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOutlineWidth

```java
String
getOutlineWidth()
```

See the outline-width property definition in CSS2.

- setOutlineWidth

```java
void setOutlineWidth​(
String
outlineWidth)
throws
DOMException
```

See the outline-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getOverflow

```java
String
getOverflow()
```

See the overflow property definition in CSS2.

- setOverflow

```java
void setOverflow​(
String
overflow)
throws
DOMException
```

See the overflow property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPadding

```java
String
getPadding()
```

See the padding property definition in CSS2.

- setPadding

```java
void setPadding​(
String
padding)
throws
DOMException
```

See the padding property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingTop

```java
String
getPaddingTop()
```

See the padding-top property definition in CSS2.

- setPaddingTop

```java
void setPaddingTop​(
String
paddingTop)
throws
DOMException
```

See the padding-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingRight

```java
String
getPaddingRight()
```

See the padding-right property definition in CSS2.

- setPaddingRight

```java
void setPaddingRight​(
String
paddingRight)
throws
DOMException
```

See the padding-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingBottom

```java
String
getPaddingBottom()
```

See the padding-bottom property definition in CSS2.

- setPaddingBottom

```java
void setPaddingBottom​(
String
paddingBottom)
throws
DOMException
```

See the padding-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPaddingLeft

```java
String
getPaddingLeft()
```

See the padding-left property definition in CSS2.

- setPaddingLeft

```java
void setPaddingLeft​(
String
paddingLeft)
throws
DOMException
```

See the padding-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPage

```java
String
getPage()
```

See the page property definition in CSS2.

- setPage

```java
void setPage​(
String
page)
throws
DOMException
```

See the page property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPageBreakAfter

```java
String
getPageBreakAfter()
```

See the page-break-after property definition in CSS2.

- setPageBreakAfter

```java
void setPageBreakAfter​(
String
pageBreakAfter)
throws
DOMException
```

See the page-break-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPageBreakBefore

```java
String
getPageBreakBefore()
```

See the page-break-before property definition in CSS2.

- setPageBreakBefore

```java
void setPageBreakBefore​(
String
pageBreakBefore)
throws
DOMException
```

See the page-break-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPageBreakInside

```java
String
getPageBreakInside()
```

See the page-break-inside property definition in CSS2.

- setPageBreakInside

```java
void setPageBreakInside​(
String
pageBreakInside)
throws
DOMException
```

See the page-break-inside property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPause

```java
String
getPause()
```

See the pause property definition in CSS2.

- setPause

```java
void setPause​(
String
pause)
throws
DOMException
```

See the pause property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPauseAfter

```java
String
getPauseAfter()
```

See the pause-after property definition in CSS2.

- setPauseAfter

```java
void setPauseAfter​(
String
pauseAfter)
throws
DOMException
```

See the pause-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPauseBefore

```java
String
getPauseBefore()
```

See the pause-before property definition in CSS2.

- setPauseBefore

```java
void setPauseBefore​(
String
pauseBefore)
throws
DOMException
```

See the pause-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPitch

```java
String
getPitch()
```

See the pitch property definition in CSS2.

- setPitch

```java
void setPitch​(
String
pitch)
throws
DOMException
```

See the pitch property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPitchRange

```java
String
getPitchRange()
```

See the pitch-range property definition in CSS2.

- setPitchRange

```java
void setPitchRange​(
String
pitchRange)
throws
DOMException
```

See the pitch-range property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPlayDuring

```java
String
getPlayDuring()
```

See the play-during property definition in CSS2.

- setPlayDuring

```java
void setPlayDuring​(
String
playDuring)
throws
DOMException
```

See the play-during property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getPosition

```java
String
getPosition()
```

See the position property definition in CSS2.

- setPosition

```java
void setPosition​(
String
position)
throws
DOMException
```

See the position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getQuotes

```java
String
getQuotes()
```

See the quotes property definition in CSS2.

- setQuotes

```java
void setQuotes​(
String
quotes)
throws
DOMException
```

See the quotes property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getRichness

```java
String
getRichness()
```

See the richness property definition in CSS2.

- setRichness

```java
void setRichness​(
String
richness)
throws
DOMException
```

See the richness property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getRight

```java
String
getRight()
```

See the right property definition in CSS2.

- setRight

```java
void setRight​(
String
right)
throws
DOMException
```

See the right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSize

```java
String
getSize()
```

See the size property definition in CSS2.

- setSize

```java
void setSize​(
String
size)
throws
DOMException
```

See the size property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeak

```java
String
getSpeak()
```

See the speak property definition in CSS2.

- setSpeak

```java
void setSpeak​(
String
speak)
throws
DOMException
```

See the speak property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeakHeader

```java
String
getSpeakHeader()
```

See the speak-header property definition in CSS2.

- setSpeakHeader

```java
void setSpeakHeader​(
String
speakHeader)
throws
DOMException
```

See the speak-header property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeakNumeral

```java
String
getSpeakNumeral()
```

See the speak-numeral property definition in CSS2.

- setSpeakNumeral

```java
void setSpeakNumeral​(
String
speakNumeral)
throws
DOMException
```

See the speak-numeral property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeakPunctuation

```java
String
getSpeakPunctuation()
```

See the speak-punctuation property definition in CSS2.

- setSpeakPunctuation

```java
void setSpeakPunctuation​(
String
speakPunctuation)
throws
DOMException
```

See the speak-punctuation property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getSpeechRate

```java
String
getSpeechRate()
```

See the speech-rate property definition in CSS2.

- setSpeechRate

```java
void setSpeechRate​(
String
speechRate)
throws
DOMException
```

See the speech-rate property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getStress

```java
String
getStress()
```

See the stress property definition in CSS2.

- setStress

```java
void setStress​(
String
stress)
throws
DOMException
```

See the stress property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTableLayout

```java
String
getTableLayout()
```

See the table-layout property definition in CSS2.

- setTableLayout

```java
void setTableLayout​(
String
tableLayout)
throws
DOMException
```

See the table-layout property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextAlign

```java
String
getTextAlign()
```

See the text-align property definition in CSS2.

- setTextAlign

```java
void setTextAlign​(
String
textAlign)
throws
DOMException
```

See the text-align property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextDecoration

```java
String
getTextDecoration()
```

See the text-decoration property definition in CSS2.

- setTextDecoration

```java
void setTextDecoration​(
String
textDecoration)
throws
DOMException
```

See the text-decoration property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextIndent

```java
String
getTextIndent()
```

See the text-indent property definition in CSS2.

- setTextIndent

```java
void setTextIndent​(
String
textIndent)
throws
DOMException
```

See the text-indent property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextShadow

```java
String
getTextShadow()
```

See the text-shadow property definition in CSS2.

- setTextShadow

```java
void setTextShadow​(
String
textShadow)
throws
DOMException
```

See the text-shadow property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTextTransform

```java
String
getTextTransform()
```

See the text-transform property definition in CSS2.

- setTextTransform

```java
void setTextTransform​(
String
textTransform)
throws
DOMException
```

See the text-transform property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getTop

```java
String
getTop()
```

See the top property definition in CSS2.

- setTop

```java
void setTop​(
String
top)
throws
DOMException
```

See the top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getUnicodeBidi

```java
String
getUnicodeBidi()
```

See the unicode-bidi property definition in CSS2.

- setUnicodeBidi

```java
void setUnicodeBidi​(
String
unicodeBidi)
throws
DOMException
```

See the unicode-bidi property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVerticalAlign

```java
String
getVerticalAlign()
```

See the vertical-align property definition in CSS2.

- setVerticalAlign

```java
void setVerticalAlign​(
String
verticalAlign)
throws
DOMException
```

See the vertical-align property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVisibility

```java
String
getVisibility()
```

See the visibility property definition in CSS2.

- setVisibility

```java
void setVisibility​(
String
visibility)
throws
DOMException
```

See the visibility property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVoiceFamily

```java
String
getVoiceFamily()
```

See the voice-family property definition in CSS2.

- setVoiceFamily

```java
void setVoiceFamily​(
String
voiceFamily)
throws
DOMException
```

See the voice-family property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getVolume

```java
String
getVolume()
```

See the volume property definition in CSS2.

- setVolume

```java
void setVolume​(
String
volume)
throws
DOMException
```

See the volume property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWhiteSpace

```java
String
getWhiteSpace()
```

See the white-space property definition in CSS2.

- setWhiteSpace

```java
void setWhiteSpace​(
String
whiteSpace)
throws
DOMException
```

See the white-space property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWidows

```java
String
getWidows()
```

See the widows property definition in CSS2.

- setWidows

```java
void setWidows​(
String
widows)
throws
DOMException
```

See the widows property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWidth

```java
String
getWidth()
```

See the width property definition in CSS2.

- setWidth

```java
void setWidth​(
String
width)
throws
DOMException
```

See the width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getWordSpacing

```java
String
getWordSpacing()
```

See the word-spacing property definition in CSS2.

- setWordSpacing

```java
void setWordSpacing​(
String
wordSpacing)
throws
DOMException
```

See the word-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

- getZIndex

```java
String
getZIndex()
```

See the z-index property definition in CSS2.

- setZIndex

```java
void setZIndex​(
String
zIndex)
throws
DOMException
```

See the z-index property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### Method Detail

getAzimuth

```java
String
getAzimuth()
```

See the azimuth property definition in CSS2.

---

#### getAzimuth

String

getAzimuth()

See the azimuth property definition in CSS2.

setAzimuth

```java
void setAzimuth​(
String
azimuth)
throws
DOMException
```

See the azimuth property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setAzimuth

void setAzimuth​(

String

azimuth)
throws

DOMException

See the azimuth property definition in CSS2.

getBackground

```java
String
getBackground()
```

See the background property definition in CSS2.

---

#### getBackground

String

getBackground()

See the background property definition in CSS2.

setBackground

```java
void setBackground​(
String
background)
throws
DOMException
```

See the background property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBackground

void setBackground​(

String

background)
throws

DOMException

See the background property definition in CSS2.

getBackgroundAttachment

```java
String
getBackgroundAttachment()
```

See the background-attachment property definition in CSS2.

---

#### getBackgroundAttachment

String

getBackgroundAttachment()

See the background-attachment property definition in CSS2.

setBackgroundAttachment

```java
void setBackgroundAttachment​(
String
backgroundAttachment)
throws
DOMException
```

See the background-attachment property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBackgroundAttachment

void setBackgroundAttachment​(

String

backgroundAttachment)
throws

DOMException

See the background-attachment property definition in CSS2.

getBackgroundColor

```java
String
getBackgroundColor()
```

See the background-color property definition in CSS2.

---

#### getBackgroundColor

String

getBackgroundColor()

See the background-color property definition in CSS2.

setBackgroundColor

```java
void setBackgroundColor​(
String
backgroundColor)
throws
DOMException
```

See the background-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBackgroundColor

void setBackgroundColor​(

String

backgroundColor)
throws

DOMException

See the background-color property definition in CSS2.

getBackgroundImage

```java
String
getBackgroundImage()
```

See the background-image property definition in CSS2.

---

#### getBackgroundImage

String

getBackgroundImage()

See the background-image property definition in CSS2.

setBackgroundImage

```java
void setBackgroundImage​(
String
backgroundImage)
throws
DOMException
```

See the background-image property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBackgroundImage

void setBackgroundImage​(

String

backgroundImage)
throws

DOMException

See the background-image property definition in CSS2.

getBackgroundPosition

```java
String
getBackgroundPosition()
```

See the background-position property definition in CSS2.

---

#### getBackgroundPosition

String

getBackgroundPosition()

See the background-position property definition in CSS2.

setBackgroundPosition

```java
void setBackgroundPosition​(
String
backgroundPosition)
throws
DOMException
```

See the background-position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBackgroundPosition

void setBackgroundPosition​(

String

backgroundPosition)
throws

DOMException

See the background-position property definition in CSS2.

getBackgroundRepeat

```java
String
getBackgroundRepeat()
```

See the background-repeat property definition in CSS2.

---

#### getBackgroundRepeat

String

getBackgroundRepeat()

See the background-repeat property definition in CSS2.

setBackgroundRepeat

```java
void setBackgroundRepeat​(
String
backgroundRepeat)
throws
DOMException
```

See the background-repeat property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBackgroundRepeat

void setBackgroundRepeat​(

String

backgroundRepeat)
throws

DOMException

See the background-repeat property definition in CSS2.

getBorder

```java
String
getBorder()
```

See the border property definition in CSS2.

---

#### getBorder

String

getBorder()

See the border property definition in CSS2.

setBorder

```java
void setBorder​(
String
border)
throws
DOMException
```

See the border property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorder

void setBorder​(

String

border)
throws

DOMException

See the border property definition in CSS2.

getBorderCollapse

```java
String
getBorderCollapse()
```

See the border-collapse property definition in CSS2.

---

#### getBorderCollapse

String

getBorderCollapse()

See the border-collapse property definition in CSS2.

setBorderCollapse

```java
void setBorderCollapse​(
String
borderCollapse)
throws
DOMException
```

See the border-collapse property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderCollapse

void setBorderCollapse​(

String

borderCollapse)
throws

DOMException

See the border-collapse property definition in CSS2.

getBorderColor

```java
String
getBorderColor()
```

See the border-color property definition in CSS2.

---

#### getBorderColor

String

getBorderColor()

See the border-color property definition in CSS2.

setBorderColor

```java
void setBorderColor​(
String
borderColor)
throws
DOMException
```

See the border-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderColor

void setBorderColor​(

String

borderColor)
throws

DOMException

See the border-color property definition in CSS2.

getBorderSpacing

```java
String
getBorderSpacing()
```

See the border-spacing property definition in CSS2.

---

#### getBorderSpacing

String

getBorderSpacing()

See the border-spacing property definition in CSS2.

setBorderSpacing

```java
void setBorderSpacing​(
String
borderSpacing)
throws
DOMException
```

See the border-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderSpacing

void setBorderSpacing​(

String

borderSpacing)
throws

DOMException

See the border-spacing property definition in CSS2.

getBorderStyle

```java
String
getBorderStyle()
```

See the border-style property definition in CSS2.

---

#### getBorderStyle

String

getBorderStyle()

See the border-style property definition in CSS2.

setBorderStyle

```java
void setBorderStyle​(
String
borderStyle)
throws
DOMException
```

See the border-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderStyle

void setBorderStyle​(

String

borderStyle)
throws

DOMException

See the border-style property definition in CSS2.

getBorderTop

```java
String
getBorderTop()
```

See the border-top property definition in CSS2.

---

#### getBorderTop

String

getBorderTop()

See the border-top property definition in CSS2.

setBorderTop

```java
void setBorderTop​(
String
borderTop)
throws
DOMException
```

See the border-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderTop

void setBorderTop​(

String

borderTop)
throws

DOMException

See the border-top property definition in CSS2.

getBorderRight

```java
String
getBorderRight()
```

See the border-right property definition in CSS2.

---

#### getBorderRight

String

getBorderRight()

See the border-right property definition in CSS2.

setBorderRight

```java
void setBorderRight​(
String
borderRight)
throws
DOMException
```

See the border-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderRight

void setBorderRight​(

String

borderRight)
throws

DOMException

See the border-right property definition in CSS2.

getBorderBottom

```java
String
getBorderBottom()
```

See the border-bottom property definition in CSS2.

---

#### getBorderBottom

String

getBorderBottom()

See the border-bottom property definition in CSS2.

setBorderBottom

```java
void setBorderBottom​(
String
borderBottom)
throws
DOMException
```

See the border-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderBottom

void setBorderBottom​(

String

borderBottom)
throws

DOMException

See the border-bottom property definition in CSS2.

getBorderLeft

```java
String
getBorderLeft()
```

See the border-left property definition in CSS2.

---

#### getBorderLeft

String

getBorderLeft()

See the border-left property definition in CSS2.

setBorderLeft

```java
void setBorderLeft​(
String
borderLeft)
throws
DOMException
```

See the border-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderLeft

void setBorderLeft​(

String

borderLeft)
throws

DOMException

See the border-left property definition in CSS2.

getBorderTopColor

```java
String
getBorderTopColor()
```

See the border-top-color property definition in CSS2.

---

#### getBorderTopColor

String

getBorderTopColor()

See the border-top-color property definition in CSS2.

setBorderTopColor

```java
void setBorderTopColor​(
String
borderTopColor)
throws
DOMException
```

See the border-top-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderTopColor

void setBorderTopColor​(

String

borderTopColor)
throws

DOMException

See the border-top-color property definition in CSS2.

getBorderRightColor

```java
String
getBorderRightColor()
```

See the border-right-color property definition in CSS2.

---

#### getBorderRightColor

String

getBorderRightColor()

See the border-right-color property definition in CSS2.

setBorderRightColor

```java
void setBorderRightColor​(
String
borderRightColor)
throws
DOMException
```

See the border-right-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderRightColor

void setBorderRightColor​(

String

borderRightColor)
throws

DOMException

See the border-right-color property definition in CSS2.

getBorderBottomColor

```java
String
getBorderBottomColor()
```

See the border-bottom-color property definition in CSS2.

---

#### getBorderBottomColor

String

getBorderBottomColor()

See the border-bottom-color property definition in CSS2.

setBorderBottomColor

```java
void setBorderBottomColor​(
String
borderBottomColor)
throws
DOMException
```

See the border-bottom-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderBottomColor

void setBorderBottomColor​(

String

borderBottomColor)
throws

DOMException

See the border-bottom-color property definition in CSS2.

getBorderLeftColor

```java
String
getBorderLeftColor()
```

See the border-left-color property definition in CSS2.

---

#### getBorderLeftColor

String

getBorderLeftColor()

See the border-left-color property definition in CSS2.

setBorderLeftColor

```java
void setBorderLeftColor​(
String
borderLeftColor)
throws
DOMException
```

See the border-left-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderLeftColor

void setBorderLeftColor​(

String

borderLeftColor)
throws

DOMException

See the border-left-color property definition in CSS2.

getBorderTopStyle

```java
String
getBorderTopStyle()
```

See the border-top-style property definition in CSS2.

---

#### getBorderTopStyle

String

getBorderTopStyle()

See the border-top-style property definition in CSS2.

setBorderTopStyle

```java
void setBorderTopStyle​(
String
borderTopStyle)
throws
DOMException
```

See the border-top-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderTopStyle

void setBorderTopStyle​(

String

borderTopStyle)
throws

DOMException

See the border-top-style property definition in CSS2.

getBorderRightStyle

```java
String
getBorderRightStyle()
```

See the border-right-style property definition in CSS2.

---

#### getBorderRightStyle

String

getBorderRightStyle()

See the border-right-style property definition in CSS2.

setBorderRightStyle

```java
void setBorderRightStyle​(
String
borderRightStyle)
throws
DOMException
```

See the border-right-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderRightStyle

void setBorderRightStyle​(

String

borderRightStyle)
throws

DOMException

See the border-right-style property definition in CSS2.

getBorderBottomStyle

```java
String
getBorderBottomStyle()
```

See the border-bottom-style property definition in CSS2.

---

#### getBorderBottomStyle

String

getBorderBottomStyle()

See the border-bottom-style property definition in CSS2.

setBorderBottomStyle

```java
void setBorderBottomStyle​(
String
borderBottomStyle)
throws
DOMException
```

See the border-bottom-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderBottomStyle

void setBorderBottomStyle​(

String

borderBottomStyle)
throws

DOMException

See the border-bottom-style property definition in CSS2.

getBorderLeftStyle

```java
String
getBorderLeftStyle()
```

See the border-left-style property definition in CSS2.

---

#### getBorderLeftStyle

String

getBorderLeftStyle()

See the border-left-style property definition in CSS2.

setBorderLeftStyle

```java
void setBorderLeftStyle​(
String
borderLeftStyle)
throws
DOMException
```

See the border-left-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderLeftStyle

void setBorderLeftStyle​(

String

borderLeftStyle)
throws

DOMException

See the border-left-style property definition in CSS2.

getBorderTopWidth

```java
String
getBorderTopWidth()
```

See the border-top-width property definition in CSS2.

---

#### getBorderTopWidth

String

getBorderTopWidth()

See the border-top-width property definition in CSS2.

setBorderTopWidth

```java
void setBorderTopWidth​(
String
borderTopWidth)
throws
DOMException
```

See the border-top-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderTopWidth

void setBorderTopWidth​(

String

borderTopWidth)
throws

DOMException

See the border-top-width property definition in CSS2.

getBorderRightWidth

```java
String
getBorderRightWidth()
```

See the border-right-width property definition in CSS2.

---

#### getBorderRightWidth

String

getBorderRightWidth()

See the border-right-width property definition in CSS2.

setBorderRightWidth

```java
void setBorderRightWidth​(
String
borderRightWidth)
throws
DOMException
```

See the border-right-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderRightWidth

void setBorderRightWidth​(

String

borderRightWidth)
throws

DOMException

See the border-right-width property definition in CSS2.

getBorderBottomWidth

```java
String
getBorderBottomWidth()
```

See the border-bottom-width property definition in CSS2.

---

#### getBorderBottomWidth

String

getBorderBottomWidth()

See the border-bottom-width property definition in CSS2.

setBorderBottomWidth

```java
void setBorderBottomWidth​(
String
borderBottomWidth)
throws
DOMException
```

See the border-bottom-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderBottomWidth

void setBorderBottomWidth​(

String

borderBottomWidth)
throws

DOMException

See the border-bottom-width property definition in CSS2.

getBorderLeftWidth

```java
String
getBorderLeftWidth()
```

See the border-left-width property definition in CSS2.

---

#### getBorderLeftWidth

String

getBorderLeftWidth()

See the border-left-width property definition in CSS2.

setBorderLeftWidth

```java
void setBorderLeftWidth​(
String
borderLeftWidth)
throws
DOMException
```

See the border-left-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderLeftWidth

void setBorderLeftWidth​(

String

borderLeftWidth)
throws

DOMException

See the border-left-width property definition in CSS2.

getBorderWidth

```java
String
getBorderWidth()
```

See the border-width property definition in CSS2.

---

#### getBorderWidth

String

getBorderWidth()

See the border-width property definition in CSS2.

setBorderWidth

```java
void setBorderWidth​(
String
borderWidth)
throws
DOMException
```

See the border-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBorderWidth

void setBorderWidth​(

String

borderWidth)
throws

DOMException

See the border-width property definition in CSS2.

getBottom

```java
String
getBottom()
```

See the bottom property definition in CSS2.

---

#### getBottom

String

getBottom()

See the bottom property definition in CSS2.

setBottom

```java
void setBottom​(
String
bottom)
throws
DOMException
```

See the bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setBottom

void setBottom​(

String

bottom)
throws

DOMException

See the bottom property definition in CSS2.

getCaptionSide

```java
String
getCaptionSide()
```

See the caption-side property definition in CSS2.

---

#### getCaptionSide

String

getCaptionSide()

See the caption-side property definition in CSS2.

setCaptionSide

```java
void setCaptionSide​(
String
captionSide)
throws
DOMException
```

See the caption-side property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCaptionSide

void setCaptionSide​(

String

captionSide)
throws

DOMException

See the caption-side property definition in CSS2.

getClear

```java
String
getClear()
```

See the clear property definition in CSS2.

---

#### getClear

String

getClear()

See the clear property definition in CSS2.

setClear

```java
void setClear​(
String
clear)
throws
DOMException
```

See the clear property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setClear

void setClear​(

String

clear)
throws

DOMException

See the clear property definition in CSS2.

getClip

```java
String
getClip()
```

See the clip property definition in CSS2.

---

#### getClip

String

getClip()

See the clip property definition in CSS2.

setClip

```java
void setClip​(
String
clip)
throws
DOMException
```

See the clip property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setClip

void setClip​(

String

clip)
throws

DOMException

See the clip property definition in CSS2.

getColor

```java
String
getColor()
```

See the color property definition in CSS2.

---

#### getColor

String

getColor()

See the color property definition in CSS2.

setColor

```java
void setColor​(
String
color)
throws
DOMException
```

See the color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setColor

void setColor​(

String

color)
throws

DOMException

See the color property definition in CSS2.

getContent

```java
String
getContent()
```

See the content property definition in CSS2.

---

#### getContent

String

getContent()

See the content property definition in CSS2.

setContent

```java
void setContent​(
String
content)
throws
DOMException
```

See the content property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setContent

void setContent​(

String

content)
throws

DOMException

See the content property definition in CSS2.

getCounterIncrement

```java
String
getCounterIncrement()
```

See the counter-increment property definition in CSS2.

---

#### getCounterIncrement

String

getCounterIncrement()

See the counter-increment property definition in CSS2.

setCounterIncrement

```java
void setCounterIncrement​(
String
counterIncrement)
throws
DOMException
```

See the counter-increment property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCounterIncrement

void setCounterIncrement​(

String

counterIncrement)
throws

DOMException

See the counter-increment property definition in CSS2.

getCounterReset

```java
String
getCounterReset()
```

See the counter-reset property definition in CSS2.

---

#### getCounterReset

String

getCounterReset()

See the counter-reset property definition in CSS2.

setCounterReset

```java
void setCounterReset​(
String
counterReset)
throws
DOMException
```

See the counter-reset property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCounterReset

void setCounterReset​(

String

counterReset)
throws

DOMException

See the counter-reset property definition in CSS2.

getCue

```java
String
getCue()
```

See the cue property definition in CSS2.

---

#### getCue

String

getCue()

See the cue property definition in CSS2.

setCue

```java
void setCue​(
String
cue)
throws
DOMException
```

See the cue property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCue

void setCue​(

String

cue)
throws

DOMException

See the cue property definition in CSS2.

getCueAfter

```java
String
getCueAfter()
```

See the cue-after property definition in CSS2.

---

#### getCueAfter

String

getCueAfter()

See the cue-after property definition in CSS2.

setCueAfter

```java
void setCueAfter​(
String
cueAfter)
throws
DOMException
```

See the cue-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCueAfter

void setCueAfter​(

String

cueAfter)
throws

DOMException

See the cue-after property definition in CSS2.

getCueBefore

```java
String
getCueBefore()
```

See the cue-before property definition in CSS2.

---

#### getCueBefore

String

getCueBefore()

See the cue-before property definition in CSS2.

setCueBefore

```java
void setCueBefore​(
String
cueBefore)
throws
DOMException
```

See the cue-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCueBefore

void setCueBefore​(

String

cueBefore)
throws

DOMException

See the cue-before property definition in CSS2.

getCursor

```java
String
getCursor()
```

See the cursor property definition in CSS2.

---

#### getCursor

String

getCursor()

See the cursor property definition in CSS2.

setCursor

```java
void setCursor​(
String
cursor)
throws
DOMException
```

See the cursor property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCursor

void setCursor​(

String

cursor)
throws

DOMException

See the cursor property definition in CSS2.

getDirection

```java
String
getDirection()
```

See the direction property definition in CSS2.

---

#### getDirection

String

getDirection()

See the direction property definition in CSS2.

setDirection

```java
void setDirection​(
String
direction)
throws
DOMException
```

See the direction property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setDirection

void setDirection​(

String

direction)
throws

DOMException

See the direction property definition in CSS2.

getDisplay

```java
String
getDisplay()
```

See the display property definition in CSS2.

---

#### getDisplay

String

getDisplay()

See the display property definition in CSS2.

setDisplay

```java
void setDisplay​(
String
display)
throws
DOMException
```

See the display property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setDisplay

void setDisplay​(

String

display)
throws

DOMException

See the display property definition in CSS2.

getElevation

```java
String
getElevation()
```

See the elevation property definition in CSS2.

---

#### getElevation

String

getElevation()

See the elevation property definition in CSS2.

setElevation

```java
void setElevation​(
String
elevation)
throws
DOMException
```

See the elevation property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setElevation

void setElevation​(

String

elevation)
throws

DOMException

See the elevation property definition in CSS2.

getEmptyCells

```java
String
getEmptyCells()
```

See the empty-cells property definition in CSS2.

---

#### getEmptyCells

String

getEmptyCells()

See the empty-cells property definition in CSS2.

setEmptyCells

```java
void setEmptyCells​(
String
emptyCells)
throws
DOMException
```

See the empty-cells property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setEmptyCells

void setEmptyCells​(

String

emptyCells)
throws

DOMException

See the empty-cells property definition in CSS2.

getCssFloat

```java
String
getCssFloat()
```

See the float property definition in CSS2.

---

#### getCssFloat

String

getCssFloat()

See the float property definition in CSS2.

setCssFloat

```java
void setCssFloat​(
String
cssFloat)
throws
DOMException
```

See the float property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setCssFloat

void setCssFloat​(

String

cssFloat)
throws

DOMException

See the float property definition in CSS2.

getFont

```java
String
getFont()
```

See the font property definition in CSS2.

---

#### getFont

String

getFont()

See the font property definition in CSS2.

setFont

```java
void setFont​(
String
font)
throws
DOMException
```

See the font property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFont

void setFont​(

String

font)
throws

DOMException

See the font property definition in CSS2.

getFontFamily

```java
String
getFontFamily()
```

See the font-family property definition in CSS2.

---

#### getFontFamily

String

getFontFamily()

See the font-family property definition in CSS2.

setFontFamily

```java
void setFontFamily​(
String
fontFamily)
throws
DOMException
```

See the font-family property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontFamily

void setFontFamily​(

String

fontFamily)
throws

DOMException

See the font-family property definition in CSS2.

getFontSize

```java
String
getFontSize()
```

See the font-size property definition in CSS2.

---

#### getFontSize

String

getFontSize()

See the font-size property definition in CSS2.

setFontSize

```java
void setFontSize​(
String
fontSize)
throws
DOMException
```

See the font-size property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontSize

void setFontSize​(

String

fontSize)
throws

DOMException

See the font-size property definition in CSS2.

getFontSizeAdjust

```java
String
getFontSizeAdjust()
```

See the font-size-adjust property definition in CSS2.

---

#### getFontSizeAdjust

String

getFontSizeAdjust()

See the font-size-adjust property definition in CSS2.

setFontSizeAdjust

```java
void setFontSizeAdjust​(
String
fontSizeAdjust)
throws
DOMException
```

See the font-size-adjust property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontSizeAdjust

void setFontSizeAdjust​(

String

fontSizeAdjust)
throws

DOMException

See the font-size-adjust property definition in CSS2.

getFontStretch

```java
String
getFontStretch()
```

See the font-stretch property definition in CSS2.

---

#### getFontStretch

String

getFontStretch()

See the font-stretch property definition in CSS2.

setFontStretch

```java
void setFontStretch​(
String
fontStretch)
throws
DOMException
```

See the font-stretch property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontStretch

void setFontStretch​(

String

fontStretch)
throws

DOMException

See the font-stretch property definition in CSS2.

getFontStyle

```java
String
getFontStyle()
```

See the font-style property definition in CSS2.

---

#### getFontStyle

String

getFontStyle()

See the font-style property definition in CSS2.

setFontStyle

```java
void setFontStyle​(
String
fontStyle)
throws
DOMException
```

See the font-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontStyle

void setFontStyle​(

String

fontStyle)
throws

DOMException

See the font-style property definition in CSS2.

getFontVariant

```java
String
getFontVariant()
```

See the font-variant property definition in CSS2.

---

#### getFontVariant

String

getFontVariant()

See the font-variant property definition in CSS2.

setFontVariant

```java
void setFontVariant​(
String
fontVariant)
throws
DOMException
```

See the font-variant property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontVariant

void setFontVariant​(

String

fontVariant)
throws

DOMException

See the font-variant property definition in CSS2.

getFontWeight

```java
String
getFontWeight()
```

See the font-weight property definition in CSS2.

---

#### getFontWeight

String

getFontWeight()

See the font-weight property definition in CSS2.

setFontWeight

```java
void setFontWeight​(
String
fontWeight)
throws
DOMException
```

See the font-weight property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setFontWeight

void setFontWeight​(

String

fontWeight)
throws

DOMException

See the font-weight property definition in CSS2.

getHeight

```java
String
getHeight()
```

See the height property definition in CSS2.

---

#### getHeight

String

getHeight()

See the height property definition in CSS2.

setHeight

```java
void setHeight​(
String
height)
throws
DOMException
```

See the height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setHeight

void setHeight​(

String

height)
throws

DOMException

See the height property definition in CSS2.

getLeft

```java
String
getLeft()
```

See the left property definition in CSS2.

---

#### getLeft

String

getLeft()

See the left property definition in CSS2.

setLeft

```java
void setLeft​(
String
left)
throws
DOMException
```

See the left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setLeft

void setLeft​(

String

left)
throws

DOMException

See the left property definition in CSS2.

getLetterSpacing

```java
String
getLetterSpacing()
```

See the letter-spacing property definition in CSS2.

---

#### getLetterSpacing

String

getLetterSpacing()

See the letter-spacing property definition in CSS2.

setLetterSpacing

```java
void setLetterSpacing​(
String
letterSpacing)
throws
DOMException
```

See the letter-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setLetterSpacing

void setLetterSpacing​(

String

letterSpacing)
throws

DOMException

See the letter-spacing property definition in CSS2.

getLineHeight

```java
String
getLineHeight()
```

See the line-height property definition in CSS2.

---

#### getLineHeight

String

getLineHeight()

See the line-height property definition in CSS2.

setLineHeight

```java
void setLineHeight​(
String
lineHeight)
throws
DOMException
```

See the line-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setLineHeight

void setLineHeight​(

String

lineHeight)
throws

DOMException

See the line-height property definition in CSS2.

getListStyle

```java
String
getListStyle()
```

See the list-style property definition in CSS2.

---

#### getListStyle

String

getListStyle()

See the list-style property definition in CSS2.

setListStyle

```java
void setListStyle​(
String
listStyle)
throws
DOMException
```

See the list-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setListStyle

void setListStyle​(

String

listStyle)
throws

DOMException

See the list-style property definition in CSS2.

getListStyleImage

```java
String
getListStyleImage()
```

See the list-style-image property definition in CSS2.

---

#### getListStyleImage

String

getListStyleImage()

See the list-style-image property definition in CSS2.

setListStyleImage

```java
void setListStyleImage​(
String
listStyleImage)
throws
DOMException
```

See the list-style-image property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setListStyleImage

void setListStyleImage​(

String

listStyleImage)
throws

DOMException

See the list-style-image property definition in CSS2.

getListStylePosition

```java
String
getListStylePosition()
```

See the list-style-position property definition in CSS2.

---

#### getListStylePosition

String

getListStylePosition()

See the list-style-position property definition in CSS2.

setListStylePosition

```java
void setListStylePosition​(
String
listStylePosition)
throws
DOMException
```

See the list-style-position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setListStylePosition

void setListStylePosition​(

String

listStylePosition)
throws

DOMException

See the list-style-position property definition in CSS2.

getListStyleType

```java
String
getListStyleType()
```

See the list-style-type property definition in CSS2.

---

#### getListStyleType

String

getListStyleType()

See the list-style-type property definition in CSS2.

setListStyleType

```java
void setListStyleType​(
String
listStyleType)
throws
DOMException
```

See the list-style-type property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setListStyleType

void setListStyleType​(

String

listStyleType)
throws

DOMException

See the list-style-type property definition in CSS2.

getMargin

```java
String
getMargin()
```

See the margin property definition in CSS2.

---

#### getMargin

String

getMargin()

See the margin property definition in CSS2.

setMargin

```java
void setMargin​(
String
margin)
throws
DOMException
```

See the margin property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMargin

void setMargin​(

String

margin)
throws

DOMException

See the margin property definition in CSS2.

getMarginTop

```java
String
getMarginTop()
```

See the margin-top property definition in CSS2.

---

#### getMarginTop

String

getMarginTop()

See the margin-top property definition in CSS2.

setMarginTop

```java
void setMarginTop​(
String
marginTop)
throws
DOMException
```

See the margin-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMarginTop

void setMarginTop​(

String

marginTop)
throws

DOMException

See the margin-top property definition in CSS2.

getMarginRight

```java
String
getMarginRight()
```

See the margin-right property definition in CSS2.

---

#### getMarginRight

String

getMarginRight()

See the margin-right property definition in CSS2.

setMarginRight

```java
void setMarginRight​(
String
marginRight)
throws
DOMException
```

See the margin-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMarginRight

void setMarginRight​(

String

marginRight)
throws

DOMException

See the margin-right property definition in CSS2.

getMarginBottom

```java
String
getMarginBottom()
```

See the margin-bottom property definition in CSS2.

---

#### getMarginBottom

String

getMarginBottom()

See the margin-bottom property definition in CSS2.

setMarginBottom

```java
void setMarginBottom​(
String
marginBottom)
throws
DOMException
```

See the margin-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMarginBottom

void setMarginBottom​(

String

marginBottom)
throws

DOMException

See the margin-bottom property definition in CSS2.

getMarginLeft

```java
String
getMarginLeft()
```

See the margin-left property definition in CSS2.

---

#### getMarginLeft

String

getMarginLeft()

See the margin-left property definition in CSS2.

setMarginLeft

```java
void setMarginLeft​(
String
marginLeft)
throws
DOMException
```

See the margin-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMarginLeft

void setMarginLeft​(

String

marginLeft)
throws

DOMException

See the margin-left property definition in CSS2.

getMarkerOffset

```java
String
getMarkerOffset()
```

See the marker-offset property definition in CSS2.

---

#### getMarkerOffset

String

getMarkerOffset()

See the marker-offset property definition in CSS2.

setMarkerOffset

```java
void setMarkerOffset​(
String
markerOffset)
throws
DOMException
```

See the marker-offset property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMarkerOffset

void setMarkerOffset​(

String

markerOffset)
throws

DOMException

See the marker-offset property definition in CSS2.

getMarks

```java
String
getMarks()
```

See the marks property definition in CSS2.

---

#### getMarks

String

getMarks()

See the marks property definition in CSS2.

setMarks

```java
void setMarks​(
String
marks)
throws
DOMException
```

See the marks property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMarks

void setMarks​(

String

marks)
throws

DOMException

See the marks property definition in CSS2.

getMaxHeight

```java
String
getMaxHeight()
```

See the max-height property definition in CSS2.

---

#### getMaxHeight

String

getMaxHeight()

See the max-height property definition in CSS2.

setMaxHeight

```java
void setMaxHeight​(
String
maxHeight)
throws
DOMException
```

See the max-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMaxHeight

void setMaxHeight​(

String

maxHeight)
throws

DOMException

See the max-height property definition in CSS2.

getMaxWidth

```java
String
getMaxWidth()
```

See the max-width property definition in CSS2.

---

#### getMaxWidth

String

getMaxWidth()

See the max-width property definition in CSS2.

setMaxWidth

```java
void setMaxWidth​(
String
maxWidth)
throws
DOMException
```

See the max-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMaxWidth

void setMaxWidth​(

String

maxWidth)
throws

DOMException

See the max-width property definition in CSS2.

getMinHeight

```java
String
getMinHeight()
```

See the min-height property definition in CSS2.

---

#### getMinHeight

String

getMinHeight()

See the min-height property definition in CSS2.

setMinHeight

```java
void setMinHeight​(
String
minHeight)
throws
DOMException
```

See the min-height property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMinHeight

void setMinHeight​(

String

minHeight)
throws

DOMException

See the min-height property definition in CSS2.

getMinWidth

```java
String
getMinWidth()
```

See the min-width property definition in CSS2.

---

#### getMinWidth

String

getMinWidth()

See the min-width property definition in CSS2.

setMinWidth

```java
void setMinWidth​(
String
minWidth)
throws
DOMException
```

See the min-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setMinWidth

void setMinWidth​(

String

minWidth)
throws

DOMException

See the min-width property definition in CSS2.

getOrphans

```java
String
getOrphans()
```

See the orphans property definition in CSS2.

---

#### getOrphans

String

getOrphans()

See the orphans property definition in CSS2.

setOrphans

```java
void setOrphans​(
String
orphans)
throws
DOMException
```

See the orphans property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setOrphans

void setOrphans​(

String

orphans)
throws

DOMException

See the orphans property definition in CSS2.

getOutline

```java
String
getOutline()
```

See the outline property definition in CSS2.

---

#### getOutline

String

getOutline()

See the outline property definition in CSS2.

setOutline

```java
void setOutline​(
String
outline)
throws
DOMException
```

See the outline property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setOutline

void setOutline​(

String

outline)
throws

DOMException

See the outline property definition in CSS2.

getOutlineColor

```java
String
getOutlineColor()
```

See the outline-color property definition in CSS2.

---

#### getOutlineColor

String

getOutlineColor()

See the outline-color property definition in CSS2.

setOutlineColor

```java
void setOutlineColor​(
String
outlineColor)
throws
DOMException
```

See the outline-color property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setOutlineColor

void setOutlineColor​(

String

outlineColor)
throws

DOMException

See the outline-color property definition in CSS2.

getOutlineStyle

```java
String
getOutlineStyle()
```

See the outline-style property definition in CSS2.

---

#### getOutlineStyle

String

getOutlineStyle()

See the outline-style property definition in CSS2.

setOutlineStyle

```java
void setOutlineStyle​(
String
outlineStyle)
throws
DOMException
```

See the outline-style property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setOutlineStyle

void setOutlineStyle​(

String

outlineStyle)
throws

DOMException

See the outline-style property definition in CSS2.

getOutlineWidth

```java
String
getOutlineWidth()
```

See the outline-width property definition in CSS2.

---

#### getOutlineWidth

String

getOutlineWidth()

See the outline-width property definition in CSS2.

setOutlineWidth

```java
void setOutlineWidth​(
String
outlineWidth)
throws
DOMException
```

See the outline-width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setOutlineWidth

void setOutlineWidth​(

String

outlineWidth)
throws

DOMException

See the outline-width property definition in CSS2.

getOverflow

```java
String
getOverflow()
```

See the overflow property definition in CSS2.

---

#### getOverflow

String

getOverflow()

See the overflow property definition in CSS2.

setOverflow

```java
void setOverflow​(
String
overflow)
throws
DOMException
```

See the overflow property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setOverflow

void setOverflow​(

String

overflow)
throws

DOMException

See the overflow property definition in CSS2.

getPadding

```java
String
getPadding()
```

See the padding property definition in CSS2.

---

#### getPadding

String

getPadding()

See the padding property definition in CSS2.

setPadding

```java
void setPadding​(
String
padding)
throws
DOMException
```

See the padding property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPadding

void setPadding​(

String

padding)
throws

DOMException

See the padding property definition in CSS2.

getPaddingTop

```java
String
getPaddingTop()
```

See the padding-top property definition in CSS2.

---

#### getPaddingTop

String

getPaddingTop()

See the padding-top property definition in CSS2.

setPaddingTop

```java
void setPaddingTop​(
String
paddingTop)
throws
DOMException
```

See the padding-top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPaddingTop

void setPaddingTop​(

String

paddingTop)
throws

DOMException

See the padding-top property definition in CSS2.

getPaddingRight

```java
String
getPaddingRight()
```

See the padding-right property definition in CSS2.

---

#### getPaddingRight

String

getPaddingRight()

See the padding-right property definition in CSS2.

setPaddingRight

```java
void setPaddingRight​(
String
paddingRight)
throws
DOMException
```

See the padding-right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPaddingRight

void setPaddingRight​(

String

paddingRight)
throws

DOMException

See the padding-right property definition in CSS2.

getPaddingBottom

```java
String
getPaddingBottom()
```

See the padding-bottom property definition in CSS2.

---

#### getPaddingBottom

String

getPaddingBottom()

See the padding-bottom property definition in CSS2.

setPaddingBottom

```java
void setPaddingBottom​(
String
paddingBottom)
throws
DOMException
```

See the padding-bottom property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPaddingBottom

void setPaddingBottom​(

String

paddingBottom)
throws

DOMException

See the padding-bottom property definition in CSS2.

getPaddingLeft

```java
String
getPaddingLeft()
```

See the padding-left property definition in CSS2.

---

#### getPaddingLeft

String

getPaddingLeft()

See the padding-left property definition in CSS2.

setPaddingLeft

```java
void setPaddingLeft​(
String
paddingLeft)
throws
DOMException
```

See the padding-left property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPaddingLeft

void setPaddingLeft​(

String

paddingLeft)
throws

DOMException

See the padding-left property definition in CSS2.

getPage

```java
String
getPage()
```

See the page property definition in CSS2.

---

#### getPage

String

getPage()

See the page property definition in CSS2.

setPage

```java
void setPage​(
String
page)
throws
DOMException
```

See the page property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPage

void setPage​(

String

page)
throws

DOMException

See the page property definition in CSS2.

getPageBreakAfter

```java
String
getPageBreakAfter()
```

See the page-break-after property definition in CSS2.

---

#### getPageBreakAfter

String

getPageBreakAfter()

See the page-break-after property definition in CSS2.

setPageBreakAfter

```java
void setPageBreakAfter​(
String
pageBreakAfter)
throws
DOMException
```

See the page-break-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPageBreakAfter

void setPageBreakAfter​(

String

pageBreakAfter)
throws

DOMException

See the page-break-after property definition in CSS2.

getPageBreakBefore

```java
String
getPageBreakBefore()
```

See the page-break-before property definition in CSS2.

---

#### getPageBreakBefore

String

getPageBreakBefore()

See the page-break-before property definition in CSS2.

setPageBreakBefore

```java
void setPageBreakBefore​(
String
pageBreakBefore)
throws
DOMException
```

See the page-break-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPageBreakBefore

void setPageBreakBefore​(

String

pageBreakBefore)
throws

DOMException

See the page-break-before property definition in CSS2.

getPageBreakInside

```java
String
getPageBreakInside()
```

See the page-break-inside property definition in CSS2.

---

#### getPageBreakInside

String

getPageBreakInside()

See the page-break-inside property definition in CSS2.

setPageBreakInside

```java
void setPageBreakInside​(
String
pageBreakInside)
throws
DOMException
```

See the page-break-inside property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPageBreakInside

void setPageBreakInside​(

String

pageBreakInside)
throws

DOMException

See the page-break-inside property definition in CSS2.

getPause

```java
String
getPause()
```

See the pause property definition in CSS2.

---

#### getPause

String

getPause()

See the pause property definition in CSS2.

setPause

```java
void setPause​(
String
pause)
throws
DOMException
```

See the pause property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPause

void setPause​(

String

pause)
throws

DOMException

See the pause property definition in CSS2.

getPauseAfter

```java
String
getPauseAfter()
```

See the pause-after property definition in CSS2.

---

#### getPauseAfter

String

getPauseAfter()

See the pause-after property definition in CSS2.

setPauseAfter

```java
void setPauseAfter​(
String
pauseAfter)
throws
DOMException
```

See the pause-after property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPauseAfter

void setPauseAfter​(

String

pauseAfter)
throws

DOMException

See the pause-after property definition in CSS2.

getPauseBefore

```java
String
getPauseBefore()
```

See the pause-before property definition in CSS2.

---

#### getPauseBefore

String

getPauseBefore()

See the pause-before property definition in CSS2.

setPauseBefore

```java
void setPauseBefore​(
String
pauseBefore)
throws
DOMException
```

See the pause-before property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPauseBefore

void setPauseBefore​(

String

pauseBefore)
throws

DOMException

See the pause-before property definition in CSS2.

getPitch

```java
String
getPitch()
```

See the pitch property definition in CSS2.

---

#### getPitch

String

getPitch()

See the pitch property definition in CSS2.

setPitch

```java
void setPitch​(
String
pitch)
throws
DOMException
```

See the pitch property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPitch

void setPitch​(

String

pitch)
throws

DOMException

See the pitch property definition in CSS2.

getPitchRange

```java
String
getPitchRange()
```

See the pitch-range property definition in CSS2.

---

#### getPitchRange

String

getPitchRange()

See the pitch-range property definition in CSS2.

setPitchRange

```java
void setPitchRange​(
String
pitchRange)
throws
DOMException
```

See the pitch-range property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPitchRange

void setPitchRange​(

String

pitchRange)
throws

DOMException

See the pitch-range property definition in CSS2.

getPlayDuring

```java
String
getPlayDuring()
```

See the play-during property definition in CSS2.

---

#### getPlayDuring

String

getPlayDuring()

See the play-during property definition in CSS2.

setPlayDuring

```java
void setPlayDuring​(
String
playDuring)
throws
DOMException
```

See the play-during property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPlayDuring

void setPlayDuring​(

String

playDuring)
throws

DOMException

See the play-during property definition in CSS2.

getPosition

```java
String
getPosition()
```

See the position property definition in CSS2.

---

#### getPosition

String

getPosition()

See the position property definition in CSS2.

setPosition

```java
void setPosition​(
String
position)
throws
DOMException
```

See the position property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setPosition

void setPosition​(

String

position)
throws

DOMException

See the position property definition in CSS2.

getQuotes

```java
String
getQuotes()
```

See the quotes property definition in CSS2.

---

#### getQuotes

String

getQuotes()

See the quotes property definition in CSS2.

setQuotes

```java
void setQuotes​(
String
quotes)
throws
DOMException
```

See the quotes property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setQuotes

void setQuotes​(

String

quotes)
throws

DOMException

See the quotes property definition in CSS2.

getRichness

```java
String
getRichness()
```

See the richness property definition in CSS2.

---

#### getRichness

String

getRichness()

See the richness property definition in CSS2.

setRichness

```java
void setRichness​(
String
richness)
throws
DOMException
```

See the richness property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setRichness

void setRichness​(

String

richness)
throws

DOMException

See the richness property definition in CSS2.

getRight

```java
String
getRight()
```

See the right property definition in CSS2.

---

#### getRight

String

getRight()

See the right property definition in CSS2.

setRight

```java
void setRight​(
String
right)
throws
DOMException
```

See the right property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setRight

void setRight​(

String

right)
throws

DOMException

See the right property definition in CSS2.

getSize

```java
String
getSize()
```

See the size property definition in CSS2.

---

#### getSize

String

getSize()

See the size property definition in CSS2.

setSize

```java
void setSize​(
String
size)
throws
DOMException
```

See the size property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setSize

void setSize​(

String

size)
throws

DOMException

See the size property definition in CSS2.

getSpeak

```java
String
getSpeak()
```

See the speak property definition in CSS2.

---

#### getSpeak

String

getSpeak()

See the speak property definition in CSS2.

setSpeak

```java
void setSpeak​(
String
speak)
throws
DOMException
```

See the speak property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setSpeak

void setSpeak​(

String

speak)
throws

DOMException

See the speak property definition in CSS2.

getSpeakHeader

```java
String
getSpeakHeader()
```

See the speak-header property definition in CSS2.

---

#### getSpeakHeader

String

getSpeakHeader()

See the speak-header property definition in CSS2.

setSpeakHeader

```java
void setSpeakHeader​(
String
speakHeader)
throws
DOMException
```

See the speak-header property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setSpeakHeader

void setSpeakHeader​(

String

speakHeader)
throws

DOMException

See the speak-header property definition in CSS2.

getSpeakNumeral

```java
String
getSpeakNumeral()
```

See the speak-numeral property definition in CSS2.

---

#### getSpeakNumeral

String

getSpeakNumeral()

See the speak-numeral property definition in CSS2.

setSpeakNumeral

```java
void setSpeakNumeral​(
String
speakNumeral)
throws
DOMException
```

See the speak-numeral property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setSpeakNumeral

void setSpeakNumeral​(

String

speakNumeral)
throws

DOMException

See the speak-numeral property definition in CSS2.

getSpeakPunctuation

```java
String
getSpeakPunctuation()
```

See the speak-punctuation property definition in CSS2.

---

#### getSpeakPunctuation

String

getSpeakPunctuation()

See the speak-punctuation property definition in CSS2.

setSpeakPunctuation

```java
void setSpeakPunctuation​(
String
speakPunctuation)
throws
DOMException
```

See the speak-punctuation property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setSpeakPunctuation

void setSpeakPunctuation​(

String

speakPunctuation)
throws

DOMException

See the speak-punctuation property definition in CSS2.

getSpeechRate

```java
String
getSpeechRate()
```

See the speech-rate property definition in CSS2.

---

#### getSpeechRate

String

getSpeechRate()

See the speech-rate property definition in CSS2.

setSpeechRate

```java
void setSpeechRate​(
String
speechRate)
throws
DOMException
```

See the speech-rate property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setSpeechRate

void setSpeechRate​(

String

speechRate)
throws

DOMException

See the speech-rate property definition in CSS2.

getStress

```java
String
getStress()
```

See the stress property definition in CSS2.

---

#### getStress

String

getStress()

See the stress property definition in CSS2.

setStress

```java
void setStress​(
String
stress)
throws
DOMException
```

See the stress property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setStress

void setStress​(

String

stress)
throws

DOMException

See the stress property definition in CSS2.

getTableLayout

```java
String
getTableLayout()
```

See the table-layout property definition in CSS2.

---

#### getTableLayout

String

getTableLayout()

See the table-layout property definition in CSS2.

setTableLayout

```java
void setTableLayout​(
String
tableLayout)
throws
DOMException
```

See the table-layout property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTableLayout

void setTableLayout​(

String

tableLayout)
throws

DOMException

See the table-layout property definition in CSS2.

getTextAlign

```java
String
getTextAlign()
```

See the text-align property definition in CSS2.

---

#### getTextAlign

String

getTextAlign()

See the text-align property definition in CSS2.

setTextAlign

```java
void setTextAlign​(
String
textAlign)
throws
DOMException
```

See the text-align property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTextAlign

void setTextAlign​(

String

textAlign)
throws

DOMException

See the text-align property definition in CSS2.

getTextDecoration

```java
String
getTextDecoration()
```

See the text-decoration property definition in CSS2.

---

#### getTextDecoration

String

getTextDecoration()

See the text-decoration property definition in CSS2.

setTextDecoration

```java
void setTextDecoration​(
String
textDecoration)
throws
DOMException
```

See the text-decoration property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTextDecoration

void setTextDecoration​(

String

textDecoration)
throws

DOMException

See the text-decoration property definition in CSS2.

getTextIndent

```java
String
getTextIndent()
```

See the text-indent property definition in CSS2.

---

#### getTextIndent

String

getTextIndent()

See the text-indent property definition in CSS2.

setTextIndent

```java
void setTextIndent​(
String
textIndent)
throws
DOMException
```

See the text-indent property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTextIndent

void setTextIndent​(

String

textIndent)
throws

DOMException

See the text-indent property definition in CSS2.

getTextShadow

```java
String
getTextShadow()
```

See the text-shadow property definition in CSS2.

---

#### getTextShadow

String

getTextShadow()

See the text-shadow property definition in CSS2.

setTextShadow

```java
void setTextShadow​(
String
textShadow)
throws
DOMException
```

See the text-shadow property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTextShadow

void setTextShadow​(

String

textShadow)
throws

DOMException

See the text-shadow property definition in CSS2.

getTextTransform

```java
String
getTextTransform()
```

See the text-transform property definition in CSS2.

---

#### getTextTransform

String

getTextTransform()

See the text-transform property definition in CSS2.

setTextTransform

```java
void setTextTransform​(
String
textTransform)
throws
DOMException
```

See the text-transform property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTextTransform

void setTextTransform​(

String

textTransform)
throws

DOMException

See the text-transform property definition in CSS2.

getTop

```java
String
getTop()
```

See the top property definition in CSS2.

---

#### getTop

String

getTop()

See the top property definition in CSS2.

setTop

```java
void setTop​(
String
top)
throws
DOMException
```

See the top property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setTop

void setTop​(

String

top)
throws

DOMException

See the top property definition in CSS2.

getUnicodeBidi

```java
String
getUnicodeBidi()
```

See the unicode-bidi property definition in CSS2.

---

#### getUnicodeBidi

String

getUnicodeBidi()

See the unicode-bidi property definition in CSS2.

setUnicodeBidi

```java
void setUnicodeBidi​(
String
unicodeBidi)
throws
DOMException
```

See the unicode-bidi property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setUnicodeBidi

void setUnicodeBidi​(

String

unicodeBidi)
throws

DOMException

See the unicode-bidi property definition in CSS2.

getVerticalAlign

```java
String
getVerticalAlign()
```

See the vertical-align property definition in CSS2.

---

#### getVerticalAlign

String

getVerticalAlign()

See the vertical-align property definition in CSS2.

setVerticalAlign

```java
void setVerticalAlign​(
String
verticalAlign)
throws
DOMException
```

See the vertical-align property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setVerticalAlign

void setVerticalAlign​(

String

verticalAlign)
throws

DOMException

See the vertical-align property definition in CSS2.

getVisibility

```java
String
getVisibility()
```

See the visibility property definition in CSS2.

---

#### getVisibility

String

getVisibility()

See the visibility property definition in CSS2.

setVisibility

```java
void setVisibility​(
String
visibility)
throws
DOMException
```

See the visibility property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setVisibility

void setVisibility​(

String

visibility)
throws

DOMException

See the visibility property definition in CSS2.

getVoiceFamily

```java
String
getVoiceFamily()
```

See the voice-family property definition in CSS2.

---

#### getVoiceFamily

String

getVoiceFamily()

See the voice-family property definition in CSS2.

setVoiceFamily

```java
void setVoiceFamily​(
String
voiceFamily)
throws
DOMException
```

See the voice-family property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setVoiceFamily

void setVoiceFamily​(

String

voiceFamily)
throws

DOMException

See the voice-family property definition in CSS2.

getVolume

```java
String
getVolume()
```

See the volume property definition in CSS2.

---

#### getVolume

String

getVolume()

See the volume property definition in CSS2.

setVolume

```java
void setVolume​(
String
volume)
throws
DOMException
```

See the volume property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setVolume

void setVolume​(

String

volume)
throws

DOMException

See the volume property definition in CSS2.

getWhiteSpace

```java
String
getWhiteSpace()
```

See the white-space property definition in CSS2.

---

#### getWhiteSpace

String

getWhiteSpace()

See the white-space property definition in CSS2.

setWhiteSpace

```java
void setWhiteSpace​(
String
whiteSpace)
throws
DOMException
```

See the white-space property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setWhiteSpace

void setWhiteSpace​(

String

whiteSpace)
throws

DOMException

See the white-space property definition in CSS2.

getWidows

```java
String
getWidows()
```

See the widows property definition in CSS2.

---

#### getWidows

String

getWidows()

See the widows property definition in CSS2.

setWidows

```java
void setWidows​(
String
widows)
throws
DOMException
```

See the widows property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setWidows

void setWidows​(

String

widows)
throws

DOMException

See the widows property definition in CSS2.

getWidth

```java
String
getWidth()
```

See the width property definition in CSS2.

---

#### getWidth

String

getWidth()

See the width property definition in CSS2.

setWidth

```java
void setWidth​(
String
width)
throws
DOMException
```

See the width property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setWidth

void setWidth​(

String

width)
throws

DOMException

See the width property definition in CSS2.

getWordSpacing

```java
String
getWordSpacing()
```

See the word-spacing property definition in CSS2.

---

#### getWordSpacing

String

getWordSpacing()

See the word-spacing property definition in CSS2.

setWordSpacing

```java
void setWordSpacing​(
String
wordSpacing)
throws
DOMException
```

See the word-spacing property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setWordSpacing

void setWordSpacing​(

String

wordSpacing)
throws

DOMException

See the word-spacing property definition in CSS2.

getZIndex

```java
String
getZIndex()
```

See the z-index property definition in CSS2.

---

#### getZIndex

String

getZIndex()

See the z-index property definition in CSS2.

setZIndex

```java
void setZIndex​(
String
zIndex)
throws
DOMException
```

See the z-index property definition in CSS2.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the new value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this property is readonly.

---

#### setZIndex

void setZIndex​(

String

zIndex)
throws

DOMException

See the z-index property definition in CSS2.

---

