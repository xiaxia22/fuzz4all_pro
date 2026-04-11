# Class InputMethodHighlight

**Source:** `java.desktop\java\awt\im\InputMethodHighlight.html`

### Class Description

```java
public class
InputMethodHighlight

extends
Object
```

An InputMethodHighlight is used to describe the highlight
attributes of text being composed.
The description can be at two levels:
at the abstract level it specifies the conversion state and whether the
text is selected; at the concrete level it specifies style attributes used
to render the highlight.
An InputMethodHighlight must provide the description at the
abstract level; it may or may not provide the description at the concrete
level.
If no concrete style is provided, a renderer should use

Toolkit.mapInputMethodHighlight(java.awt.im.InputMethodHighlight)

to map to a concrete style.

The abstract description consists of three fields:

selected

,

state

, and

variation

.

selected

indicates whether the text range is the one that the
input method is currently working on, for example, the segment for which
conversion candidates are currently shown in a menu.

state

represents the conversion state. State values are defined
by the input method framework and should be distinguished in all
mappings from abstract to concrete styles. Currently defined state values
are raw (unconverted) and converted.
These state values are recommended for use before and after the
main conversion step of text composition, say, before and after kana->kanji
or pinyin->hanzi conversion.
The

variation

field allows input methods to express additional
information about the conversion results.

InputMethodHighlight instances are typically used as attribute values
returned from AttributedCharacterIterator for the INPUT_METHOD_HIGHLIGHT
attribute. They may be wrapped into

Annotation

instances to indicate separate text segments.

**Since:** 1.2
**See Also:** AttributedCharacterIterator

---

### Field Details

#### public static final int RAW_TEXT

Constant for the raw text state.

**See Also:**
- Constant Field Values

---

#### public static final int CONVERTED_TEXT

Constant for the converted text state.

**See Also:**
- Constant Field Values

---

#### public static final
InputMethodHighlight
UNSELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for unselected raw text.

---

#### public static final
InputMethodHighlight
SELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for selected raw text.

---

#### public static final
InputMethodHighlight
UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for unselected converted text.

---

#### public static final
InputMethodHighlight
SELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for selected converted text.

---

### Constructor Details

#### public InputMethodHighlight​(boolean selected,
int state)

Constructs an input method highlight record.
The variation is set to 0, the style to null.

**Parameters:**
- selected

- Whether the text range is selected
- state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT

**Throws:**
- IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given

**See Also:**
- RAW_TEXT

,

CONVERTED_TEXT

---

#### public InputMethodHighlight​(boolean selected,
int state,
int variation)

Constructs an input method highlight record.
The style is set to null.

**Parameters:**
- selected

- Whether the text range is selected
- state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
- variation

- The style variation for the text range

**Throws:**
- IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given

**See Also:**
- RAW_TEXT

,

CONVERTED_TEXT

---

#### public InputMethodHighlight​(boolean selected,
int state,
int variation,

Map
<
TextAttribute
,​?> style)

Constructs an input method highlight record.
The style attributes map provided must be unmodifiable.

**Parameters:**
- selected

- whether the text range is selected
- state

- the conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
- variation

- the variation for the text range
- style

- the rendering style attributes for the text range, or null

**Throws:**
- IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given

**See Also:**
- RAW_TEXT

,

CONVERTED_TEXT

**Since:**
- 1.3

---

### Method Details

#### public boolean isSelected()

Returns whether the text range is selected.

**Returns:**
- whether the text range is selected

---

#### public int getState()

Returns the conversion state of the text range.

**Returns:**
- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT.

**See Also:**
- RAW_TEXT

,

CONVERTED_TEXT

---

#### public int getVariation()

Returns the variation of the text range.

**Returns:**
- the variation of the text range

---

#### public
Map
<
TextAttribute
,​?> getStyle()

Returns the rendering style attributes for the text range, or null.

**Returns:**
- the rendering style attributes for the text range, or null

