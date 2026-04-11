# Class StyleConstants

**Source:** `java.desktop\javax\swing\text\StyleConstants.html`

### Class Description

```java
public class
StyleConstants

extends
Object
```

A collection of

well known

or common attribute keys
and methods to apply to an AttributeSet or MutableAttributeSet
to get/set the properties in a typesafe manner.

The paragraph attributes form the definition of a paragraph to be rendered.
All sizes are specified in points (such as found in postscript), a
device independent measure.

**Direct Known Subclasses:** StyleConstants.CharacterConstants

,

StyleConstants.ColorConstants

,

StyleConstants.FontConstants

,

StyleConstants.ParagraphConstants

---

### Field Details

#### public static final
String
ComponentElementName

Name of elements used to represent components.

**See Also:**
- Constant Field Values

---

#### public static final
String
IconElementName

Name of elements used to represent icons.

**See Also:**
- Constant Field Values

---

#### public static final
Object
NameAttribute

Attribute name used to name the collection of
attributes.

---

#### public static final
Object
ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

---

#### public static final
Object
ModelAttribute

Attribute used to identify the model for embedded
objects that have a model view separation.

---

#### public static final
Object
BidiLevel

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

---

#### public static final
Object
FontFamily

Name of the font family.

---

#### public static final
Object
Family

Name of the font family.

**Since:**
- 1.5

---

#### public static final
Object
FontSize

Name of the font size.

---

#### public static final
Object
Size

Name of the font size.

**Since:**
- 1.5

---

#### public static final
Object
Bold

Name of the bold attribute.

---

#### public static final
Object
Italic

Name of the italic attribute.

---

#### public static final
Object
Underline

Name of the underline attribute.

---

#### public static final
Object
StrikeThrough

Name of the Strikethrough attribute.

---

#### public static final
Object
Superscript

Name of the Superscript attribute.

---

#### public static final
Object
Subscript

Name of the Subscript attribute.

---

#### public static final
Object
Foreground

Name of the foreground color attribute.

---

#### public static final
Object
Background

Name of the background color attribute.

---

#### public static final
Object
ComponentAttribute

Name of the component attribute.

---

#### public static final
Object
IconAttribute

Name of the icon attribute.

---

#### public static final
Object
ComposedTextAttribute

Name of the input method composed text attribute. The value of
this attribute is an instance of AttributedString which represents
the composed text.

---

#### public static final
Object
FirstLineIndent

The amount of space to indent the first
line of the paragraph. This value may be negative
to offset in the reverse direction. The type
is Float and specifies the size of the space
in points.

---

#### public static final
Object
LeftIndent

The amount to indent the left side
of the paragraph.
Type is float and specifies the size in points.

---

#### public static final
Object
RightIndent

The amount to indent the right side
of the paragraph.
Type is float and specifies the size in points.

---

#### public static final
Object
LineSpacing

The amount of space between lines
of the paragraph.
Type is float and specifies the size as a factor of the line height

---

#### public static final
Object
SpaceAbove

The amount of space above the paragraph.
Type is float and specifies the size in points.

---

#### public static final
Object
SpaceBelow

The amount of space below the paragraph.
Type is float and specifies the size in points.

---

#### public static final
Object
Alignment

Alignment for the paragraph. The type is
Integer. Valid values are:

- ALIGN_LEFT

ALIGN_RIGHT

ALIGN_CENTER

ALIGN_JUSTIFED

---

#### public static final
Object
TabSet

TabSet for the paragraph, type is a TabSet containing
TabStops.

---

#### public static final
Object
Orientation

Orientation for a paragraph.

---

#### public static final int ALIGN_LEFT

A possible value for paragraph alignment. This
specifies that the text is aligned to the left
indent and extra whitespace should be placed on
the right.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_CENTER

A possible value for paragraph alignment. This
specifies that the text is aligned to the center
and extra whitespace should be placed equally on
the left and right.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_RIGHT

A possible value for paragraph alignment. This
specifies that the text is aligned to the right
indent and extra whitespace should be placed on
the left.

**See Also:**
- Constant Field Values

---

#### public static final int ALIGN_JUSTIFIED

A possible value for paragraph alignment. This
specifies that extra whitespace should be spread
out through the rows of the paragraph with the
text lined up with the left and right indent
except on the last line which should be aligned
to the left.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
toString()

Returns the string representation.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string

---

#### public static int getBidiLevel​(
AttributeSet
a)

Gets the BidiLevel setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value

---

#### public static void setBidiLevel​(
MutableAttributeSet
a,
int o)

Sets the BidiLevel.

**Parameters:**
- a

- the attribute set
- o

- the bidi level value

---

#### public static
Component
getComponent​(
AttributeSet
a)

Gets the component setting from the attribute list.

**Parameters:**
- a

- the attribute set

**Returns:**
- the component, null if none

---

#### public static void setComponent​(
MutableAttributeSet
a,

Component
c)

Sets the component attribute.

**Parameters:**
- a

- the attribute set
- c

- the component

---

#### public static
Icon
getIcon​(
AttributeSet
a)

Gets the icon setting from the attribute list.

**Parameters:**
- a

- the attribute set

**Returns:**
- the icon, null if none

---

#### public static void setIcon​(
MutableAttributeSet
a,

Icon
c)

Sets the icon attribute.

**Parameters:**
- a

- the attribute set
- c

- the icon

---

#### public static
String
getFontFamily​(
AttributeSet
a)

Gets the font family setting from the attribute list.

**Parameters:**
- a

- the attribute set

**Returns:**
- the font family, "Monospaced" as the default

---

#### public static void setFontFamily​(
MutableAttributeSet
a,

String
fam)

Sets the font attribute.

**Parameters:**
- a

- the attribute set
- fam

- the font

---

#### public static int getFontSize​(
AttributeSet
a)

Gets the font size setting from the attribute list.

**Parameters:**
- a

- the attribute set

**Returns:**
- the font size, 12 as the default

---

#### public static void setFontSize​(
MutableAttributeSet
a,
int s)

Sets the font size attribute.

**Parameters:**
- a

- the attribute set
- s

- the font size

---

#### public static boolean isBold​(
AttributeSet
a)

Checks whether the bold attribute is set.

**Parameters:**
- a

- the attribute set

**Returns:**
- true if set else false

---

#### public static void setBold​(
MutableAttributeSet
a,
boolean b)

Sets the bold attribute.

**Parameters:**
- a

- the attribute set
- b

- specifies true/false for setting the attribute

---

#### public static boolean isItalic​(
AttributeSet
a)

Checks whether the italic attribute is set.

**Parameters:**
- a

- the attribute set

**Returns:**
- true if set else false

---

#### public static void setItalic​(
MutableAttributeSet
a,
boolean b)

Sets the italic attribute.

**Parameters:**
- a

- the attribute set
- b

- specifies true/false for setting the attribute

---

#### public static boolean isUnderline​(
AttributeSet
a)

Checks whether the underline attribute is set.

**Parameters:**
- a

- the attribute set

**Returns:**
- true if set else false

---

#### public static boolean isStrikeThrough​(
AttributeSet
a)

Checks whether the strikethrough attribute is set.

**Parameters:**
- a

- the attribute set

**Returns:**
- true if set else false

---

#### public static boolean isSuperscript​(
AttributeSet
a)

Checks whether the superscript attribute is set.

**Parameters:**
- a

- the attribute set

**Returns:**
- true if set else false

---

#### public static boolean isSubscript​(
AttributeSet
a)

Checks whether the subscript attribute is set.

**Parameters:**
- a

- the attribute set

**Returns:**
- true if set else false

---

#### public static void setUnderline​(
MutableAttributeSet
a,
boolean b)

Sets the underline attribute.

**Parameters:**
- a

- the attribute set
- b

- specifies true/false for setting the attribute

---

#### public static void setStrikeThrough​(
MutableAttributeSet
a,
boolean b)

Sets the strikethrough attribute.

**Parameters:**
- a

- the attribute set
- b

- specifies true/false for setting the attribute

---

#### public static void setSuperscript​(
MutableAttributeSet
a,
boolean b)

Sets the superscript attribute.

**Parameters:**
- a

- the attribute set
- b

- specifies true/false for setting the attribute

---

#### public static void setSubscript​(
MutableAttributeSet
a,
boolean b)

Sets the subscript attribute.

**Parameters:**
- a

- the attribute set
- b

- specifies true/false for setting the attribute

---

#### public static
Color
getForeground​(
AttributeSet
a)

Gets the foreground color setting from the attribute list.

**Parameters:**
- a

- the attribute set

**Returns:**
- the color, Color.black as the default

---

#### public static void setForeground​(
MutableAttributeSet
a,

Color
fg)

Sets the foreground color.

**Parameters:**
- a

