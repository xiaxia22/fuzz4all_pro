# Class FontUIResource

**Source:** `java.desktop\javax\swing\plaf\FontUIResource.html`

### Class Description

```java
public class
FontUIResource

extends
Font

implements
UIResource
```

A subclass of java.awt.Font that implements UIResource.
UI classes which set default font properties should use
this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

UIResource

---

### Field Details

*No entries found.*

### Constructor Details

#### public FontUIResource​(
String
name,
int style,
int size)

Constructs a

FontUIResource

.

**Parameters:**
- name

- the font name
- style

- the style constant for the font
- size

- the point size of the font

---

#### public FontUIResource​(
Font
font)

Constructs a

FontUIResource

.

**Parameters:**
- font

- the font

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FontUIResource

java.lang.Object

- java.awt.Font
- - javax.swing.plaf.FontUIResource

java.awt.Font

- javax.swing.plaf.FontUIResource

javax.swing.plaf.FontUIResource

**All Implemented Interfaces:** Serializable

,

UIResource

```java
public class
FontUIResource

extends
Font

implements
UIResource
```

A subclass of java.awt.Font that implements UIResource.
UI classes which set default font properties should use
this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** UIResource

,

Serialized Form

public class

FontUIResource

extends

Font

implements

UIResource

A subclass of java.awt.Font that implements UIResource.
UI classes which set default font properties should use
this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.

Font

BOLD

,

CENTER_BASELINE

,

DIALOG

,

DIALOG_INPUT

,

HANGING_BASELINE

,

ITALIC

,

LAYOUT_LEFT_TO_RIGHT

,

LAYOUT_NO_LIMIT_CONTEXT

,

LAYOUT_NO_START_CONTEXT

,

LAYOUT_RIGHT_TO_LEFT

,

MONOSPACED

,

name

,

PLAIN

,

pointSize

,

ROMAN_BASELINE

,

SANS_SERIF

,

SERIF

,

size

,

style

,

TRUETYPE_FONT

,

TYPE1_FONT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FontUIResource

​(

Font

font)

Constructs a

FontUIResource

.

FontUIResource

​(

String

name,
int style,
int size)

Constructs a

FontUIResource

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.awt.

Font

canDisplay

,

canDisplay

,

canDisplayUpTo

,

canDisplayUpTo

,

canDisplayUpTo

,

createFont

,

createFont

,

createFonts

,

createFonts

,

createGlyphVector

,

createGlyphVector

,

createGlyphVector

,

createGlyphVector

,

decode

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

equals

,

getAttributes

,

getAvailableAttributes

,

getBaselineFor

,

getFamily

,

getFamily

,

getFont

,

getFont

,

getFont

,

getFontName

,

getFontName

,

getItalicAngle

,

getLineMetrics

,

getLineMetrics

,

getLineMetrics

,

getLineMetrics

,

getMaxCharBounds

,

getMissingGlyphCode

,

getName

,

getNumGlyphs

,

getPSName

,

getSize

,

getSize2D

,

getStringBounds

,

getStringBounds

,

getStringBounds

,

getStringBounds

,

getStyle

,

getTransform

,

hashCode

,

hasLayoutAttributes

,

hasUniformLineMetrics

,

isBold

,

isItalic

,

isPlain

,

isTransformed

,

layoutGlyphVector

,

textRequiresLayout

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Field Summary

- Fields declared in class java.awt.

Font

BOLD

,

CENTER_BASELINE

,

DIALOG

,

DIALOG_INPUT

,

HANGING_BASELINE

,

ITALIC

,

LAYOUT_LEFT_TO_RIGHT

,

LAYOUT_NO_LIMIT_CONTEXT

,

LAYOUT_NO_START_CONTEXT

,

LAYOUT_RIGHT_TO_LEFT

,

MONOSPACED

,

name

,

PLAIN

,

pointSize

,

ROMAN_BASELINE

,

SANS_SERIF

,

SERIF

,

size

,

style

,

TRUETYPE_FONT

,

TYPE1_FONT

---

#### Field Summary

Fields declared in class java.awt.

Font

BOLD

,

CENTER_BASELINE

,

DIALOG

,

DIALOG_INPUT

,

HANGING_BASELINE

,

ITALIC

,

LAYOUT_LEFT_TO_RIGHT

,

LAYOUT_NO_LIMIT_CONTEXT

,

LAYOUT_NO_START_CONTEXT

,

LAYOUT_RIGHT_TO_LEFT

,

MONOSPACED

