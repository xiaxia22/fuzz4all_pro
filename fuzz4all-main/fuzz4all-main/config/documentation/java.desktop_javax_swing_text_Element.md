# Interface Element

**Source:** `java.desktop\javax\swing\text\Element.html`

### Class Description

```java
public interface
Element
```

Interface to describe a structural piece of a document. It
is intended to capture the spirit of an SGML element.

**All Known Implementing Classes:** AbstractDocument.AbstractElement

,

AbstractDocument.BranchElement

,

AbstractDocument.LeafElement

,

DefaultStyledDocument.SectionElement

,

HTMLDocument.BlockElement

,

HTMLDocument.RunElement

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Document
getDocument()

Fetches the document associated with this element.

**Returns:**
- the document

---

#### Element
getParentElement()

Fetches the parent element. If the element is a root level
element returns

null

.

**Returns:**
- the parent element

---

#### String
getName()

Fetches the name of the element. If the element is used to
represent some type of structure, this would be the type
name.

**Returns:**
- the element name

---

#### AttributeSet
getAttributes()

Fetches the collection of attributes this element contains.

**Returns:**
- the attributes for the element

---

#### int getStartOffset()

Fetches the offset from the beginning of the document
that this element begins at. If this element has
children, this will be the offset of the first child.
As a document position, there is an implied forward bias.

**Returns:**
- the starting offset >= 0 and < getEndOffset();

**See Also:**
- Document

,

AbstractDocument

---

#### int getEndOffset()

Fetches the offset from the beginning of the document
that this element ends at. If this element has
children, this will be the end offset of the last child.
As a document position, there is an implied backward bias.

All the default

Document

implementations
descend from

AbstractDocument

.

AbstractDocument

models an implied break at the end of
the document. As a result of this, it is possible for this to
return a value greater than the length of the document.

**Returns:**
- the ending offset > getStartOffset() and
<= getDocument().getLength() + 1

**See Also:**
- Document

,

AbstractDocument

---

#### int getElementIndex​(int offset)

Gets the child element index closest to the given offset.
The offset is specified relative to the beginning of the
document. Returns

-1

if the

Element

is a leaf, otherwise returns
the index of the

Element

that best represents
the given location. Returns

0

if the location
is less than the start offset. Returns

getElementCount() - 1

if the location is
greater than or equal to the end offset.

**Parameters:**
- offset

- the specified offset >= 0

**Returns:**
- the element index >= 0

---

#### int getElementCount()

Gets the number of child elements contained by this element.
If this element is a leaf, a count of zero is returned.

**Returns:**
- the number of child elements >= 0

---

#### Element
getElement​(int index)

Fetches the child element at the given index.

**Parameters:**
- index

- the specified index >= 0

**Returns:**
- the child element

---

#### boolean isLeaf()

Is this element a leaf element? An element that

may

have children, even if it currently
has no children, would return

false

.

**Returns:**
- true if a leaf element else false

---

### Additional Sections

#### Interface Element

**All Known Implementing Classes:** AbstractDocument.AbstractElement

,

AbstractDocument.BranchElement

,

AbstractDocument.LeafElement

,

DefaultStyledDocument.SectionElement

,

HTMLDocument.BlockElement

,

HTMLDocument.RunElement

```java
public interface
Element
```

Interface to describe a structural piece of a document. It
is intended to capture the spirit of an SGML element.

public interface

Element

Interface to describe a structural piece of a document. It
is intended to capture the spirit of an SGML element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AttributeSet

getAttributes

()

Fetches the collection of attributes this element contains.

Document

getDocument

()

Fetches the document associated with this element.

Element

getElement

​(int index)

Fetches the child element at the given index.

int

getElementCount

()

Gets the number of child elements contained by this element.

int

getElementIndex

​(int offset)

Gets the child element index closest to the given offset.

int

getEndOffset

()

Fetches the offset from the beginning of the document
that this element ends at.

String

getName

()

Fetches the name of the element.

Element

getParentElement

()

Fetches the parent element.

int

getStartOffset

()

Fetches the offset from the beginning of the document
that this element begins at.

boolean

isLeaf

()

Is this element a leaf element?

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AttributeSet

getAttributes

()

Fetches the collection of attributes this element contains.

Document

getDocument

()

Fetches the document associated with this element.

Element

getElement

​(int index)

Fetches the child element at the given index.

int

getElementCount

()

Gets the number of child elements contained by this element.

int

getElementIndex

​(int offset)

Gets the child element index closest to the given offset.

int

getEndOffset

()

Fetches the offset from the beginning of the document
that this element ends at.

String

getName

()

Fetches the name of the element.

Element

getParentElement

()

Fetches the parent element.

int

getStartOffset

()

Fetches the offset from the beginning of the document
that this element begins at.

boolean

isLeaf

()