**Since:**
- 1.3

---

### Additional Sections

#### Class InputMethodHighlight

java.lang.Object

- java.awt.im.InputMethodHighlight

java.awt.im.InputMethodHighlight

```java
public class
InputMethodHighlight

extends
Object
```

An InputMethodHighlight is used to describe the highlight
attributes of text being composed.
The description can be at two levels:
at the abstract level it specifies the conversion state and whether the
text is selected; at the concrete level it specifies style attributes used
to render the highlight.
An InputMethodHighlight must provide the description at the
abstract level; it may or may not provide the description at the concrete
level.
If no concrete style is provided, a renderer should use

Toolkit.mapInputMethodHighlight(java.awt.im.InputMethodHighlight)

to map to a concrete style.

The abstract description consists of three fields:

selected

,

state

, and

variation

.

selected

indicates whether the text range is the one that the
input method is currently working on, for example, the segment for which
conversion candidates are currently shown in a menu.

state

represents the conversion state. State values are defined
by the input method framework and should be distinguished in all
mappings from abstract to concrete styles. Currently defined state values
are raw (unconverted) and converted.
These state values are recommended for use before and after the
main conversion step of text composition, say, before and after kana->kanji
or pinyin->hanzi conversion.
The

variation

field allows input methods to express additional
information about the conversion results.

InputMethodHighlight instances are typically used as attribute values
returned from AttributedCharacterIterator for the INPUT_METHOD_HIGHLIGHT
attribute. They may be wrapped into

Annotation

instances to indicate separate text segments.

**Since:** 1.2
**See Also:** AttributedCharacterIterator

public class

InputMethodHighlight

extends

Object

An InputMethodHighlight is used to describe the highlight
attributes of text being composed.
The description can be at two levels:
at the abstract level it specifies the conversion state and whether the
text is selected; at the concrete level it specifies style attributes used
to render the highlight.
An InputMethodHighlight must provide the description at the
abstract level; it may or may not provide the description at the concrete
level.
If no concrete style is provided, a renderer should use

Toolkit.mapInputMethodHighlight(java.awt.im.InputMethodHighlight)

to map to a concrete style.

The abstract description consists of three fields:

selected

,

state

, and

variation

.

selected

indicates whether the text range is the one that the
input method is currently working on, for example, the segment for which
conversion candidates are currently shown in a menu.

state

represents the conversion state. State values are defined
by the input method framework and should be distinguished in all
mappings from abstract to concrete styles. Currently defined state values
are raw (unconverted) and converted.
These state values are recommended for use before and after the
main conversion step of text composition, say, before and after kana->kanji
or pinyin->hanzi conversion.
The

variation

field allows input methods to express additional
information about the conversion results.

InputMethodHighlight instances are typically used as attribute values
returned from AttributedCharacterIterator for the INPUT_METHOD_HIGHLIGHT
attribute. They may be wrapped into

Annotation

instances to indicate separate text segments.

The abstract description consists of three fields:

selected

,

state

, and

variation

.

selected

indicates whether the text range is the one that the
input method is currently working on, for example, the segment for which
conversion candidates are currently shown in a menu.

state

represents the conversion state. State values are defined
by the input method framework and should be distinguished in all
mappings from abstract to concrete styles. Currently defined state values
are raw (unconverted) and converted.
These state values are recommended for use before and after the
main conversion step of text composition, say, before and after kana->kanji
or pinyin->hanzi conversion.
The

variation

field allows input methods to express additional
information about the conversion results.

InputMethodHighlight instances are typically used as attribute values
returned from AttributedCharacterIterator for the INPUT_METHOD_HIGHLIGHT
attribute. They may be wrapped into

Annotation

instances to indicate separate text segments.

InputMethodHighlight instances are typically used as attribute values
returned from AttributedCharacterIterator for the INPUT_METHOD_HIGHLIGHT
attribute. They may be wrapped into

