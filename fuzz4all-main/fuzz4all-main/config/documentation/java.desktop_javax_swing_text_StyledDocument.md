# Interface StyledDocument

**Source:** `java.desktop\javax\swing\text\StyledDocument.html`

### Class Description

```java
public interface
StyledDocument

extends
Document
```

Interface for a generic styled document.

**All Superinterfaces:** Document

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Style
addStyle​(
String
nm,

Style
parent)

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:**
- nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
- parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.

**Returns:**
- the style

---

#### void removeStyle​(
String
nm)

Removes a named style previously added to the document.

**Parameters:**
- nm

- the name of the style to remove

---

#### Style
getStyle​(
String
nm)

Fetches a named style previously added.

**Parameters:**
- nm

- the name of the style

**Returns:**
- the style

---

#### void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)

Changes the content element attributes used for the given range of
existing content in the document. All of the attributes
defined in the given Attributes argument are applied to the
given range. This method can be used to completely remove
all content level attributes for the given range by
giving an Attributes argument that has no attributes defined
and setting replace to true.

**Parameters:**
- offset

- the start of the change >= 0
- length

- the length of the change >= 0
- s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
- replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
as set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

---

#### void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)

Sets paragraph attributes.

**Parameters:**
- offset

- the start of the change >= 0
- length

- the length of the change >= 0
- s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
- replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
are set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

---

#### void setLogicalStyle​(int pos,

Style
s)

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

**Parameters:**
- pos

- the starting position >= 0
- s

- the style to set

---

#### Style
getLogicalStyle​(int p)

Gets a logical style for a given position in a paragraph.

**Parameters:**
- p

- the position >= 0

**Returns:**
- the style

---

#### Element
getParagraphElement​(int pos)

Gets the element that represents the paragraph that
encloses the given offset within the document.

**Parameters:**
- pos

- the offset >= 0

**Returns:**
- the element

---

#### Element
getCharacterElement​(int pos)

Gets the element that represents the character that
is at the given offset within the document.

**Parameters:**
- pos

- the offset >= 0

**Returns:**
- the element

---

#### Color
getForeground​(
AttributeSet
attr)

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:**
- attr

- the set of attributes

**Returns:**
- the color

---

#### Color
getBackground​(
AttributeSet
attr)

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:**
- attr

- the set of attributes

**Returns:**
- the color

---

#### Font
getFont​(
AttributeSet
attr)

Takes a set of attributes and turn it into a font
specification. This can be used to turn things like
family, style, size, etc into a font that is available
on the system the document is currently being used on.

**Parameters:**
- attr

- the set of attributes

**Returns:**
- the font

---

### Additional Sections

#### Interface StyledDocument

**All Superinterfaces:** Document

**All Known Implementing Classes:** DefaultStyledDocument

,

HTMLDocument

```java
public interface
StyledDocument

extends
Document
```

Interface for a generic styled document.

public interface

StyledDocument

extends

Document

Interface for a generic styled document.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Style

addStyle

​(

String

nm,

Style

parent)

Adds a new style into the logical style hierarchy.

Color

getBackground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a background color
specification.

Element

getCharacterElement

​(int pos)

Gets the element that represents the character that
is at the given offset within the document.

Font

getFont

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a font
specification.

Color

getForeground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a foreground color
specification.

Style

getLogicalStyle

​(int p)

Gets a logical style for a given position in a paragraph.

Element

getParagraphElement

​(int pos)

Gets the element that represents the paragraph that
encloses the given offset within the document.

Style

getStyle

​(

String

nm)

Fetches a named style previously added.

void

removeStyle

​(

String

nm)

Removes a named style previously added to the document.

void

setCharacterAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Changes the content element attributes used for the given range of
existing content in the document.

void

setLogicalStyle

​(int pos,

Style

s)

Sets the logical style to use for the paragraph at the
given position.

void

setParagraphAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets paragraph attributes.

