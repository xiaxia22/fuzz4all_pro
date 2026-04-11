# Class DocumentFilter.FilterBypass

**Source:** `java.desktop\javax\swing\text\DocumentFilter.FilterBypass.html`

### Class Description

```java
public abstract static class
DocumentFilter.FilterBypass

extends
Object
```

Used as a way to circumvent calling back into the Document to
change it. Document implementations that wish to support
a DocumentFilter must provide an implementation that will
not callback into the DocumentFilter when the following methods
are invoked from the DocumentFilter.

**Enclosing class:** DocumentFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public FilterBypass()

*No description found.*

---

### Method Details

#### public abstract
Document
getDocument()

Returns the Document the mutation is occurring on.

**Returns:**
- Document that remove/insertString will operate on

---

#### public abstract void remove​(int offset,
int length)
throws
BadLocationException

Removes the specified region of text, bypassing the
DocumentFilter.

**Parameters:**
- offset

- the offset from the beginning >= 0
- length

- the number of characters to remove >= 0

**Throws:**
- BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the
exception is the first bad position encountered.

---

#### public abstract void insertString​(int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException

Inserts the specified text, bypassing the
DocumentFilter.

**Parameters:**
- offset

- the offset into the document to insert the
content >= 0. All positions that track change at or after the
given location will move.
- string

- the string to insert
- attr

- the attributes to associate with the inserted
content. This may be null if there are no attributes.

**Throws:**
- BadLocationException

- the given insert position is not a
valid position within the document

---

#### public abstract void replace​(int offset,
int length,

String
string,

AttributeSet
attrs)
throws
BadLocationException

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

**Parameters:**
- offset

- Location in Document
- length

- Length of text to delete
- string

- Text to insert, null indicates no text to insert
- attrs

- AttributeSet indicating attributes of inserted text,
null is legal.

**Throws:**
- BadLocationException

- the given insert is not a
valid position within the document

---

### Additional Sections

#### Class DocumentFilter.FilterBypass

java.lang.Object

- javax.swing.text.DocumentFilter.FilterBypass

javax.swing.text.DocumentFilter.FilterBypass

**Enclosing class:** DocumentFilter

```java
public abstract static class
DocumentFilter.FilterBypass

extends
Object
```

Used as a way to circumvent calling back into the Document to
change it. Document implementations that wish to support
a DocumentFilter must provide an implementation that will
not callback into the DocumentFilter when the following methods
are invoked from the DocumentFilter.

**Since:** 1.4

public abstract static class

DocumentFilter.FilterBypass

extends

Object

Used as a way to circumvent calling back into the Document to
change it. Document implementations that wish to support
a DocumentFilter must provide an implementation that will
not callback into the DocumentFilter when the following methods
are invoked from the DocumentFilter.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FilterBypass

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

Document

getDocument

()

Returns the Document the mutation is occurring on.

abstract void

insertString

​(int offset,

String

string,

AttributeSet

attr)

Inserts the specified text, bypassing the
DocumentFilter.

abstract void

remove

​(int offset,
int length)

Removes the specified region of text, bypassing the
DocumentFilter.

abstract void

replace

​(int offset,
int length,

String

string,

AttributeSet

attrs)

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

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

FilterBypass

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

Document

getDocument

()

Returns the Document the mutation is occurring on.

abstract void

insertString

​(int offset,

String

string,

AttributeSet

attr)

Inserts the specified text, bypassing the
DocumentFilter.

abstract void

remove

​(int offset,
int length)

Removes the specified region of text, bypassing the
DocumentFilter.

abstract void

replace

​(int offset,
int length,

String

string,

AttributeSet

attrs)

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

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

Returns the Document the mutation is occurring on.

Inserts the specified text, bypassing the
DocumentFilter.

Removes the specified region of text, bypassing the
DocumentFilter.

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

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

- FilterBypass

```java
public FilterBypass()
```

============ METHOD DETAIL ==========

- Method Detail

- getDocument

```java
public abstract
Document
getDocument()
```

Returns the Document the mutation is occurring on.

**Returns:** Document that remove/insertString will operate on

- remove

```java
public abstract void remove​(int offset,
int length)
throws
BadLocationException
```

Removes the specified region of text, bypassing the
DocumentFilter.

**Parameters:** offset

