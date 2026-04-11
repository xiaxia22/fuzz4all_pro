# Interface AccessibleHypertext

**Source:** `java.desktop\javax\accessibility\AccessibleHypertext.html`

### Class Description

```java
public interface
AccessibleHypertext

extends
AccessibleText
```

The

AccessibleHypertext

class is the base class for all classes that
present hypertext information on the display. This class provides the
standard mechanism for an assistive technology to access that text via its
content, attributes, and spatial location. It also provides standard
mechanisms for manipulating hyperlinks. Applications can determine if an
object supports the

AccessibleHypertext

interface by first obtaining
its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is a class which extends

AccessibleHypertext

, then that object supports

AccessibleHypertext

.

**All Superinterfaces:** AccessibleText

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLinkCount()

Returns the number of links within this hypertext document.

**Returns:**
- number of links in this hypertext doc

---

#### AccessibleHyperlink
getLink​(int linkIndex)

Returns the nth Link of this Hypertext document.

**Parameters:**
- linkIndex

- within the links of this Hypertext

**Returns:**
- Link object encapsulating the nth link(s)

---

#### int getLinkIndex​(int charIndex)

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

**Parameters:**
- charIndex

- index within the text

**Returns:**
- index into the set of hyperlinks for this hypertext doc

---

### Additional Sections

#### Interface AccessibleHypertext

**All Superinterfaces:** AccessibleText

**All Known Implementing Classes:** JEditorPane.JEditorPaneAccessibleHypertextSupport

```java
public interface
AccessibleHypertext

extends
AccessibleText
```

The

AccessibleHypertext

class is the base class for all classes that
present hypertext information on the display. This class provides the
standard mechanism for an assistive technology to access that text via its
content, attributes, and spatial location. It also provides standard
mechanisms for manipulating hyperlinks. Applications can determine if an
object supports the

AccessibleHypertext

interface by first obtaining
its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is a class which extends

AccessibleHypertext

, then that object supports

AccessibleHypertext

.

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleText

,

AccessibleContext.getAccessibleText()

public interface

AccessibleHypertext

extends

AccessibleText

The

AccessibleHypertext

class is the base class for all classes that
present hypertext information on the display. This class provides the
standard mechanism for an assistive technology to access that text via its
content, attributes, and spatial location. It also provides standard
mechanisms for manipulating hyperlinks. Applications can determine if an
object supports the

AccessibleHypertext

interface by first obtaining
its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleText()

method of

AccessibleContext

. If the return value is a class which extends

AccessibleHypertext

, then that object supports

AccessibleHypertext

.

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

AccessibleHyperlink

getLink

​(int linkIndex)

Returns the nth Link of this Hypertext document.

int

getLinkCount

()

Returns the number of links within this hypertext document.

int

getLinkIndex

​(int charIndex)

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

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

AccessibleHyperlink

getLink

​(int linkIndex)

Returns the nth Link of this Hypertext document.

int

getLinkCount

()

Returns the number of links within this hypertext document.

int

getLinkIndex

​(int charIndex)

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

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

Returns the nth Link of this Hypertext document.

Returns the number of links within this hypertext document.

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

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

- getLinkCount

```java
int getLinkCount()
```

Returns the number of links within this hypertext document.

**Returns:** number of links in this hypertext doc

- getLink

```java
AccessibleHyperlink
getLink​(int linkIndex)
```

Returns the nth Link of this Hypertext document.

**Parameters:** linkIndex

- within the links of this Hypertext
**Returns:** Link object encapsulating the nth link(s)

- getLinkIndex

```java
int getLinkIndex​(int charIndex)
```

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

**Parameters:** charIndex

- index within the text
**Returns:** index into the set of hyperlinks for this hypertext doc

Method Detail

- getLinkCount

```java
int getLinkCount()
```

Returns the number of links within this hypertext document.

**Returns:** number of links in this hypertext doc

- getLink

```java
AccessibleHyperlink
getLink​(int linkIndex)
```

Returns the nth Link of this Hypertext document.

**Parameters:** linkIndex

- within the links of this Hypertext
**Returns:** Link object encapsulating the nth link(s)

- getLinkIndex

```java
int getLinkIndex​(int charIndex)
```

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

**Parameters:** charIndex

- index within the text
**Returns:** index into the set of hyperlinks for this hypertext doc

---

#### Method Detail

getLinkCount

```java
int getLinkCount()
```

Returns the number of links within this hypertext document.

**Returns:** number of links in this hypertext doc

---

#### getLinkCount

int getLinkCount()

Returns the number of links within this hypertext document.

getLink

```java
AccessibleHyperlink
getLink​(int linkIndex)
```

Returns the nth Link of this Hypertext document.

**Parameters:** linkIndex

- within the links of this Hypertext
**Returns:** Link object encapsulating the nth link(s)

---

#### getLink

AccessibleHyperlink

getLink​(int linkIndex)

Returns the nth Link of this Hypertext document.

getLinkIndex

```java
int getLinkIndex​(int charIndex)
```

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

**Parameters:** charIndex

- index within the text
**Returns:** index into the set of hyperlinks for this hypertext doc

---

#### getLinkIndex

int getLinkIndex​(int charIndex)

Returns the index into an array of hyperlinks that is associated with
this character index, or -1 if there is no hyperlink associated with this
index.

---