- Methods declared in interface javax.swing.text.

Document

addDocumentListener

,

addUndoableEditListener

,

createPosition

,

getDefaultRootElement

,

getEndPosition

,

getLength

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

insertString

,

putProperty

,

remove

,

removeDocumentListener

,

removeUndoableEditListener

,

render

Field Summary

- Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

---

#### Field Summary

Fields declared in interface javax.swing.text.

Document

StreamDescriptionProperty

,

TitleProperty

---

#### Fields declared in interface javax.swing.text. Document

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Style

addStyle

​(

String

nm,

Style

parent)

Adds a new style into the logical style hierarchy.

Color

getBackground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a background color
specification.

Element

getCharacterElement

​(int pos)

Gets the element that represents the character that
is at the given offset within the document.

Font

getFont

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a font
specification.

Color

getForeground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a foreground color
specification.

Style

getLogicalStyle

​(int p)

Gets a logical style for a given position in a paragraph.

Element

getParagraphElement

​(int pos)

Gets the element that represents the paragraph that
encloses the given offset within the document.

Style

getStyle

​(

String

nm)

Fetches a named style previously added.

void

removeStyle

​(

String

nm)

Removes a named style previously added to the document.

void

setCharacterAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Changes the content element attributes used for the given range of
existing content in the document.

void

setLogicalStyle

​(int pos,

Style

s)

Sets the logical style to use for the paragraph at the
given position.

void

setParagraphAttributes

​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets paragraph attributes.

- Methods declared in interface javax.swing.text.

Document

addDocumentListener

,

addUndoableEditListener

,

createPosition

,

getDefaultRootElement

,

getEndPosition

,

getLength

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

insertString

,

putProperty

,

remove

,

removeDocumentListener

,

removeUndoableEditListener

,

render

---

#### Method Summary

Adds a new style into the logical style hierarchy.

Takes a set of attributes and turn it into a background color
specification.

Gets the element that represents the character that
is at the given offset within the document.

Takes a set of attributes and turn it into a font
specification.

Takes a set of attributes and turn it into a foreground color
specification.

Gets a logical style for a given position in a paragraph.

Gets the element that represents the paragraph that
encloses the given offset within the document.

Fetches a named style previously added.

Removes a named style previously added to the document.

Changes the content element attributes used for the given range of
existing content in the document.

Sets the logical style to use for the paragraph at the
given position.

Sets paragraph attributes.

Methods declared in interface javax.swing.text.

Document

addDocumentListener

,

addUndoableEditListener

,

createPosition

,

getDefaultRootElement

,

getEndPosition

,

getLength

,

getProperty

,

getRootElements

,

getStartPosition

,

getText

,

getText

,

insertString

,

putProperty

,

remove

,

removeDocumentListener

,

removeUndoableEditListener

,

render

---

#### Methods declared in interface javax.swing.text. Document

============ METHOD DETAIL ==========

- Method Detail

- addStyle

```java
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the style

- removeStyle

```java
void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Parameters:** nm

- the name of the style to remove

- getStyle

```java
Style
getStyle​(
String
nm)
```

Fetches a named style previously added.

**Parameters:** nm

- the name of the style
**Returns:** the style

- setCharacterAttributes

```java
void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Changes the content element attributes used for the given range of
existing content in the document. All of the attributes
defined in the given Attributes argument are applied to the
given range. This method can be used to completely remove
all content level attributes for the given range by
giving an Attributes argument that has no attributes defined
and setting replace to true.

**Parameters:** offset

- the start of the change >= 0
**Parameters:** length

- the length of the change >= 0
**Parameters:** s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
**Parameters:** replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
as set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

- setParagraphAttributes

```java
void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets paragraph attributes.

**Parameters:** offset

- the start of the change >= 0
**Parameters:** length

- the length of the change >= 0
**Parameters:** s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
**Parameters:** replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
are set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

