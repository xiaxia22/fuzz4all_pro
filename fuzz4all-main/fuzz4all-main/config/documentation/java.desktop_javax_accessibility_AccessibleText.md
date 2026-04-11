# Interface AccessibleText

**Source:** `java.desktop\javax\accessibility\AccessibleText.html`

### Class Description

```java
public interface
AccessibleText
```

The

AccessibleText

interface should be implemented by all classes
that present textual information on the display. This interface provides the
standard mechanism for an assistive technology to access that text via its
content, attributes, and spatial location. Applications can determine if an
object supports the

AccessibleText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is not

null

, the
object supports this interface.

**All Known Subinterfaces:** AccessibleEditableText

,

AccessibleHypertext

---

### Field Details

#### static final int CHARACTER

Constant used to indicate that the part of the text that should be
retrieved is a character.

**See Also:**
- getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

#### static final int WORD

Constant used to indicate that the part of the text that should be
retrieved is a word.

**See Also:**
- getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

#### static final int SENTENCE

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

A sentence is a string of words which expresses an assertion, a question,
a command, a wish, an exclamation, or the performance of an action. In
English locales, the string usually begins with a capital letter and
concludes with appropriate end punctuation; such as a period, question or
exclamation mark. Other locales may use different capitalization and/or
punctuation.

**See Also:**
- getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getIndexAtPoint​(
Point
p)

Given a point in local coordinates, return the zero-based index of the
character under that point. If the point is invalid, this method returns
-1.

**Parameters:**
- p

- the point in local coordinates

**Returns:**
- the zero-based index of the character under

Point p

; if
point is invalid return -1.

---

#### Rectangle
getCharacterBounds​(int i)

Determines the bounding box of the character at the given index into the
string. The bounds are returned in local coordinates. If the index is
invalid an empty rectangle is returned.

**Parameters:**
- i

- the index into the string

**Returns:**
- the screen coordinates of the character's bounding box, if index
is invalid return an empty rectangle.

---

#### int getCharCount()

Returns the number of characters (valid indicies).

**Returns:**
- the number of characters

---

#### int getCaretPosition()

Returns the zero-based offset of the caret.

Note: That to the right of the caret will have the same index value as
the offset (the caret is between two characters).

**Returns:**
- the zero-based offset of the caret

---

#### String
getAtIndex​(int part,
int index)

Returns the

String

at a given index.

**Parameters:**
- part

- the CHARACTER, WORD, or SENTENCE to retrieve
- index

- an index within the text

**Returns:**
- the letter, word, or sentence

---

#### String
getAfterIndex​(int part,
int index)

Returns the

String

after a given index.

**Parameters:**
- part

- the CHARACTER, WORD, or SENTENCE to retrieve
- index

- an index within the text

**Returns:**
- the letter, word, or sentence

---

#### String
getBeforeIndex​(int part,
int index)

Returns the

String

before a given index.

**Parameters:**
- part

- the CHARACTER, WORD, or SENTENCE to retrieve
- index

- an index within the text

**Returns:**
- the letter, word, or sentence

---

#### AttributeSet
getCharacterAttribute​(int i)

Returns the

AttributeSet

for a given character at a given index.

**Parameters:**
- i

- the zero-based index into the text

**Returns:**
- the

AttributeSet

of the character

---

#### int getSelectionStart()

Returns the start offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:**
- the index into the text of the start of the selection

---

#### int getSelectionEnd()

Returns the end offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:**
- the index into the text of the end of the selection

---

#### String
getSelectedText()

Returns the portion of the text that is selected.

**Returns:**
- the

String

portion of the text that is selected

---

### Additional Sections

#### Interface AccessibleText

**All Known Subinterfaces:** AccessibleEditableText

,

AccessibleHypertext

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

,

JButton.AccessibleJButton

,

JCheckBox.AccessibleJCheckBox

,

JCheckBoxMenuItem.AccessibleJCheckBoxMenuItem

,

JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JLabel.AccessibleJLabel

,

JMenu.AccessibleJMenu

,

JMenuItem.AccessibleJMenuItem

,

JPasswordField.AccessibleJPasswordField

,

JRadioButton.AccessibleJRadioButton

,

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

,

JSpinner.AccessibleJSpinner

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

,

JToggleButton.AccessibleJToggleButton

,

ProgressMonitor.AccessibleProgressMonitor

,

TextArea.AccessibleAWTTextArea

,

TextComponent.AccessibleAWTTextComponent

,

TextField.AccessibleAWTTextField

```java
public interface
AccessibleText
```

The

AccessibleText

interface should be implemented by all classes
that present textual information on the display. This interface provides the
standard mechanism for an assistive technology to access that text via its
content, attributes, and spatial location. Applications can determine if an
object supports the

