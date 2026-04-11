# Interface Style

**Source:** `java.desktop\javax\swing\text\Style.html`

### Class Description

```java
public interface
Style

extends
MutableAttributeSet
```

A collection of attributes to associate with an element in a document.
Since these are typically used to associate character and paragraph
styles with the element, operations for this are provided. Other
customized attributes that get associated with the element will
effectively be name-value pairs that live in a hierarchy and if a name
(key) is not found locally, the request is forwarded to the parent.
Commonly used attributes are separated out to facilitate alternative
implementations that are more efficient.

**All Superinterfaces:** AttributeSet

,

MutableAttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Fetches the name of the style. A style is not required to be named,
so

null

is returned if there is no name
associated with the style.

**Returns:**
- the name

---

#### void addChangeListener​(
ChangeListener
l)

Adds a listener to track whenever an attribute
has been changed.

**Parameters:**
- l

- the change listener

---

#### void removeChangeListener​(
ChangeListener
l)

Removes a listener that was tracking attribute changes.

**Parameters:**
- l

- the change listener

---

### Additional Sections

#### Interface Style

**All Superinterfaces:** AttributeSet

,

MutableAttributeSet

**All Known Implementing Classes:** StyleContext.NamedStyle

```java
public interface
Style

extends
MutableAttributeSet
```

A collection of attributes to associate with an element in a document.
Since these are typically used to associate character and paragraph
styles with the element, operations for this are provided. Other
customized attributes that get associated with the element will
effectively be name-value pairs that live in a hierarchy and if a name
(key) is not found locally, the request is forwarded to the parent.
Commonly used attributes are separated out to facilitate alternative
implementations that are more efficient.

public interface

Style

extends

MutableAttributeSet

A collection of attributes to associate with an element in a document.
Since these are typically used to associate character and paragraph
styles with the element, operations for this are provided. Other
customized attributes that get associated with the element will
effectively be name-value pairs that live in a hierarchy and if a name
(key) is not found locally, the request is forwarded to the parent.
Commonly used attributes are separated out to facilitate alternative
implementations that are more efficient.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.swing.text.

AttributeSet

AttributeSet.CharacterAttribute

,

AttributeSet.ColorAttribute

,

AttributeSet.FontAttribute

,

AttributeSet.ParagraphAttribute

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.swing.text.

AttributeSet

NameAttribute

,

ResolveAttribute

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a listener to track whenever an attribute
has been changed.

String

getName

()

Fetches the name of the style.

void

removeChangeListener

​(

ChangeListener

l)

Removes a listener that was tracking attribute changes.

- Methods declared in interface javax.swing.text.

AttributeSet

containsAttribute

,

containsAttributes

,

copyAttributes

,

getAttribute

,

getAttributeCount

,

getAttributeNames

,

getResolveParent

,

isDefined

,

isEqual

- Methods declared in interface javax.swing.text.

MutableAttributeSet

addAttribute

,

addAttributes

,

removeAttribute

,

removeAttributes

,

removeAttributes

,

setResolveParent

Nested Class Summary

- Nested classes/interfaces declared in interface javax.swing.text.

AttributeSet

AttributeSet.CharacterAttribute

,

AttributeSet.ColorAttribute

,

AttributeSet.FontAttribute

,

AttributeSet.ParagraphAttribute

---

#### Nested Class Summary

Nested classes/interfaces declared in interface javax.swing.text.

AttributeSet

AttributeSet.CharacterAttribute

,

AttributeSet.ColorAttribute

,

AttributeSet.FontAttribute

,

AttributeSet.ParagraphAttribute

---

#### Nested classes/interfaces declared in interface javax.swing.text. AttributeSet

Field Summary

- Fields declared in interface javax.swing.text.

AttributeSet

NameAttribute

,

ResolveAttribute

---

#### Field Summary

Fields declared in interface javax.swing.text.

AttributeSet

NameAttribute

,

ResolveAttribute

---

#### Fields declared in interface javax.swing.text. AttributeSet

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a listener to track whenever an attribute
has been changed.

String

getName

()

Fetches the name of the style.

void

removeChangeListener

​(

ChangeListener

l)

Removes a listener that was tracking attribute changes.

- Methods declared in interface javax.swing.text.

AttributeSet

containsAttribute

,

containsAttributes

,

copyAttributes

,

getAttribute

,

getAttributeCount

,

getAttributeNames

,

getResolveParent

,

isDefined

,

isEqual

- Methods declared in interface javax.swing.text.

MutableAttributeSet

addAttribute

,

addAttributes

,

removeAttribute

,

removeAttributes

,

removeAttributes

,

setResolveParent

---

#### Method Summary

Adds a listener to track whenever an attribute
has been changed.

Fetches the name of the style.

Removes a listener that was tracking attribute changes.

Methods declared in interface javax.swing.text.

AttributeSet

containsAttribute

,

containsAttributes

,

copyAttributes

,

getAttribute

,

getAttributeCount

,

getAttributeNames

,

getResolveParent

,

isDefined

,

isEqual

---

#### Methods declared in interface javax.swing.text. AttributeSet

Methods declared in interface javax.swing.text.

MutableAttributeSet

addAttribute

,

addAttributes

,

removeAttribute

,

removeAttributes

,

removeAttributes

,

setResolveParent

---

#### Methods declared in interface javax.swing.text. MutableAttributeSet

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Fetches the name of the style. A style is not required to be named,
so

null

is returned if there is no name
associated with the style.

**Returns:** the name

- addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track whenever an attribute
has been changed.

**Parameters:** l

- the change listener

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking attribute changes.

**Parameters:** l

- the change listener

Method Detail

- getName

```java
String
getName()
```

Fetches the name of the style. A style is not required to be named,
so

null

is returned if there is no name
associated with the style.

**Returns:** the name

- addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track whenever an attribute
has been changed.

**Parameters:** l

- the change listener

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking attribute changes.

**Parameters:** l

- the change listener

---

#### Method Detail

getName

```java
String
getName()
```

Fetches the name of the style. A style is not required to be named,
so

null

is returned if there is no name
associated with the style.

**Returns:** the name

---

#### getName

String

getName()

Fetches the name of the style. A style is not required to be named,
so

null

is returned if there is no name
associated with the style.

addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track whenever an attribute
has been changed.

**Parameters:** l

- the change listener

---

#### addChangeListener

void addChangeListener​(

ChangeListener

l)

Adds a listener to track whenever an attribute
has been changed.

removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking attribute changes.

**Parameters:** l

- the change listener

---

#### removeChangeListener

void removeChangeListener​(

ChangeListener

l)

Removes a listener that was tracking attribute changes.

---

