# Interface AccessibleEditableText

**Source:** `java.desktop\javax\accessibility\AccessibleEditableText.html`

### Class Description

```java
public interface
AccessibleEditableText

extends
AccessibleText
```

The

AccessibleEditableText

interface should be implemented by all
classes that present editable textual information on the display. Along with
the

AccessibleText

interface, this interface provides the standard
mechanism for an assistive technology to access that text via its content,
attributes, and spatial location. Applications can determine if an object
supports the

AccessibleEditableText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleEditableText()

method of

AccessibleContext

. If the return value is not

null

, the
object supports this interface.

**All Superinterfaces:** AccessibleText

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setTextContents​(
String
s)

Sets the text contents to the specified string.

**Parameters:**
- s

- the string to set the text contents

---

#### void insertTextAtIndex​(int index,

String
s)

Inserts the specified string at the given index.

**Parameters:**
- index

- the index in the text where the string will be inserted
- s

- the string to insert in the text

---

#### String
getTextRange​(int startIndex,
int endIndex)

Returns the text string between two indices.

**Parameters:**
- startIndex

- the starting index in the text
- endIndex

- the ending index in the text

**Returns:**
- the text string between the indices

---

#### void delete​(int startIndex,
int endIndex)

Deletes the text between two indices.

**Parameters:**
- startIndex

- the starting index in the text
- endIndex

- the ending index in the text

---

#### void cut​(int startIndex,
int endIndex)

Cuts the text between two indices into the system clipboard.

**Parameters:**
- startIndex

- the starting index in the text
- endIndex

- the ending index in the text

---

#### void paste​(int startIndex)

Pastes the text from the system clipboard into the text starting at the
specified index.

**Parameters:**
- startIndex

- the starting index in the text

---

#### void replaceText​(int startIndex,
int endIndex,

String
s)

Replaces the text between two indices with the specified string.

**Parameters:**
- startIndex

- the starting index in the text
- endIndex

- the ending index in the text
- s

- the string to replace the text between two indices

---

#### void selectText​(int startIndex,
int endIndex)

Selects the text between two indices.

**Parameters:**
- startIndex

- the starting index in the text
- endIndex

- the ending index in the text

---

#### void setAttributes​(int startIndex,
int endIndex,

AttributeSet
as)

Sets attributes for the text between two indices.

**Parameters:**
- startIndex

- the starting index in the text
- endIndex

- the ending index in the text
- as

- the attribute set

**See Also:**
- AttributeSet

---

### Additional Sections

#### Interface AccessibleEditableText

**All Superinterfaces:** AccessibleText

**All Known Implementing Classes:** JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JPasswordField.AccessibleJPasswordField

,

JSpinner.AccessibleJSpinner

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

```java
public interface
AccessibleEditableText

extends
AccessibleText
```

The

AccessibleEditableText

interface should be implemented by all
classes that present editable textual information on the display. Along with
the

AccessibleText

interface, this interface provides the standard
mechanism for an assistive technology to access that text via its content,
attributes, and spatial location. Applications can determine if an object
supports the

AccessibleEditableText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleEditableText()

method of

AccessibleContext

. If the return value is not

null

, the
object supports this interface.

**Since:** 1.4
**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleText()

,

AccessibleContext.getAccessibleEditableText()

public interface

AccessibleEditableText

extends

AccessibleText

The

AccessibleEditableText

interface should be implemented by all
classes that present editable textual information on the display. Along with
the

AccessibleText

interface, this interface provides the standard
mechanism for an assistive technology to access that text via its content,
attributes, and spatial location. Applications can determine if an object
supports the

AccessibleEditableText

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleEditableText()

method of

AccessibleContext

. If the return value is not

null

, the
object supports this interface.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.accessibility.

AccessibleText

CHARACTER

,

SENTENCE

,

WORD

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cut

​(int startIndex,
int endIndex)

Cuts the text between two indices into the system clipboard.

void

delete

​(int startIndex,
int endIndex)

Deletes the text between two indices.

String

getTextRange

​(int startIndex,
int endIndex)

Returns the text string between two indices.

void

insertTextAtIndex

​(int index,

String

s)

Inserts the specified string at the given index.

void

paste

​(int startIndex)

Pastes the text from the system clipboard into the text starting at the
specified index.

