# Interface MutableAttributeSet

**Source:** `java.desktop\javax\swing\text\MutableAttributeSet.html`

### Class Description

```java
public interface
MutableAttributeSet

extends
AttributeSet
```

A generic interface for a mutable collection of unique attributes.

Implementations will probably want to provide a constructor of the
form:

```java
public XXXAttributeSet(ConstAttributeSet source);
```

**All Superinterfaces:** AttributeSet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addAttribute​(
Object
name,

Object
value)

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value. The object must be
immutable, or not mutated by any client.

**Parameters:**
- name

- the name
- value

- the value

---

#### void addAttributes​(
AttributeSet
attributes)

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

**Parameters:**
- attributes

- the set of attributes

---

#### void removeAttribute​(
Object
name)

Removes an attribute with the given

name

.

**Parameters:**
- name

- the attribute name

---

#### void removeAttributes​(
Enumeration
<?> names)

Removes an attribute set with the given

names

.

**Parameters:**
- names

- the set of names

---

#### void removeAttributes​(
AttributeSet
attributes)

Removes a set of attributes with the given

name

.

**Parameters:**
- attributes

- the set of attributes

---

#### void setResolveParent​(
AttributeSet
parent)

Sets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally.

**Parameters:**
- parent

- the parent

---

### Additional Sections

#### Interface MutableAttributeSet

**All Superinterfaces:** AttributeSet

**All Known Subinterfaces:** Style

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

,

SimpleAttributeSet

,

StyleContext.NamedStyle

```java
public interface
MutableAttributeSet

extends
AttributeSet
```

A generic interface for a mutable collection of unique attributes.

Implementations will probably want to provide a constructor of the
form:

```java
public XXXAttributeSet(ConstAttributeSet source);
```

public interface

MutableAttributeSet

extends

AttributeSet

A generic interface for a mutable collection of unique attributes.

Implementations will probably want to provide a constructor of the
form:

```java
public XXXAttributeSet(ConstAttributeSet source);
```

public XXXAttributeSet(ConstAttributeSet source);

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

addAttribute

​(

Object

name,

Object

value)

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value.

void

addAttributes

​(

AttributeSet

attributes)

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

void

removeAttribute

​(

Object

name)

Removes an attribute with the given

name

.

void

removeAttributes

​(

Enumeration

<?> names)

Removes an attribute set with the given

names

.

void

removeAttributes

​(

AttributeSet

attributes)

Removes a set of attributes with the given

name

.

void

setResolveParent

​(

AttributeSet

parent)

Sets the resolving parent.

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

addAttribute

​(

Object

name,

Object

value)

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value.

void

addAttributes

​(

AttributeSet

attributes)

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

void

removeAttribute

​(

Object

name)

Removes an attribute with the given

name

.

void

removeAttributes

​(

Enumeration

<?> names)

Removes an attribute set with the given

names

.

void

removeAttributes

​(

AttributeSet

attributes)

Removes a set of attributes with the given

name

.

void

setResolveParent

​(

AttributeSet

parent)

Sets the resolving parent.

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

---

#### Method Summary

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value.

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

Removes an attribute with the given

name

.

Removes an attribute set with the given

names

.

Removes a set of attributes with the given

name

.

Sets the resolving parent.

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

============ METHOD DETAIL ==========

- Method Detail

- addAttribute

```java
void addAttribute​(
Object
name,

Object
value)
```

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value. The object must be
immutable, or not mutated by any client.

**Parameters:** name

- the name
**Parameters:** value

- the value

- addAttributes

```java
void addAttributes​(
AttributeSet
attributes)
```

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

**Parameters:** attributes

- the set of attributes

- removeAttribute

```java
void removeAttribute​(
Object
name)
```

Removes an attribute with the given

name

.

**Parameters:** name

- the attribute name

- removeAttributes

```java
void removeAttributes​(
Enumeration
<?> names)
```

Removes an attribute set with the given

names

.

**Parameters:** names

- the set of names

- removeAttributes

```java
void removeAttributes​(
AttributeSet
attributes)
```

Removes a set of attributes with the given

name

.

**Parameters:** attributes

- the set of attributes

- setResolveParent

```java
void setResolveParent​(
AttributeSet
parent)
```

Sets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally.

**Parameters:** parent

- the parent

Method Detail

- addAttribute

```java
void addAttribute​(
Object
name,

Object
value)
```

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value. The object must be
immutable, or not mutated by any client.

**Parameters:** name

- the name
**Parameters:** value

- the value

- addAttributes

```java
void addAttributes​(
AttributeSet
attributes)
```

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

**Parameters:** attributes

- the set of attributes

- removeAttribute

```java
void removeAttribute​(
Object
name)
```

Removes an attribute with the given

name

.

**Parameters:** name

- the attribute name

- removeAttributes

```java
void removeAttributes​(
Enumeration
<?> names)
```

Removes an attribute set with the given

names

.

**Parameters:** names

- the set of names

- removeAttributes

```java
void removeAttributes​(
AttributeSet
attributes)
```

Removes a set of attributes with the given

name

.

**Parameters:** attributes

- the set of attributes

- setResolveParent

```java
void setResolveParent​(
AttributeSet
parent)
```

Sets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally.

**Parameters:** parent

- the parent

---

#### Method Detail

addAttribute

```java
void addAttribute​(
Object
name,

Object
value)
```

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value. The object must be
immutable, or not mutated by any client.

**Parameters:** name

- the name
**Parameters:** value

- the value

---

#### addAttribute

void addAttribute​(

Object

name,

Object

value)

Creates a new attribute set similar to this one except that it contains
an attribute with the given name and value. The object must be
immutable, or not mutated by any client.

addAttributes

```java
void addAttributes​(
AttributeSet
attributes)
```

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

**Parameters:** attributes

- the set of attributes

---

#### addAttributes

void addAttributes​(

AttributeSet

attributes)

Creates a new attribute set similar to this one except that it contains
the given attributes and values.

removeAttribute

```java
void removeAttribute​(
Object
name)
```

Removes an attribute with the given

name

.

**Parameters:** name

- the attribute name

---

#### removeAttribute

void removeAttribute​(

Object

name)

Removes an attribute with the given

name

.

removeAttributes

```java
void removeAttributes​(
Enumeration
<?> names)
```

Removes an attribute set with the given

names

.

**Parameters:** names

- the set of names

---

#### removeAttributes

void removeAttributes​(

Enumeration

<?> names)

Removes an attribute set with the given

names

.

removeAttributes

```java
void removeAttributes​(
AttributeSet
attributes)
```

Removes a set of attributes with the given

name

.

**Parameters:** attributes

- the set of attributes

---

#### removeAttributes

void removeAttributes​(

AttributeSet

attributes)

Removes a set of attributes with the given

name

.

setResolveParent

```java
void setResolveParent​(
AttributeSet
parent)
```

Sets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally.

**Parameters:** parent

- the parent

---

#### setResolveParent

void setResolveParent​(

AttributeSet

parent)

Sets the resolving parent. This is the set
of attributes to resolve through if an attribute
isn't defined locally.

---