- the attribute set
- fg

- the color

---

#### public static
Color
getBackground​(
AttributeSet
a)

Gets the background color setting from the attribute list.

**Parameters:**
- a

- the attribute set

**Returns:**
- the color, Color.black as the default

---

#### public static void setBackground​(
MutableAttributeSet
a,

Color
fg)

Sets the background color.

**Parameters:**
- a

- the attribute set
- fg

- the color

---

#### public static float getFirstLineIndent​(
AttributeSet
a)

Gets the first line indent setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value, 0 if not set

---

#### public static void setFirstLineIndent​(
MutableAttributeSet
a,
float i)

Sets the first line indent.

**Parameters:**
- a

- the attribute set
- i

- the value

---

#### public static float getRightIndent​(
AttributeSet
a)

Gets the right indent setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value, 0 if not set

---

#### public static void setRightIndent​(
MutableAttributeSet
a,
float i)

Sets right indent.

**Parameters:**
- a

- the attribute set
- i

- the value

---

#### public static float getLeftIndent​(
AttributeSet
a)

Gets the left indent setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value, 0 if not set

---

#### public static void setLeftIndent​(
MutableAttributeSet
a,
float i)

Sets left indent.

**Parameters:**
- a

- the attribute set
- i

- the value

---

#### public static float getLineSpacing​(
AttributeSet
a)

Gets the line spacing setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value, 0 if not set

---

#### public static void setLineSpacing​(
MutableAttributeSet
a,
float i)

Sets line spacing.

**Parameters:**
- a

- the attribute set
- i

- the value

---

#### public static float getSpaceAbove​(
AttributeSet
a)

Gets the space above setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value, 0 if not set

---

#### public static void setSpaceAbove​(
MutableAttributeSet
a,
float i)

Sets space above.

**Parameters:**
- a

- the attribute set
- i

- the value

---

#### public static float getSpaceBelow​(
AttributeSet
a)

Gets the space below setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value, 0 if not set

---

#### public static void setSpaceBelow​(
MutableAttributeSet
a,
float i)

Sets space below.

**Parameters:**
- a

- the attribute set
- i

- the value

---

#### public static int getAlignment​(
AttributeSet
a)

Gets the alignment setting.

**Parameters:**
- a

- the attribute set

**Returns:**
- the value

StyleConstants.ALIGN_LEFT

if not set

---

#### public static void setAlignment​(
MutableAttributeSet
a,
int align)

Sets alignment.

**Parameters:**
- a

- the attribute set
- align

- the alignment value

---

#### public static
TabSet
getTabSet​(
AttributeSet
a)

Gets the TabSet.

**Parameters:**
- a

- the attribute set

**Returns:**
- the

TabSet

---

#### public static void setTabSet​(
MutableAttributeSet
a,

TabSet
tabs)

Sets the TabSet.

**Parameters:**
- a

- the attribute set.
- tabs

- the TabSet

---

### Additional Sections

#### Class StyleConstants

java.lang.Object

- javax.swing.text.StyleConstants

javax.swing.text.StyleConstants

**Direct Known Subclasses:** StyleConstants.CharacterConstants

,

StyleConstants.ColorConstants

,

StyleConstants.FontConstants

,

StyleConstants.ParagraphConstants

```java
public class
StyleConstants

extends
Object
```

A collection of

well known

or common attribute keys
and methods to apply to an AttributeSet or MutableAttributeSet
to get/set the properties in a typesafe manner.

The paragraph attributes form the definition of a paragraph to be rendered.
All sizes are specified in points (such as found in postscript), a
device independent measure.

public class

StyleConstants

extends

Object

A collection of

well known

or common attribute keys
and methods to apply to an AttributeSet or MutableAttributeSet
to get/set the properties in a typesafe manner.

The paragraph attributes form the definition of a paragraph to be rendered.
All sizes are specified in points (such as found in postscript), a
device independent measure.

The paragraph attributes form the definition of a paragraph to be rendered.
All sizes are specified in points (such as found in postscript), a
device independent measure.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

StyleConstants.CharacterConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a character style.

static class

StyleConstants.ColorConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a color.

static class

StyleConstants.FontConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a font.

static class

StyleConstants.ParagraphConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a paragraph style.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALIGN_CENTER

A possible value for paragraph alignment.

static int

ALIGN_JUSTIFIED

A possible value for paragraph alignment.

static int

ALIGN_LEFT

A possible value for paragraph alignment.

static int

ALIGN_RIGHT

A possible value for paragraph alignment.

static

Object

Alignment

Alignment for the paragraph.

static

Object

Background

Name of the background color attribute.

static

Object

BidiLevel

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

static

Object

Bold

Name of the bold attribute.

static

Object

ComponentAttribute

Name of the component attribute.

static

String

ComponentElementName

Name of elements used to represent components.

static

Object

ComposedTextAttribute

Name of the input method composed text attribute.

static

Object

Family

Name of the font family.

static

Object

FirstLineIndent

The amount of space to indent the first
line of the paragraph.

static

Object

FontFamily

Name of the font family.

static

Object

FontSize

Name of the font size.

static

Object

Foreground

Name of the foreground color attribute.

static

Object

IconAttribute

Name of the icon attribute.

static

String

IconElementName

Name of elements used to represent icons.

static

Object

Italic

Name of the italic attribute.

static

Object

LeftIndent

The amount to indent the left side
of the paragraph.

static

Object

LineSpacing

The amount of space between lines
of the paragraph.

static

Object

ModelAttribute

Attribute used to identify the model for embedded
objects that have a model view separation.

static

Object

NameAttribute

Attribute name used to name the collection of
attributes.

static

Object

Orientation

Orientation for a paragraph.

static

Object

ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

static

Object

RightIndent

The amount to indent the right side
of the paragraph.

static

Object

Size

Name of the font size.

static

Object

SpaceAbove

The amount of space above the paragraph.

static

Object

SpaceBelow

The amount of space below the paragraph.

static

Object

StrikeThrough

Name of the Strikethrough attribute.

static

Object

Subscript

Name of the Subscript attribute.

static

Object

Superscript

Name of the Superscript attribute.

static

Object

TabSet

TabSet for the paragraph, type is a TabSet containing
TabStops.

static

Object

Underline

Name of the underline attribute.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static int

getAlignment

​(

AttributeSet

a)

Gets the alignment setting.

static

Color

getBackground

​(

AttributeSet

a)

Gets the background color setting from the attribute list.

static int

getBidiLevel

​(

AttributeSet

a)

Gets the BidiLevel setting.

static

Component

getComponent

​(

AttributeSet

a)

Gets the component setting from the attribute list.

static float

getFirstLineIndent

​(

AttributeSet

a)

Gets the first line indent setting.

static

String

getFontFamily

​(

AttributeSet

a)

Gets the font family setting from the attribute list.

static int

getFontSize

​(

AttributeSet

a)

Gets the font size setting from the attribute list.

static

Color

getForeground

​(

AttributeSet

a)

Gets the foreground color setting from the attribute list.

static

Icon

getIcon

​(

AttributeSet

a)

Gets the icon setting from the attribute list.

static float

getLeftIndent

​(

AttributeSet

a)

Gets the left indent setting.

static float

getLineSpacing

​(

AttributeSet

a)

Gets the line spacing setting.

static float

getRightIndent

​(

AttributeSet

a)

Gets the right indent setting.

static float

getSpaceAbove

​(

AttributeSet

a)

Gets the space above setting.

static float

getSpaceBelow

​(

AttributeSet

a)

Gets the space below setting.

static

TabSet

getTabSet

​(

AttributeSet

a)

Gets the TabSet.

static boolean

isBold

​(

AttributeSet

a)

Checks whether the bold attribute is set.

static boolean

isItalic

​(

AttributeSet

a)

Checks whether the italic attribute is set.

static boolean

isStrikeThrough

​(

AttributeSet

a)

Checks whether the strikethrough attribute is set.

static boolean

isSubscript

​(

AttributeSet

a)

Checks whether the subscript attribute is set.

static boolean

isSuperscript

​(

AttributeSet

a)

Checks whether the superscript attribute is set.

static boolean

isUnderline

​(

AttributeSet

a)

Checks whether the underline attribute is set.

static void

setAlignment

​(

MutableAttributeSet

a,
int align)

Sets alignment.

static void

setBackground

​(

MutableAttributeSet

a,

Color

fg)

Sets the background color.

static void

setBidiLevel

​(

MutableAttributeSet

a,
int o)

Sets the BidiLevel.

static void

setBold

​(

MutableAttributeSet

a,
boolean b)

Sets the bold attribute.

static void

setComponent

​(

MutableAttributeSet

a,

Component

c)

Sets the component attribute.

static void

