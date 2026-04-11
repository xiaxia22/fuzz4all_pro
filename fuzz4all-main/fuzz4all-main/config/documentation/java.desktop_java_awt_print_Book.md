# Class Book

**Source:** `java.desktop\java\awt\print\Book.html`

### Class Description

```java
public class
Book

extends
Object

implements
Pageable
```

The

Book

class provides a representation of a document in
which pages may have different page formats and page painters. This
class uses the

Pageable

interface to interact with a

PrinterJob

.

**All Implemented Interfaces:** Pageable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Book()

Creates a new, empty

Book

.

---

### Method Details

#### public int getNumberOfPages()

Returns the number of pages in this

Book

.

**Specified by:**
- getNumberOfPages

in interface

Pageable

**Returns:**
- the number of pages this

Book

contains.

---

#### public
PageFormat
getPageFormat​(int pageIndex)
throws
IndexOutOfBoundsException

Returns the

PageFormat

of the page specified by

pageIndex

.

**Specified by:**
- getPageFormat

in interface

Pageable

**Parameters:**
- pageIndex

- the zero based index of the page whose

PageFormat

is being requested

**Returns:**
- the

PageFormat

describing the size and
orientation of the page.

**Throws:**
- IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

---

#### public
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

**Specified by:**
- getPrintable

in interface

Pageable

**Parameters:**
- pageIndex

- the zero based index of the page whose

Printable

is being requested

**Returns:**
- the

Printable

that renders the page.

**Throws:**
- IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

---

#### public void setPage​(int pageIndex,

Printable
painter,

PageFormat
page)
throws
IndexOutOfBoundsException

Sets the

PageFormat

and the

Painter

for a
specified page number.

**Parameters:**
- pageIndex

- the zero based index of the page whose
painter and format is altered
- painter

- the

Printable

instance that
renders the page
- page

- the size and orientation of the page

**Throws:**
- IndexOutOfBoundsException

- if the specified
page is not already in this

Book
- NullPointerException

- if the

painter

or

page

argument is

null

---

#### public void append​(
Printable
painter,

PageFormat
page)

Appends a single page to the end of this

Book

.

**Parameters:**
- painter

- the

Printable

instance that
renders the page
- page

- the size and orientation of the page

**Throws:**
- NullPointerException

- If the

painter

or

page

argument is

null

---

#### public void append​(
Printable
painter,

PageFormat
page,
int numPages)

Appends

numPages

pages to the end of this

Book

. Each of the pages is associated with

page

.

**Parameters:**
- painter

- the

Printable

instance that renders
the page
- page

- the size and orientation of the page
- numPages

- the number of pages to be added to the
this

Book

.

**Throws:**
- NullPointerException

- If the

painter

or

page

argument is

null

---

### Additional Sections

#### Class Book

java.lang.Object

- java.awt.print.Book

java.awt.print.Book

**All Implemented Interfaces:** Pageable

```java
public class
Book

extends
Object

implements
Pageable
```

The

Book

class provides a representation of a document in
which pages may have different page formats and page painters. This
class uses the

Pageable

interface to interact with a

PrinterJob

.

**See Also:** Pageable

,

PrinterJob

public class

Book

extends

Object

implements

Pageable

The

Book

class provides a representation of a document in
which pages may have different page formats and page painters. This
class uses the

Pageable

interface to interact with a

PrinterJob

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.awt.print.

Pageable

UNKNOWN_NUMBER_OF_PAGES

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Book

()

Creates a new, empty

Book

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

append

​(

Printable

painter,

PageFormat

page)

Appends a single page to the end of this

Book

.

void

append

​(

Printable

painter,

PageFormat

page,
int numPages)

Appends

numPages

pages to the end of this

Book

.

int

getNumberOfPages

()

Returns the number of pages in this

Book

.

PageFormat

getPageFormat

​(int pageIndex)

Returns the

PageFormat

of the page specified by

pageIndex

.

Printable

getPrintable

​(int pageIndex)

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

void

setPage

​(int pageIndex,

Printable

painter,

PageFormat

page)

Sets the

PageFormat

and the

Painter

for a
specified page number.

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

Field Summary

- Fields declared in interface java.awt.print.

Pageable

UNKNOWN_NUMBER_OF_PAGES

---

#### Field Summary

Fields declared in interface java.awt.print.

Pageable

UNKNOWN_NUMBER_OF_PAGES

---

#### Fields declared in interface java.awt.print. Pageable

Constructor Summary

Constructors

Constructor

Description

Book