AccessibleText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is not

null

, the
object supports this interface.

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleText()

public interface

AccessibleText

The

AccessibleText

interface should be implemented by all classes
that present textual information on the display. This interface provides the
standard mechanism for an assistive technology to access that text via its
content, attributes, and spatial location. Applications can determine if an
object supports the

AccessibleText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is not

null

, the
object supports this interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CHARACTER

Constant used to indicate that the part of the text that should be
retrieved is a character.

static int

SENTENCE

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

static int

WORD

Constant used to indicate that the part of the text that should be
retrieved is a word.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAfterIndex

​(int part,
int index)

Returns the

String

after a given index.

String

getAtIndex

​(int part,
int index)

Returns the

String

at a given index.

String

getBeforeIndex

​(int part,
int index)

Returns the

String

before a given index.

int

getCaretPosition

()

Returns the zero-based offset of the caret.

AttributeSet

getCharacterAttribute

​(int i)

Returns the

AttributeSet

for a given character at a given index.

Rectangle

getCharacterBounds

​(int i)

Determines the bounding box of the character at the given index into the
string.

int

getCharCount

()

Returns the number of characters (valid indicies).

int

getIndexAtPoint

​(

Point

p)

Given a point in local coordinates, return the zero-based index of the
character under that point.

String

getSelectedText

()

Returns the portion of the text that is selected.

int

getSelectionEnd

()

Returns the end offset within the selected text.

int

getSelectionStart

()

Returns the start offset within the selected text.

Field Summary

Fields

Modifier and Type

Field

Description

static int

CHARACTER

Constant used to indicate that the part of the text that should be
retrieved is a character.

static int

SENTENCE

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

static int

WORD

Constant used to indicate that the part of the text that should be
retrieved is a word.

---

#### Field Summary

Constant used to indicate that the part of the text that should be
retrieved is a character.

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

Constant used to indicate that the part of the text that should be
retrieved is a word.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAfterIndex

​(int part,
int index)

Returns the

String

after a given index.

String

getAtIndex

​(int part,
int index)

Returns the

String

at a given index.

String

getBeforeIndex

​(int part,
int index)

Returns the

String

before a given index.

int

getCaretPosition

()

Returns the zero-based offset of the caret.

AttributeSet

getCharacterAttribute

​(int i)

Returns the

AttributeSet

for a given character at a given index.

Rectangle

getCharacterBounds

​(int i)

Determines the bounding box of the character at the given index into the
string.

int

getCharCount

()

Returns the number of characters (valid indicies).

int

getIndexAtPoint

​(

Point

p)

Given a point in local coordinates, return the zero-based index of the
character under that point.

String

getSelectedText

()

Returns the portion of the text that is selected.

int

getSelectionEnd

()

Returns the end offset within the selected text.

int

getSelectionStart

()

Returns the start offset within the selected text.

---

#### Method Summary

Returns the

String

after a given index.

Returns the

String

at a given index.

Returns the

String

before a given index.

Returns the zero-based offset of the caret.

Returns the

AttributeSet

for a given character at a given index.

Determines the bounding box of the character at the given index into the
string.

Returns the number of characters (valid indicies).

Given a point in local coordinates, return the zero-based index of the
character under that point.

Returns the portion of the text that is selected.

Returns the end offset within the selected text.

Returns the start offset within the selected text.

============ FIELD DETAIL ===========

- Field Detail

- CHARACTER

```java
static final int CHARACTER
```

Constant used to indicate that the part of the text that should be
retrieved is a character.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

- WORD

```java
static final int WORD
```

Constant used to indicate that the part of the text that should be
retrieved is a word.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

- SENTENCE

```java
static final int SENTENCE
```

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

A sentence is a string of words which expresses an assertion, a question,
a command, a wish, an exclamation, or the performance of an action. In
English locales, the string usually begins with a capital letter and
concludes with appropriate end punctuation; such as a period, question or
exclamation mark. Other locales may use different capitalization and/or
punctuation.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getIndexAtPoint

```java
int getIndexAtPoint​(
Point
p)
```

Given a point in local coordinates, return the zero-based index of the
character under that point. If the point is invalid, this method returns
-1.

**Parameters:** p

- the point in local coordinates
**Returns:** the zero-based index of the character under

Point p

; if
point is invalid return -1.

- getCharacterBounds

```java
Rectangle
getCharacterBounds​(int i)
```

Determines the bounding box of the character at the given index into the
string. The bounds are returned in local coordinates. If the index is
invalid an empty rectangle is returned.

**Parameters:** i

- the index into the string
**Returns:** the screen coordinates of the character's bounding box, if index
is invalid return an empty rectangle.