setFirstLineIndent

​(

MutableAttributeSet

a,
float i)

Sets the first line indent.

static void

setFontFamily

​(

MutableAttributeSet

a,

String

fam)

Sets the font attribute.

static void

setFontSize

​(

MutableAttributeSet

a,
int s)

Sets the font size attribute.

static void

setForeground

​(

MutableAttributeSet

a,

Color

fg)

Sets the foreground color.

static void

setIcon

​(

MutableAttributeSet

a,

Icon

c)

Sets the icon attribute.

static void

setItalic

​(

MutableAttributeSet

a,
boolean b)

Sets the italic attribute.

static void

setLeftIndent

​(

MutableAttributeSet

a,
float i)

Sets left indent.

static void

setLineSpacing

​(

MutableAttributeSet

a,
float i)

Sets line spacing.

static void

setRightIndent

​(

MutableAttributeSet

a,
float i)

Sets right indent.

static void

setSpaceAbove

​(

MutableAttributeSet

a,
float i)

Sets space above.

static void

setSpaceBelow

​(

MutableAttributeSet

a,
float i)

Sets space below.

static void

setStrikeThrough

​(

MutableAttributeSet

a,
boolean b)

Sets the strikethrough attribute.

static void

setSubscript

​(

MutableAttributeSet

a,
boolean b)

Sets the subscript attribute.

static void

setSuperscript

​(

MutableAttributeSet

a,
boolean b)

Sets the superscript attribute.

static void

setTabSet

​(

MutableAttributeSet

a,

TabSet

tabs)

Sets the TabSet.

static void

setUnderline

​(

MutableAttributeSet

a,
boolean b)

Sets the underline attribute.

String

toString

()

Returns the string representation.

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

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

StyleConstants.CharacterConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a character style.

static class

StyleConstants.ColorConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a color.

static class

StyleConstants.FontConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a font.

static class

StyleConstants.ParagraphConstants

This is a typesafe enumeration of the

well-known

attributes that contribute to a paragraph style.

---

#### Nested Class Summary

This is a typesafe enumeration of the

well-known

attributes that contribute to a character style.

This is a typesafe enumeration of the

well-known

attributes that contribute to a color.

This is a typesafe enumeration of the

well-known

attributes that contribute to a font.

This is a typesafe enumeration of the

well-known

attributes that contribute to a paragraph style.

Field Summary

Fields

Modifier and Type

Field

Description

static int

ALIGN_CENTER

A possible value for paragraph alignment.

static int

ALIGN_JUSTIFIED

A possible value for paragraph alignment.

static int

ALIGN_LEFT

A possible value for paragraph alignment.

static int

ALIGN_RIGHT

A possible value for paragraph alignment.

static

Object

Alignment

Alignment for the paragraph.

static

Object

Background

Name of the background color attribute.

static

Object

BidiLevel

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

static

Object

Bold

Name of the bold attribute.

static

Object

ComponentAttribute

Name of the component attribute.

static

String

ComponentElementName

Name of elements used to represent components.

static

Object

ComposedTextAttribute

Name of the input method composed text attribute.

static

Object

Family

Name of the font family.

static

Object

FirstLineIndent

The amount of space to indent the first
line of the paragraph.

static

Object

FontFamily

Name of the font family.

static

Object

FontSize

Name of the font size.

static

Object

Foreground

Name of the foreground color attribute.

static

Object

IconAttribute

Name of the icon attribute.

static

String

IconElementName

Name of elements used to represent icons.

static

Object

Italic

Name of the italic attribute.

static

Object

LeftIndent

The amount to indent the left side
of the paragraph.

static

Object

LineSpacing

The amount of space between lines
of the paragraph.

static

Object

ModelAttribute

Attribute used to identify the model for embedded
objects that have a model view separation.

static

Object

NameAttribute

Attribute name used to name the collection of
attributes.

static

Object

Orientation

Orientation for a paragraph.

static

Object

ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

static

Object

RightIndent

The amount to indent the right side
of the paragraph.

static

Object

Size

Name of the font size.

static

Object

SpaceAbove

The amount of space above the paragraph.

static

Object

SpaceBelow

The amount of space below the paragraph.

static

Object

StrikeThrough

Name of the Strikethrough attribute.

static

Object

Subscript

Name of the Subscript attribute.

static

Object

Superscript

Name of the Superscript attribute.

static

Object

TabSet

TabSet for the paragraph, type is a TabSet containing
TabStops.

static

Object

Underline

Name of the underline attribute.

---

#### Field Summary

A possible value for paragraph alignment.

Alignment for the paragraph.

Name of the background color attribute.

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

Name of the bold attribute.

Name of the component attribute.

Name of elements used to represent components.

Name of the input method composed text attribute.

Name of the font family.

The amount of space to indent the first
line of the paragraph.

Name of the font size.

Name of the foreground color attribute.

Name of the icon attribute.

Name of elements used to represent icons.

Name of the italic attribute.

The amount to indent the left side
of the paragraph.

The amount of space between lines
of the paragraph.

Attribute used to identify the model for embedded
objects that have a model view separation.

Attribute name used to name the collection of
attributes.

Orientation for a paragraph.

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

The amount to indent the right side
of the paragraph.

The amount of space above the paragraph.

The amount of space below the paragraph.

Name of the Strikethrough attribute.

Name of the Subscript attribute.

Name of the Superscript attribute.

TabSet for the paragraph, type is a TabSet containing
TabStops.

Name of the underline attribute.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static int

getAlignment

​(

AttributeSet

a)

Gets the alignment setting.

static

Color

getBackground

​(

AttributeSet

a)

Gets the background color setting from the attribute list.

static int

getBidiLevel

​(

AttributeSet

a)

Gets the BidiLevel setting.

static

Component

getComponent

​(

AttributeSet

a)

Gets the component setting from the attribute list.

static float

getFirstLineIndent

​(

AttributeSet

a)

Gets the first line indent setting.

static

String

getFontFamily

​(

AttributeSet

a)

Gets the font family setting from the attribute list.

static int

getFontSize

​(

AttributeSet

a)

Gets the font size setting from the attribute list.

static

Color

getForeground

​(

AttributeSet

a)

Gets the foreground color setting from the attribute list.

static

Icon

getIcon

​(

AttributeSet

a)

Gets the icon setting from the attribute list.

static float

getLeftIndent

​(

AttributeSet

a)

Gets the left indent setting.

static float

getLineSpacing

​(

AttributeSet

a)

Gets the line spacing setting.

static float

getRightIndent

​(

AttributeSet

a)

Gets the right indent setting.

static float

getSpaceAbove

​(

AttributeSet

a)

Gets the space above setting.

static float

getSpaceBelow

​(

AttributeSet

a)

Gets the space below setting.

static

TabSet

getTabSet

​(

AttributeSet

a)

Gets the TabSet.

static boolean

isBold

​(

AttributeSet

a)

Checks whether the bold attribute is set.

static boolean

isItalic

​(

AttributeSet

a)

Checks whether the italic attribute is set.

static boolean

isStrikeThrough

​(

AttributeSet

a)

Checks whether the strikethrough attribute is set.

static boolean

isSubscript

​(

AttributeSet

a)

Checks whether the subscript attribute is set.

static boolean

isSuperscript

​(

AttributeSet

a)

Checks whether the superscript attribute is set.

static boolean

isUnderline

​(

AttributeSet

a)

Checks whether the underline attribute is set.

static void

setAlignment

​(

MutableAttributeSet

a,
int align)

Sets alignment.

static void

setBackground

​(

MutableAttributeSet

a,

Color

fg)

Sets the background color.

static void

setBidiLevel

​(

MutableAttributeSet

a,
int o)

Sets the BidiLevel.

static void

setBold

​(

MutableAttributeSet

a,
boolean b)

Sets the bold attribute.

static void

setComponent

​(

MutableAttributeSet

a,

Component

c)

Sets the component attribute.

static void

setFirstLineIndent

​(

MutableAttributeSet

a,
float i)

Sets the first line indent.

static void

setFontFamily

​(

MutableAttributeSet

a,

String

fam)

Sets the font attribute.

static void

setFontSize

​(

MutableAttributeSet

a,
int s)

Sets the font size attribute.

static void

setForeground

​(

MutableAttributeSet

a,

Color

fg)

Sets the foreground color.

static void

setIcon

​(

MutableAttributeSet

a,

Icon

c)

Sets the icon attribute.

static void

setItalic

​(

MutableAttributeSet

a,
boolean b)

Sets the italic attribute.

static void

setLeftIndent

​(

MutableAttributeSet

a,
float i)

Sets left indent.

static void

setLineSpacing

​(

MutableAttributeSet

a,
float i)

Sets line spacing.

static void

setRightIndent

