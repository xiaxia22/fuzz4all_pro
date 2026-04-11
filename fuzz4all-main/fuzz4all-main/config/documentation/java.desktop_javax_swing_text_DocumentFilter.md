# Class DocumentFilter

**Source:** `java.desktop\javax\swing\text\DocumentFilter.html`

### Class Description

```java
public class
DocumentFilter

extends
Object
```

DocumentFilter

, as the name implies, is a filter for the

Document

mutation methods. When a

Document

containing a

DocumentFilter

is modified (either through

insert

or

remove

), it forwards the appropriate
method invocation to the

DocumentFilter

. The
default implementation allows the modification to
occur. Subclasses can filter the modifications by conditionally invoking
methods on the superclass, or invoking the necessary methods on
the passed in

FilterBypass

. Subclasses should NOT call back
into the Document for the modification
instead call into the superclass or the

FilterBypass

.

When

remove

or

insertString

is invoked
on the

DocumentFilter

, the

DocumentFilter

may callback into the

FilterBypass

multiple times, or for different regions, but
it should not callback into the

FilterBypass

after returning
from the

remove

or

insertString

method.

By default, text related document mutation methods such as

insertString

,

replace

and

remove

in

AbstractDocument

use

DocumentFilter

when
available, and

Element

related mutation methods such as

create

,

insert

and

removeElement

in

DefaultStyledDocument

do not use

DocumentFilter

.
If a method doesn't follow these defaults, this must be explicitly stated
in the method documentation.

**Since:** 1.4
**See Also:** Document

,

AbstractDocument

,

DefaultStyledDocument

---

### Field Details

*No entries found.*

### Constructor Details

#### public DocumentFilter()

*No description found.*

---

### Method Details

#### public void remove​(
DocumentFilter.FilterBypass
fb,
int offset,
int length)
throws
BadLocationException

Invoked prior to removal of the specified region in the
specified Document. Subclasses that want to conditionally allow
removal should override this and only call supers implementation as
necessary, or call directly into the

FilterBypass

as
necessary.

**Parameters:**
- fb

- FilterBypass that can be used to mutate Document
- offset

- the offset from the beginning >= 0
- length

- the number of characters to remove >= 0

**Throws:**
- BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

---

#### public void insertString​(
DocumentFilter.FilterBypass
fb,
int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException

Invoked prior to insertion of text into the
specified Document. Subclasses that want to conditionally allow
insertion should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:**
- fb

- FilterBypass that can be used to mutate Document
- offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
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

#### public void replace​(
DocumentFilter.FilterBypass
fb,
int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException

Invoked prior to replacing a region of text in the
specified Document. Subclasses that want to conditionally allow
replace should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:**
- fb

- FilterBypass that can be used to mutate Document
- offset

- Location in Document
- length

- Length of text to delete
- text

- Text to insert, null indicates no text to insert
- attrs

- AttributeSet indicating attributes of inserted text,
null is legal.

**Throws:**
- BadLocationException

- the given insert position is not a
valid position within the document

---

### Additional Sections

#### Class DocumentFilter

java.lang.Object

- javax.swing.text.DocumentFilter

javax.swing.text.DocumentFilter

```java
public class
DocumentFilter

extends
Object
```

DocumentFilter

, as the name implies, is a filter for the

Document

mutation methods. When a

Document

containing a

DocumentFilter

is modified (either through

insert

or

remove

), it forwards the appropriate
method invocation to the

DocumentFilter

. The
default implementation allows the modification to
occur. Subclasses can filter the modifications by conditionally invoking
methods on the superclass, or invoking the necessary methods on
the passed in

FilterBypass

. Subclasses should NOT call back
into the Document for the modification
instead call into the superclass or the

FilterBypass

.

When

remove

or

insertString

is invoked
on the

DocumentFilter

, the

DocumentFilter

may callback into the

FilterBypass

multiple times, or for different regions, but
it should not callback into the

FilterBypass

after returning
from the

remove

or

insertString

method.

By default, text related document mutation methods such as

insertString

,

replace

and

remove

in

AbstractDocument

use

DocumentFilter

when
available, and

Element

related mutation methods such as

create

,

insert

and

removeElement

in

DefaultStyledDocument

do not use

DocumentFilter

.
If a method doesn't follow these defaults, this must be explicitly stated
in the method documentation.