void

replaceText

​(int startIndex,
int endIndex,

String

s)

Replaces the text between two indices with the specified string.

void

selectText

​(int startIndex,
int endIndex)

Selects the text between two indices.

void

setAttributes

​(int startIndex,
int endIndex,

AttributeSet

as)

Sets attributes for the text between two indices.

void

setTextContents

​(

String

s)

Sets the text contents to the specified string.

- Methods declared in interface javax.accessibility.

AccessibleText

getAfterIndex

,

getAtIndex

,

getBeforeIndex

,

getCaretPosition

,

getCharacterAttribute

,

getCharacterBounds

,

getCharCount

,

getIndexAtPoint

,

getSelectedText

,

getSelectionEnd

,

getSelectionStart

Field Summary

- Fields declared in interface javax.accessibility.

AccessibleText

CHARACTER

,

SENTENCE

,

WORD

---

#### Field Summary

Fields declared in interface javax.accessibility.

AccessibleText

CHARACTER

,

SENTENCE

,

WORD

---

#### Fields declared in interface javax.accessibility. AccessibleText

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

cut

​(int startIndex,
int endIndex)

Cuts the text between two indices into the system clipboard.

void

delete

​(int startIndex,
int endIndex)

Deletes the text between two indices.

String

getTextRange

​(int startIndex,
int endIndex)

Returns the text string between two indices.

void

insertTextAtIndex

​(int index,

String

s)

Inserts the specified string at the given index.

void

paste

​(int startIndex)

Pastes the text from the system clipboard into the text starting at the
specified index.

void

replaceText

​(int startIndex,
int endIndex,

String

s)

Replaces the text between two indices with the specified string.

void

selectText

​(int startIndex,
int endIndex)

Selects the text between two indices.

void

setAttributes

​(int startIndex,
int endIndex,

AttributeSet

as)

Sets attributes for the text between two indices.

void

setTextContents

​(

String

s)

Sets the text contents to the specified string.

- Methods declared in interface javax.accessibility.

AccessibleText

getAfterIndex

,

getAtIndex

,

getBeforeIndex

,

getCaretPosition

,

getCharacterAttribute

,

getCharacterBounds

,

getCharCount

,

getIndexAtPoint

,

getSelectedText

,

getSelectionEnd

,

getSelectionStart

---

#### Method Summary

Cuts the text between two indices into the system clipboard.

Deletes the text between two indices.

Returns the text string between two indices.

Inserts the specified string at the given index.

Pastes the text from the system clipboard into the text starting at the
specified index.

Replaces the text between two indices with the specified string.

Selects the text between two indices.

Sets attributes for the text between two indices.

Sets the text contents to the specified string.

Methods declared in interface javax.accessibility.

AccessibleText

getAfterIndex

,

getAtIndex

,

getBeforeIndex

,

getCaretPosition

,

getCharacterAttribute

,

getCharacterBounds

,

getCharCount

,

getIndexAtPoint

,

getSelectedText

,

getSelectionEnd

,

getSelectionStart

---

#### Methods declared in interface javax.accessibility. AccessibleText

============ METHOD DETAIL ==========

- Method Detail

- setTextContents

```java
void setTextContents​(
String
s)
```

Sets the text contents to the specified string.

**Parameters:** s

- the string to set the text contents

- insertTextAtIndex

```java
void insertTextAtIndex​(int index,

String
s)
```

Inserts the specified string at the given index.

**Parameters:** index

- the index in the text where the string will be inserted
**Parameters:** s

- the string to insert in the text

- getTextRange

```java
String
getTextRange​(int startIndex,
int endIndex)
```

Returns the text string between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Returns:** the text string between the indices

- delete

```java
void delete​(int startIndex,
int endIndex)
```

Deletes the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

- cut

```java
void cut​(int startIndex,
int endIndex)
```

Cuts the text between two indices into the system clipboard.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

- paste

```java
void paste​(int startIndex)
```

Pastes the text from the system clipboard into the text starting at the
specified index.

**Parameters:** startIndex

- the starting index in the text

- replaceText

```java
void replaceText​(int startIndex,
int endIndex,

String
s)
```

Replaces the text between two indices with the specified string.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Parameters:** s

- the string to replace the text between two indices