​(

MutableAttributeSet

a,
float i)

Sets right indent.

static void

setSpaceAbove

​(

MutableAttributeSet

a,
float i)

Sets space above.

static void

setSpaceBelow

​(

MutableAttributeSet

a,
float i)

Sets space below.

static void

setStrikeThrough

​(

MutableAttributeSet

a,
boolean b)

Sets the strikethrough attribute.

static void

setSubscript

​(

MutableAttributeSet

a,
boolean b)

Sets the subscript attribute.

static void

setSuperscript

​(

MutableAttributeSet

a,
boolean b)

Sets the superscript attribute.

static void

setTabSet

​(

MutableAttributeSet

a,

TabSet

tabs)

Sets the TabSet.

static void

setUnderline

​(

MutableAttributeSet

a,
boolean b)

Sets the underline attribute.

String

toString

()

Returns the string representation.

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

wait

,

wait

,

wait

---

#### Method Summary

Gets the alignment setting.

Gets the background color setting from the attribute list.

Gets the BidiLevel setting.

Gets the component setting from the attribute list.

Gets the first line indent setting.

Gets the font family setting from the attribute list.

Gets the font size setting from the attribute list.

Gets the foreground color setting from the attribute list.

Gets the icon setting from the attribute list.

Gets the left indent setting.

Gets the line spacing setting.

Gets the right indent setting.

Gets the space above setting.

Gets the space below setting.

Gets the TabSet.

Checks whether the bold attribute is set.

Checks whether the italic attribute is set.

Checks whether the strikethrough attribute is set.

Checks whether the subscript attribute is set.

Checks whether the superscript attribute is set.

Checks whether the underline attribute is set.

Sets alignment.

Sets the background color.

Sets the BidiLevel.

Sets the bold attribute.

Sets the component attribute.

Sets the first line indent.

Sets the font attribute.

Sets the font size attribute.

Sets the foreground color.

Sets the icon attribute.

Sets the italic attribute.

Sets left indent.

Sets line spacing.

Sets right indent.

Sets space above.

Sets space below.

Sets the strikethrough attribute.

Sets the subscript attribute.

Sets the superscript attribute.

Sets the TabSet.

Sets the underline attribute.

Returns the string representation.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- ComponentElementName

```java
public static final
String
ComponentElementName
```

Name of elements used to represent components.

**See Also:** Constant Field Values

- IconElementName

```java
public static final
String
IconElementName
```

Name of elements used to represent icons.

**See Also:** Constant Field Values

- NameAttribute

```java
public static final
Object
NameAttribute
```

Attribute name used to name the collection of
attributes.

- ResolveAttribute

```java
public static final
Object
ResolveAttribute
```

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

- ModelAttribute

```java
public static final
Object
ModelAttribute
```

Attribute used to identify the model for embedded
objects that have a model view separation.

- BidiLevel

```java
public static final
Object
BidiLevel
```

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

- FontFamily

```java
public static final
Object
FontFamily
```

Name of the font family.

- Family

```java
public static final
Object
Family
```

Name of the font family.

**Since:** 1.5

- FontSize

```java
public static final
Object
FontSize
```

Name of the font size.

- Size

```java
public static final
Object
Size
```

Name of the font size.

**Since:** 1.5

- Bold

```java
public static final
Object
Bold
```

Name of the bold attribute.

- Italic

```java
public static final
Object
Italic
```

Name of the italic attribute.

- Underline

```java
public static final
Object
Underline
```

Name of the underline attribute.

- StrikeThrough

```java
public static final
Object
StrikeThrough
```

Name of the Strikethrough attribute.

- Superscript

```java
public static final
Object
Superscript
```

Name of the Superscript attribute.

- Subscript

```java
public static final
Object
Subscript
```

Name of the Subscript attribute.

- Foreground

```java
public static final
Object
Foreground
```

Name of the foreground color attribute.

- Background

```java
public static final
Object
Background
```

Name of the background color attribute.

- ComponentAttribute

```java
public static final
Object
ComponentAttribute
```

Name of the component attribute.

- IconAttribute

```java
public static final
Object
IconAttribute
```

Name of the icon attribute.

- ComposedTextAttribute

```java
public static final
Object
ComposedTextAttribute
```

Name of the input method composed text attribute. The value of
this attribute is an instance of AttributedString which represents
the composed text.

- FirstLineIndent

```java
public static final
Object
FirstLineIndent
```

The amount of space to indent the first
line of the paragraph. This value may be negative
to offset in the reverse direction. The type
is Float and specifies the size of the space
in points.

- LeftIndent

```java
public static final
Object
LeftIndent
```

The amount to indent the left side
of the paragraph.
Type is float and specifies the size in points.

- RightIndent

```java
public static final
Object
RightIndent
```

The amount to indent the right side
of the paragraph.
Type is float and specifies the size in points.

- LineSpacing

```java
public static final
Object
LineSpacing
```

The amount of space between lines
of the paragraph.
Type is float and specifies the size as a factor of the line height

- SpaceAbove

```java
public static final
Object
SpaceAbove
```

The amount of space above the paragraph.
Type is float and specifies the size in points.

- SpaceBelow

```java
public static final
Object
SpaceBelow
```

The amount of space below the paragraph.
Type is float and specifies the size in points.

- Alignment

```java
public static final
Object
Alignment
```

Alignment for the paragraph. The type is
Integer. Valid values are:

- ALIGN_LEFT

ALIGN_RIGHT

ALIGN_CENTER

ALIGN_JUSTIFED

- TabSet

```java
public static final
Object
TabSet
```

TabSet for the paragraph, type is a TabSet containing
TabStops.

- Orientation

```java
public static final
Object
Orientation
```

Orientation for a paragraph.

- ALIGN_LEFT

```java
public static final int ALIGN_LEFT
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the left
indent and extra whitespace should be placed on
the right.

**See Also:** Constant Field Values

- ALIGN_CENTER

```java
public static final int ALIGN_CENTER
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the center
and extra whitespace should be placed equally on
the left and right.

**See Also:** Constant Field Values

- ALIGN_RIGHT