- getCharCount

```java
int getCharCount()
```

Returns the number of characters (valid indicies).

**Returns:** the number of characters

- getCaretPosition

```java
int getCaretPosition()
```

Returns the zero-based offset of the caret.

Note: That to the right of the caret will have the same index value as
the offset (the caret is between two characters).

**Returns:** the zero-based offset of the caret

- getAtIndex

```java
String
getAtIndex​(int part,
int index)
```

Returns the

String

at a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

- getAfterIndex

```java
String
getAfterIndex​(int part,
int index)
```

Returns the

String

after a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

- getBeforeIndex

```java
String
getBeforeIndex​(int part,
int index)
```

Returns the

String

before a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

- getCharacterAttribute

```java
AttributeSet
getCharacterAttribute​(int i)
```

Returns the

AttributeSet

for a given character at a given index.

**Parameters:** i

- the zero-based index into the text
**Returns:** the

AttributeSet

of the character

- getSelectionStart

```java
int getSelectionStart()
```

Returns the start offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:** the index into the text of the start of the selection

- getSelectionEnd

```java
int getSelectionEnd()
```

Returns the end offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:** the index into the text of the end of the selection

- getSelectedText

```java
String
getSelectedText()
```

Returns the portion of the text that is selected.

**Returns:** the

String

portion of the text that is selected

Field Detail

- CHARACTER

```java
static final int CHARACTER
```

Constant used to indicate that the part of the text that should be
retrieved is a character.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

- WORD

```java
static final int WORD
```

Constant used to indicate that the part of the text that should be
retrieved is a word.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

- SENTENCE

```java
static final int SENTENCE
```

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

A sentence is a string of words which expresses an assertion, a question,
a command, a wish, an exclamation, or the performance of an action. In
English locales, the string usually begins with a capital letter and
concludes with appropriate end punctuation; such as a period, question or
exclamation mark. Other locales may use different capitalization and/or
punctuation.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

#### Field Detail

CHARACTER

```java
static final int CHARACTER
```

Constant used to indicate that the part of the text that should be
retrieved is a character.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

#### CHARACTER

static final int CHARACTER

Constant used to indicate that the part of the text that should be
retrieved is a character.

WORD

```java
static final int WORD
```

Constant used to indicate that the part of the text that should be
retrieved is a word.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

#### WORD

static final int WORD

Constant used to indicate that the part of the text that should be
retrieved is a word.

SENTENCE

```java
static final int SENTENCE
```

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

A sentence is a string of words which expresses an assertion, a question,
a command, a wish, an exclamation, or the performance of an action. In
English locales, the string usually begins with a capital letter and
concludes with appropriate end punctuation; such as a period, question or
exclamation mark. Other locales may use different capitalization and/or
punctuation.

**See Also:** getAtIndex(int, int)

,

getAfterIndex(int, int)

,

getBeforeIndex(int, int)

,

Constant Field Values

---

#### SENTENCE

static final int SENTENCE

Constant used to indicate that the part of the text that should be
retrieved is a sentence.

A sentence is a string of words which expresses an assertion, a question,
a command, a wish, an exclamation, or the performance of an action. In
English locales, the string usually begins with a capital letter and
concludes with appropriate end punctuation; such as a period, question or
exclamation mark. Other locales may use different capitalization and/or
punctuation.

A sentence is a string of words which expresses an assertion, a question,
a command, a wish, an exclamation, or the performance of an action. In
English locales, the string usually begins with a capital letter and
concludes with appropriate end punctuation; such as a period, question or
exclamation mark. Other locales may use different capitalization and/or
punctuation.

Method Detail

- getIndexAtPoint

```java
int getIndexAtPoint​(
Point
p)
```

Given a point in local coordinates, return the zero-based index of the
character under that point. If the point is invalid, this method returns
-1.

**Parameters:** p

- the point in local coordinates
**Returns:** the zero-based index of the character under

Point p

; if
point is invalid return -1.

- getCharacterBounds

```java
Rectangle
getCharacterBounds​(int i)
```

Determines the bounding box of the character at the given index into the
string. The bounds are returned in local coordinates. If the index is
invalid an empty rectangle is returned.

**Parameters:** i

- the index into the string
**Returns:** the screen coordinates of the character's bounding box, if index
is invalid return an empty rectangle.

- getCharCount

```java
int getCharCount()
```

Returns the number of characters (valid indicies).

**Returns:** the number of characters

- getCaretPosition

```java
int getCaretPosition()
```

Returns the zero-based offset of the caret.

Note: That to the right of the caret will have the same index value as
the offset (the caret is between two characters).

**Returns:** the zero-based offset of the caret

- getAtIndex