**Since:** 1.4
**See Also:** Document

,

AbstractDocument

,

DefaultStyledDocument

public class

DocumentFilter

extends

Object

DocumentFilter

, as the name implies, is a filter for the

Document

mutation methods. When a

Document

containing a

DocumentFilter

is modified (either through

insert

or

remove

), it forwards the appropriate
method invocation to the

DocumentFilter

. The
default implementation allows the modification to
occur. Subclasses can filter the modifications by conditionally invoking
methods on the superclass, or invoking the necessary methods on
the passed in

FilterBypass

. Subclasses should NOT call back
into the Document for the modification
instead call into the superclass or the

FilterBypass

.

When

remove

or

insertString

is invoked
on the

DocumentFilter

, the

DocumentFilter

may callback into the

FilterBypass

multiple times, or for different regions, but
it should not callback into the

FilterBypass

after returning
from the

remove

or

insertString

method.

By default, text related document mutation methods such as

insertString

,

replace

and

remove

in

AbstractDocument

use

DocumentFilter

when
available, and

Element

related mutation methods such as

create

,

insert

and

removeElement

in

DefaultStyledDocument

do not use

DocumentFilter

.
If a method doesn't follow these defaults, this must be explicitly stated
in the method documentation.

When

remove

or

insertString

is invoked
on the

DocumentFilter

, the

DocumentFilter

may callback into the

FilterBypass

multiple times, or for different regions, but
it should not callback into the

FilterBypass

after returning
from the

remove

or

insertString

method.

By default, text related document mutation methods such as

insertString

,

replace

and

remove

in

AbstractDocument

use

DocumentFilter

when
available, and

Element

related mutation methods such as

create

,

insert

and

removeElement

in

DefaultStyledDocument

do not use

DocumentFilter

.
If a method doesn't follow these defaults, this must be explicitly stated
in the method documentation.

By default, text related document mutation methods such as

insertString

,

replace

and

remove

in

AbstractDocument

use

DocumentFilter

when
available, and

Element

related mutation methods such as

create

,

insert

and

removeElement

in

DefaultStyledDocument

do not use

DocumentFilter

.
If a method doesn't follow these defaults, this must be explicitly stated
in the method documentation.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DocumentFilter.FilterBypass

Used as a way to circumvent calling back into the Document to
change it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DocumentFilter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

insertString

​(

DocumentFilter.FilterBypass

fb,
int offset,

String

string,

AttributeSet

attr)

Invoked prior to insertion of text into the
specified Document.

void

remove

​(

DocumentFilter.FilterBypass

fb,
int offset,
int length)

Invoked prior to removal of the specified region in the
specified Document.

void

replace

​(

DocumentFilter.FilterBypass

fb,
int offset,
int length,

String

text,

AttributeSet

attrs)

Invoked prior to replacing a region of text in the
specified Document.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

DocumentFilter.FilterBypass

Used as a way to circumvent calling back into the Document to
change it.

---

#### Nested Class Summary

Used as a way to circumvent calling back into the Document to
change it.

Constructor Summary

Constructors

Constructor

Description

DocumentFilter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

insertString

​(

DocumentFilter.FilterBypass

fb,
int offset,

String

string,

AttributeSet

attr)

Invoked prior to insertion of text into the
specified Document.

void

remove

​(

DocumentFilter.FilterBypass

fb,
int offset,
int length)

Invoked prior to removal of the specified region in the
specified Document.

void

replace

​(

DocumentFilter.FilterBypass

fb,
int offset,
int length,

String

text,

AttributeSet

attrs)

Invoked prior to replacing a region of text in the
specified Document.

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

Invoked prior to insertion of text into the
specified Document.

Invoked prior to removal of the specified region in the
specified Document.

Invoked prior to replacing a region of text in the
specified Document.

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

- DocumentFilter

```java
public DocumentFilter()
```

============ METHOD DETAIL ==========

- Method Detail

- remove

```java
public void remove​(
DocumentFilter.FilterBypass
fb,
int offset,
int length)
throws
BadLocationException
```

Invoked prior to removal of the specified region in the
specified Document. Subclasses that want to conditionally allow
removal should override this and only call supers implementation as
necessary, or call directly into the

FilterBypass

as
necessary.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- the offset from the beginning >= 0
**Parameters:** length

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

- insertString

```java
public void insertString​(
DocumentFilter.FilterBypass
fb,
int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException
```