Annotation

instances to indicate separate text segments.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CONVERTED_TEXT

Constant for the converted text state.

static int

RAW_TEXT

Constant for the raw text state.

static

InputMethodHighlight

SELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for selected converted text.

static

InputMethodHighlight

SELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for selected raw text.

static

InputMethodHighlight

UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for unselected converted text.

static

InputMethodHighlight

UNSELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for unselected raw text.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InputMethodHighlight

​(boolean selected,
int state)

Constructs an input method highlight record.

InputMethodHighlight

​(boolean selected,
int state,
int variation)

Constructs an input method highlight record.

InputMethodHighlight

​(boolean selected,
int state,
int variation,

Map

<

TextAttribute

,​?> style)

Constructs an input method highlight record.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getState

()

Returns the conversion state of the text range.

Map

<

TextAttribute

,​?>

getStyle

()

Returns the rendering style attributes for the text range, or null.

int

getVariation

()

Returns the variation of the text range.

boolean

isSelected

()

Returns whether the text range is selected.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

CONVERTED_TEXT

Constant for the converted text state.

static int

RAW_TEXT

Constant for the raw text state.

static

InputMethodHighlight

SELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for selected converted text.

static

InputMethodHighlight

SELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for selected raw text.

static

InputMethodHighlight

UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for unselected converted text.

static

InputMethodHighlight

UNSELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for unselected raw text.

---

#### Field Summary

Constant for the converted text state.

Constant for the raw text state.

Constant for the default highlight for selected converted text.

Constant for the default highlight for selected raw text.

Constant for the default highlight for unselected converted text.

Constant for the default highlight for unselected raw text.

Constructor Summary

Constructors

Constructor

Description

InputMethodHighlight

​(boolean selected,
int state)

Constructs an input method highlight record.

InputMethodHighlight

​(boolean selected,
int state,
int variation)

Constructs an input method highlight record.

InputMethodHighlight

​(boolean selected,
int state,
int variation,

Map

<

TextAttribute

,​?> style)

Constructs an input method highlight record.

---

#### Constructor Summary

Constructs an input method highlight record.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getState

()

Returns the conversion state of the text range.

Map

<

TextAttribute

,​?>

getStyle

()

Returns the rendering style attributes for the text range, or null.

int

getVariation

()

Returns the variation of the text range.

boolean

isSelected

()

Returns whether the text range is selected.

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

Returns the conversion state of the text range.

Returns the rendering style attributes for the text range, or null.

Returns the variation of the text range.

Returns whether the text range is selected.

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

============ FIELD DETAIL ===========

- Field Detail

- RAW_TEXT

```java
public static final int RAW_TEXT
```

Constant for the raw text state.

**See Also:** Constant Field Values

- CONVERTED_TEXT

```java
public static final int CONVERTED_TEXT
```

Constant for the converted text state.

**See Also:** Constant Field Values

- UNSELECTED_RAW_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
UNSELECTED_RAW_TEXT_HIGHLIGHT
```

Constant for the default highlight for unselected raw text.

- SELECTED_RAW_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
SELECTED_RAW_TEXT_HIGHLIGHT
```

Constant for the default highlight for selected raw text.

- UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
UNSELECTED_CONVERTED_TEXT_HIGHLIGHT
```

Constant for the default highlight for unselected converted text.

- SELECTED_CONVERTED_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
SELECTED_CONVERTED_TEXT_HIGHLIGHT
```

Constant for the default highlight for selected converted text.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state)
```

Constructs an input method highlight record.
The variation is set to 0, the style to null.

**Parameters:** selected

- Whether the text range is selected
**Parameters:** state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

- InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state,
int variation)
```

Constructs an input method highlight record.
The style is set to null.

**Parameters:** selected

- Whether the text range is selected
**Parameters:** state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Parameters:** variation

- The style variation for the text range
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

- InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state,
int variation,