Is this element a leaf element?

---

#### Method Summary

Fetches the collection of attributes this element contains.

Fetches the document associated with this element.

Fetches the child element at the given index.

Gets the number of child elements contained by this element.

Gets the child element index closest to the given offset.

Fetches the offset from the beginning of the document
that this element ends at.

Fetches the name of the element.

Fetches the parent element.

Fetches the offset from the beginning of the document
that this element begins at.

Is this element a leaf element?

============ METHOD DETAIL ==========

- Method Detail

- getDocument

```java
Document
getDocument()
```

Fetches the document associated with this element.

**Returns:** the document

- getParentElement

```java
Element
getParentElement()
```

Fetches the parent element. If the element is a root level
element returns

null

.

**Returns:** the parent element

- getName

```java
String
getName()
```

Fetches the name of the element. If the element is used to
represent some type of structure, this would be the type
name.

**Returns:** the element name

- getAttributes

```java
AttributeSet
getAttributes()
```

Fetches the collection of attributes this element contains.

**Returns:** the attributes for the element

- getStartOffset

```java
int getStartOffset()
```

Fetches the offset from the beginning of the document
that this element begins at. If this element has
children, this will be the offset of the first child.
As a document position, there is an implied forward bias.

**Returns:** the starting offset >= 0 and < getEndOffset();
**See Also:** Document

,

AbstractDocument

- getEndOffset

```java
int getEndOffset()
```

Fetches the offset from the beginning of the document
that this element ends at. If this element has
children, this will be the end offset of the last child.
As a document position, there is an implied backward bias.

All the default

Document

implementations
descend from

AbstractDocument

.

AbstractDocument

models an implied break at the end of
the document. As a result of this, it is possible for this to
return a value greater than the length of the document.

**Returns:** the ending offset > getStartOffset() and
<= getDocument().getLength() + 1
**See Also:** Document

,

AbstractDocument

- getElementIndex

```java
int getElementIndex​(int offset)
```

Gets the child element index closest to the given offset.
The offset is specified relative to the beginning of the
document. Returns

-1

if the

Element

is a leaf, otherwise returns
the index of the

Element

that best represents
the given location. Returns

0

if the location
is less than the start offset. Returns

getElementCount() - 1

if the location is
greater than or equal to the end offset.

**Parameters:** offset

- the specified offset >= 0
**Returns:** the element index >= 0

- getElementCount

```java
int getElementCount()
```

Gets the number of child elements contained by this element.
If this element is a leaf, a count of zero is returned.

**Returns:** the number of child elements >= 0

- getElement

```java
Element
getElement​(int index)
```

Fetches the child element at the given index.

**Parameters:** index

- the specified index >= 0
**Returns:** the child element

- isLeaf

```java
boolean isLeaf()
```

Is this element a leaf element? An element that

may

have children, even if it currently
has no children, would return

false

.

**Returns:** true if a leaf element else false

Method Detail

- getDocument

```java
Document
getDocument()
```

Fetches the document associated with this element.

**Returns:** the document

- getParentElement

```java
Element
getParentElement()
```

Fetches the parent element. If the element is a root level
element returns

null

.

**Returns:** the parent element

- getName

```java
String
getName()
```

Fetches the name of the element. If the element is used to
represent some type of structure, this would be the type
name.

**Returns:** the element name

- getAttributes

```java
AttributeSet
getAttributes()
```

Fetches the collection of attributes this element contains.

**Returns:** the attributes for the element

- getStartOffset

```java
int getStartOffset()
```

Fetches the offset from the beginning of the document
that this element begins at. If this element has
children, this will be the offset of the first child.
As a document position, there is an implied forward bias.

**Returns:** the starting offset >= 0 and < getEndOffset();
**See Also:** Document

,

AbstractDocument

- getEndOffset

```java
int getEndOffset()
```

Fetches the offset from the beginning of the document
that this element ends at. If this element has
children, this will be the end offset of the last child.
As a document position, there is an implied backward bias.

All the default

Document

implementations
descend from

AbstractDocument

.

AbstractDocument

models an implied break at the end of
the document. As a result of this, it is possible for this to
return a value greater than the length of the document.

**Returns:** the ending offset > getStartOffset() and
<= getDocument().getLength() + 1
**See Also:** Document

,

AbstractDocument

- getElementIndex

```java
int getElementIndex​(int offset)
```

Gets the child element index closest to the given offset.
The offset is specified relative to the beginning of the
document. Returns

-1

if the

Element

is a leaf, otherwise returns
the index of the

Element

that best represents
the given location. Returns

0

if the location
is less than the start offset. Returns

getElementCount() - 1

if the location is
greater than or equal to the end offset.

**Parameters:** offset

- the specified offset >= 0
**Returns:** the element index >= 0

- getElementCount

```java
int getElementCount()
```