- setLogicalStyle

```java
void setLogicalStyle​(int pos,

Style
s)
```

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

**Parameters:** pos

- the starting position >= 0
**Parameters:** s

- the style to set

- getLogicalStyle

```java
Style
getLogicalStyle​(int p)
```

Gets a logical style for a given position in a paragraph.

**Parameters:** p

- the position >= 0
**Returns:** the style

- getParagraphElement

```java
Element
getParagraphElement​(int pos)
```

Gets the element that represents the paragraph that
encloses the given offset within the document.

**Parameters:** pos

- the offset >= 0
**Returns:** the element

- getCharacterElement

```java
Element
getCharacterElement​(int pos)
```

Gets the element that represents the character that
is at the given offset within the document.

**Parameters:** pos

- the offset >= 0
**Returns:** the element

- getForeground

```java
Color
getForeground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getBackground

```java
Color
getBackground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getFont

```java
Font
getFont​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a font
specification. This can be used to turn things like
family, style, size, etc into a font that is available
on the system the document is currently being used on.

**Parameters:** attr

- the set of attributes
**Returns:** the font

Method Detail

- addStyle

```java
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the style

- removeStyle

```java
void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Parameters:** nm

- the name of the style to remove

- getStyle

```java
Style
getStyle​(
String
nm)
```

Fetches a named style previously added.

**Parameters:** nm

- the name of the style
**Returns:** the style

- setCharacterAttributes

```java
void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Changes the content element attributes used for the given range of
existing content in the document. All of the attributes
defined in the given Attributes argument are applied to the
given range. This method can be used to completely remove
all content level attributes for the given range by
giving an Attributes argument that has no attributes defined
and setting replace to true.

**Parameters:** offset

- the start of the change >= 0
**Parameters:** length

- the length of the change >= 0
**Parameters:** s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
**Parameters:** replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
as set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

- setParagraphAttributes

```java
void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets paragraph attributes.

**Parameters:** offset

- the start of the change >= 0
**Parameters:** length

- the length of the change >= 0
**Parameters:** s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
**Parameters:** replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
are set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

- setLogicalStyle

```java
void setLogicalStyle​(int pos,

Style
s)
```

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

**Parameters:** pos

- the starting position >= 0
**Parameters:** s

- the style to set

- getLogicalStyle

```java
Style
getLogicalStyle​(int p)
```

Gets a logical style for a given position in a paragraph.

**Parameters:** p

- the position >= 0
**Returns:** the style

- getParagraphElement

```java
Element
getParagraphElement​(int pos)
```

Gets the element that represents the paragraph that
encloses the given offset within the document.

**Parameters:** pos

- the offset >= 0
**Returns:** the element

- getCharacterElement

```java
Element
getCharacterElement​(int pos)
```

Gets the element that represents the character that
is at the given offset within the document.

**Parameters:** pos

- the offset >= 0
**Returns:** the element

- getForeground

```java
Color
getForeground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getBackground

```java
Color
getBackground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getFont

```java
Font
getFont​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a font
specification. This can be used to turn things like
family, style, size, etc into a font that is available
on the system the document is currently being used on.

**Parameters:** attr

- the set of attributes
**Returns:** the font

---

#### Method Detail

addStyle

```java
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles). The name may be null if the style
is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the style

---

#### addStyle

Style

addStyle​(

String

nm,

Style

parent)

Adds a new style into the logical style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

removeStyle

```java
void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Parameters:** nm

- the name of the style to remove

---

#### removeStyle

void removeStyle​(

String

nm)

Removes a named style previously added to the document.

getStyle

```java
Style
getStyle​(
String
nm)
```

Fetches a named style previously added.

**Parameters:** nm

- the name of the style
**Returns:** the style

---

#### getStyle

Style

getStyle​(

String

nm)

Fetches a named style previously added.

setCharacterAttributes