Map
<
TextAttribute
,​?> style)
```

Constructs an input method highlight record.
The style attributes map provided must be unmodifiable.

**Parameters:** selected

- whether the text range is selected
**Parameters:** state

- the conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Parameters:** variation

- the variation for the text range
**Parameters:** style

- the rendering style attributes for the text range, or null
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**Since:** 1.3
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

============ METHOD DETAIL ==========

- Method Detail

- isSelected

```java
public boolean isSelected()
```

Returns whether the text range is selected.

**Returns:** whether the text range is selected

- getState

```java
public int getState()
```

Returns the conversion state of the text range.

**Returns:** The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT.
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

- getVariation

```java
public int getVariation()
```

Returns the variation of the text range.

**Returns:** the variation of the text range

- getStyle

```java
public
Map
<
TextAttribute
,​?> getStyle()
```

Returns the rendering style attributes for the text range, or null.

**Returns:** the rendering style attributes for the text range, or null
**Since:** 1.3

Field Detail

- RAW_TEXT

```java
public static final int RAW_TEXT
```

Constant for the raw text state.

**See Also:** Constant Field Values

- CONVERTED_TEXT

```java
public static final int CONVERTED_TEXT
```

Constant for the converted text state.

**See Also:** Constant Field Values

- UNSELECTED_RAW_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
UNSELECTED_RAW_TEXT_HIGHLIGHT
```

Constant for the default highlight for unselected raw text.

- SELECTED_RAW_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
SELECTED_RAW_TEXT_HIGHLIGHT
```

Constant for the default highlight for selected raw text.

- UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
UNSELECTED_CONVERTED_TEXT_HIGHLIGHT
```

Constant for the default highlight for unselected converted text.

- SELECTED_CONVERTED_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
SELECTED_CONVERTED_TEXT_HIGHLIGHT
```

Constant for the default highlight for selected converted text.

---

#### Field Detail

RAW_TEXT

```java
public static final int RAW_TEXT
```

Constant for the raw text state.

**See Also:** Constant Field Values

---

#### RAW_TEXT

public static final int RAW_TEXT

Constant for the raw text state.

CONVERTED_TEXT

```java
public static final int CONVERTED_TEXT
```

Constant for the converted text state.

**See Also:** Constant Field Values

---

#### CONVERTED_TEXT

public static final int CONVERTED_TEXT

Constant for the converted text state.

UNSELECTED_RAW_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
UNSELECTED_RAW_TEXT_HIGHLIGHT
```

Constant for the default highlight for unselected raw text.

---

#### UNSELECTED_RAW_TEXT_HIGHLIGHT

public static final

InputMethodHighlight

UNSELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for unselected raw text.

SELECTED_RAW_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
SELECTED_RAW_TEXT_HIGHLIGHT
```

Constant for the default highlight for selected raw text.

---

#### SELECTED_RAW_TEXT_HIGHLIGHT

public static final

InputMethodHighlight

SELECTED_RAW_TEXT_HIGHLIGHT

Constant for the default highlight for selected raw text.

UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
UNSELECTED_CONVERTED_TEXT_HIGHLIGHT
```

Constant for the default highlight for unselected converted text.

---

#### UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

public static final

InputMethodHighlight

UNSELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for unselected converted text.

SELECTED_CONVERTED_TEXT_HIGHLIGHT

```java
public static final
InputMethodHighlight
SELECTED_CONVERTED_TEXT_HIGHLIGHT
```

Constant for the default highlight for selected converted text.

---

#### SELECTED_CONVERTED_TEXT_HIGHLIGHT

public static final

InputMethodHighlight

SELECTED_CONVERTED_TEXT_HIGHLIGHT

Constant for the default highlight for selected converted text.

Constructor Detail

- InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state)
```

Constructs an input method highlight record.
The variation is set to 0, the style to null.

**Parameters:** selected

- Whether the text range is selected
**Parameters:** state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

- InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state,
int variation)
```