- the offset from the beginning >= 0
**Parameters:** length

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the
exception is the first bad position encountered.

- insertString

```java
public abstract void insertString​(int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException
```

Inserts the specified text, bypassing the
DocumentFilter.

**Parameters:** offset

- the offset into the document to insert the
content >= 0. All positions that track change at or after the
given location will move.
**Parameters:** string

- the string to insert
**Parameters:** attr

- the attributes to associate with the inserted
content. This may be null if there are no attributes.
**Throws:** BadLocationException

- the given insert position is not a
valid position within the document

- replace

```java
public abstract void replace​(int offset,
int length,

String
string,

AttributeSet
attrs)
throws
BadLocationException
```

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

**Parameters:** offset

- Location in Document
**Parameters:** length

- Length of text to delete
**Parameters:** string

- Text to insert, null indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,
null is legal.
**Throws:** BadLocationException

- the given insert is not a
valid position within the document

Constructor Detail

- FilterBypass

```java
public FilterBypass()
```

---

#### Constructor Detail

FilterBypass

```java
public FilterBypass()
```

---

#### FilterBypass

public FilterBypass()

Method Detail

- getDocument

```java
public abstract
Document
getDocument()
```

Returns the Document the mutation is occurring on.

**Returns:** Document that remove/insertString will operate on

- remove

```java
public abstract void remove​(int offset,
int length)
throws
BadLocationException
```

Removes the specified region of text, bypassing the
DocumentFilter.

**Parameters:** offset

- the offset from the beginning >= 0
**Parameters:** length

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the
exception is the first bad position encountered.

- insertString

```java
public abstract void insertString​(int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException
```

Inserts the specified text, bypassing the
DocumentFilter.

**Parameters:** offset

- the offset into the document to insert the
content >= 0. All positions that track change at or after the
given location will move.
**Parameters:** string

- the string to insert
**Parameters:** attr

- the attributes to associate with the inserted
content. This may be null if there are no attributes.
**Throws:** BadLocationException

- the given insert position is not a
valid position within the document

- replace

```java
public abstract void replace​(int offset,
int length,

String
string,

AttributeSet
attrs)
throws
BadLocationException
```

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

**Parameters:** offset

- Location in Document
**Parameters:** length

- Length of text to delete
**Parameters:** string

- Text to insert, null indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,
null is legal.
**Throws:** BadLocationException

- the given insert is not a
valid position within the document

---

#### Method Detail

getDocument

```java
public abstract
Document
getDocument()
```

Returns the Document the mutation is occurring on.

**Returns:** Document that remove/insertString will operate on

---

#### getDocument

public abstract

Document

getDocument()

Returns the Document the mutation is occurring on.

remove

```java
public abstract void remove​(int offset,
int length)
throws
BadLocationException
```

Removes the specified region of text, bypassing the
DocumentFilter.

**Parameters:** offset

- the offset from the beginning >= 0
**Parameters:** length

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the
exception is the first bad position encountered.

---

#### remove

public abstract void remove​(int offset,
int length)
throws

BadLocationException

Removes the specified region of text, bypassing the
DocumentFilter.

insertString

```java
public abstract void insertString​(int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException
```

Inserts the specified text, bypassing the
DocumentFilter.

**Parameters:** offset

- the offset into the document to insert the
content >= 0. All positions that track change at or after the
given location will move.
**Parameters:** string

- the string to insert
**Parameters:** attr

- the attributes to associate with the inserted
content. This may be null if there are no attributes.
**Throws:** BadLocationException

- the given insert position is not a
valid position within the document

---

#### insertString

public abstract void insertString​(int offset,

String

string,

AttributeSet

attr)
throws

BadLocationException

Inserts the specified text, bypassing the
DocumentFilter.

replace

```java
public abstract void replace​(int offset,
int length,

String
string,

AttributeSet
attrs)
throws
BadLocationException
```

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

**Parameters:** offset

- Location in Document
**Parameters:** length

- Length of text to delete
**Parameters:** string

- Text to insert, null indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,
null is legal.
**Throws:** BadLocationException

- the given insert is not a
valid position within the document

---

#### replace

public abstract void replace​(int offset,
int length,

String

string,

AttributeSet

attrs)
throws

BadLocationException

Deletes the region of text from

offset

to

offset + length

, and replaces it with

text

.

---