```java
void setCharacterAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Changes the content element attributes used for the given range of
existing content in the document. All of the attributes
defined in the given Attributes argument are applied to the
given range. This method can be used to completely remove
all content level attributes for the given range by
giving an Attributes argument that has no attributes defined
and setting replace to true.

**Parameters:** offset

- the start of the change >= 0
**Parameters:** length

- the length of the change >= 0
**Parameters:** s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
**Parameters:** replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
as set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

---

#### setCharacterAttributes

void setCharacterAttributes​(int offset,
int length,

AttributeSet

s,
boolean replace)

Changes the content element attributes used for the given range of
existing content in the document. All of the attributes
defined in the given Attributes argument are applied to the
given range. This method can be used to completely remove
all content level attributes for the given range by
giving an Attributes argument that has no attributes defined
and setting replace to true.

setParagraphAttributes

```java
void setParagraphAttributes​(int offset,
int length,

AttributeSet
s,
boolean replace)
```

Sets paragraph attributes.

**Parameters:** offset

- the start of the change >= 0
**Parameters:** length

- the length of the change >= 0
**Parameters:** s

- the non-null attributes to change to. Any attributes
defined will be applied to the text for the given range.
**Parameters:** replace

- indicates whether or not the previous
attributes should be cleared before the new attributes
are set. If true, the operation will replace the
previous attributes entirely. If false, the new
attributes will be merged with the previous attributes.

---

#### setParagraphAttributes

void setParagraphAttributes​(int offset,
int length,

AttributeSet

s,
boolean replace)

Sets paragraph attributes.

setLogicalStyle

```java
void setLogicalStyle​(int pos,

Style
s)
```

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

**Parameters:** pos

- the starting position >= 0
**Parameters:** s

- the style to set

---

#### setLogicalStyle

void setLogicalStyle​(int pos,

Style

s)

Sets the logical style to use for the paragraph at the
given position. If attributes aren't explicitly set
for character and paragraph attributes they will resolve
through the logical style assigned to the paragraph, which
in turn may resolve through some hierarchy completely
independent of the element hierarchy in the document.

getLogicalStyle

```java
Style
getLogicalStyle​(int p)
```

Gets a logical style for a given position in a paragraph.

**Parameters:** p

- the position >= 0
**Returns:** the style

---

#### getLogicalStyle

Style

getLogicalStyle​(int p)

Gets a logical style for a given position in a paragraph.

getParagraphElement

```java
Element
getParagraphElement​(int pos)
```

Gets the element that represents the paragraph that
encloses the given offset within the document.

**Parameters:** pos

- the offset >= 0
**Returns:** the element

---

#### getParagraphElement

Element

getParagraphElement​(int pos)

Gets the element that represents the paragraph that
encloses the given offset within the document.

getCharacterElement

```java
Element
getCharacterElement​(int pos)
```

Gets the element that represents the character that
is at the given offset within the document.

**Parameters:** pos

- the offset >= 0
**Returns:** the element

---

#### getCharacterElement

Element

getCharacterElement​(int pos)

Gets the element that represents the character that
is at the given offset within the document.

getForeground

```java
Color
getForeground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:** attr

- the set of attributes
**Returns:** the color

---

#### getForeground

Color

getForeground​(

AttributeSet

attr)

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc.

getBackground

```java
Color
getBackground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc.

**Parameters:** attr

- the set of attributes
**Returns:** the color

---

#### getBackground

Color

getBackground​(

AttributeSet

attr)

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc.

getFont

```java
Font
getFont​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a font
specification. This can be used to turn things like
family, style, size, etc into a font that is available
on the system the document is currently being used on.

**Parameters:** attr

- the set of attributes
**Returns:** the font

---

#### getFont

Font

getFont​(

AttributeSet

attr)

Takes a set of attributes and turn it into a font
specification. This can be used to turn things like
family, style, size, etc into a font that is available
on the system the document is currently being used on.

---