,

name

,

PLAIN

,

pointSize

,

ROMAN_BASELINE

,

SANS_SERIF

,

SERIF

,

size

,

style

,

TRUETYPE_FONT

,

TYPE1_FONT

---

#### Fields declared in class java.awt. Font

Constructor Summary

Constructors

Constructor

Description

FontUIResource

​(

Font

font)

Constructs a

FontUIResource

.

FontUIResource

​(

String

name,
int style,
int size)

Constructs a

FontUIResource

.

---

#### Constructor Summary

Constructs a

FontUIResource

.

Method Summary

- Methods declared in class java.awt.

Font

canDisplay

,

canDisplay

,

canDisplayUpTo

,

canDisplayUpTo

,

canDisplayUpTo

,

createFont

,

createFont

,

createFonts

,

createFonts

,

createGlyphVector

,

createGlyphVector

,

createGlyphVector

,

createGlyphVector

,

decode

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

equals

,

getAttributes

,

getAvailableAttributes

,

getBaselineFor

,

getFamily

,

getFamily

,

getFont

,

getFont

,

getFont

,

getFontName

,

getFontName

,

getItalicAngle

,

getLineMetrics

,

getLineMetrics

,

getLineMetrics

,

getLineMetrics

,

getMaxCharBounds

,

getMissingGlyphCode

,

getName

,

getNumGlyphs

,

getPSName

,

getSize

,

getSize2D

,

getStringBounds

,

getStringBounds

,

getStringBounds

,

getStringBounds

,

getStyle

,

getTransform

,

hashCode

,

hasLayoutAttributes

,

hasUniformLineMetrics

,

isBold

,

isItalic

,

isPlain

,

isTransformed

,

layoutGlyphVector

,

textRequiresLayout

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Methods declared in class java.awt.

Font

canDisplay

,

canDisplay

,

canDisplayUpTo

,

canDisplayUpTo

,

canDisplayUpTo

,

createFont

,

createFont

,

createFonts

,

createFonts

,

createGlyphVector

,

createGlyphVector

,

createGlyphVector

,

createGlyphVector

,

decode

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

deriveFont

,

equals

,

getAttributes

,

getAvailableAttributes

,

getBaselineFor

,

getFamily

,

getFamily

,

getFont

,

getFont

,

getFont

,

getFontName

,

getFontName

,

getItalicAngle

,

getLineMetrics

,

getLineMetrics

,

getLineMetrics

,

getLineMetrics

,

getMaxCharBounds

,

getMissingGlyphCode

,

getName

,

getNumGlyphs

,

getPSName

,

getSize

,

getSize2D

,

getStringBounds

,

getStringBounds

,

getStringBounds

,

getStringBounds

,

getStyle

,

getTransform

,

hashCode

,

hasLayoutAttributes

,

hasUniformLineMetrics

,

isBold

,

isItalic

,

isPlain

,

isTransformed

,

layoutGlyphVector

,

textRequiresLayout

,

toString

---

#### Methods declared in class java.awt. Font

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FontUIResource

```java
public FontUIResource​(
String
name,
int style,
int size)
```

Constructs a

FontUIResource

.

**Parameters:** name

- the font name
**Parameters:** style

- the style constant for the font
**Parameters:** size

- the point size of the font

- FontUIResource

```java
public FontUIResource​(
Font
font)
```

Constructs a

FontUIResource

.

**Parameters:** font

- the font

Constructor Detail

- FontUIResource

```java
public FontUIResource​(
String
name,
int style,
int size)
```

Constructs a

FontUIResource

.

**Parameters:** name

- the font name
**Parameters:** style

- the style constant for the font
**Parameters:** size

- the point size of the font

- FontUIResource

```java
public FontUIResource​(
Font
font)
```

Constructs a

FontUIResource

.

**Parameters:** font

- the font

---

#### Constructor Detail

FontUIResource

```java
public FontUIResource​(
String
name,
int style,
int size)
```

Constructs a

FontUIResource

.

**Parameters:** name

- the font name
**Parameters:** style

- the style constant for the font
**Parameters:** size

- the point size of the font

---

#### FontUIResource

public FontUIResource​(

String

name,
int style,
int size)

Constructs a

FontUIResource

.

FontUIResource

```java
public FontUIResource​(
Font
font)
```

Constructs a

FontUIResource

.

**Parameters:** font

- the font

---

#### FontUIResource

public FontUIResource​(

Font

font)

Constructs a

FontUIResource

.

---