()

Creates a new, empty

Book

.

---

#### Constructor Summary

Creates a new, empty

Book

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

append

​(

Printable

painter,

PageFormat

page)

Appends a single page to the end of this

Book

.

void

append

​(

Printable

painter,

PageFormat

page,
int numPages)

Appends

numPages

pages to the end of this

Book

.

int

getNumberOfPages

()

Returns the number of pages in this

Book

.

PageFormat

getPageFormat

​(int pageIndex)

Returns the

PageFormat

of the page specified by

pageIndex

.

Printable

getPrintable

​(int pageIndex)

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

void

setPage

​(int pageIndex,

Printable

painter,

PageFormat

page)

Sets the

PageFormat

and the

Painter

for a
specified page number.

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

Appends a single page to the end of this

Book

.

Appends

numPages

pages to the end of this

Book

.

Returns the number of pages in this

Book

.

Returns the

PageFormat

of the page specified by

pageIndex

.

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

Sets the

PageFormat

and the

Painter

for a
specified page number.

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

- Book

```java
public Book()
```

Creates a new, empty

Book

.

============ METHOD DETAIL ==========

- Method Detail

- getNumberOfPages

```java
public int getNumberOfPages()
```

Returns the number of pages in this

Book

.

**Specified by:** getNumberOfPages

in interface

Pageable
**Returns:** the number of pages this

Book

contains.

- getPageFormat

```java
public
PageFormat
getPageFormat​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

PageFormat

of the page specified by

pageIndex

.

**Specified by:** getPageFormat

in interface

Pageable
**Parameters:** pageIndex

- the zero based index of the page whose

PageFormat

is being requested
**Returns:** the

PageFormat

describing the size and
orientation of the page.
**Throws:** IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

- getPrintable

```java
public
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

**Specified by:** getPrintable

in interface

Pageable
**Parameters:** pageIndex

- the zero based index of the page whose

Printable

is being requested
**Returns:** the

Printable

that renders the page.
**Throws:** IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

- setPage

```java
public void setPage​(int pageIndex,

Printable
painter,

PageFormat
page)
throws
IndexOutOfBoundsException
```

Sets the

PageFormat

and the

Painter

for a
specified page number.

**Parameters:** pageIndex

- the zero based index of the page whose
painter and format is altered
**Parameters:** painter

- the

Printable

instance that
renders the page
**Parameters:** page

- the size and orientation of the page
**Throws:** IndexOutOfBoundsException

- if the specified
page is not already in this

Book
**Throws:** NullPointerException

- if the

painter

or

page

argument is

null

- append

```java
public void append​(
Printable
painter,

PageFormat
page)
```

Appends a single page to the end of this

Book

.

**Parameters:** painter

- the

Printable

instance that
renders the page
**Parameters:** page

- the size and orientation of the page
**Throws:** NullPointerException

- If the

painter

or

page

argument is

null

- append

```java
public void append​(
Printable
painter,

PageFormat
page,
int numPages)
```

Appends

numPages

pages to the end of this

Book

. Each of the pages is associated with

page

.

**Parameters:** painter

- the

Printable

instance that renders
the page
**Parameters:** page

- the size and orientation of the page
**Parameters:** numPages

- the number of pages to be added to the
this

Book

.
**Throws:** NullPointerException

- If the

painter

or

page

argument is

null

Constructor Detail

- Book

```java
public Book()
```

Creates a new, empty

Book

.

---

#### Constructor Detail

Book

```java
public Book()
```

Creates a new, empty

Book

.

---

#### Book

public Book()

Creates a new, empty

Book

.

Method Detail

- getNumberOfPages

```java
public int getNumberOfPages()
```

Returns the number of pages in this

Book

.

**Specified by:** getNumberOfPages

in interface

Pageable
**Returns:** the number of pages this

Book

contains.

- getPageFormat

```java
public
PageFormat
getPageFormat​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

PageFormat

of the page specified by

pageIndex

.

**Specified by:** getPageFormat

in interface

Pageable
**Parameters:** pageIndex

- the zero based index of the page whose

PageFormat

is being requested
**Returns:** the

PageFormat

describing the size and
orientation of the page.
**Throws:** IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

- getPrintable

```java
public
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

**Specified by:** getPrintable

in interface

Pageable
**Parameters:** pageIndex

- the zero based index of the page whose

Printable

is being requested
**Returns:** the

Printable

that renders the page.
**Throws:** IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

- setPage

```java
public void setPage​(int pageIndex,

Printable
painter,

PageFormat
page)
throws
IndexOutOfBoundsException
```