```java
public static final int ALIGN_RIGHT
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the right
indent and extra whitespace should be placed on
the left.

**See Also:** Constant Field Values

- ALIGN_JUSTIFIED

```java
public static final int ALIGN_JUSTIFIED
```

A possible value for paragraph alignment. This
specifies that extra whitespace should be spread
out through the rows of the paragraph with the
text lined up with the left and right indent
except on the last line which should be aligned
to the left.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns the string representation.

**Overrides:** toString

in class

Object
**Returns:** the string

- getBidiLevel

```java
public static int getBidiLevel​(
AttributeSet
a)
```

Gets the BidiLevel setting.

**Parameters:** a

- the attribute set
**Returns:** the value

- setBidiLevel

```java
public static void setBidiLevel​(
MutableAttributeSet
a,
int o)
```

Sets the BidiLevel.

**Parameters:** a

- the attribute set
**Parameters:** o

- the bidi level value

- getComponent

```java
public static
Component
getComponent​(
AttributeSet
a)
```

Gets the component setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the component, null if none

- setComponent

```java
public static void setComponent​(
MutableAttributeSet
a,

Component
c)
```

Sets the component attribute.

**Parameters:** a

- the attribute set
**Parameters:** c

- the component

- getIcon

```java
public static
Icon
getIcon​(
AttributeSet
a)
```

Gets the icon setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the icon, null if none

- setIcon

```java
public static void setIcon​(
MutableAttributeSet
a,

Icon
c)
```

Sets the icon attribute.

**Parameters:** a

- the attribute set
**Parameters:** c

- the icon

- getFontFamily

```java
public static
String
getFontFamily​(
AttributeSet
a)
```

Gets the font family setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the font family, "Monospaced" as the default

- setFontFamily

```java
public static void setFontFamily​(
MutableAttributeSet
a,

String
fam)
```

Sets the font attribute.

**Parameters:** a

- the attribute set
**Parameters:** fam

- the font

- getFontSize

```java
public static int getFontSize​(
AttributeSet
a)
```

Gets the font size setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the font size, 12 as the default

- setFontSize

```java
public static void setFontSize​(
MutableAttributeSet
a,
int s)
```

Sets the font size attribute.

**Parameters:** a

- the attribute set
**Parameters:** s

- the font size

- isBold

```java
public static boolean isBold​(
AttributeSet
a)
```

Checks whether the bold attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- setBold

```java
public static void setBold​(
MutableAttributeSet
a,
boolean b)
```

Sets the bold attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- isItalic

```java
public static boolean isItalic​(
AttributeSet
a)
```

Checks whether the italic attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- setItalic

```java
public static void setItalic​(
MutableAttributeSet
a,
boolean b)
```

Sets the italic attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- isUnderline

```java
public static boolean isUnderline​(
AttributeSet
a)
```

Checks whether the underline attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- isStrikeThrough

```java
public static boolean isStrikeThrough​(
AttributeSet
a)
```

Checks whether the strikethrough attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- isSuperscript

```java
public static boolean isSuperscript​(
AttributeSet
a)
```

Checks whether the superscript attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- isSubscript

```java
public static boolean isSubscript​(
AttributeSet
a)
```

Checks whether the subscript attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- setUnderline

```java
public static void setUnderline​(
MutableAttributeSet
a,
boolean b)
```

Sets the underline attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- setStrikeThrough

```java
public static void setStrikeThrough​(
MutableAttributeSet
a,
boolean b)
```

Sets the strikethrough attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- setSuperscript

```java
public static void setSuperscript​(
MutableAttributeSet
a,
boolean b)
```

Sets the superscript attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- setSubscript

```java
public static void setSubscript​(
MutableAttributeSet
a,
boolean b)
```

Sets the subscript attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- getForeground

```java
public static
Color
getForeground​(
AttributeSet
a)
```

Gets the foreground color setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the color, Color.black as the default

- setForeground

```java
public static void setForeground​(
MutableAttributeSet
a,

Color
fg)
```

Sets the foreground color.

**Parameters:** a

- the attribute set
**Parameters:** fg

- the color

- getBackground

```java
public static
Color
getBackground​(
AttributeSet
a)
```

Gets the background color setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the color, Color.black as the default

- setBackground

```java
public static void setBackground​(
MutableAttributeSet
a,

Color
fg)
```

Sets the background color.

**Parameters:** a

- the attribute set
**Parameters:** fg

- the color

- getFirstLineIndent

```java
public static float getFirstLineIndent​(
AttributeSet
a)
```

Gets the first line indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setFirstLineIndent

```java
public static void setFirstLineIndent​(
MutableAttributeSet
a,
float i)
```

Sets the first line indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getRightIndent

```java
public static float getRightIndent​(
AttributeSet
a)
```

Gets the right indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setRightIndent

```java
public static void setRightIndent​(
MutableAttributeSet
a,
float i)
```

Sets right indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getLeftIndent

```java
public static float getLeftIndent​(
AttributeSet
a)
```

Gets the left indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setLeftIndent

```java
public static void setLeftIndent​(
MutableAttributeSet
a,
float i)
```

Sets left indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getLineSpacing

```java
public static float getLineSpacing​(
AttributeSet
a)
```

Gets the line spacing setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setLineSpacing

```java
public static void setLineSpacing​(
MutableAttributeSet
a,
float i)
```

Sets line spacing.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getSpaceAbove

```java
public static float getSpaceAbove​(
AttributeSet
a)
```

Gets the space above setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setSpaceAbove

```java
public static void setSpaceAbove​(
MutableAttributeSet
a,
float i)
```

Sets space above.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getSpaceBelow

```java
public static float getSpaceBelow​(
AttributeSet
a)
```

Gets the space below setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setSpaceBelow

```java
public static void setSpaceBelow​(
MutableAttributeSet
a,
float i)
```

Sets space below.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getAlignment

```java
public static int getAlignment​(
AttributeSet
a)
```

Gets the alignment setting.

**Parameters:** a

- the attribute set
**Returns:** the value

StyleConstants.ALIGN_LEFT

if not set

- setAlignment

```java
public static void setAlignment​(
MutableAttributeSet
a,
int align)
```

Sets alignment.

**Parameters:** a

- the attribute set
**Parameters:** align

- the alignment value

- getTabSet

```java
public static
TabSet
getTabSet​(
AttributeSet
a)
```

Gets the TabSet.

**Parameters:** a

- the attribute set
**Returns:** the

TabSet

- setTabSet

```java
public static void setTabSet​(
MutableAttributeSet
a,

TabSet
tabs)
```

Sets the TabSet.

**Parameters:** a

- the attribute set.
**Parameters:** tabs

- the TabSet

Field Detail

- ComponentElementName

```java
public static final
String
ComponentElementName
```

Name of elements used to represent components.

**See Also:** Constant Field Values

- IconElementName

```java
public static final
String
IconElementName
```

Name of elements used to represent icons.

**See Also:** Constant Field Values

- NameAttribute

```java
public static final
Object
NameAttribute
```

Attribute name used to name the collection of
attributes.

- ResolveAttribute

```java
public static final
Object
ResolveAttribute
```

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

- ModelAttribute

```java
public static final
Object
ModelAttribute
```

Attribute used to identify the model for embedded
objects that have a model view separation.

- BidiLevel

```java
public static final
Object
BidiLevel
```

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

- FontFamily

```java
public static final
Object
FontFamily
```

Name of the font family.

- Family

```java
public static final
Object
Family
```

Name of the font family.

**Since:** 1.5

- FontSize

```java
public static final
Object
FontSize
```

Name of the font size.

- Size

```java
public static final
Object
Size
```

Name of the font size.

**Since:** 1.5

- Bold

```java
public static final
Object
Bold
```

Name of the bold attribute.

- Italic

```java
public static final
Object
Italic
```

Name of the italic attribute.

- Underline

```java
public static final
Object
Underline
```

Name of the underline attribute.

- StrikeThrough

```java
public static final
Object
StrikeThrough
```

Name of the Strikethrough attribute.

- Superscript

```java
public static final
Object
Superscript
```

Name of the Superscript attribute.

- Subscript

```java
public static final
Object
Subscript
```

Name of the Subscript attribute.

- Foreground

```java
public static final
Object
Foreground
```

Name of the foreground color attribute.

- Background

```java
public static final
Object
Background
```

Name of the background color attribute.

- ComponentAttribute

```java
public static final
Object
ComponentAttribute
```

Name of the component attribute.

- IconAttribute

```java
public static final
Object
IconAttribute
```

Name of the icon attribute.

- ComposedTextAttribute

```java
public static final
Object
ComposedTextAttribute
```

Name of the input method composed text attribute. The value of
this attribute is an instance of AttributedString which represents
the composed text.

- FirstLineIndent

```java
public static final
Object
FirstLineIndent
```

The amount of space to indent the first
line of the paragraph. This value may be negative
to offset in the reverse direction. The type
is Float and specifies the size of the space
in points.

- LeftIndent

```java
public static final
Object
LeftIndent
```

The amount to indent the left side
of the paragraph.
Type is float and specifies the size in points.

- RightIndent

```java
public static final
Object
RightIndent
```

The amount to indent the right side
of the paragraph.
Type is float and specifies the size in points.

- LineSpacing

```java
public static final
Object
LineSpacing
```

The amount of space between lines
of the paragraph.
Type is float and specifies the size as a factor of the line height

- SpaceAbove

```java
public static final
Object
SpaceAbove
```

The amount of space above the paragraph.
Type is float and specifies the size in points.

- SpaceBelow

```java
public static final
Object
SpaceBelow
```

The amount of space below the paragraph.
Type is float and specifies the size in points.

- Alignment

```java
public static final
Object
Alignment
```

Alignment for the paragraph. The type is
Integer. Valid values are:

- ALIGN_LEFT

ALIGN_RIGHT

ALIGN_CENTER

ALIGN_JUSTIFED

- TabSet

```java
public static final
Object
TabSet
```

TabSet for the paragraph, type is a TabSet containing
TabStops.

- Orientation

```java
public static final
Object
Orientation
```

Orientation for a paragraph.

- ALIGN_LEFT

```java
public static final int ALIGN_LEFT
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the left
indent and extra whitespace should be placed on
the right.

**See Also:** Constant Field Values

- ALIGN_CENTER

```java
public static final int ALIGN_CENTER
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the center
and extra whitespace should be placed equally on
the left and right.

**See Also:** Constant Field Values

- ALIGN_RIGHT

```java
public static final int ALIGN_RIGHT
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the right
indent and extra whitespace should be placed on
the left.

**See Also:** Constant Field Values

- ALIGN_JUSTIFIED

```java
public static final int ALIGN_JUSTIFIED
```

A possible value for paragraph alignment. This
specifies that extra whitespace should be spread
out through the rows of the paragraph with the
text lined up with the left and right indent
except on the last line which should be aligned
to the left.

**See Also:** Constant Field Values

---

#### Field Detail

ComponentElementName

```java
public static final
String
ComponentElementName
```

Name of elements used to represent components.

**See Also:** Constant Field Values

---

#### ComponentElementName

public static final

String

ComponentElementName

Name of elements used to represent components.

IconElementName

```java
public static final
String
IconElementName
```

Name of elements used to represent icons.

**See Also:** Constant Field Values

---

#### IconElementName

public static final

String

IconElementName

Name of elements used to represent icons.

