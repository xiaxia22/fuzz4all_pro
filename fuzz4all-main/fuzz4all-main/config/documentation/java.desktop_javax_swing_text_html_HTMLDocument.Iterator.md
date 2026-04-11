# Class HTMLDocument.Iterator

**Source:** `java.desktop\javax\swing\text\html\HTMLDocument.Iterator.html`

### Class Description

```java
public abstract static class
HTMLDocument.Iterator

extends
Object
```

An iterator to iterate over a particular type of
tag. The iterator is not thread safe. If reliable
access to the document is not already ensured by
the context under which the iterator is being used,
its use should be performed under the protection of
Document.render.

**Enclosing class:** HTMLDocument

---

### Field Details

*No entries found.*

### Constructor Details

#### public Iterator()

*No description found.*

---

### Method Details

#### public abstract
AttributeSet
getAttributes()

Return the attributes for this tag.

**Returns:**
- the

AttributeSet

for this tag, or

null

if none can be found

---

#### public abstract int getStartOffset()

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:**
- the start of the range, or -1 if it can't be found

---

#### public abstract int getEndOffset()

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:**
- the end of the range

---

#### public abstract void next()

Move the iterator forward to the next occurrence
of the tag it represents.

---

#### public abstract boolean isValid()

Indicates if the iterator is currently
representing an occurrence of a tag. If
false there are no more tags for this iterator.

**Returns:**
- true if the iterator is currently representing an
occurrence of a tag, otherwise returns false

---

#### public abstract
HTML.Tag
getTag()

Type of tag this iterator represents.

**Returns:**
- the tag

---

### Additional Sections

#### Class HTMLDocument.Iterator

java.lang.Object

- javax.swing.text.html.HTMLDocument.Iterator

javax.swing.text.html.HTMLDocument.Iterator

**Enclosing class:** HTMLDocument

```java
public abstract static class
HTMLDocument.Iterator

extends
Object
```

An iterator to iterate over a particular type of
tag. The iterator is not thread safe. If reliable
access to the document is not already ensured by
the context under which the iterator is being used,
its use should be performed under the protection of
Document.render.

public abstract static class

HTMLDocument.Iterator

extends

Object

An iterator to iterate over a particular type of
tag. The iterator is not thread safe. If reliable
access to the document is not already ensured by
the context under which the iterator is being used,
its use should be performed under the protection of
Document.render.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Iterator

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

AttributeSet

getAttributes

()

Return the attributes for this tag.

abstract int

getEndOffset

()

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

abstract int

getStartOffset

()

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

abstract

HTML.Tag

getTag

()

Type of tag this iterator represents.

abstract boolean

isValid

()

Indicates if the iterator is currently
representing an occurrence of a tag.

abstract void

next

()

Move the iterator forward to the next occurrence
of the tag it represents.

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

Constructor Summary

Constructors

Constructor

Description

Iterator

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

AttributeSet

getAttributes

()

Return the attributes for this tag.

abstract int

getEndOffset

()

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

abstract int

getStartOffset

()

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

abstract

HTML.Tag

getTag

()

Type of tag this iterator represents.

abstract boolean

isValid

()

Indicates if the iterator is currently
representing an occurrence of a tag.

abstract void

next

()

Move the iterator forward to the next occurrence
of the tag it represents.

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

Return the attributes for this tag.

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

Type of tag this iterator represents.

Indicates if the iterator is currently
representing an occurrence of a tag.

Move the iterator forward to the next occurrence
of the tag it represents.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Iterator

```java
public Iterator()
```

============ METHOD DETAIL ==========

- Method Detail

- getAttributes

```java
public abstract
AttributeSet
getAttributes()
```

Return the attributes for this tag.

**Returns:** the

AttributeSet

for this tag, or

null

if none can be found

- getStartOffset

```java
public abstract int getStartOffset()
```

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:** the start of the range, or -1 if it can't be found

- getEndOffset

```java
public abstract int getEndOffset()
```

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:** the end of the range

- next

```java
public abstract void next()
```

Move the iterator forward to the next occurrence
of the tag it represents.

- isValid

```java
public abstract boolean isValid()
```

Indicates if the iterator is currently
representing an occurrence of a tag. If
false there are no more tags for this iterator.

**Returns:** true if the iterator is currently representing an
occurrence of a tag, otherwise returns false

- getTag

```java
public abstract
HTML.Tag
getTag()
```

Type of tag this iterator represents.

**Returns:** the tag

Constructor Detail

- Iterator

```java
public Iterator()
```

---

#### Constructor Detail

Iterator

```java
public Iterator()
```

---

#### Iterator

public Iterator()

Method Detail

- getAttributes

```java
public abstract
AttributeSet
getAttributes()
```

Return the attributes for this tag.

**Returns:** the

AttributeSet

for this tag, or

null

if none can be found

- getStartOffset

```java
public abstract int getStartOffset()
```

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:** the start of the range, or -1 if it can't be found

- getEndOffset

```java
public abstract int getEndOffset()
```

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:** the end of the range

- next

```java
public abstract void next()
```

Move the iterator forward to the next occurrence
of the tag it represents.

- isValid

```java
public abstract boolean isValid()
```

Indicates if the iterator is currently
representing an occurrence of a tag. If
false there are no more tags for this iterator.

**Returns:** true if the iterator is currently representing an
occurrence of a tag, otherwise returns false

- getTag

```java
public abstract
HTML.Tag
getTag()
```

Type of tag this iterator represents.

**Returns:** the tag

---

#### Method Detail

getAttributes

```java
public abstract
AttributeSet
getAttributes()
```

Return the attributes for this tag.

**Returns:** the

AttributeSet

for this tag, or

null

if none can be found

---

#### getAttributes

public abstract

AttributeSet

getAttributes()

Return the attributes for this tag.

getStartOffset

```java
public abstract int getStartOffset()
```

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:** the start of the range, or -1 if it can't be found

---

#### getStartOffset

public abstract int getStartOffset()

Returns the start of the range for which the current occurrence of
the tag is defined and has the same attributes.

getEndOffset

```java
public abstract int getEndOffset()
```

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

**Returns:** the end of the range

---

#### getEndOffset

public abstract int getEndOffset()

Returns the end of the range for which the current occurrence of
the tag is defined and has the same attributes.

next

```java
public abstract void next()
```

Move the iterator forward to the next occurrence
of the tag it represents.

---

#### next

public abstract void next()

Move the iterator forward to the next occurrence
of the tag it represents.

isValid

```java
public abstract boolean isValid()
```

Indicates if the iterator is currently
representing an occurrence of a tag. If
false there are no more tags for this iterator.

**Returns:** true if the iterator is currently representing an
occurrence of a tag, otherwise returns false

---

#### isValid

public abstract boolean isValid()

Indicates if the iterator is currently
representing an occurrence of a tag. If
false there are no more tags for this iterator.

getTag

```java
public abstract
HTML.Tag
getTag()
```

Type of tag this iterator represents.

**Returns:** the tag

---

#### getTag

public abstract

HTML.Tag

getTag()

Type of tag this iterator represents.

---