Sets the

PageFormat

and the

Painter

for a
specified page number.

**Parameters:** pageIndex

- the zero based index of the page whose
painter and format is altered
**Parameters:** painter

- the

Printable

instance that
renders the page
**Parameters:** page

- the size and orientation of the page
**Throws:** IndexOutOfBoundsException

- if the specified
page is not already in this

Book
**Throws:** NullPointerException

- if the

painter

or

page

argument is

null

- append

```java
public void append​(
Printable
painter,

PageFormat
page)
```

Appends a single page to the end of this

Book

.

**Parameters:** painter

- the

Printable

instance that
renders the page
**Parameters:** page

- the size and orientation of the page
**Throws:** NullPointerException

- If the

painter

or

page

argument is

null

- append

```java
public void append​(
Printable
painter,

PageFormat
page,
int numPages)
```

Appends

numPages

pages to the end of this

Book

. Each of the pages is associated with

page

.

**Parameters:** painter

- the

Printable

instance that renders
the page
**Parameters:** page

- the size and orientation of the page
**Parameters:** numPages

- the number of pages to be added to the
this

Book

.
**Throws:** NullPointerException

- If the

painter

or

page

argument is

null

---

#### Method Detail

getNumberOfPages

```java
public int getNumberOfPages()
```

Returns the number of pages in this

Book

.

**Specified by:** getNumberOfPages

in interface

Pageable
**Returns:** the number of pages this

Book

contains.

---

#### getNumberOfPages

public int getNumberOfPages()

Returns the number of pages in this

Book

.

getPageFormat

```java
public
PageFormat
getPageFormat​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

PageFormat

of the page specified by

pageIndex

.

**Specified by:** getPageFormat

in interface

Pageable
**Parameters:** pageIndex

- the zero based index of the page whose

PageFormat

is being requested
**Returns:** the

PageFormat

describing the size and
orientation of the page.
**Throws:** IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

---

#### getPageFormat

public

PageFormat

getPageFormat​(int pageIndex)
throws

IndexOutOfBoundsException

Returns the

PageFormat

of the page specified by

pageIndex

.

getPrintable

```java
public
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

**Specified by:** getPrintable

in interface

Pageable
**Parameters:** pageIndex

- the zero based index of the page whose

Printable

is being requested
**Returns:** the

Printable

that renders the page.
**Throws:** IndexOutOfBoundsException

- if the

Pageable

does not contain the requested page

---

#### getPrintable

public

Printable

getPrintable​(int pageIndex)
throws

IndexOutOfBoundsException

Returns the

Printable

instance responsible for rendering
the page specified by

pageIndex

.

setPage

```java
public void setPage​(int pageIndex,

Printable
painter,

PageFormat
page)
throws
IndexOutOfBoundsException
```

Sets the

PageFormat

and the

Painter

for a
specified page number.

**Parameters:** pageIndex

- the zero based index of the page whose
painter and format is altered
**Parameters:** painter

- the

Printable

instance that
renders the page
**Parameters:** page

- the size and orientation of the page
**Throws:** IndexOutOfBoundsException

- if the specified
page is not already in this

Book
**Throws:** NullPointerException

- if the

painter

or

page

argument is

null

---

#### setPage

public void setPage​(int pageIndex,

Printable

painter,

PageFormat

page)
throws

IndexOutOfBoundsException

Sets the

PageFormat

and the

Painter

for a
specified page number.

append

```java
public void append​(
Printable
painter,

PageFormat
page)
```

Appends a single page to the end of this

Book

.

**Parameters:** painter

- the

Printable

instance that
renders the page
**Parameters:** page

- the size and orientation of the page
**Throws:** NullPointerException

- If the

painter

or

page

argument is

null

---

#### append

public void append​(

Printable

painter,

PageFormat

page)

Appends a single page to the end of this

Book

.

append

```java
public void append​(
Printable
painter,

PageFormat
page,
int numPages)
```

Appends

numPages

pages to the end of this

Book

. Each of the pages is associated with

page

.

**Parameters:** painter

- the

Printable

instance that renders
the page
**Parameters:** page

- the size and orientation of the page
**Parameters:** numPages

- the number of pages to be added to the
this

Book

.
**Throws:** NullPointerException

- If the

painter

or

page

argument is

null

---

#### append

public void append​(

Printable

painter,

PageFormat

page,
int numPages)

Appends

numPages

pages to the end of this

Book

. Each of the pages is associated with

page

.

---