Gets the number of child elements contained by this element.
If this element is a leaf, a count of zero is returned.

**Returns:** the number of child elements >= 0

- getElement

```java
Element
getElement​(int index)
```

Fetches the child element at the given index.

**Parameters:** index

- the specified index >= 0
**Returns:** the child element

- isLeaf

```java
boolean isLeaf()
```

Is this element a leaf element? An element that

may

have children, even if it currently
has no children, would return

false

.

**Returns:** true if a leaf element else false

---

#### Method Detail

getDocument

```java
Document
getDocument()
```

Fetches the document associated with this element.

**Returns:** the document

---

#### getDocument

Document

getDocument()

Fetches the document associated with this element.

getParentElement

```java
Element
getParentElement()
```

Fetches the parent element. If the element is a root level
element returns

null

.

**Returns:** the parent element

---

#### getParentElement

Element

getParentElement()

Fetches the parent element. If the element is a root level
element returns

null

.

getName

```java
String
getName()
```

Fetches the name of the element. If the element is used to
represent some type of structure, this would be the type
name.

**Returns:** the element name

---

#### getName

String

getName()

Fetches the name of the element. If the element is used to
represent some type of structure, this would be the type
name.

getAttributes

```java
AttributeSet
getAttributes()
```

Fetches the collection of attributes this element contains.

**Returns:** the attributes for the element

---

#### getAttributes

AttributeSet

getAttributes()

Fetches the collection of attributes this element contains.

getStartOffset

```java
int getStartOffset()
```

Fetches the offset from the beginning of the document
that this element begins at. If this element has
children, this will be the offset of the first child.
As a document position, there is an implied forward bias.

**Returns:** the starting offset >= 0 and < getEndOffset();
**See Also:** Document

,

AbstractDocument

---

#### getStartOffset

int getStartOffset()

Fetches the offset from the beginning of the document
that this element begins at. If this element has
children, this will be the offset of the first child.
As a document position, there is an implied forward bias.

getEndOffset

```java
int getEndOffset()
```

Fetches the offset from the beginning of the document
that this element ends at. If this element has
children, this will be the end offset of the last child.
As a document position, there is an implied backward bias.

All the default

Document

implementations
descend from

AbstractDocument

.

AbstractDocument

models an implied break at the end of
the document. As a result of this, it is possible for this to
return a value greater than the length of the document.

**Returns:** the ending offset > getStartOffset() and
<= getDocument().getLength() + 1
**See Also:** Document

,

AbstractDocument

---

#### getEndOffset

int getEndOffset()

Fetches the offset from the beginning of the document
that this element ends at. If this element has
children, this will be the end offset of the last child.
As a document position, there is an implied backward bias.

All the default

Document

implementations
descend from

AbstractDocument

.

AbstractDocument

models an implied break at the end of
the document. As a result of this, it is possible for this to
return a value greater than the length of the document.

All the default

Document

implementations
descend from

AbstractDocument

.

AbstractDocument

models an implied break at the end of
the document. As a result of this, it is possible for this to
return a value greater than the length of the document.

getElementIndex

```java
int getElementIndex​(int offset)
```

Gets the child element index closest to the given offset.
The offset is specified relative to the beginning of the
document. Returns

-1

if the

Element

is a leaf, otherwise returns
the index of the

Element

that best represents
the given location. Returns

0

if the location
is less than the start offset. Returns

getElementCount() - 1

if the location is
greater than or equal to the end offset.

**Parameters:** offset

- the specified offset >= 0
**Returns:** the element index >= 0

---

#### getElementIndex

int getElementIndex​(int offset)

Gets the child element index closest to the given offset.
The offset is specified relative to the beginning of the
document. Returns

-1

if the

Element

is a leaf, otherwise returns
the index of the

Element

that best represents
the given location. Returns

0

if the location
is less than the start offset. Returns

getElementCount() - 1

if the location is
greater than or equal to the end offset.

getElementCount

```java
int getElementCount()
```

Gets the number of child elements contained by this element.
If this element is a leaf, a count of zero is returned.

**Returns:** the number of child elements >= 0

---

#### getElementCount

int getElementCount()

Gets the number of child elements contained by this element.
If this element is a leaf, a count of zero is returned.

getElement

```java
Element
getElement​(int index)
```

Fetches the child element at the given index.

**Parameters:** index

- the specified index >= 0
**Returns:** the child element

---

#### getElement

Element

getElement​(int index)

Fetches the child element at the given index.

isLeaf

```java
boolean isLeaf()
```

Is this element a leaf element? An element that

may

have children, even if it currently
has no children, would return

false

.

**Returns:** true if a leaf element else false

---

#### isLeaf

boolean isLeaf()

Is this element a leaf element? An element that

may

have children, even if it currently
has no children, would return

false

.

---

