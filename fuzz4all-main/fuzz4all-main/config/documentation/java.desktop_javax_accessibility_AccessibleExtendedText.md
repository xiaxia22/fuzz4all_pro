# Interface AccessibleExtendedText

**Source:** `java.desktop\javax\accessibility\AccessibleExtendedText.html`

### Class Description

```java
public interface
AccessibleExtendedText
```

The

AccessibleExtendedText

interface contains additional methods not
provided by the

AccessibleText

interface.

Applications can determine if an object supports the

AccessibleExtendedText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is an instance of

AccessibleExtendedText

, the object supports this interface.

**All Known Implementing Classes:** JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JPasswordField.AccessibleJPasswordField

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

---

### Field Details

#### static final int LINE

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

**See Also:**
- AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

---

#### static final int ATTRIBUTE_RUN

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

**See Also:**
- AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getTextRange​(int startIndex,
int endIndex)

Returns the text between two indices.

**Parameters:**
- startIndex

- the start index in the text
- endIndex

- the end index in the text

**Returns:**
- the text string if the indices are valid. Otherwise,

null

is returned.

---

#### AccessibleTextSequence
getTextSequenceAt​(int part,
int index)

Returns the

AccessibleTextSequence

at a given index.

**Parameters:**
- part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
- index

- an index within the text

**Returns:**
- an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.

**See Also:**
- AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

---

#### AccessibleTextSequence
getTextSequenceAfter​(int part,
int index)

Returns the

AccessibleTextSequence

after a given index.

**Parameters:**
- part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
- index

- an index within the text

**Returns:**
- an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.

**See Also:**
- AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

---

#### AccessibleTextSequence
getTextSequenceBefore​(int part,
int index)

Returns the

AccessibleTextSequence

before a given index.

**Parameters:**
- part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
- index

- an index within the text

**Returns:**
- an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.

**See Also:**
- AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

---

#### Rectangle
getTextBounds​(int startIndex,
int endIndex)

Returns the bounding rectangle of the text between two indices.

**Parameters:**
- startIndex

- the start index in the text
- endIndex

- the end index in the text

**Returns:**
- the bounding rectangle of the text if the indices are valid.
Otherwise,

null

is returned.

---

### Additional Sections

#### Interface AccessibleExtendedText

**All Known Implementing Classes:** JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JPasswordField.AccessibleJPasswordField

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

```java
public interface
AccessibleExtendedText
```

The

AccessibleExtendedText

interface contains additional methods not
provided by the

AccessibleText

interface.

Applications can determine if an object supports the

AccessibleExtendedText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is an instance of

AccessibleExtendedText

, the object supports this interface.

**Since:** 1.5
**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleText()

public interface

AccessibleExtendedText

The

AccessibleExtendedText

interface contains additional methods not
provided by the

AccessibleText

interface.

Applications can determine if an object supports the

AccessibleExtendedText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is an instance of

AccessibleExtendedText

, the object supports this interface.

Applications can determine if an object supports the

AccessibleExtendedText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is an instance of

AccessibleExtendedText

, the object supports this interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ATTRIBUTE_RUN

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

static int

LINE

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Rectangle

getTextBounds

​(int startIndex,
int endIndex)

Returns the bounding rectangle of the text between two indices.

String

getTextRange

​(int startIndex,
int endIndex)

Returns the text between two indices.

AccessibleTextSequence

getTextSequenceAfter

​(int part,
int index)

Returns the

AccessibleTextSequence

after a given index.

AccessibleTextSequence

getTextSequenceAt

​(int part,
int index)

Returns the

AccessibleTextSequence

at a given index.

AccessibleTextSequence

getTextSequenceBefore

​(int part,
int index)

Returns the

AccessibleTextSequence

before a given index.

Field Summary

Fields

Modifier and Type

Field

Description

static int

ATTRIBUTE_RUN

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

static int

LINE

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

---

#### Field Summary

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Rectangle

getTextBounds

​(int startIndex,
int endIndex)

Returns the bounding rectangle of the text between two indices.

String

getTextRange

​(int startIndex,
int endIndex)

Returns the text between two indices.

AccessibleTextSequence

getTextSequenceAfter

​(int part,
int index)

Returns the

AccessibleTextSequence

after a given index.

AccessibleTextSequence

getTextSequenceAt

​(int part,
int index)

Returns the

AccessibleTextSequence

at a given index.

AccessibleTextSequence

getTextSequenceBefore

​(int part,
int index)

Returns the

AccessibleTextSequence

before a given index.

---

#### Method Summary

Returns the bounding rectangle of the text between two indices.

Returns the text between two indices.

Returns the

AccessibleTextSequence

after a given index.

Returns the

AccessibleTextSequence

at a given index.

Returns the

AccessibleTextSequence

before a given index.

============ FIELD DETAIL ===========

- Field Detail

- LINE

```java
static final int LINE
```

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

**See Also:** AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

- ATTRIBUTE_RUN

```java
static final int ATTRIBUTE_RUN
```

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

**See Also:** AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getTextRange

```java
String
getTextRange​(int startIndex,
int endIndex)
```

Returns the text between two indices.

**Parameters:** startIndex

- the start index in the text
**Parameters:** endIndex

- the end index in the text
**Returns:** the text string if the indices are valid. Otherwise,

null

is returned.