Invoked prior to insertion of text into the
specified Document. Subclasses that want to conditionally allow
insertion should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
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
public void replace​(
DocumentFilter.FilterBypass
fb,
int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException
```

Invoked prior to replacing a region of text in the
specified Document. Subclasses that want to conditionally allow
replace should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- Location in Document
**Parameters:** length

- Length of text to delete
**Parameters:** text

- Text to insert, null indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,
null is legal.
**Throws:** BadLocationException

- the given insert position is not a
valid position within the document

Constructor Detail

- DocumentFilter

```java
public DocumentFilter()
```

---

#### Constructor Detail

DocumentFilter

```java
public DocumentFilter()
```

---

#### DocumentFilter

public DocumentFilter()

Method Detail

- remove

```java
public void remove​(
DocumentFilter.FilterBypass
fb,
int offset,
int length)
throws
BadLocationException
```

Invoked prior to removal of the specified region in the
specified Document. Subclasses that want to conditionally allow
removal should override this and only call supers implementation as
necessary, or call directly into the

FilterBypass

as
necessary.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- the offset from the beginning >= 0
**Parameters:** length

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

- insertString

```java
public void insertString​(
DocumentFilter.FilterBypass
fb,
int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException
```

Invoked prior to insertion of text into the
specified Document. Subclasses that want to conditionally allow
insertion should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
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
public void replace​(
DocumentFilter.FilterBypass
fb,
int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException
```

Invoked prior to replacing a region of text in the
specified Document. Subclasses that want to conditionally allow
replace should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- Location in Document
**Parameters:** length

- Length of text to delete
**Parameters:** text

- Text to insert, null indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,
null is legal.
**Throws:** BadLocationException

- the given insert position is not a
valid position within the document

---

#### Method Detail

remove

```java
public void remove​(
DocumentFilter.FilterBypass
fb,
int offset,
int length)
throws
BadLocationException
```

Invoked prior to removal of the specified region in the
specified Document. Subclasses that want to conditionally allow
removal should override this and only call supers implementation as
necessary, or call directly into the

FilterBypass

as
necessary.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- the offset from the beginning >= 0
**Parameters:** length

- the number of characters to remove >= 0
**Throws:** BadLocationException

- some portion of the removal range
was not a valid part of the document. The location in the exception
is the first bad position encountered.

---

#### remove

public void remove​(

DocumentFilter.FilterBypass

fb,
int offset,
int length)
throws

BadLocationException

Invoked prior to removal of the specified region in the
specified Document. Subclasses that want to conditionally allow
removal should override this and only call supers implementation as
necessary, or call directly into the

FilterBypass

as
necessary.

insertString

```java
public void insertString​(
DocumentFilter.FilterBypass
fb,
int offset,

String
string,

AttributeSet
attr)
throws
BadLocationException
```

Invoked prior to insertion of text into the
specified Document. Subclasses that want to conditionally allow
insertion should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- the offset into the document to insert the content >= 0.
All positions that track change at or after the given location
will move.
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

public void insertString​(

DocumentFilter.FilterBypass

fb,
int offset,

String

string,

AttributeSet

attr)
throws

BadLocationException

Invoked prior to insertion of text into the
specified Document. Subclasses that want to conditionally allow
insertion should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

replace

```java
public void replace​(
DocumentFilter.FilterBypass
fb,
int offset,
int length,

String
text,

AttributeSet
attrs)
throws
BadLocationException
```

Invoked prior to replacing a region of text in the
specified Document. Subclasses that want to conditionally allow
replace should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

**Parameters:** fb

- FilterBypass that can be used to mutate Document
**Parameters:** offset

- Location in Document
**Parameters:** length

- Length of text to delete
**Parameters:** text

- Text to insert, null indicates no text to insert
**Parameters:** attrs

- AttributeSet indicating attributes of inserted text,
null is legal.
**Throws:** BadLocationException

- the given insert position is not a
valid position within the document

---

#### replace

public void replace​(

DocumentFilter.FilterBypass

fb,
int offset,
int length,

String

text,

AttributeSet

attrs)
throws

BadLocationException

Invoked prior to replacing a region of text in the
specified Document. Subclasses that want to conditionally allow
replace should override this and only call supers implementation as
necessary, or call directly into the FilterBypass.

---