```java
String
getAtIndex​(int part,
int index)
```

Returns the

String

at a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

- getAfterIndex

```java
String
getAfterIndex​(int part,
int index)
```

Returns the

String

after a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

- getBeforeIndex

```java
String
getBeforeIndex​(int part,
int index)
```

Returns the

String

before a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

- getCharacterAttribute

```java
AttributeSet
getCharacterAttribute​(int i)
```

Returns the

AttributeSet

for a given character at a given index.

**Parameters:** i

- the zero-based index into the text
**Returns:** the

AttributeSet

of the character

- getSelectionStart

```java
int getSelectionStart()
```

Returns the start offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:** the index into the text of the start of the selection

- getSelectionEnd

```java
int getSelectionEnd()
```

Returns the end offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:** the index into the text of the end of the selection

- getSelectedText

```java
String
getSelectedText()
```

Returns the portion of the text that is selected.

**Returns:** the

String

portion of the text that is selected

---

#### Method Detail

getIndexAtPoint

```java
int getIndexAtPoint​(
Point
p)
```

Given a point in local coordinates, return the zero-based index of the
character under that point. If the point is invalid, this method returns
-1.

**Parameters:** p

- the point in local coordinates
**Returns:** the zero-based index of the character under

Point p

; if
point is invalid return -1.

---

#### getIndexAtPoint

int getIndexAtPoint​(

Point

p)

Given a point in local coordinates, return the zero-based index of the
character under that point. If the point is invalid, this method returns
-1.

getCharacterBounds

```java
Rectangle
getCharacterBounds​(int i)
```

Determines the bounding box of the character at the given index into the
string. The bounds are returned in local coordinates. If the index is
invalid an empty rectangle is returned.

**Parameters:** i

- the index into the string
**Returns:** the screen coordinates of the character's bounding box, if index
is invalid return an empty rectangle.

---

#### getCharacterBounds

Rectangle

getCharacterBounds​(int i)

Determines the bounding box of the character at the given index into the
string. The bounds are returned in local coordinates. If the index is
invalid an empty rectangle is returned.

getCharCount

```java
int getCharCount()
```

Returns the number of characters (valid indicies).

**Returns:** the number of characters

---

#### getCharCount

int getCharCount()

Returns the number of characters (valid indicies).

getCaretPosition

```java
int getCaretPosition()
```

Returns the zero-based offset of the caret.

Note: That to the right of the caret will have the same index value as
the offset (the caret is between two characters).

**Returns:** the zero-based offset of the caret

---

#### getCaretPosition

int getCaretPosition()

Returns the zero-based offset of the caret.

Note: That to the right of the caret will have the same index value as
the offset (the caret is between two characters).

Note: That to the right of the caret will have the same index value as
the offset (the caret is between two characters).

getAtIndex

```java
String
getAtIndex​(int part,
int index)
```

Returns the

String

at a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

---

#### getAtIndex

String

getAtIndex​(int part,
int index)

Returns the

String

at a given index.

getAfterIndex

```java
String
getAfterIndex​(int part,
int index)
```

Returns the

String

after a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

---

#### getAfterIndex

String

getAfterIndex​(int part,
int index)

Returns the

String

after a given index.

getBeforeIndex

```java
String
getBeforeIndex​(int part,
int index)
```

Returns the

String

before a given index.

**Parameters:** part

- the CHARACTER, WORD, or SENTENCE to retrieve
**Parameters:** index

- an index within the text
**Returns:** the letter, word, or sentence

---

#### getBeforeIndex

String

getBeforeIndex​(int part,
int index)

Returns the

String

before a given index.

getCharacterAttribute

```java
AttributeSet
getCharacterAttribute​(int i)
```

Returns the

AttributeSet

for a given character at a given index.

**Parameters:** i

- the zero-based index into the text
**Returns:** the

AttributeSet

of the character

---

#### getCharacterAttribute

AttributeSet

getCharacterAttribute​(int i)

Returns the

AttributeSet

for a given character at a given index.

getSelectionStart

```java
int getSelectionStart()
```

Returns the start offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:** the index into the text of the start of the selection

---

#### getSelectionStart

int getSelectionStart()

Returns the start offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

getSelectionEnd

```java
int getSelectionEnd()
```

Returns the end offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

**Returns:** the index into the text of the end of the selection

---

#### getSelectionEnd

int getSelectionEnd()

Returns the end offset within the selected text. If there is no
selection, but there is a caret, the start and end offsets will be the
same.

getSelectedText

```java
String
getSelectedText()
```

Returns the portion of the text that is selected.

**Returns:** the

String

portion of the text that is selected

---

#### getSelectedText

String

getSelectedText()

Returns the portion of the text that is selected.

---