- getTextSequenceAt

```java
AccessibleTextSequence
getTextSequenceAt​(int part,
int index)
```

Returns the

AccessibleTextSequence

at a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

- getTextSequenceAfter

```java
AccessibleTextSequence
getTextSequenceAfter​(int part,
int index)
```

Returns the

AccessibleTextSequence

after a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

- getTextSequenceBefore

```java
AccessibleTextSequence
getTextSequenceBefore​(int part,
int index)
```

Returns the

AccessibleTextSequence

before a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

- getTextBounds

```java
Rectangle
getTextBounds​(int startIndex,
int endIndex)
```

Returns the bounding rectangle of the text between two indices.

**Parameters:** startIndex

- the start index in the text
**Parameters:** endIndex

- the end index in the text
**Returns:** the bounding rectangle of the text if the indices are valid.
Otherwise,

null

is returned.

Field Detail

- LINE

```java
static final int LINE
```

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

**See Also:** AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

- ATTRIBUTE_RUN

```java
static final int ATTRIBUTE_RUN
```

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

**See Also:** AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

---

#### Field Detail

LINE

```java
static final int LINE
```

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

**See Also:** AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

---

#### LINE

static final int LINE

Constant used to indicate that the part of the text that should be
retrieved is a line of text.

ATTRIBUTE_RUN

```java
static final int ATTRIBUTE_RUN
```

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

**See Also:** AccessibleText.getAtIndex(int, int)

,

AccessibleText.getAfterIndex(int, int)

,

AccessibleText.getBeforeIndex(int, int)

,

Constant Field Values

---

#### ATTRIBUTE_RUN

static final int ATTRIBUTE_RUN

Constant used to indicate that the part of the text that should be
retrieved is contiguous text with the same text attributes.

Method Detail

- getTextRange

```java
String
getTextRange​(int startIndex,
int endIndex)
```

Returns the text between two indices.

**Parameters:** startIndex

- the start index in the text
**Parameters:** endIndex

- the end index in the text
**Returns:** the text string if the indices are valid. Otherwise,

null

is returned.

- getTextSequenceAt

```java
AccessibleTextSequence
getTextSequenceAt​(int part,
int index)
```

Returns the

AccessibleTextSequence

at a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

- getTextSequenceAfter

```java
AccessibleTextSequence
getTextSequenceAfter​(int part,
int index)
```

Returns the

AccessibleTextSequence

after a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

- getTextSequenceBefore

```java
AccessibleTextSequence
getTextSequenceBefore​(int part,
int index)
```

Returns the

AccessibleTextSequence

before a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

- getTextBounds

```java
Rectangle
getTextBounds​(int startIndex,
int endIndex)
```

Returns the bounding rectangle of the text between two indices.

**Parameters:** startIndex

- the start index in the text
**Parameters:** endIndex

- the end index in the text
**Returns:** the bounding rectangle of the text if the indices are valid.
Otherwise,

null

is returned.

---

#### Method Detail

getTextRange

```java
String
getTextRange​(int startIndex,
int endIndex)
```

Returns the text between two indices.

**Parameters:** startIndex

- the start index in the text
**Parameters:** endIndex

- the end index in the text
**Returns:** the text string if the indices are valid. Otherwise,

null

is returned.

---

#### getTextRange

String

getTextRange​(int startIndex,
int endIndex)

Returns the text between two indices.

getTextSequenceAt

```java
AccessibleTextSequence
getTextSequenceAt​(int part,
int index)
```

Returns the

AccessibleTextSequence

at a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

---

#### getTextSequenceAt

AccessibleTextSequence

getTextSequenceAt​(int part,
int index)

Returns the

AccessibleTextSequence

at a given index.

getTextSequenceAfter

```java
AccessibleTextSequence
getTextSequenceAfter​(int part,
int index)
```

Returns the

AccessibleTextSequence

after a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

---

#### getTextSequenceAfter

AccessibleTextSequence

getTextSequenceAfter​(int part,
int index)

Returns the

AccessibleTextSequence

after a given index.

getTextSequenceBefore

```java
AccessibleTextSequence
getTextSequenceBefore​(int part,
int index)
```

Returns the

AccessibleTextSequence

before a given index.

**Parameters:** part

- the

CHARACTER

,

WORD

,

SENTENCE

,

LINE

or

ATTRIBUTE_RUN

to retrieve
**Parameters:** index

- an index within the text
**Returns:** an

AccessibleTextSequence

specifying the text if

part

and

index

are valid. Otherwise,

null

is returned.
**See Also:** AccessibleText.CHARACTER

,

AccessibleText.WORD

,

AccessibleText.SENTENCE

---

#### getTextSequenceBefore

AccessibleTextSequence

getTextSequenceBefore​(int part,
int index)

Returns the

AccessibleTextSequence

before a given index.

getTextBounds

```java
Rectangle
getTextBounds​(int startIndex,
int endIndex)
```

Returns the bounding rectangle of the text between two indices.

**Parameters:** startIndex

- the start index in the text
**Parameters:** endIndex

- the end index in the text
**Returns:** the bounding rectangle of the text if the indices are valid.
Otherwise,

null

is returned.

---

#### getTextBounds

Rectangle

getTextBounds​(int startIndex,
int endIndex)

Returns the bounding rectangle of the text between two indices.

---

