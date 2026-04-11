# Interface Pageable

**Source:** `java.desktop\java\awt\print\Pageable.html`

### Class Description

```java
public interface
Pageable
```

The

Pageable

implementation represents a set of
pages to be printed. The

Pageable

object returns
the total number of pages in the set as well as the

PageFormat

and

Printable

for a specified page.

**All Known Implementing Classes:** Book

---

### Field Details

#### @Native

static final int UNKNOWN_NUMBER_OF_PAGES

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getNumberOfPages()

Returns the number of pages in the set.
To enable advanced printing features,
it is recommended that

Pageable

implementations return the true number of pages
rather than the
UNKNOWN_NUMBER_OF_PAGES constant.

**Returns:**
- the number of pages in this

Pageable

.

---

#### PageFormat
getPageFormat​(int pageIndex)
throws
IndexOutOfBoundsException

Returns the

PageFormat

of the page specified by

pageIndex

.

**Parameters:**
- pageIndex

- the zero based index of the page whose

PageFormat

is being requested

**Returns:**
- the

PageFormat

describing the size and
orientation.

**Throws:**
- IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

---

#### Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException

Returns the

Printable

instance responsible for
rendering the page specified by

pageIndex

.

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

- if
the

Pageable

does not contain the requested
page.

---

### Additional Sections

#### Interface Pageable

**All Known Implementing Classes:** Book

```java
public interface
Pageable
```

The

Pageable

implementation represents a set of
pages to be printed. The

Pageable

object returns
the total number of pages in the set as well as the

PageFormat

and

Printable

for a specified page.

**See Also:** PageFormat

,

Printable

public interface

Pageable

The

Pageable

implementation represents a set of
pages to be printed. The

Pageable

object returns
the total number of pages in the set as well as the

PageFormat

and

Printable

for a specified page.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

UNKNOWN_NUMBER_OF_PAGES

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getNumberOfPages

()

Returns the number of pages in the set.

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

instance responsible for
rendering the page specified by

pageIndex

.

Field Summary

Fields

Modifier and Type

Field

Description

static int

UNKNOWN_NUMBER_OF_PAGES

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

---

#### Field Summary

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getNumberOfPages

()

Returns the number of pages in the set.

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

instance responsible for
rendering the page specified by

pageIndex

.

---

#### Method Summary

Returns the number of pages in the set.

Returns the

PageFormat

of the page specified by

pageIndex

.

Returns the

Printable

instance responsible for
rendering the page specified by

pageIndex

.

============ FIELD DETAIL ===========

- Field Detail

- UNKNOWN_NUMBER_OF_PAGES

```java
@Native

static final int UNKNOWN_NUMBER_OF_PAGES
```

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getNumberOfPages

```java
int getNumberOfPages()
```

Returns the number of pages in the set.
To enable advanced printing features,
it is recommended that

Pageable

implementations return the true number of pages
rather than the
UNKNOWN_NUMBER_OF_PAGES constant.

**Returns:** the number of pages in this

Pageable

.

- getPageFormat

```java
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

**Parameters:** pageIndex

- the zero based index of the page whose

PageFormat

is being requested
**Returns:** the

PageFormat

describing the size and
orientation.
**Throws:** IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

- getPrintable

```java
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

Printable

instance responsible for
rendering the page specified by

pageIndex

.

**Parameters:** pageIndex

- the zero based index of the page whose

Printable

is being requested
**Returns:** the

Printable

that renders the page.
**Throws:** IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

Field Detail

- UNKNOWN_NUMBER_OF_PAGES

```java
@Native

static final int UNKNOWN_NUMBER_OF_PAGES
```

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

**See Also:** Constant Field Values

---

#### Field Detail

UNKNOWN_NUMBER_OF_PAGES

```java
@Native

static final int UNKNOWN_NUMBER_OF_PAGES
```

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

**See Also:** Constant Field Values

---

#### UNKNOWN_NUMBER_OF_PAGES

@Native

static final int UNKNOWN_NUMBER_OF_PAGES

This constant is returned from the

getNumberOfPages

method if a

Pageable

implementation does not know
the number of pages in its set.

Method Detail

- getNumberOfPages

```java
int getNumberOfPages()
```

Returns the number of pages in the set.
To enable advanced printing features,
it is recommended that

Pageable

implementations return the true number of pages
rather than the
UNKNOWN_NUMBER_OF_PAGES constant.

**Returns:** the number of pages in this

Pageable

.

- getPageFormat

```java
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

**Parameters:** pageIndex

- the zero based index of the page whose

PageFormat

is being requested
**Returns:** the

PageFormat

describing the size and
orientation.
**Throws:** IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

- getPrintable

```java
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

Printable

instance responsible for
rendering the page specified by

pageIndex

.

**Parameters:** pageIndex

- the zero based index of the page whose

Printable

is being requested
**Returns:** the

Printable

that renders the page.
**Throws:** IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

---

#### Method Detail

getNumberOfPages

```java
int getNumberOfPages()
```

Returns the number of pages in the set.
To enable advanced printing features,
it is recommended that

Pageable

implementations return the true number of pages
rather than the
UNKNOWN_NUMBER_OF_PAGES constant.

**Returns:** the number of pages in this

Pageable

.

---

#### getNumberOfPages

int getNumberOfPages()

Returns the number of pages in the set.
To enable advanced printing features,
it is recommended that

Pageable

implementations return the true number of pages
rather than the
UNKNOWN_NUMBER_OF_PAGES constant.

getPageFormat

```java
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

**Parameters:** pageIndex

- the zero based index of the page whose

PageFormat

is being requested
**Returns:** the

PageFormat

describing the size and
orientation.
**Throws:** IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

---

#### getPageFormat

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
Printable
getPrintable​(int pageIndex)
throws
IndexOutOfBoundsException
```

Returns the

Printable

instance responsible for
rendering the page specified by

pageIndex

.

**Parameters:** pageIndex

- the zero based index of the page whose

Printable

is being requested
**Returns:** the

Printable

that renders the page.
**Throws:** IndexOutOfBoundsException

- if
the

Pageable

does not contain the requested
page.

---

#### getPrintable

Printable

getPrintable​(int pageIndex)
throws

IndexOutOfBoundsException

Returns the

Printable

instance responsible for
rendering the page specified by

pageIndex

.

---