- selectText

```java
void selectText​(int startIndex,
int endIndex)
```

Selects the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

- setAttributes

```java
void setAttributes​(int startIndex,
int endIndex,

AttributeSet
as)
```

Sets attributes for the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Parameters:** as

- the attribute set
**See Also:** AttributeSet

Method Detail

- setTextContents

```java
void setTextContents​(
String
s)
```

Sets the text contents to the specified string.

**Parameters:** s

- the string to set the text contents

- insertTextAtIndex

```java
void insertTextAtIndex​(int index,

String
s)
```

Inserts the specified string at the given index.

**Parameters:** index

- the index in the text where the string will be inserted
**Parameters:** s

- the string to insert in the text

- getTextRange

```java
String
getTextRange​(int startIndex,
int endIndex)
```

Returns the text string between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Returns:** the text string between the indices

- delete

```java
void delete​(int startIndex,
int endIndex)
```

Deletes the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

- cut

```java
void cut​(int startIndex,
int endIndex)
```

Cuts the text between two indices into the system clipboard.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

- paste

```java
void paste​(int startIndex)
```

Pastes the text from the system clipboard into the text starting at the
specified index.

**Parameters:** startIndex

- the starting index in the text

- replaceText

```java
void replaceText​(int startIndex,
int endIndex,

String
s)
```

Replaces the text between two indices with the specified string.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Parameters:** s

- the string to replace the text between two indices

- selectText

```java
void selectText​(int startIndex,
int endIndex)
```

Selects the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

- setAttributes

```java
void setAttributes​(int startIndex,
int endIndex,

AttributeSet
as)
```

Sets attributes for the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Parameters:** as

- the attribute set
**See Also:** AttributeSet

---

#### Method Detail

setTextContents

```java
void setTextContents​(
String
s)
```

Sets the text contents to the specified string.

**Parameters:** s

- the string to set the text contents

---

#### setTextContents

void setTextContents​(

String

s)

Sets the text contents to the specified string.

insertTextAtIndex

```java
void insertTextAtIndex​(int index,

String
s)
```

Inserts the specified string at the given index.

**Parameters:** index

- the index in the text where the string will be inserted
**Parameters:** s

- the string to insert in the text

---

#### insertTextAtIndex

void insertTextAtIndex​(int index,

String

s)

Inserts the specified string at the given index.

getTextRange

```java
String
getTextRange​(int startIndex,
int endIndex)
```

Returns the text string between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Returns:** the text string between the indices

---

#### getTextRange

String

getTextRange​(int startIndex,
int endIndex)

Returns the text string between two indices.

delete

```java
void delete​(int startIndex,
int endIndex)
```

Deletes the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

---

#### delete

void delete​(int startIndex,
int endIndex)

Deletes the text between two indices.

cut

```java
void cut​(int startIndex,
int endIndex)
```

Cuts the text between two indices into the system clipboard.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

---

#### cut

void cut​(int startIndex,
int endIndex)

Cuts the text between two indices into the system clipboard.

paste

```java
void paste​(int startIndex)
```

Pastes the text from the system clipboard into the text starting at the
specified index.

**Parameters:** startIndex

- the starting index in the text

---

#### paste

void paste​(int startIndex)

Pastes the text from the system clipboard into the text starting at the
specified index.

replaceText

```java
void replaceText​(int startIndex,
int endIndex,

String
s)
```

Replaces the text between two indices with the specified string.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Parameters:** s

- the string to replace the text between two indices

---

#### replaceText

void replaceText​(int startIndex,
int endIndex,

String

s)

Replaces the text between two indices with the specified string.

selectText

```java
void selectText​(int startIndex,
int endIndex)
```

Selects the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text

---

#### selectText

void selectText​(int startIndex,
int endIndex)

Selects the text between two indices.

setAttributes

```java
void setAttributes​(int startIndex,
int endIndex,

AttributeSet
as)
```

Sets attributes for the text between two indices.

**Parameters:** startIndex

- the starting index in the text
**Parameters:** endIndex

- the ending index in the text
**Parameters:** as

- the attribute set
**See Also:** AttributeSet

---

#### setAttributes

void setAttributes​(int startIndex,
int endIndex,

AttributeSet

as)

Sets attributes for the text between two indices.

---