NameAttribute

```java
public static final
Object
NameAttribute
```

Attribute name used to name the collection of
attributes.

---

#### NameAttribute

public static final

Object

NameAttribute

Attribute name used to name the collection of
attributes.

ResolveAttribute

```java
public static final
Object
ResolveAttribute
```

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

---

#### ResolveAttribute

public static final

Object

ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

ModelAttribute

```java
public static final
Object
ModelAttribute
```

Attribute used to identify the model for embedded
objects that have a model view separation.

---

#### ModelAttribute

public static final

Object

ModelAttribute

Attribute used to identify the model for embedded
objects that have a model view separation.

BidiLevel

```java
public static final
Object
BidiLevel
```

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

---

#### BidiLevel

public static final

Object

BidiLevel

Bidirectional level of a character as assigned by the Unicode bidi
algorithm.

FontFamily

```java
public static final
Object
FontFamily
```

Name of the font family.

---

#### FontFamily

public static final

Object

FontFamily

Name of the font family.

Family

```java
public static final
Object
Family
```

Name of the font family.

**Since:** 1.5

---

#### Family

public static final

Object

Family

Name of the font family.

FontSize

```java
public static final
Object
FontSize
```

Name of the font size.

---

#### FontSize

public static final

Object

FontSize

Name of the font size.

Size

```java
public static final
Object
Size
```

Name of the font size.

**Since:** 1.5

---

#### Size

public static final

Object

Size

Name of the font size.

Bold

```java
public static final
Object
Bold
```

Name of the bold attribute.

---

#### Bold

public static final

Object

Bold

Name of the bold attribute.

Italic

```java
public static final
Object
Italic
```

Name of the italic attribute.

---

#### Italic

public static final

Object

Italic

Name of the italic attribute.

Underline

```java
public static final
Object
Underline
```

Name of the underline attribute.

---

#### Underline

public static final

Object

Underline

Name of the underline attribute.

StrikeThrough

```java
public static final
Object
StrikeThrough
```

Name of the Strikethrough attribute.

---

#### StrikeThrough

public static final

Object

StrikeThrough

Name of the Strikethrough attribute.

Superscript

```java
public static final
Object
Superscript
```

Name of the Superscript attribute.

---

#### Superscript

public static final

Object

Superscript

Name of the Superscript attribute.

Subscript

```java
public static final
Object
Subscript
```

Name of the Subscript attribute.

---

#### Subscript

public static final

Object

Subscript

Name of the Subscript attribute.

Foreground

```java
public static final
Object
Foreground
```

Name of the foreground color attribute.

---

#### Foreground

public static final

Object

Foreground

Name of the foreground color attribute.

Background

```java
public static final
Object
Background
```

Name of the background color attribute.

---

#### Background

public static final

Object

Background

Name of the background color attribute.

ComponentAttribute

```java
public static final
Object
ComponentAttribute
```

Name of the component attribute.

---

#### ComponentAttribute

public static final

Object

ComponentAttribute

Name of the component attribute.

IconAttribute

```java
public static final
Object
IconAttribute
```

Name of the icon attribute.

---

#### IconAttribute

public static final

Object

IconAttribute

Name of the icon attribute.

ComposedTextAttribute

```java
public static final
Object
ComposedTextAttribute
```

Name of the input method composed text attribute. The value of
this attribute is an instance of AttributedString which represents
the composed text.

---

#### ComposedTextAttribute

public static final

Object

ComposedTextAttribute

Name of the input method composed text attribute. The value of
this attribute is an instance of AttributedString which represents
the composed text.

FirstLineIndent

```java
public static final
Object
FirstLineIndent
```

The amount of space to indent the first
line of the paragraph. This value may be negative
to offset in the reverse direction. The type
is Float and specifies the size of the space
in points.

---

#### FirstLineIndent

public static final

Object

FirstLineIndent

The amount of space to indent the first
line of the paragraph. This value may be negative
to offset in the reverse direction. The type
is Float and specifies the size of the space
in points.

LeftIndent

```java
public static final
Object
LeftIndent
```

The amount to indent the left side
of the paragraph.
Type is float and specifies the size in points.

---

#### LeftIndent

public static final

Object

LeftIndent

The amount to indent the left side
of the paragraph.
Type is float and specifies the size in points.

RightIndent

```java
public static final
Object
RightIndent
```

The amount to indent the right side
of the paragraph.
Type is float and specifies the size in points.

---

#### RightIndent

public static final

Object

RightIndent

The amount to indent the right side
of the paragraph.
Type is float and specifies the size in points.

LineSpacing

```java
public static final
Object
LineSpacing
```

The amount of space between lines
of the paragraph.
Type is float and specifies the size as a factor of the line height

---

#### LineSpacing

public static final

Object

LineSpacing

The amount of space between lines
of the paragraph.
Type is float and specifies the size as a factor of the line height

SpaceAbove

```java
public static final
Object
SpaceAbove
```

The amount of space above the paragraph.
Type is float and specifies the size in points.

---

#### SpaceAbove

public static final

Object

SpaceAbove

The amount of space above the paragraph.
Type is float and specifies the size in points.

SpaceBelow

```java
public static final
Object
SpaceBelow
```

The amount of space below the paragraph.
Type is float and specifies the size in points.

---

#### SpaceBelow

public static final

Object

SpaceBelow

The amount of space below the paragraph.
Type is float and specifies the size in points.

Alignment

```java
public static final
Object
Alignment
```

Alignment for the paragraph. The type is
Integer. Valid values are:

- ALIGN_LEFT

ALIGN_RIGHT

ALIGN_CENTER

ALIGN_JUSTIFED

---

#### Alignment

public static final

Object

Alignment

Alignment for the paragraph. The type is
Integer. Valid values are:

- ALIGN_LEFT

ALIGN_RIGHT

ALIGN_CENTER

ALIGN_JUSTIFED

ALIGN_LEFT

ALIGN_RIGHT

ALIGN_CENTER

ALIGN_JUSTIFED

TabSet

```java
public static final
Object
TabSet
```

TabSet for the paragraph, type is a TabSet containing
TabStops.

---

#### TabSet

public static final

Object

TabSet

TabSet for the paragraph, type is a TabSet containing
TabStops.

Orientation

```java
public static final
Object
Orientation
```

Orientation for a paragraph.

---

#### Orientation

public static final

Object

Orientation

Orientation for a paragraph.

ALIGN_LEFT

```java
public static final int ALIGN_LEFT
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the left
indent and extra whitespace should be placed on
the right.

**See Also:** Constant Field Values

---

#### ALIGN_LEFT

public static final int ALIGN_LEFT

A possible value for paragraph alignment. This
specifies that the text is aligned to the left
indent and extra whitespace should be placed on
the right.

ALIGN_CENTER

```java
public static final int ALIGN_CENTER
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the center
and extra whitespace should be placed equally on
the left and right.

**See Also:** Constant Field Values

---

#### ALIGN_CENTER

public static final int ALIGN_CENTER

A possible value for paragraph alignment. This
specifies that the text is aligned to the center
and extra whitespace should be placed equally on
the left and right.

ALIGN_RIGHT

```java
public static final int ALIGN_RIGHT
```

A possible value for paragraph alignment. This
specifies that the text is aligned to the right
indent and extra whitespace should be placed on
the left.

**See Also:** Constant Field Values

---

#### ALIGN_RIGHT

public static final int ALIGN_RIGHT

A possible value for paragraph alignment. This
specifies that the text is aligned to the right
indent and extra whitespace should be placed on
the left.

ALIGN_JUSTIFIED

```java
public static final int ALIGN_JUSTIFIED
```

A possible value for paragraph alignment. This
specifies that extra whitespace should be spread
out through the rows of the paragraph with the
text lined up with the left and right indent
except on the last line which should be aligned
to the left.

**See Also:** Constant Field Values

---

#### ALIGN_JUSTIFIED

public static final int ALIGN_JUSTIFIED

A possible value for paragraph alignment. This
specifies that extra whitespace should be spread
out through the rows of the paragraph with the
text lined up with the left and right indent
except on the last line which should be aligned
to the left.

Method Detail

- toString

```java
public
String
toString()
```

Returns the string representation.

**Overrides:** toString

in class

Object
**Returns:** the string

- getBidiLevel

```java
public static int getBidiLevel​(
AttributeSet
a)
```

Gets the BidiLevel setting.

**Parameters:** a

- the attribute set
**Returns:** the value

- setBidiLevel

```java
public static void setBidiLevel​(
MutableAttributeSet
a,
int o)
```

Sets the BidiLevel.

**Parameters:** a

- the attribute set
**Parameters:** o

- the bidi level value

- getComponent

```java
public static
Component
getComponent​(
AttributeSet
a)
```