Constructs an input method highlight record.
The style is set to null.

**Parameters:** selected

- Whether the text range is selected
**Parameters:** state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Parameters:** variation

- The style variation for the text range
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

- InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state,
int variation,

Map
<
TextAttribute
,​?> style)
```

Constructs an input method highlight record.
The style attributes map provided must be unmodifiable.

**Parameters:** selected

- whether the text range is selected
**Parameters:** state

- the conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Parameters:** variation

- the variation for the text range
**Parameters:** style

- the rendering style attributes for the text range, or null
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**Since:** 1.3
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

---

#### Constructor Detail

InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state)
```

Constructs an input method highlight record.
The variation is set to 0, the style to null.

**Parameters:** selected

- Whether the text range is selected
**Parameters:** state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

---

#### InputMethodHighlight

public InputMethodHighlight​(boolean selected,
int state)

Constructs an input method highlight record.
The variation is set to 0, the style to null.

InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state,
int variation)
```

Constructs an input method highlight record.
The style is set to null.

**Parameters:** selected

- Whether the text range is selected
**Parameters:** state

- The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Parameters:** variation

- The style variation for the text range
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

---

#### InputMethodHighlight

public InputMethodHighlight​(boolean selected,
int state,
int variation)

Constructs an input method highlight record.
The style is set to null.

InputMethodHighlight

```java
public InputMethodHighlight​(boolean selected,
int state,
int variation,

Map
<
TextAttribute
,​?> style)
```

Constructs an input method highlight record.
The style attributes map provided must be unmodifiable.

**Parameters:** selected

- whether the text range is selected
**Parameters:** state

- the conversion state for the text range - RAW_TEXT or CONVERTED_TEXT
**Parameters:** variation

- the variation for the text range
**Parameters:** style

- the rendering style attributes for the text range, or null
**Throws:** IllegalArgumentException

- if a state other than RAW_TEXT or CONVERTED_TEXT is given
**Since:** 1.3
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

---

#### InputMethodHighlight

public InputMethodHighlight​(boolean selected,
int state,
int variation,

Map

<

TextAttribute

,​?> style)

Constructs an input method highlight record.
The style attributes map provided must be unmodifiable.

Method Detail

- isSelected

```java
public boolean isSelected()
```

Returns whether the text range is selected.

**Returns:** whether the text range is selected

- getState

```java
public int getState()
```

Returns the conversion state of the text range.

**Returns:** The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT.
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

- getVariation

```java
public int getVariation()
```

Returns the variation of the text range.

**Returns:** the variation of the text range

- getStyle

```java
public
Map
<
TextAttribute
,​?> getStyle()
```

Returns the rendering style attributes for the text range, or null.

**Returns:** the rendering style attributes for the text range, or null
**Since:** 1.3

---

#### Method Detail

isSelected

```java
public boolean isSelected()
```

Returns whether the text range is selected.

**Returns:** whether the text range is selected

---

#### isSelected

public boolean isSelected()

Returns whether the text range is selected.

getState

```java
public int getState()
```

Returns the conversion state of the text range.

**Returns:** The conversion state for the text range - RAW_TEXT or CONVERTED_TEXT.
**See Also:** RAW_TEXT

,

CONVERTED_TEXT

---

#### getState

public int getState()

Returns the conversion state of the text range.

getVariation

```java
public int getVariation()
```

Returns the variation of the text range.

**Returns:** the variation of the text range

---

#### getVariation

public int getVariation()

Returns the variation of the text range.

getStyle

```java
public
Map
<
TextAttribute
,​?> getStyle()
```

Returns the rendering style attributes for the text range, or null.

**Returns:** the rendering style attributes for the text range, or null
**Since:** 1.3

---

#### getStyle

public

Map

<

TextAttribute

,​?> getStyle()

Returns the rendering style attributes for the text range, or null.

---