Gets the component setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the component, null if none

- setComponent

```java
public static void setComponent​(
MutableAttributeSet
a,

Component
c)
```

Sets the component attribute.

**Parameters:** a

- the attribute set
**Parameters:** c

- the component

- getIcon

```java
public static
Icon
getIcon​(
AttributeSet
a)
```

Gets the icon setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the icon, null if none

- setIcon

```java
public static void setIcon​(
MutableAttributeSet
a,

Icon
c)
```

Sets the icon attribute.

**Parameters:** a

- the attribute set
**Parameters:** c

- the icon

- getFontFamily

```java
public static
String
getFontFamily​(
AttributeSet
a)
```

Gets the font family setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the font family, "Monospaced" as the default

- setFontFamily

```java
public static void setFontFamily​(
MutableAttributeSet
a,

String
fam)
```

Sets the font attribute.

**Parameters:** a

- the attribute set
**Parameters:** fam

- the font

- getFontSize

```java
public static int getFontSize​(
AttributeSet
a)
```

Gets the font size setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the font size, 12 as the default

- setFontSize

```java
public static void setFontSize​(
MutableAttributeSet
a,
int s)
```

Sets the font size attribute.

**Parameters:** a

- the attribute set
**Parameters:** s

- the font size

- isBold

```java
public static boolean isBold​(
AttributeSet
a)
```

Checks whether the bold attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- setBold

```java
public static void setBold​(
MutableAttributeSet
a,
boolean b)
```

Sets the bold attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- isItalic

```java
public static boolean isItalic​(
AttributeSet
a)
```

Checks whether the italic attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- setItalic

```java
public static void setItalic​(
MutableAttributeSet
a,
boolean b)
```

Sets the italic attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- isUnderline

```java
public static boolean isUnderline​(
AttributeSet
a)
```

Checks whether the underline attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- isStrikeThrough

```java
public static boolean isStrikeThrough​(
AttributeSet
a)
```

Checks whether the strikethrough attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- isSuperscript

```java
public static boolean isSuperscript​(
AttributeSet
a)
```

Checks whether the superscript attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- isSubscript

```java
public static boolean isSubscript​(
AttributeSet
a)
```

Checks whether the subscript attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

- setUnderline

```java
public static void setUnderline​(
MutableAttributeSet
a,
boolean b)
```

Sets the underline attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- setStrikeThrough

```java
public static void setStrikeThrough​(
MutableAttributeSet
a,
boolean b)
```

Sets the strikethrough attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- setSuperscript

```java
public static void setSuperscript​(
MutableAttributeSet
a,
boolean b)
```

Sets the superscript attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- setSubscript

```java
public static void setSubscript​(
MutableAttributeSet
a,
boolean b)
```

Sets the subscript attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

- getForeground

```java
public static
Color
getForeground​(
AttributeSet
a)
```

Gets the foreground color setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the color, Color.black as the default

- setForeground

```java
public static void setForeground​(
MutableAttributeSet
a,

Color
fg)
```

Sets the foreground color.

**Parameters:** a

- the attribute set
**Parameters:** fg

- the color

- getBackground

```java
public static
Color
getBackground​(
AttributeSet
a)
```

Gets the background color setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the color, Color.black as the default

- setBackground

```java
public static void setBackground​(
MutableAttributeSet
a,

Color
fg)
```

Sets the background color.

**Parameters:** a

- the attribute set
**Parameters:** fg

- the color

- getFirstLineIndent

```java
public static float getFirstLineIndent​(
AttributeSet
a)
```

Gets the first line indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setFirstLineIndent

```java
public static void setFirstLineIndent​(
MutableAttributeSet
a,
float i)
```

Sets the first line indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getRightIndent

```java
public static float getRightIndent​(
AttributeSet
a)
```

Gets the right indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setRightIndent

```java
public static void setRightIndent​(
MutableAttributeSet
a,
float i)
```

Sets right indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getLeftIndent

```java
public static float getLeftIndent​(
AttributeSet
a)
```

Gets the left indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setLeftIndent

```java
public static void setLeftIndent​(
MutableAttributeSet
a,
float i)
```

Sets left indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getLineSpacing

```java
public static float getLineSpacing​(
AttributeSet
a)
```

Gets the line spacing setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setLineSpacing

```java
public static void setLineSpacing​(
MutableAttributeSet
a,
float i)
```

Sets line spacing.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getSpaceAbove

```java
public static float getSpaceAbove​(
AttributeSet
a)
```

Gets the space above setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setSpaceAbove

```java
public static void setSpaceAbove​(
MutableAttributeSet
a,
float i)
```

Sets space above.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getSpaceBelow

```java
public static float getSpaceBelow​(
AttributeSet
a)
```

Gets the space below setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

- setSpaceBelow

```java
public static void setSpaceBelow​(
MutableAttributeSet
a,
float i)
```

Sets space below.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

- getAlignment

```java
public static int getAlignment​(
AttributeSet
a)
```

Gets the alignment setting.

**Parameters:** a

- the attribute set
**Returns:** the value

StyleConstants.ALIGN_LEFT

if not set

- setAlignment

```java
public static void setAlignment​(
MutableAttributeSet
a,
int align)
```

Sets alignment.

**Parameters:** a

- the attribute set
**Parameters:** align

- the alignment value

- getTabSet

```java
public static
TabSet
getTabSet​(
AttributeSet
a)
```

Gets the TabSet.

**Parameters:** a

- the attribute set
**Returns:** the

TabSet

- setTabSet

```java
public static void setTabSet​(
MutableAttributeSet
a,

TabSet
tabs)
```

Sets the TabSet.

**Parameters:** a

- the attribute set.
**Parameters:** tabs

- the TabSet

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns the string representation.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### toString

public

String

toString()

Returns the string representation.

getBidiLevel

```java
public static int getBidiLevel​(
AttributeSet
a)
```

Gets the BidiLevel setting.

**Parameters:** a

- the attribute set
**Returns:** the value

---

#### getBidiLevel

public static int getBidiLevel​(

AttributeSet

a)

Gets the BidiLevel setting.

setBidiLevel

```java
public static void setBidiLevel​(
MutableAttributeSet
a,
int o)
```

Sets the BidiLevel.

**Parameters:** a

- the attribute set
**Parameters:** o

- the bidi level value

---

#### setBidiLevel

public static void setBidiLevel​(

MutableAttributeSet

a,
int o)

Sets the BidiLevel.

getComponent

```java
public static
Component
getComponent​(
AttributeSet
a)
```

Gets the component setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the component, null if none

---

#### getComponent

public static

Component

getComponent​(

AttributeSet

a)

Gets the component setting from the attribute list.

setComponent

```java
public static void setComponent​(
MutableAttributeSet
a,

Component
c)
```

Sets the component attribute.

**Parameters:** a

- the attribute set
**Parameters:** c

- the component

---

#### setComponent

public static void setComponent​(

MutableAttributeSet

a,

Component

c)

Sets the component attribute.

getIcon

```java
public static
Icon
getIcon​(
AttributeSet
a)
```

Gets the icon setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the icon, null if none

---

#### getIcon

public static

Icon

getIcon​(

AttributeSet

a)

Gets the icon setting from the attribute list.

setIcon

```java
public static void setIcon​(
MutableAttributeSet
a,

Icon
c)
```

Sets the icon attribute.

**Parameters:** a

- the attribute set
**Parameters:** c

- the icon

---

#### setIcon

public static void setIcon​(

MutableAttributeSet

a,

Icon

c)

Sets the icon attribute.

getFontFamily

```java
public static
String
getFontFamily​(
AttributeSet
a)
```

Gets the font family setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the font family, "Monospaced" as the default

---

#### getFontFamily

public static

String

getFontFamily​(

AttributeSet

a)

Gets the font family setting from the attribute list.

setFontFamily

```java
public static void setFontFamily​(
MutableAttributeSet
a,

String
fam)
```

Sets the font attribute.

**Parameters:** a

- the attribute set
**Parameters:** fam

- the font

---

#### setFontFamily

public static void setFontFamily​(

MutableAttributeSet

a,

String

fam)

Sets the font attribute.

getFontSize

```java
public static int getFontSize​(
AttributeSet
a)
```

Gets the font size setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the font size, 12 as the default

---

#### getFontSize

public static int getFontSize​(

AttributeSet

a)

Gets the font size setting from the attribute list.

setFontSize

```java
public static void setFontSize​(
MutableAttributeSet
a,
int s)
```

Sets the font size attribute.

**Parameters:** a

- the attribute set
**Parameters:** s

- the font size

---

#### setFontSize

public static void setFontSize​(

MutableAttributeSet

a,
int s)

Sets the font size attribute.

isBold

```java
public static boolean isBold​(
AttributeSet
a)
```

Checks whether the bold attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

---

#### isBold

public static boolean isBold​(

AttributeSet

a)

Checks whether the bold attribute is set.

setBold

```java
public static void setBold​(
MutableAttributeSet
a,
boolean b)
```

Sets the bold attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

---

#### setBold

public static void setBold​(

MutableAttributeSet

a,
boolean b)

Sets the bold attribute.

isItalic

```java
public static boolean isItalic​(
AttributeSet
a)
```

Checks whether the italic attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

---

#### isItalic

public static boolean isItalic​(

AttributeSet

a)

Checks whether the italic attribute is set.

setItalic

```java
public static void setItalic​(
MutableAttributeSet
a,
boolean b)
```

Sets the italic attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

---

#### setItalic

public static void setItalic​(

MutableAttributeSet

a,
boolean b)

Sets the italic attribute.

isUnderline

```java
public static boolean isUnderline​(
AttributeSet
a)
```

Checks whether the underline attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

---

#### isUnderline

public static boolean isUnderline​(

AttributeSet

a)

Checks whether the underline attribute is set.

isStrikeThrough

```java
public static boolean isStrikeThrough​(
AttributeSet
a)
```

Checks whether the strikethrough attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

---

#### isStrikeThrough

public static boolean isStrikeThrough​(

AttributeSet

a)

Checks whether the strikethrough attribute is set.

isSuperscript

```java
public static boolean isSuperscript​(
AttributeSet
a)
```

Checks whether the superscript attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

---

#### isSuperscript

public static boolean isSuperscript​(

AttributeSet

a)

Checks whether the superscript attribute is set.

isSubscript

```java
public static boolean isSubscript​(
AttributeSet
a)
```

Checks whether the subscript attribute is set.

**Parameters:** a

- the attribute set
**Returns:** true if set else false

---

#### isSubscript

public static boolean isSubscript​(

AttributeSet

a)

Checks whether the subscript attribute is set.

setUnderline

```java
public static void setUnderline​(
MutableAttributeSet
a,
boolean b)
```

Sets the underline attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

---

#### setUnderline

public static void setUnderline​(

MutableAttributeSet

a,
boolean b)

Sets the underline attribute.

setStrikeThrough

```java
public static void setStrikeThrough​(
MutableAttributeSet
a,
boolean b)
```

Sets the strikethrough attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

---

#### setStrikeThrough

public static void setStrikeThrough​(

MutableAttributeSet

a,
boolean b)

Sets the strikethrough attribute.

setSuperscript

```java
public static void setSuperscript​(
MutableAttributeSet
a,
boolean b)
```

Sets the superscript attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

---

#### setSuperscript

public static void setSuperscript​(

MutableAttributeSet

a,
boolean b)

Sets the superscript attribute.

setSubscript

```java
public static void setSubscript​(
MutableAttributeSet
a,
boolean b)
```

Sets the subscript attribute.

**Parameters:** a

- the attribute set
**Parameters:** b

- specifies true/false for setting the attribute

---

#### setSubscript

public static void setSubscript​(

MutableAttributeSet

a,
boolean b)

Sets the subscript attribute.

getForeground

```java
public static
Color
getForeground​(
AttributeSet
a)
```

Gets the foreground color setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the color, Color.black as the default

---

#### getForeground

public static

Color

getForeground​(

AttributeSet

a)

Gets the foreground color setting from the attribute list.

setForeground

```java
public static void setForeground​(
MutableAttributeSet
a,

Color
fg)
```

Sets the foreground color.

**Parameters:** a

- the attribute set
**Parameters:** fg

- the color

---

#### setForeground

public static void setForeground​(

MutableAttributeSet

a,

Color

fg)

Sets the foreground color.

getBackground

```java
public static
Color
getBackground​(
AttributeSet
a)
```

Gets the background color setting from the attribute list.

**Parameters:** a

- the attribute set
**Returns:** the color, Color.black as the default

---

#### getBackground

public static

Color

getBackground​(

AttributeSet

a)

Gets the background color setting from the attribute list.

setBackground

```java
public static void setBackground​(
MutableAttributeSet
a,

Color
fg)
```

Sets the background color.

**Parameters:** a

- the attribute set
**Parameters:** fg

- the color

---

#### setBackground

public static void setBackground​(

MutableAttributeSet

a,

Color

fg)

Sets the background color.

getFirstLineIndent

```java
public static float getFirstLineIndent​(
AttributeSet
a)
```

Gets the first line indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

---

#### getFirstLineIndent

public static float getFirstLineIndent​(

AttributeSet

a)

Gets the first line indent setting.

setFirstLineIndent

```java
public static void setFirstLineIndent​(
MutableAttributeSet
a,
float i)
```

Sets the first line indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

---

#### setFirstLineIndent

public static void setFirstLineIndent​(

MutableAttributeSet

a,
float i)

Sets the first line indent.

getRightIndent

```java
public static float getRightIndent​(
AttributeSet
a)
```

Gets the right indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

---

#### getRightIndent

public static float getRightIndent​(

AttributeSet

a)

Gets the right indent setting.

setRightIndent

```java
public static void setRightIndent​(
MutableAttributeSet
a,
float i)
```

Sets right indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

---

#### setRightIndent

public static void setRightIndent​(

MutableAttributeSet

a,
float i)

Sets right indent.

getLeftIndent

```java
public static float getLeftIndent​(
AttributeSet
a)
```

Gets the left indent setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

---

#### getLeftIndent

public static float getLeftIndent​(

AttributeSet

a)

Gets the left indent setting.

setLeftIndent

```java
public static void setLeftIndent​(
MutableAttributeSet
a,
float i)
```

Sets left indent.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

---

#### setLeftIndent

public static void setLeftIndent​(

MutableAttributeSet

a,
float i)

Sets left indent.

getLineSpacing

```java
public static float getLineSpacing​(
AttributeSet
a)
```

Gets the line spacing setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

---

#### getLineSpacing

public static float getLineSpacing​(

AttributeSet

a)

Gets the line spacing setting.

setLineSpacing

```java
public static void setLineSpacing​(
MutableAttributeSet
a,
float i)
```

Sets line spacing.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

---

#### setLineSpacing

public static void setLineSpacing​(

MutableAttributeSet

a,
float i)

Sets line spacing.

getSpaceAbove

```java
public static float getSpaceAbove​(
AttributeSet
a)
```

Gets the space above setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

---

#### getSpaceAbove

public static float getSpaceAbove​(

AttributeSet

a)

Gets the space above setting.

setSpaceAbove

```java
public static void setSpaceAbove​(
MutableAttributeSet
a,
float i)
```

Sets space above.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

---

#### setSpaceAbove

public static void setSpaceAbove​(

MutableAttributeSet

a,
float i)

Sets space above.

getSpaceBelow

```java
public static float getSpaceBelow​(
AttributeSet
a)
```

Gets the space below setting.

**Parameters:** a

- the attribute set
**Returns:** the value, 0 if not set

---

#### getSpaceBelow

public static float getSpaceBelow​(

AttributeSet

a)

Gets the space below setting.

setSpaceBelow

```java
public static void setSpaceBelow​(
MutableAttributeSet
a,
float i)
```

Sets space below.

**Parameters:** a

- the attribute set
**Parameters:** i

- the value

---

#### setSpaceBelow

public static void setSpaceBelow​(

MutableAttributeSet

a,
float i)

Sets space below.

getAlignment

```java
public static int getAlignment​(
AttributeSet
a)
```

Gets the alignment setting.

**Parameters:** a

- the attribute set
**Returns:** the value

StyleConstants.ALIGN_LEFT

if not set

---

#### getAlignment

public static int getAlignment​(

AttributeSet

a)

Gets the alignment setting.

setAlignment

```java
public static void setAlignment​(
MutableAttributeSet
a,
int align)
```

Sets alignment.

**Parameters:** a

- the attribute set
**Parameters:** align

- the alignment value

---

#### setAlignment

public static void setAlignment​(

MutableAttributeSet

a,
int align)

Sets alignment.

getTabSet

```java
public static
TabSet
getTabSet​(
AttributeSet
a)
```

Gets the TabSet.

**Parameters:** a

- the attribute set
**Returns:** the

TabSet

---

#### getTabSet

public static

TabSet

getTabSet​(

AttributeSet

a)

Gets the TabSet.

setTabSet

```java
public static void setTabSet​(
MutableAttributeSet
a,

TabSet
tabs)
```

Sets the TabSet.

**Parameters:** a

- the attribute set.
**Parameters:** tabs

- the TabSet

---

#### setTabSet

public static void setTabSet​(

MutableAttributeSet

a,

TabSet

tabs)

Sets the TabSet.

---

